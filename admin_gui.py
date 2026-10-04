# Member 4:
# Tkinter Admin GUI

import tkinter as tk

from tkinter import ttk, messagebox

import threading

from client import send_request


class AdminGUI:

    def __init__(self, root):

        self.root = root

        root.title(
            "Admin - Smart Campus Helpdesk"
        )

        root.geometry("1050x600")


        # --------------------------------
        # TITLE
        # --------------------------------

        tk.Label(

            root,

            text="ADMIN DASHBOARD",

            font=("Arial", 20, "bold")

        ).pack(pady=15)


        # --------------------------------
        # COMPLAINT TABLE
        # --------------------------------

        self.table = ttk.Treeview(

            root,

            columns=(

                "id",

                "student",

                "category",

                "description",

                "status",

                "department"

            ),

            show="headings"
        )


        for column in (

            "id",

            "student",

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

            pady=10
        )


        # --------------------------------
        # CONTROL AREA
        # --------------------------------

        controls = tk.Frame(root)

        controls.pack(pady=10)


        # Status

        self.status = ttk.Combobox(

            controls,

            values=[

                "Pending",

                "In Progress",

                "Resolved"
            ],

            state="readonly",

            width=18
        )

        self.status.current(0)

        self.status.grid(

            row=0,

            column=0,

            padx=5
        )


        # Department

        self.department = ttk.Combobox(

            controls,

            values=[

                "Hostel Department",

                "Mess Department",

                "Academic Department",

                "IT Department",

                "Electrical Department",

                "Administration"

            ],

            state="readonly",

            width=22
        )

        self.department.current(0)

        self.department.grid(

            row=0,

            column=1,

            padx=5
        )


        # Update button

        tk.Button(

            controls,

            text="Update Selected",

            command=self.update

        ).grid(

            row=0,

            column=2,

            padx=5
        )


        # Refresh button

        tk.Button(

            controls,

            text="Refresh",

            command=self.refresh

        ).grid(

            row=0,

            column=3,

            padx=5
        )


        self.refresh()


    # --------------------------------
    # GET ALL COMPLAINTS
    # --------------------------------

    def refresh(self):

        threading.Thread(

            target=self.refresh_worker,

            daemon=True

        ).start()


    def refresh_worker(self):

        response = send_request({

            "action": "all"

        })


        self.root.after(

            0,

            lambda:
                self.show(response)
        )


    def show(self, response):

        # Clear table

        for item in self.table.get_children():

            self.table.delete(item)


        # Add complaints

        for complaint in response.get(

            "complaints",

            []

        ):

            self.table.insert(

                "",

                tk.END,

                values=(

                    complaint["id"],

                    complaint["student"],

                    complaint["category"],

                    complaint["description"],

                    complaint["status"],

                    complaint["department"]
                )
            )


    # --------------------------------
    # UPDATE COMPLAINT
    # --------------------------------

    def update(self):

        selected = self.table.selection()


        if not selected:

            messagebox.showwarning(

                "Warning",

                "Select a complaint first."
            )

            return


        values = self.table.item(

            selected[0],

            "values"
        )


        request = {

            "action": "update",

            "id": values[0],

            "status":
                self.status.get(),

            "department":
                self.department.get()
        }


        threading.Thread(

            target=self.update_worker,

            args=(request,),

            daemon=True

        ).start()


    def update_worker(self, request):

        response = send_request(request)


        self.root.after(

            0,

            lambda:
                self.after_update(response)
        )


    def after_update(self, response):

        messagebox.showinfo(

            "Result",

            response["message"]
        )

        self.refresh()