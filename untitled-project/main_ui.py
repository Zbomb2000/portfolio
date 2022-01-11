#!/usr/bin/python3
import PIL
from PIL import ImageTk
import sys
import os
import json
import re
from validate_email_address import validate_email

# Checks for libraries that might not be installed
try:
    try:
        import tkinter as tk
    except:
        import Tkinter as tk
except:
    print("You need to install the tkinter module (sudo apt-get install python3-tk python3-dev).")
    sys.exit()

try:
    import pyautogui as pygui
except:
    print("You need to install the pyautogui module (pip install pyautogui).")
    sys.exit()


# Displays the "what's new" screen
def whatsNew():
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Apilevel window to center
            """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    print("[INFO] Displaying 'What's New' screen.")

    # This gets the current working directory from file path files
    file_directory = os.path.dirname(__file__)
    file = open(file_directory + r"/ef_file_path.json")
    cd_var = json.load(file)
    cd = r"{}".format(cd_var)
    file.close()

    # Window properties
    window = tk.Tk()
    window.title("What's New | untitled_project")
    # Resizes the window
    window.geometry("600x600")
    # Changes the background color of the window
    window.configure(bg="#616161")
    # Centers the window
    center(window)

    # Closes the window
    def onClosing():
        if dsa.get() == 1:
            with open(cd + r"/data/run.json", 'r') as open_file:
                load_data = json.load(open_file)
                load_data['whats_new'] = 1
            with open(cd + r"/data/run.json", 'w') as open_file:
                json.dump(load_data, open_file)
        print()
        print("[INFO] 'What's New' window closed")
        print()

        window.destroy()

    # Read the Image
    first_image = PIL.Image.open(cd + r"/external-functions/other/images/update_info_001.png")
    # Resize the image using resize() method
    resized_image = first_image.resize((550, 425))
    # Create photoimage
    img_var = ImageTk.PhotoImage(resized_image)

    # This is the main image
    info_image = tk.Label(
        image=img_var,
        bg="#616161",
    )

    # This is the border for the checkbox
    check_box_frame = tk.Frame(
        bg="black",
    )

    # This asks if the window should be shown next time the user opens the program
    dsa = tk.IntVar()
    check_box = tk.Checkbutton(
        check_box_frame,
        text="Don't show again",
        bg="white",
        width=20,
        height=1,
        font=("Arial", 10, 'bold'),
        variable=dsa,
    )

    # This is the quit button to close the window
    quit_button = tk.Button(
        text="Close",
        command=onClosing,
        width=10,
        bg="#4d4d4d",
        fg="white",
    )

    # Packs all the elements
    info_image.pack(side=tk.TOP, pady=(20, 0))
    check_box_frame.pack(pady=(5, 5), padx=(5, 5))
    check_box.pack(pady=(5, 5), padx=(5, 5))
    quit_button.pack(side=tk.BOTTOM, pady=(0, 25))

    window.protocol("WM_DELETE_WINDOW", onClosing)

    window.mainloop()


# Start screens
class StartScreens:
    def __init__(self):
        print("[PROGRAM] Started functions in class 'startScreens'")
        print()

    @staticmethod
    def getUiCd():
        # This gets the current working directory from file path files
        file_directory = os.path.dirname(__file__)
        file = open(file_directory + r"/ef_file_path.json")
        cd_var = json.load(file)
        cd = r"{}".format(cd_var)
        file.close()
        return cd

    @staticmethod
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Apilevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    @staticmethod
    def writeUserInformation(cd, email, grade):
        # Creates the default user_information dictionary
        info_dict = {'email': 0, 'grade': 0}
        # Checks if the email is a valid email
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            email_valid = validate_email(email)
            if email_valid:
                info_dict['email'] = email
            else:
                print("[ERROR] Email does not exist")
                print()
        # Sets grade as an integer
        info_dict['grade'] = int(grade)
        # Writes data to user_information file
        with open(cd + r"/data/user_information.json", 'w') as file:
            json.dump(info_dict, file)

    def adminVerification(self):
        cd = self.getUiCd()

        # Functions that run when you click a button
        def onClosing():
            print("[INFO] Sudo mode verification window closed")
            print()
            sys.exit()

        def yesFunc():
            writeAdminFunc(1)

        def noFunc():
            writeAdminFunc(0)

        def writeAdminFunc(info):
            with open(cd + r"/data/device_info.json", 'r') as load_dump_file:
                load_data_dict = json.load(load_dump_file)
                load_data_dict['admin'] = info
            with open(cd + r"/data/device_info.json", 'w') as dump_file_2:
                json.dump(load_data_dict, dump_file_2)
            root.destroy()

        print("[INFO] Displaying sudo mode verification screen")
        print()
        # Adds main window
        root = tk.Tk()
        # Sets title
        root.title("Admin Verification | Set Up")
        # Adjust size
        root.geometry("400x500")
        # Makes window un-resizeable
        root.resizable(0, 0)
        # set window color
        root.configure(bg="#f0f0f0")
        # Centers window
        self.center(root)
        # Get the current screen resolution
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Writes resolution to device info file
        with open(cd + r"/data/device_info.json", 'r') as load_file:
            load_data = json.load(load_file)
            load_data['x'] = screen_width
            load_data['y'] = screen_height
        with open(cd + r"/data/device_info.json", 'w') as dump_file:
            json.dump(load_data, dump_file)

        top_label = tk.Text(
            bg="orange",
            fg="white",
            font=("Arial", 12),
            height="3",
        )

        # Configure the alignment of the text
        top_label.tag_configure("center_stuff", justify='center')
        top_label.tag_configure("red", foreground="blue", font=('Arial', 12, "bold"), )
        top_label.insert('1.0', "Would you like to set up in sudo mode?\n(Password required)")

        # Add the tag in the given text
        top_label.tag_add("center_stuff", "1.0", "end")
        top_label.tag_add("red", "1.28", "1.37")

        # Disables typing in the text widget
        top_label.config(state='disabled')

        no_button = tk.Button(
            text="No (Recommended)",
            background="orange",
            foreground="white",
            width=17,
            height=3,
            font="Arial",
            command=noFunc,
        )

        yes_button = tk.Button(
            text="Yes",
            background="orange",
            foreground="white",
            width=17,
            height=3,
            font="Arial",
            command=yesFunc,
        )
        yes_button_label = tk.Label(text="*Only click this if you have the password.", foreground="red",
                                    background="#f0f0f0", )

        quit_button = tk.Button(
            text="Quit",
            command=onClosing,
            width=10,
        )

        root.protocol("WM_DELETE_WINDOW", onClosing)

        top_label.pack(fill='x')
        no_button.pack(pady=(25, 25))
        yes_button.pack(pady=(25, 0))
        yes_button_label.pack()
        quit_button.pack(side=tk.BOTTOM, pady=(45, 10))

        root.mainloop()

    def userInformation(self):
        cd = self.getUiCd()

        print("[INFO] Displaying user information screen")
        print()
        # Adds main window
        root = tk.Tk()
        # Sets title
        root.title("User Information | Set Up")
        # Adjust size
        root.geometry("400x500")
        # Makes window un-resizeable
        root.resizable(0, 0)
        # set window color
        root.configure(bg="#f0f0f0")
        # Centers window
        self.center(root)

        def onClosing():
            sys.exit()

        def getGradeValue(value):
            # Creates a global variable for grade number
            global grade_num
            grade_num = value

        def submitInformation():
            # Gets input for email
            email_input = email.get()
            # Checks if email is valid if provided
            if email_input != '':
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if re.search(regex, email_input):
                    email_valid = validate_email(email_input)
                    if email_valid:
                        # Runs writeUserInformation function with valid email variable
                        self.writeUserInformation(cd, email_input, grade_num)
                        root.destroy()
                    else:
                        # Makes email_incorrect label visible
                        print("[PROGRAM] Invalid email 2")
                        print()
                        email_incorrect.config(fg="red", )
                else:
                    # Makes email_incorrect label visible
                    print("[PROGRAM] Invalid email 1")
                    print()
                    email_incorrect.config(fg="red", )
            else:
                # Runs writeUserInformation with blank email variable
                self.writeUserInformation(cd, email_input, grade_num)
                root.destroy()

        top_label = tk.Text(
            bg="orange",
            fg="white",
            font=("Arial", 12),
            height="3",
        )

        # Configure the alignment of the text
        top_label.tag_configure("center_stuff", justify='center')
        top_label.insert('1.0', "Please enter information about yourself.")

        # Add the tag in the given text
        top_label.tag_add("center_stuff", "1.0", "end")

        # Disables typing in the text widget
        top_label.config(state='disabled')

        # Error message if the email isn't valid
        email_incorrect = tk.Label(
            text="*Invalid email",
            bg="#f0f0f0",
            fg="#f0f0f0"
        )

        # First prompt
        email_label = tk.Label(
            text="Enter your email (optional):",
            font=("Arial", 12),
            bg="#f0f0f0",
        )
        email = tk.Entry(
            font=("Arial", 10),
            width=50,
        )

        # Second prompt
        grade_label = tk.Label(
            text="Select your grade number:",
            font=("Arial", 12),
            bg="#f0f0f0",
        )
        grade = tk.Scale(
            bg="#f0f0f0",
            from_=1,
            to=12,
            command=getGradeValue,
        )

        # Buttons at the bottom of the page
        login_button = tk.Button(
            text="Continue",
            width=10,
            command=submitInformation
        )

        quit_button = tk.Button(
            text="Quit",
            command=onClosing,
            width=10,
        )

        # Exits program if 'x' is clicked
        root.protocol("WM_DELETE_WINDOW", onClosing)

        # Packs widgets in order from top to bottom
        top_label.pack(fill='x')
        email_incorrect.pack(pady=(20, 0), padx=(0, 200))
        email_label.pack(pady=(5, 0))
        email.pack(pady=(0, 0))
        grade_label.pack(side=tk.LEFT, padx=(50, 0), pady=(0, 0))
        grade.pack(side=tk.RIGHT, padx=(0, 50), pady=(0, 0))
        quit_button.pack(side=tk.BOTTOM, pady=(2, 2), padx=(0, 0))
        login_button.pack(side=tk.BOTTOM, pady=(0, 5), padx=(0, 0))

        root.mainloop()

    @staticmethod
    def finalWarning():
        warning_input = pygui.confirm(
            "[WARNING]\nUsing this program is cheating. Do not use this unless you have a VERY good excuse if you are caught.\nTHIS IS YOUR LAST WARNING",
            buttons=["CONTINUE", "TURN BACK"])
        if warning_input is None:
            pygui.alert("Good choice", button="EXIT")
            sys.exit()
        elif warning_input == "TURN BACK":
            pygui.alert("Good choice", button="EXIT")
            sys.exit()
        elif warning_input == "CONTINUE":
            pygui.alert("YOU HAVE BEEN WARNED.", button="CONTINUE")
