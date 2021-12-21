from unittest import TestCase, main

from testing_10.lab.worker.worker import Worker


class WorkerTests(TestCase):
    valid_name = "Dan"
    valid_salary = 2000
    valid_energy = 10

    def test_worker_is_initialised_correctly(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_if_worker_energy_is_correctly_incremented_after_rest(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        worker.rest()
        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work_with_energy_0_expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)

        with self.assertRaises(Exception) as exc:
            worker.work()

        self.assertEqual('Not enough energy.', str(exc.exception))

    def test_work_with_negative_energy_expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)

        with self.assertRaises(Exception) as exc:
            worker.work()

        self.assertEqual('Not enough energy.', str(exc.exception))

    def test_if_salary_correctly_added_to_money_after_work(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        worker.work()
        self.assertEqual(self.valid_salary, worker.salary)


if __name__ == '__main__':
    main()



