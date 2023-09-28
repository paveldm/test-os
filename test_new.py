import unittest
from new import Task, ToDoList

class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        task = Task("Название задачи", "Описание задачи")
        self.assertEqual(task.title, "Название задачи")
        self.assertEqual(task.description, "Описание задачи")
        self.assertFalse(task.completed)

    def test_task_completion(self):
        task = Task("Название задачи", "Описание задачи")
        task.completed = True
        self.assertTrue(task.completed)

class TestToDoList(unittest.TestCase):
    def test_add_task(self):
        todo_list = ToDoList()
        task = Task("Название задачи", "Описание задачи")
        todo_list.add_task(task)
        self.assertEqual(len(todo_list.tasks), 1)

    def test_complete_task(self):
        todo_list = ToDoList()
        task = Task("Название задачи", "Описание задачи")
        todo_list.add_task(task)
        todo_list.complete_task(task)
        self.assertTrue(task.completed)

    def test_get_incomplete_tasks(self):
        todo_list = ToDoList()
        task1 = Task("Задача 1", "Описание 1")
        task2 = Task("Задача 2", "Описание 2")
        todo_list.add_task(task1)
        todo_list.add_task(task2)
        task1.completed = True
        incomplete_tasks = todo_list.get_incomplete_tasks()
        self.assertEqual(len(incomplete_tasks), 1)
        self.assertEqual(incomplete_tasks[0], task2)

    def test_get_completed_tasks(self):
        todo_list = ToDoList()
        task1 = Task("Задача 1", "Описание 1")
        task2 = Task("Задача 2", "Описание 2")
        todo_list.add_task(task1)
        todo_list.add_task(task2)
        task1.completed = True
        completed_tasks = todo_list.get_completed_tasks()
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0], task1)

if __name__ == '__main__':
    unittest.main()