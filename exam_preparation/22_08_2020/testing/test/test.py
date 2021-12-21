from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_name = "Dancho"
        self.school_year = 7
        self.src = StudentReportCard(self.student_name, self.school_year)

    def test_student_report_card_initialisation_with_empty_string_for_student_name(self):
        student_name = ""
        school_year = 1

        with self.assertRaises(ValueError) as ex:
            StudentReportCard(student_name, school_year)

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_student_report_card_initialisation_with_correct_name_and_valid_school_year(self):
        student_name = "Dancho"
        school_year_min = 1  # inclusive
        school_year_max = 12  # inclusive

        for syear in range(school_year_min, (school_year_max + 1)):
            src = StudentReportCard(student_name, syear)
            self.assertEqual(student_name, src.student_name)
            self.assertEqual(syear, src.school_year)
            self.assertEqual({}, src.grades_by_subject)

    def test_student_report_card_initialisation_with_correct_name_and_invalid_school_year(self):
        student_name = "Dancho"
        school_year_invalid_value = [-100, 0, 200]

        for syear in school_year_invalid_value:
            with self.assertRaises(ValueError) as ex:
                StudentReportCard(student_name, syear)

            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_to_non_existing_subject_in_grades_by_subject_dict(self):
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 5)
        self.assertEqual({"Math": [6], "Bio": [5]}, self.src.grades_by_subject)

    def test_add_grade_to_existing_subject_in_grades_by_subject_dict(self):
        self.src.add_grade("Math", 6)
        self.src.add_grade("Math", 4)
        self.assertEqual({"Math": [6, 4]}, self.src.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.src.add_grade("Math", 6)
        self.src.add_grade("Math", 4)
        self.src.add_grade("Bio", 6)
        self.src.add_grade("Bio", 5)

        grades_by_subject_dict = {"Math": [6, 4], "Bio": [6, 5]}
        expected_result = ""
        for subject, grades in grades_by_subject_dict.items():
            expected_result += f"{subject}: {sum(grades) / len(grades):.2f}\n"
        self.assertEqual(expected_result.strip(), self.src.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.src.add_grade("Math", 6)
        self.src.add_grade("Math", 4)
        self.src.add_grade("Bio", 6)
        self.src.add_grade("Bio", 5)

        grades_by_subject_dict = {"Math": [6, 4], "Bio": [6, 5]}
        sum_all_grades = 0
        all_count = 0
        for subject, grades in grades_by_subject_dict.items():
            sum_all_grades += sum(grades)
            all_count += len(grades)
        expected_result = f"Average Grade: {sum_all_grades/ all_count :.2f}"
        self.assertEqual(expected_result, self.src.average_grade_for_all_subjects())

    def test_repr_returns_the_correct_representation(self):
        self.src.add_grade("Math", 6)
        self.src.add_grade("Math", 4)
        self.src.add_grade("Bio", 6)
        self.src.add_grade("Bio", 5)

        report = f"Name: {self.student_name}\n" \
                 f"Year: {self.school_year}\n" \
                 f"----------\n" \
                 f"{self.src.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.src.average_grade_for_all_subjects()}"

        self.assertEqual(report, self.src.__repr__())


if __name__ == '__main__':
    main()