from unittest import TestCase, main

from testing_10.exe.student.project.student import Student


class TestStudent(TestCase):
    def test_student_initialization(self):
        student_name = "Dancho"
        courses = [None, {"PR": ["n1", "n2"]}]

        for course in courses:
            student = Student(student_name, course)
            if not course:
                self.assertEqual({}, student.courses)
            else:
                self.assertEqual(course, student.courses)
            self.assertEqual(student_name, student.name)

    def setUp(self) -> None:
        self.student_name = "Dancho"
        self.course = "PR"
        self.notes = ["n1", "n2"]
        self.courses = {self.course: self.notes}
        self.student = Student(self.student_name, self.courses)

    def test_enroll_should_extend_notes_for_already_enrolled_course(self):
        new_notes = ["n3,", "n4"]
        expected_notes = self.notes + new_notes
        result = self.student.enroll(self.course, new_notes)
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertTrue(self.course in self.courses)
        self.assertEqual(expected_notes, self.student.courses[self.course])

    def test_enroll_should_add_new_course_with_notes(self):
        for idx, command in enumerate(["", "Y"]):
            course_name = f"Java{idx}"
            course_notes = ["random", "J"]
            result = self.student.enroll(f"Java{idx}",course_notes, command)

            self.assertEqual("Course and course notes have been added.", result)
            self.assertTrue(course_name in self.courses)
            self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_should_add_new_course_without_notes(self):
        course_notes = ["notes", "notes2"]
        course_name = "Java"
        result = self.student.enroll(course_name, course_notes, "N")
        self.assertEqual([], self.student.courses[course_name])
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_existing_course_when_student_is_enrolled_to_the_course(self):
        notes_to_add = "new_notes"
        expected_notes = [x for x in self.notes]
        expected_notes.append(notes_to_add)
        result = self.student.add_notes(self.course, notes_to_add)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(expected_notes, self.student.courses[self.course])

    def test_add_notes_raises_error_when_student_is_not_enrolled_to_the_course(self):
        notes_to_add = "new_notes"
        course = "Java"
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, notes_to_add)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertTrue(course not in self.student.courses)

    def test_leave_course_raises_error_when_student_not_enrolled_for_the_course(self):
        course = "Java"
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertTrue(course not in self.student.courses)

    def test_leave_course_removes_course_when_student_is_enrolled(self):
        self.student.enroll("Java", [])
        expected_courses_count = len(self.student.courses) - 1
        result = self.student.leave_course(self.course)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(self.course not in self.student.courses)
        self.assertEqual(expected_courses_count, len(self.student.courses))


if __name__ == '__main__':
    main()