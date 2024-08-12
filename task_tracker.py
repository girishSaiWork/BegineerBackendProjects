print("####################################################################################################")
print("#                                            TASK TRACKER IN PYTHON                                #")
print("####################################################################################################")

tasks_list = []
def add_task(title, task_description):
    """
    Add a new task to the task list.

    Args:
        title (str): The title of the task.
        task_description (str): A detailed description of the task.

    Returns:
        None

    Note:
        This function automatically assigns an ID to the task based on the current number of tasks.
        The new task is always added with a 'pending' status.
    """
    task_id = len(tasks_list) + 1
    task = {
        'id': task_id,
        'task_title': title,
        'description': task_description,
        'task_status': 'pending'
    }
    tasks_list.append(task)

def view_tasks():
    """
    Display all tasks in the task list.

    This function prints out all tasks currently stored in the tasks_list.
    For each task, it displays the ID, title, description, and status.
    If there are no tasks in the list, it prints a message indicating that no tasks have been added yet.

    Args:
        None

    Returns:
        None

    Note:
        This function does not modify the tasks_list; it only reads and displays the information.
    """
    if len(tasks_list) == 0:
        print("No tasks yet. Add your tasks")
    else:
        print(f"Total tasks is in the list are ")
        for task in tasks_list:
            print(f"ID: {task['id']}")
            print(f"Title: {task['task_title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['task_status']}")
            print("===========================================")

def update_task(task_id, title=None, description=None, status=None):
    """
    Update an existing task in the task list.

    This function allows for updating the title, description, and/or status of a task
    identified by its task_id. If a parameter is not provided, that field remains unchanged.

    Args:
        task_id (int): The ID of the task to be updated.
        title (str, optional): The new title for the task. Defaults to None.
        description (str, optional): The new description for the task. Defaults to None.
        status (str, optional): The new status for the task. Defaults to None.

    Returns:
        None

    Note:
        If the task_id is not found in the task list, a message is printed indicating that
        the task was not found. If the task list is empty, a message is printed indicating
        that there are no tasks to update.
    """
    if len(tasks_list) == 0:
        print("No tasks yet. Add your tasks")
    else:
        for task in tasks_list:
            if task['id'] == task_id:
                if title:
                    task['task_title'] = title
                if description:
                    task['description'] = description
                if status:
                    task['task_status'] = status
                print(f"Task ID {task_id} updated successfully.")
                return
        print(f"Task ID {task_id} not found.")
    
def delete_task(task_id):
    """
    Delete a task from the task list based on its ID.

    This function removes a task from the tasks_list if a task with the given task_id exists.
    If the task list is empty or if no task with the given ID is found, appropriate messages are displayed.

    Args:
        task_id (int): The ID of the task to be deleted.

    Returns:
        None

    Note:
        This function modifies the global tasks_list variable.
        After successful deletion, a confirmation message is printed.
        If the task list is empty, a message indicating so is printed instead of attempting deletion.
    """
    global tasks_list
    if len(tasks_list) == 0:
        print("No tasks yet. Add your tasks")
    else:
        tasks_list = [task for task in tasks_list if task['id'] != task_id]
        print(f"Task ID {task_id} deleted successfully.")
         
def search_tasks(keyword):
    """
    Search for tasks based on a keyword.

    This function searches through all tasks in the tasks_list and returns those
    that contain the given keyword in either their title or description.
    The search is case-insensitive.

    Args:
        keyword (str): The keyword to search for in task titles and descriptions.

    Returns:
        None

    Note:
        If the task list is empty, a message is printed indicating that there are no tasks.
        If no tasks match the keyword, a message is printed indicating that no matching tasks were found.
        For each matching task, the function prints its ID, title, description, and status.
    """
    if len(tasks_list) == 0:
        print("No tasks yet. Add your tasks")
    else:
        results = [task for task in tasks_list if keyword.lower() in task['task_title'].lower() or keyword.lower() in task['description'].lower()]
        if not results:
            print("No matching tasks found.")
            return
        for task in results:
            print(f"ID: {task['id']}")
            print(f"Title: {task['task_title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['task_status']}")
            print("===========================================")

def view_tasks_status(status_filter=None):
    """
    View tasks filtered by a specific status.

    This function displays tasks from the tasks_list that match the given status filter.
    If no status filter is provided, it defaults to None and will prompt the user for input.

    Args:
        status_filter (str, optional): The status to filter tasks by. 
                                       Should be one of 'pending', 'done', or 'in progress'.
                                       Defaults to None.

    Returns:
        None

    Note:
        If an invalid status filter is provided, an error message is displayed.
        If no tasks match the given status, a message is printed indicating so.
        For each matching task, the function prints its ID, title, description, and status.
        The total count of tasks matching the status is also displayed.
    """
    if status_filter is None:
        status_filter = input("Enter status filter (pending/done/in progress): ").lower()
    if status_filter not in ['pending', 'done', 'in progress']:
        print("Invalid status filter. Please use 'pending', 'done', or 'in progress'.")
        return

    filtered_tasks = [task for task in tasks_list if task['task_status'] == status_filter]
    if not filtered_tasks:
        print(f"No tasks with the status '{status_filter}'.")
    else:
        print(f"Total tasks with status '{status_filter}': {len(filtered_tasks)}")
        for task in filtered_tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['task_title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['task_status']}")
            print("===========================================")
            

def main():
    """
    Main function to run the Task Tracker CLI application.

    This function implements the main loop of the application, presenting a menu
    of options to the user and calling the appropriate functions based on the
    user's choice. The loop continues until the user chooses to exit.

    The menu options include:
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Search Tasks
    6. List all pending Tasks
    7. List all completed Tasks
    8. List all in progress Tasks
    9. Exit

    For each option, the function prompts for necessary inputs and calls the
    corresponding function to perform the requested operation.

    The function handles invalid inputs by displaying an error message and
    continuing the loop.

    Returns:
        None
    """
    while True:
        print("\nTask Tracker CLI")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. List all pending Tasks")
        print("7. List all completed Tasks")
        print("8. List all in progress Tasks")
        print("9. Exit")
    
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")
            update_task(task_id, title, description, status)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            search_tasks(keyword)
        elif choice == '6':
            view_tasks_status('pending')
        elif choice == '7':
            view_tasks_status('done')
        elif choice == '8':
            view_tasks_status('in progress')
        elif choice == '9':
                print("Exiting Task Tracker. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()