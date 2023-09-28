class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        task.completed = True

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def add_task_from_input(self):
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        task = Task(title, description)
        self.add_task(task)

    def display_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Выполнено" if task.completed else "Не выполнено"
                print(f"{index}. Название: {task.title}, Описание: {task.description}, Статус: {status}")

    def mark_task_completed(self):
        self.display_tasks()
        task_number = int(input("Введите номер задачи, которую хотите пометить как выполненную: ")) - 1
        if 0 <= task_number < len(self.tasks):
            task = self.tasks[task_number]
            self.complete_task(task)
            print(f"Задача '{task.title}' помечена как выполненная.")
        else:
            print("Недопустимый номер задачи. Пожалуйста, выберите существующий номер.")

if __name__ == '__main__':
    todo_list = ToDoList()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Вывести список задач")
        print("3. Пометить задачу как выполненную")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            todo_list.add_task_from_input()
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            todo_list.mark_task_completed()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие 1, 2, 3 или 4.")