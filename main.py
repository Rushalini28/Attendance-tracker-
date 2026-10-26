
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path
from datetime import date

# File used to store attendance records
DATA_FILE = Path(__file__).parent / "attendance.csv"

# Create the CSV file if it does not exist
if not DATA_FILE.exists():
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Student Name", "Date", "Status"])


def load_records():
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_student():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Missing Name", "Enter a student name.")
        return

    # Avoid adding the same student twice
    for record in load_records():
        if record["Student Name"].lower() == name.lower():
            messagebox.showwarning(
                "Already Exists",
                "This student already has an attendance record."
            )
            return

    # Add an initial record with no attendance marked
    name_entry.delete(0, tk.END)
    messagebox.showinfo(
        "Student Added",
        f"{name} has been added. Select the student and mark attendance."
    )

    # Store student names in a separate list in memory
    if name.lower() not in [student.lower() for student in students]:
        students.append(name)
        refresh_students()


def refresh_students():
    student_list.delete(0, tk.END)
    for student in students:
        student_list.insert(tk.END, student)


def mark_attendance():
    selection = student_list.curselection()

    if not selection:
        messagebox.showwarning(
            "Select Student",
            "Please select a student first."
        )
        return

    name = student_list.get(selection[0])
    status = attendance_var.get()
    today = date.today().isoformat()

    records = load_records()

    # Prevent duplicate attendance for the same student on the same day
    for record in records:
        if record["Student Name"].lower() == name.lower():
            if record["Date"] == today:
                messagebox.showwarning(
                    "Already Marked",
                    "Attendance has already been marked for this student today."
                )
                return

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, today, status])

    refresh_records()
    messagebox.showinfo("Success", f"{name} marked {status}.")


def refresh_records():
    for item in records_table.get_children():
        records_table.delete(item)

    records = load_records()

    for record in records:
        records_table.insert(
            "",
            tk.END,
            values=(
                record["Student Name"],
                record["Date"],
                record["Status"]
            )
        )


def show_percentage():
    selection = student_list.curselection()

    if not selection:
        messagebox.showwarning(
            "Select Student",
            "Please select a student first."
        )
        return

    name = student_list.get(selection[0])
    records = load_records()

    student_records = [
        record for record in records
        if record["Student Name"].lower() == name.lower()
    ]

    total = len(student_records)
    present = sum(
        1 for record in student_records
        if record["Status"] == "Present"
    )

    if total == 0:
        percentage = 0
    else:
        percentage = (present / total) * 100

    messagebox.showinfo(
        "Attendance Percentage",
        f"Student: {name}\n"
        f"Present: {present}\n"
        f"Total marked days: {total}\n"
        f"Attendance: {percentage:.2f}%"
    )


# Main application window
root = tk.Tk()
root.title("Student Attendance Tracker")
root.geometry("780x600")
root.configure(bg="#f0f4f8")

students = []

title = tk.Label(
    root,
    text="Student Attendance Tracker",
    font=("Arial", 22, "bold"),
    bg="#f0f4f8",
    fg="#183153"
)
title.pack(pady=15)

# Add student section
add_frame = tk.Frame(root, bg="#f0f4f8")
add_frame.pack(pady=5)

tk.Label(
    add_frame,
    text="Student Name:",
    font=("Arial", 11),
    bg="#f0f4f8"
).pack(side=tk.LEFT, padx=5)

name_entry = tk.Entry(add_frame, font=("Arial", 11), width=25)
name_entry.pack(side=tk.LEFT, padx=5)

tk.Button(
    add_frame,
    text="Add Student",
    command=add_student,
    bg="#2563eb",
    fg="white"
).pack(side=tk.LEFT, padx=5)

# Student list and attendance controls
main_frame = tk.Frame(root, bg="#f0f4f8")
main_frame.pack(pady=10)

tk.Label(
    main_frame,
    text="Students",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
).grid(row=0, column=0, pady=5)

student_list = tk.Listbox(
    main_frame,
    width=28,
    height=10,
    font=("Arial", 11),
    exportselection=False
)
student_list.grid(row=1, column=0, padx=15)

controls = tk.Frame(main_frame, bg="#f0f4f8")
controls.grid(row=1, column=1, padx=15)

tk.Label(
    controls,
    text="Attendance Status",
    font=("Arial", 11, "bold"),
    bg="#f0f4f8"
).pack(pady=5)

attendance_var = tk.StringVar(value="Present")

tk.Radiobutton(
    controls,
    text="Present",
    variable=attendance_var,
    value="Present",
    bg="#f0f4f8"
).pack(anchor="w")

tk.Radiobutton(
    controls,
    text="Absent",
    variable=attendance_var,
    value="Absent",
    bg="#f0f4f8"
).pack(anchor="w")

tk.Button(
    controls,
    text="Mark Attendance",
    command=mark_attendance,
    bg="#15803d",
    fg="white"
).pack(pady=10)

tk.Button(
    controls,
    text="Attendance Percentage",
    command=show_percentage,
    bg="#7c3aed",
    fg="white"
).pack(pady=5)

# Attendance records table
tk.Label(
    root,
    text="Attendance Records",
    font=("Arial", 13, "bold"),
    bg="#f0f4f8"
).pack(pady=(10, 5))

records_table = ttk.Treeview(
    root,
    columns=("Name", "Date", "Status"),
    show="headings",
    height=8
)

records_table.heading("Name", text="Student Name")
records_table.heading("Date", text="Date")
records_table.heading("Status", text="Status")

records_table.column("Name", width=250)
records_table.column("Date", width=200)
records_table.column("Status", width=150)

records_table.pack(padx=15, fill="x")

# Load previously saved records
for record in load_records():
    name = record["Student Name"]
    if name.lower() not in [student.lower() for student in students]:
        students.append(name)

refresh_students()
refresh_records()

root.mainloop()
