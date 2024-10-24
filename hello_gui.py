import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")
root.geometry("300x200")  # Width x Height

# Create a label with the text "Hello, World!"
label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
label.pack(pady=20)  # Add some vertical padding

# Create a button to close the application
button = tk.Button(root, text="Exit", command=root.quit)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
