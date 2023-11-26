# To-Do_List-Application-Using-Python

### To-Do App with Tkinter

This Python script implements a basic To-Do application using the Tkinter library for the graphical user interface (GUI).

### Code Explanation:

1. **Import Libraries:**
   ```python
   import tkinter as tk
   from tkinter import messagebox
   from tkinter import Text
   from random import choice
   ```

   - `tkinter`: Standard GUI toolkit for Python.
   - `messagebox`: Module to create pop-up message boxes.
   - `Text`: Widget for displaying multiline text.
   - `choice`: Function to make a random choice from a sequence.

2. **Global Variables:**
   ```python
   tasks_list = []  # Global list to store tasks
   counter = 1  # Global variable for counting tasks
   ```

   - `tasks_list`: List to store tasks.
   - `counter`: Counter for tracking the number of tasks.

3. **Input Error Function:**
   ```python
   def inputError():
       # Function to check for input errors (empty task field)
   ```

4. **Clear Task Number Field Function:**
   ```python
   def clear_taskNumberField():
       # Function to clear the contents of the task number text field
   ```

5. **Clear Task Field Function:**
   ```python
   def clear_taskField():
       # Function to clear the contents of the task entry field
   ```

6. **Insert Task Function:**
   ```python
   def insertTask():
       # Function to insert task into the text area
   ```

7. **Delete Task Function:**
   ```python
   def delete():
       # Function to delete a specified task
   ```

8. **Main Code:**
   ```python
   if __name__ == "__main__":
       # Driver code
   ```

   - Initialize the Tkinter GUI window and configure its properties.

9. **Widgets Creation:**
   - Labels, entry fields, buttons, and text areas are created for task entry, display, and deletion.

10. **Grid Placement:**
    - Widgets are placed in a grid layout within the GUI window.

11. **Start GUI:**
    ```python
    gui.mainloop()
    ```

    - Start the GUI event loop.

### How to Use:

1. Run the script.
2. Enter tasks in the "Enter Your Task" entry field and click "Submit" to add them to the To-Do list.
3. To delete a task, enter the task number in the "Delete Task Number" entry field and click "Delete."
4. Use the "Exit" button to close the application.

This simple To-Do app provides a straightforward interface for adding and deleting tasks using Tkinter's GUI components. Customize it further based on your requirements.
