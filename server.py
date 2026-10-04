# Member 1:
# Networking + Client/Server + Multithreading

import socket
import threading
import json

from datetime import datetime

from config import HOST, PORT
from storage import load_complaints, save_complaints


class HelpdeskServer:

    def __init__(self):

        # Load previously stored complaints
        self.complaints = load_complaints()

        # Lock protects shared complaint data
        self.lock = threading.Lock()

        # Generate next complaint ID
        self.next_id = self.get_next_id()


    def get_next_id(self):

        if not self.complaints:
            return 1001

        return max(
            int(c["id"])
            for c in self.complaints
        ) + 1


    def start(self):

        # Create TCP socket
        server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # Allow reuse of the port
        server.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        # Bind server to IP and port
        server.bind((HOST, PORT))

        # Start listening
        server.listen(10)

        print("======================================")
        print(" SMART CAMPUS HELPDESK SERVER")
        print("======================================")
        print(f"Server running on {HOST}:{PORT}")
        print("Waiting for clients...")
        print()


        while True:

            # Accept a client connection
            client, address = server.accept()

            print("Client connected:", address)


            # Create a separate thread for each client
            thread = threading.Thread(
                target=self.handle_client,
                args=(client,),
                daemon=True
            )

            thread.start()


    def handle_client(self, client):

        try:

            # Receive data from client
            data = client.recv(16384).decode("utf-8")

            # Convert JSON string to Python dictionary
            request = json.loads(data)

            # Process request
            response = self.process_request(request)

            # Convert response to JSON
            response_data = json.dumps(response)

            # Send response back
            client.sendall(
                response_data.encode("utf-8")
            )


        except Exception as error:

            response = {
                "success": False,
                "message": str(error)
            }

            client.sendall(
                json.dumps(response).encode("utf-8")
            )


        finally:

            # Close client connection
            client.close()


    def process_request(self, request):

        action = request.get("action")


        # --------------------------------
        # LOGIN
        # --------------------------------

        if action == "login":

            users = {

                "raghav": (
                    "1234",
                    "Student"
                ),

                "student": (
                    "1234",
                    "Student"
                ),

                "admin": (
                    "admin123",
                    "Admin"
                )
            }


            username = request.get("username")
            password = request.get("password")
            role = request.get("role")


            if (
                username in users
                and users[username] == (password, role)
            ):

                return {
                    "success": True,
                    "message": "Login successful",
                    "role": role
                }


            return {
                "success": False,
                "message": "Invalid login details"
            }


        # --------------------------------
        # ADD COMPLAINT
        # --------------------------------

        if action == "add":

            # Lock shared data
            with self.lock:

                complaint = {

                    "id": str(self.next_id),

                    "student": request["student"],

                    "category": request["category"],

                    "description": request["description"],

                    "status": "Pending",

                    "department": "Not Assigned",

                    "created": datetime.now().strftime(
                        "%d-%m-%Y %H:%M"
                    )
                }


                self.next_id += 1

                self.complaints.append(complaint)

                save_complaints(
                    self.complaints
                )


            return {

                "success": True,

                "message":
                    f"Complaint submitted. "
                    f"ID: {complaint['id']}"
            }


        # --------------------------------
        # STUDENT COMPLAINTS
        # --------------------------------

        if action == "student_list":

            result = [

                complaint

                for complaint in self.complaints

                if complaint["student"]
                == request["student"]
            ]


            return {

                "success": True,

                "complaints": result
            }


        # --------------------------------
        # ALL COMPLAINTS
        # --------------------------------

        if action == "all":

            return {

                "success": True,

                "complaints":
                    self.complaints
            }


        # --------------------------------
        # UPDATE COMPLAINT
        # --------------------------------

        if action == "update":

            with self.lock:

                for complaint in self.complaints:

                    if (
                        complaint["id"]
                        == str(request["id"])
                    ):

                        complaint["status"] = \
                            request["status"]

                        complaint["department"] = \
                            request["department"]


                        save_complaints(
                            self.complaints
                        )


                        return {

                            "success": True,

                            "message":
                                "Complaint updated"
                        }


            return {

                "success": False,

                "message":
                    "Complaint not found"
            }


        return {

            "success": False,

            "message":
                "Unknown request"
        }


# --------------------------------
# START SERVER
# --------------------------------

if __name__ == "__main__":

    server = HelpdeskServer()

    server.start()