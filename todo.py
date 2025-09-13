# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1 ):
        print(f"{i}. {task}")
# Step 4: Delete a task
def delete_task(index):
    task = tasks.pop(index)
    print(f"Deleted: {task}")

# Step 5: Mark task complete

def mark_complete(index):
    tasks[index] = ((tasks[index]) + "(COMPLETE)")



add_task("Finish Cyber 201 assignment")
add_task("Push code to GitHub")
add_task("Study today's notes")
view_tasks()
delete_task(0)   
mark_complete(1)
view_tasks()
# Demo flow (you can run this file directly: python todo.py)
