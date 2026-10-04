# Member 6:
# Login + Application Controller

import tkinter as tk

from tkinter import ttk, messagebox

import threading

from client import send_request

from student_gui import StudentGUI

from admin_gui import AdminGUI


class LoginGUI:

    def __init__(self, root):

        self.root = root

        root.title(
            "Smart Campus Helpdesk"
        )

        root.geometry(
            "450x350"
        )

        root.resizable(
            False,
            False
        )


        self.username = tk.StringVar()

        self.password = tk.StringVar()

        self.role = tk.StringVar(
            value="Student"
        )


        # --------------------------------
        # TITLE
        # --------------------------------

        tk.Label(

            root,

            text="SMART CAMPUS HELPDESK",

            font=("Arial", 20, "bold")

        ).pack(pady=25)


        frame = tk.Frame(root)

        frame.pack()


        # Username

        tk.Label(

            frame,

            text="Username"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=10
        )


        tk.Entry(

            frame,

            textvariable=self.username

        ).grid(

            row=0,

            column=1
        )


        # Password

        tk.Label(

            frame,

            text="Password"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=10
        )


        tk.Entry(

            frame,

            textvariable=self.password,

            show="*"

        ).grid(

            row=1,

            column=1
        )


        # Role

        tk.Label(

            frame,

            text="Role"

        ).grid(

            row=2,

            column=0,

            padx=10,

            pady=10
        )


        ttk.Combobox(

            frame,

            textvariable=self.role,

            values=[

                "Student",

                "Admin"

            ],

            state="readonly"

        ).grid(

            row=2,

            column=1
        )


        # Login button

        tk.Button(

            root,

            text="LOGIN",

            width=20,

            command=self.login

        ).pack(pady=20)


        # Demo credentials

        tk.Label(

            root,

            text=(
                "Student: raghav / 1234\n"
                "Admin: admin / admin123"
            )

        ).pack()


    # --------------------------------
    # LOGIN
    # --------------------------------

    def login(self):

        request = {

            "action": "login",

            "username":
                self.username.get(),

            "password":
                self.password.get(),

            "role":
                self.role.get()
        }


        threading.Thread(

            target=self.login_worker,

            args=(request,),

            daemon=True

        ).start()


    def login_worker(self, request):

        response = send_request(request)


        self.root.after(

            0,

            lambda:
                self.open_dashboard(response)
        )


    # --------------------------------
    # OPEN DASHBOARD
    # --------------------------------

    def open_dashboard(self, response):

        if not response["success"]:

            messagebox.showerror(

                "Login Failed",

                response["message"]
            )

            return


        self.root.destroy()


        dashboard = tk.Tk()


        if response.get("role") == "Admin":

            AdminGUI(dashboard)

        else:

            StudentGUI(

                dashboard,

                self.username.get()
            )


        dashboard.mainloop()


# --------------------------------
# START APPLICATION
# --------------------------------

def run():

    root = tk.Tk()

    LoginGUI(root)

    root.mainloop()


if __name__ == "__main__":

    run()