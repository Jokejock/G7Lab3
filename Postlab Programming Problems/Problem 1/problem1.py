import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Color Labels")
root.geometry("300x300")  # Set the window size
root.configure(bg='green')  # Set the background color to green

# Create a frame to hold the labels and center them vertically
frame = tk.Frame(root, bg='green')
frame.pack(expand=True)

# Create labels with the specified colors
label_red = tk.Label(frame, text="RED", fg="red", bg="black", font=("Helvetica", 24))
label_white = tk.Label(frame, text="WHITE", fg="white", bg="black", font=("Helvetica", 24))
label_blue = tk.Label(frame, text="BLUE", fg="blue", bg="black", font=("Helvetica", 24))

# Pack the labels into the frame, centering them vertically
label_red.pack(pady=10)   # Add some vertical padding
label_white.pack(pady=10)  # Add some vertical padding
label_blue.pack(pady=10)   # Add some vertical padding

# Start the main event loop
root.mainloop()