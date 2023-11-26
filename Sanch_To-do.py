import tkinter as tk
from tkinter import messagebox
from tkinter import Text
from random import choice

# Global list to store tasks
tasks_list = []
# Global variable for counting tasks
counter = 1

# Function for checking input error when empty input is given in the task field
def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

# Function for clearing the contents of the task number text field
def clear_taskNumberField():
    taskNumberField.delete(0.0, tk.END)

# Function for clearing the contents of the task entry field
def clear_taskField():
    enterTaskField.delete(0, tk.END)

# Function for inserting the contents from the task entry field to the text area
def insertTask():
    global counter
    # Check for error
    value = inputError()
    # If error occurs, then return
    if value == 0:
        return
    # Get the task string concatenating with a new line character
    content = enterTaskField.get() + "\n"
    # Store task in the list
    tasks_list.append(content)
    # Insert content of the task entry field to the text area
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content, choice(["bg", "fg"]))
    counter += 1
    # Call the function to delete the content of the task field
    clear_taskField()

# Function for deleting the specified task
def delete():
    global counter
    # Handling the empty task error
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    # Get the task number, which is required to delete
    number = taskNumberField.get(1.0, tk.END)
    # Checking for input error when empty input in task number field
    if number == "\n":
        messagebox.showerror("Invalid Input error")
        return
    else:
        task_no = int(number)
    # Call the function for deleting the content of the task number field
    clear_taskNumberField()
    # Deleted specified task from the list
    tasks_list.pop(task_no - 1)
    # Decremented counter
    counter -= 1
    # Whole content of text area widget is deleted
    TextArea.delete(1.0, tk.END)
    # Rewriting the task after deleting one task at a time
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i], choice(["bg", "fg"]))

# Driver code
if __name__ == "__main__":

    # Create a GUI window
    gui = tk.Tk()

    # Set the title and background color of GUI window
    gui.title("To-Do App")
    gui.configure(background=choice(['light green', 'light blue', 'light yellow']))

    # Set the configuration of GUI window
    gui.geometry("250x300")

    # Create a label: Enter Your Task
    enterTask = tk.Label(gui, text="Enter Your Task", bg=choice(['light green', 'light blue', 'light yellow']))

    # Create a text entry box for typing the task
    enterTaskField = tk.Entry(gui)

    # Create a Submit Button
    Submit = tk.Button(gui, text="Submit", fg="Black", bg=choice(['Red', 'Blue', 'Yellow']), command=insertTask)

    # Create a text area for writing the content
    TextArea = Text(gui, height=5, width=25, font="lucida 13")

    # Create a label: Delete Task Number
    taskNumber = tk.Label(gui, text="Delete Task Number", bg=choice(['light green', 'light blue', 'light yellow']))

    taskNumberField = Text(gui, height=1, width=2, font="lucida 13")

    # Create a Delete Button
    delete = tk.Button(gui, text="Delete", fg="Black", bg=choice(['Red', 'Blue', 'Yellow']), command=delete)

    # Create an Exit Button
    Exit = tk.Button(gui, text="Exit", fg="Black", bg=choice(['Red', 'Blue', 'Yellow']), command=exit)

    # Grid method is used for placing the widgets at respective positions
    enterTask.grid(row=0, column=2)

    # ipadx attributed set the entry box horizontal size
    enterTaskField.grid(row=1, column=2, ipadx=50)

    Submit.grid(row=2, column=2)

    # padx attributed provide x-axis margin
    TextArea.grid(row=3, column=2, padx=10, sticky="W")

    taskNumber.grid(row=4, column=2, pady=5)

    taskNumberField.grid(row=5, column=2)

    # pady attributed provide y-axis margin from the widget.
    delete.grid(row=6, column=2, pady=5)

    Exit.grid(row=7, column=2)

    # Start the GUI
    gui.mainloop()
