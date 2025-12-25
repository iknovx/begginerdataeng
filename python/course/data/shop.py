class TodoList:
    def __init__(self):
        self.task = []

    def add_task(self): #function to add an task
        input_task = input("Add a new task: ")
        self.task.append(input_task)
        print("Task successfully added!")

    def remove_task(self): #function to remove an task
        if not self.task:
            print("Task list is empty.")
            return

        print("Current tasks:")
        for i, t in enumerate(self.task, 1):
            print(f"{i}. {t}")

        task_index = input("Enter the task number to remove: ")

        
        if not task_index.isdigit():
            print("Invalid input. Please enter a number.")
            return

        task_index = int(task_index) - 1
        if 0 <= task_index < len(self.task):
            removed_task = self.task.pop(task_index)
            print(f"Task successfully removed: {removed_task}")
        else:
            print("Invalid task number.")

    def view_tasks(self): #function to view all tasks
        if not self.task:
            print("Task list is empty.")
        else:
            print("Current tasks:")
            for i, t in enumerate(self.task, 1):
                print(f"{i}. {t}")
    def check_point(self):
     if not self.task:
         print("Task list is empty.")
         return

     print("Current tasks:")
     for i, t in enumerate(self.task, 1):
        print(f"{i}. {t}")

     choice = input("Enter the task number to mark as complete: ")

    
     if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

     task_index = int(choice) - 1
     if 0 <= task_index < len(self.task):
        self.task[task_index] = self.task[task_index] + " *"  
        print(f"Task completed: {self.task[task_index]}")
     else:
        print("Invalid task number.")
            
        


def main():
    todo = TodoList()

    while True:
        print("\n--- TODO LIST ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Check point")
        print("5. Exit")

        choice = input("Select an action (1-5): ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.remove_task()
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            todo.check_point()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 5.")

if __name__ == "__main__":
    main()