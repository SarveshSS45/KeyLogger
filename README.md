KeyLogger A simple Keylogger application built with Python, Tkinter, and
pynput. This program captures and logs keyboard events, displaying
real-time keypresses in a Tkinter GUI and saving them to a text file.

Features Real-time display of key presses in a Tkinter window. Logs both
regular and special keys (like Shift, Enter, etc.). Captures and stores
key presses in a key_log.txt file. The application stops key logging
when the Esc key is pressed. Simple start/stop GUI with buttons to
control the keylogger. Requirements Make sure to have Python installed.
You can check if Python is installed using:

bash Copy code python \--version If Python is not installed, download
and install it from Python\'s official website.

Install Required Libraries Install the dependencies using pip:

bash Copy code pip install pynput Tkinter is included in standard Python
installations, so you don\'t need to install it separately.

Getting Started Clone the Repository:

bash Copy code git clone https://github.com/SarveshSS45/KeyLogger.git
Navigate to the Project Directory:

bash Copy code cd KeyLogger Run the Application:

Execute the Python script to start the Tkinter Keylogger:

bash Copy code python keylogger.py Usage Start the Keylogger:

Click the \"Start Keylogger\" button to begin logging key presses. The
keys pressed will be displayed in real-time within the Tkinter window.
Log Output:

All captured keystrokes are saved in the key_log.txt file, located in
the same directory as the script. Quit the Application:

To stop the keylogger, press the \"Quit\" button in the GUI or manually
press the Esc key to stop logging. File Structure bash Copy code ├──
keylogger.py \# The main Python script that runs the Keylogger ├──
key_log.txt \# The log file where keystrokes are saved └── README.md \#
Project README file Important Notes Ethical Use: This keylogger is
intended for educational and ethical purposes only. Please ensure that
you have permission before running the keylogger on any device, and be
transparent about its usage. Security: Avoid using this tool for
malicious purposes, as it can violate privacy laws and lead to legal
consequences. Contributing Feel free to fork this project and make your
own improvements. Contributions are welcome via pull requests.

Fork the project Create your feature branch (git checkout -b
feature/AmazingFeature) Commit your changes (git commit -m \'Add some
AmazingFeature\') Push to the branch (git push origin
feature/AmazingFeature) Open a pull request License This project is
licensed under the MIT License. See the LICENSE file for more details.
