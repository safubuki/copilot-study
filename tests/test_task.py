import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_add_task(self):
        task = Task()
        task.add_task("Task 1")
        self.assertEqual(len(task.get_tasks()), 1)

    def test_display_tasks(self):
        task = Task()
        task.add_task("Task 1")
        task.add_task("Task 2")
        self.assertEqual(task.display_tasks(), "Tasks:\n1. Task 1\n2. Task 2")

    def test_delete_task(self):
        task = Task()
        task.add_task("Task 1")
        task.add_task("Task 2")
        task.delete_task(1)
        self.assertEqual(len(task.get_tasks()), 1)

if __name__ == '__main__':
    unittest.main()