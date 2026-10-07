# Smart Campus Helpdesk

A Python-based **client-server complaint management system** designed to help students report and track campus-related issues such as hostel problems, mess issues, classroom problems, Wi-Fi problems, and electrical complaints.

The project demonstrates important Python concepts from **GUI development, event-driven programming, file handling, multithreading, networking, and client-server programming**.

---

## 📌 Problem Statement

Students often face different problems on campus related to:

* Hostel facilities
* Mess services
* Classrooms
* Internet/Wi-Fi
* Electrical equipment
* Other campus facilities

In a traditional system, students may have to contact different departments manually, making it difficult to track the progress of a complaint.

The **Smart Campus Helpdesk** provides a centralized system where:

1. Students can submit complaints.
2. Students can view the status of their complaints.
3. Administrators can view all complaints.
4. Administrators can assign departments.
5. Administrators can update complaint status.

---

## 🎯 Objectives

* Create a simple digital complaint management system.
* Provide a graphical interface using **Tkinter**.
* Implement **event-driven programming** using buttons and GUI events.
* Demonstrate **client-server communication** using Python sockets.
* Handle multiple clients using **multithreading**.
* Store complaint data using **JSON file handling**.
* Provide separate interfaces for students and administrators.

---

## 🛠️ Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Main programming language      |
| Tkinter            | Graphical User Interface       |
| Socket Programming | Client-server communication    |
| Multithreading     | Handling multiple clients      |
| JSON               | Data storage and communication |
| File Handling      | Persistent complaint storage   |
| TCP                | Network communication          |

No external database or web framework is required.

---

## 📂 Project Structure

```text
Smart_Campus_Helpdesk/
│
├── config.py
├── storage.py
├── server.py
├── client.py
├── student_gui.py
├── admin_gui.py
├── main.py
├── run_server.py
└── README.md
```

---

## 👥 Team Member Responsibilities

The project is divided into six major sections so that each team member can explain a separate part.

### Member 1 — Server & Networking

**File:** `server.py`

Responsible for:

* Creating the TCP server
* Accepting client connections
* Processing client requests
* Multithreading
* Complaint management
* Login verification
* Sending responses to clients

Main concepts:

* `socket`
* `threading`
* TCP communication
* Client-server architecture

---

### Member 2 — Client Networking

**Files:**

* `client.py`
* `config.py`

Responsible for:

* Connecting the GUI to the server
* Sending requests
* Receiving responses
* JSON conversion
* Server IP and port configuration

Main concepts:

* Socket client
* JSON
* Network communication
* Exception handling

---

### Member 3 — Student GUI

**File:** `student_gui.py`

Responsible for the student interface.

Features:

* Complaint submission
* Category selection
* Complaint description
* Complaint status table
* Refreshing complaints
* Message boxes

Main concepts:

* Tkinter
* Labels
* Buttons
* Text widgets
* Combobox
* Treeview
* Event-driven programming
* GUI threading

---

### Member 4 — Admin GUI

**File:** `admin_gui.py`

Responsible for the administrator dashboard.

Features:

* View all complaints
* Select complaints
* Assign departments
* Change complaint status
* Refresh complaint list

Main concepts:

* Tkinter
* Treeview
* Combobox
* Buttons
* Event handling
* Multithreading

---

### Member 5 — File Handling

**File:** `storage.py`

Responsible for persistent complaint storage.

Functions:

```python
load_complaints()
save_complaints()
```

The system stores complaints in:

```text
complaints.json
```

Main concepts:

* File handling
* JSON
* Reading files
* Writing files
* Exception handling

---

### Member 6 — Application Integration

**Files:**

* `main.py`
* `run_server.py`

Responsible for:

* Login screen
* Role selection
* Opening the correct dashboard
* Connecting all modules
* Starting the server

Main concepts:

* Tkinter
* Functions
* Classes
* Modules
* Application flow

---

# 🔄 System Architecture

