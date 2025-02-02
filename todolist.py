class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

    def edit_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_number < len(self.tasks):
            new_task = input("Enter the new task: ")
            self.tasks[task_number]["task"] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def mark_task_as_completed(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.mark_task_as_completed()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()