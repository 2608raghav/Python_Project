# Member 3:
# Tkinter Student GUI

import tkinter as tk

from tkinter import ttk, messagebox

import threading

from client import send_request


class StudentGUI:

    def __init__(self, root, username):

        self.root = root

        self.username = username

        root.title(
            
            "Student - Smart Campus Helpdesk"
        )

        root.geometry("900x600")


        # --------------------------------
        # TITLE
        # --------------------------------

        tk.Label(

            root,

            text=f"Welcome, {username}",

            font=("Arial", 20, "bold")

        ).pack(pady=15)


        # --------------------------------
        # COMPLAINT FORM
        # --------------------------------

        form = tk.LabelFrame(

            root,

            text="Submit Complaint",

            padx=10,

            pady=10
        )

        form.pack(
            fill="x",
            padx=20
        )


        # Category label

        tk.Label(
            form,
            text="Category"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )


        # Category dropdown

        self.category = ttk.Combobox(

            form,

            values=[

                "Hostel",
                "Mess",
                "Classroom",
                "Internet/Wi-Fi",
                "Electrical",
                "Other"
            ],

            state="readonly",

            width=25
        )

        self.category.current(0)

        self.category.grid(
            row=0,
            column=1
        )


        # Description label

        tk.Label(

            form,

            text="Description"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=10,

            sticky="n"
        )


        # Description box

        self.description = tk.Text(

            form,

            width=60,

            height=5
        )

        self.description.grid(

            row=1,

            column=1,

            pady=10
        )


        # Submit button

        tk.Button(

            form,

            text="Submit Complaint",

            command=self.submit

        ).grid(

            row=2,

            column=1,

            sticky="w",

            pady=10
        )


        # --------------------------------
        # COMPLAINT TABLE
        # --------------------------------

        self.table = ttk.Treeview(

            root,

            columns=(

                "id",

                "category",

                "description",

                "status",

                "department"
            ),

            show="headings"
        )


        for column in (

            "id",

            "category",

            "description",

            "status",

            "department"

        ):

            self.table.heading(

                column,

                text=column.title()
            )

            self.table.column(

                column,

                width=150
            )


        self.table.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=15
        )


        # Load existing complaints

        self.refresh()


    # --------------------------------
    # SUBMIT COMPLAINT
    # --------------------------------

    def submit(self):

        description = self.description.get(

            "1.0",

            tk.END

        ).strip()


        if not description:

            messagebox.showwarning(

                "Warning",

                "Enter a complaint."
            )

            return


        request = {

            "action": "add",

            "student":
                self.username,

            "category":
                self.category.get(),

            "description":
                description
        }


        # Run network request
        # in background thread

        threading.Thread(

            target=self.submit_worker,

            args=(request,),

            daemon=True

        ).start()


    def submit_worker(self, request):

        response = send_request(request)


        # Update GUI safely

        self.root.after(

            0,

            lambda:
                self.after_submit(response)
        )


    def after_submit(self, response):

        if response["success"]:

            messagebox.showinfo(

                "Success",

                response["message"]
            )

            self.description.delete(

                "1.0",

                tk.END
            )

            self.refresh()

        else:

            messagebox.showerror(

                "Error",

                response["message"]
            )


    # --------------------------------
    # REFRESH COMPLAINTS
    # --------------------------------

    def refresh(self):

        threading.Thread(

            target=self.refresh_worker,

            daemon=True

        ).start()


    def refresh_worker(self):

        response = send_request({

            "action":
                "student_list",

            "student":
                self.username
        })


        self.root.after(

            0,

            lambda:
                self.show_complaints(response)
        )


    def show_complaints(self, response):

        # Remove old rows

        for item in self.table.get_children():

            self.table.delete(item)


        # Insert new rows

        for complaint in response.get(
            "complaints",
            []
        ):

            self.table.insert(

                "",

                tk.END,

                values=(

                    complaint["id"],

                    complaint["category"],

                    complaint["description"],

                    complaint["status"],

                    complaint["department"]
                )
            )