```text
                    SMART CAMPUS HELPDESK
                           │
                           ▼
                    ┌──────────────┐
                    │ Login Screen │
                    └──────┬───────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          ┌─────────────┐      ┌─────────────┐
          │   Student   │      │    Admin    │
          │     GUI     │      │     GUI     │
          └──────┬──────┘      └──────┬──────┘
                 │                    │
                 └─────────┬──────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Client    │
                    │   Socket     │
                    └──────┬───────┘
                           │
                     TCP / JSON
                           │
                           ▼
                    ┌──────────────┐
                    │    Server    │
                    │    Socket    │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │              │
                    ▼              ▼
             ┌─────────────┐ ┌─────────────┐
             │  Complaint  │ │ Multithread │
             │  Processing │ │   Handling  │
             └──────┬──────┘ └─────────────┘
                    │
                    ▼
             ┌─────────────┐
             │ complaints  │
             │    .json    │
             └─────────────┘
```

---

# 🔑 Main Features

## 1. Student Login

Students can log into the system using their credentials.

Demo account:

```text
Username: raghav
Password: 1234
Role: Student
```

Another student account:

```text
Username: student
Password: 1234
Role: Student
```

---

## 2. Admin Login

Administrator credentials:

```text
Username: admin
Password: admin123
Role: Admin
```

---

## 3. Submit Complaint

Students can select a complaint category:

```text
Hostel
Mess
Classroom
Internet/Wi-Fi
Electrical
Other
```

They can then enter a description of the problem and submit it.

---

## 4. Complaint Tracking

Every complaint receives a unique complaint ID.

Example:

```text
Complaint ID: 1001
```

The initial status is:

```text
Pending
```

---

## 5. Admin Dashboard

The administrator can view:

* Complaint ID
* Student
* Category
* Description
* Status
* Department

---

## 6. Complaint Status

The administrator can change the complaint status to:

```text
Pending
In Progress
Resolved
```

---

## 7. Department Assignment

The administrator can assign a complaint to:

```text
Hostel Department
Mess Department
Academic Department
IT Department
Electrical Department
Administration
```

---

# 💾 Data Storage

The project uses a JSON file instead of a database.

The file is:

```text
complaints.json
```

Example data:

```json
[
    {
        "id": "1001",
        "student": "raghav",
        "category": "Internet/Wi-Fi",
        "description": "Wi-Fi is not working in the hostel.",
        "status": "In Progress",
        "department": "IT Department",
        "created": "07-10-2026 19:30"
    }
]
```

This demonstrates Python's **file handling and JSON processing**.

---

# 🌐 Client-Server Communication

The project follows a basic client-server architecture.

The server runs on:

```text
127.0.0.1:5000
```

The client connects to the server using TCP sockets.

Communication flow:

```text
Student/Admin GUI
       │
       ▼
   client.py
       │
       │ JSON Request
       ▼
   server.py
       │
       ▼
Process Request
       │
       ▼
   JSON Response
       │
       ▼
   client.py
       │
       ▼
      GUI
```

---

# 🧵 Multithreading

The server uses a separate thread for each connected client.

Example:

```python
thread = threading.Thread(
    target=self.handle_client,
    args=(client,),
    daemon=True
)

thread.start()
```

This allows the server to handle multiple clients without blocking the entire application.

The GUI also uses background threads for network operations so that the interface remains responsive.

---

# 🖥️ Tkinter GUI

The project uses Python's built-in **Tkinter** module.

Important widgets used include:

* `Label`
* `Button`
* `Entry`
* `Text`
* `Combobox`
* `Treeview`
* `Frame`
* `LabelFrame`
* `messagebox`

Example:

```python
tk.Button(
    root,
    text="LOGIN",
    command=self.login
)
```

The button triggers the `login()` function when the user clicks it.

This demonstrates **event-driven programming**.

---

# ⚙️ Installation

## Requirements

Python 3.x is required.

Tkinter is normally included with standard Python installations on Windows.

Check Python installation:

```bash
python --version
```

---

# ▶️ How to Run

The project requires **two terminals**.

## Step 1 — Start the Server

Open the project folder in Terminal 1 and run:

```bash
python run_server.py
```

You should see:

