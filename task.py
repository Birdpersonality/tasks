class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{idx}. {task.title} - {task.description} (Due: {task.due_date}) - {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_as_completed()
            print(f"Marked '{task.title}' as completed.")
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            new_task = Task(title, description, due_date)
            task_manager.add_task(new_task)
            print("Task added successfully.")

        elif choice == "2":
            print("\nTask List:")
            task_manager.list_tasks()

        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            task_manager.mark_task_completed(task_index)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")