```text
======================================
 SMART CAMPUS HELPDESK SERVER
======================================
Server running on 127.0.0.1:5000
Waiting for clients...
```

---

## Step 2 — Start the Application

Open another terminal in the same project folder:

```bash
python main.py
```

The login window will appear.

---

# 🔐 Login Credentials

### Student

```text
Username: raghav
Password: 1234
Role: Student
```

### Admin

```text
Username: admin
Password: admin123
Role: Admin
```

---

# 🧪 Example Workflow

### Student

```text
Login
  ↓
Student Dashboard
  ↓
Select Category
  ↓
Enter Complaint
  ↓
Submit Complaint
  ↓
Complaint ID Generated
  ↓
Status = Pending
```

### Admin

```text
Login
  ↓
Admin Dashboard
  ↓
View Complaints
  ↓
Select Complaint
  ↓
Assign Department
  ↓
Change Status
  ↓
Update Complaint
```

### Student Tracking

After the administrator updates a complaint:

```text
Pending
   ↓
In Progress
   ↓
Resolved
```

The student can refresh the dashboard and see the updated status.

---

# 📚 Python Concepts Demonstrated

This project demonstrates several important Python concepts.

### GUI

```text
Tkinter
Widgets
Layouts
Dialogs
Event-driven programming
```

### File Handling

```text
open()
read
write
JSON
Exception handling
```

### Networking

```text
Socket
TCP
Client
Server
IP address
Port
```

### Multithreading

```text
threading.Thread()
Background tasks
Concurrent client handling
```

### Object-Oriented Programming

The project uses classes such as:

```python
HelpdeskServer
StudentGUI
AdminGUI
LoginGUI
```

### Modules

The project is divided into multiple Python modules:

```text
config.py
storage.py
server.py
client.py
student_gui.py
admin_gui.py
main.py
```

This makes the project easier to understand and maintain.

---

# 📈 Advantages

* Simple and easy-to-use interface
* Centralized complaint management
* Complaint tracking
* Separate student and admin roles
* Persistent data storage
* Demonstrates client-server architecture
* Supports multiple clients through multithreading
* Uses only Python and built-in modules
* Easy to demonstrate during a presentation

---

# ⚠️ Limitations

This is an academic demonstration project.

Current limitations include:

* Login credentials are hard-coded.
* Data is stored in a JSON file instead of a database.
* The server runs locally.
* No encryption is implemented.
* No email/SMS notification system is included.
* Authentication is basic.
* The system does not yet provide advanced analytics.

These limitations can be discussed as possible future improvements.

---

# 🚀 Future Enhancements

Possible future improvements include:

1. **Database Integration**

   * MySQL
   * PostgreSQL

2. **Secure Authentication**

   * Password hashing
   * User registration
   * Session management

3. **Notification System**

   * Email notifications
   * Complaint resolution alerts

4. **Advanced Admin Dashboard**

   * Complaint statistics
   * Charts
   * Department-wise analysis

5. **Deployment**

   * Deploy the server on a campus network or cloud server.

6. **Web Application**

   * Create a web-based version of the system.

7. **Priority Management**

   * Low
   * Medium
   * High
   * Critical

---

# 🎓 Academic Relevance

The project demonstrates concepts related to Python GUI, event-driven programming, file handling, multithreading, networking, and client/server programming.

It is therefore designed primarily as a **Module 5 Python Programming project** and focuses on demonstrating the concepts rather than building a production-level enterprise system.

---

# 👨‍💻 Team Project

**Project:** Smart Campus Helpdesk

**Type:** Python Client-Server Application

**Interface:** Tkinter GUI

**Communication:** TCP Socket Programming

**Storage:** JSON File

**Concurrency:** Python Multithreading

**Domain:** Smart Campus / Complaint Management

---

## ⭐ Conclusion

The **Smart Campus Helpdesk** provides a simple centralized platform for managing student complaints.

It combines:

```text
Python
   +
Tkinter
   +
File Handling
   +
Socket Programming
   +
Client-Server Architecture
   +
Multithreading
```

The project demonstrates how these Python concepts can be combined to solve a practical campus problem in a simple and understandable way.
