# 📋 Student Attendance Tracker

## 📌 About the Project

The Student Attendance Tracker is a beginner-friendly Python application that helps users manage student attendance through a simple graphical user interface (GUI).

Users can add students, mark them as present or absent, view attendance records, and calculate attendance percentages. The attendance data is stored in a CSV file so that recorded information remains available after the application is closed.

## ✨ Features

- Add students to the attendance list.
- Mark students as Present or Absent.
- Record the date of attendance automatically.
- Prevent duplicate attendance entries for the same student on the same day.
- Display attendance records in a table.
- Calculate attendance percentages.
- Store attendance data in a CSV file.
- Simple and user-friendly graphical interface.

## 🛠️ Technologies Used

- **Python 3** — Programming language.
- **Tkinter** — Graphical user interface.
- **CSV module** — Attendance data storage.
- **Datetime module** — Date management.
- **ttk.Treeview** — Display attendance records in a table.

## 📋 Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.
- No additional Python packages required.

## 🚀 How to Run the Project

### Step 1: Download the Project

Download or clone this repository to your computer.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Open the Terminal

Open the integrated terminal in VS Code.

### Step 4: Run the Application

Execute the following command:

```bash
python main.py
```

### Step 5: Manage Attendance

1. Enter a student's name and click **Add Student**.
2. Select the student from the list.
3. Choose Present or Absent.
4. Click **Mark Attendance**.
5. View the attendance records in the table.
6. Select a student and click **Attendance Percentage** to see their attendance summary.

## 📂 Project Structure

```text
Attendance-Tracker/
├── main.py
├── attendance.csv
└── README.md
```

**Note:** The `attendance.csv` file is created automatically when the application runs. It stores the attendance records.

## 📊 Attendance Percentage

The attendance percentage is calculated using the following formula:

```text
Attendance Percentage =
(Number of Present Days / Total Marked Days) × 100
```

For example, if a student is present for 8 days out of 10 marked days:

```text
Attendance Percentage = (8 / 10) × 100 = 80%
```

## 📚 Concepts Learned

- Python functions and variables.
- Conditional statements and loops.
- GUI development using Tkinter.
- Reading and writing CSV files.
- Date handling.
- Data validation.
- Displaying records in tables.
- Calculating percentages.

## 🔮 Future Improvements

- Store student details separately.
- Edit and delete student records.
- Add monthly attendance reports.
- Export attendance reports to Excel.
- Add search and filtering options.
- Create a login system for administrators.
- Generate attendance charts and summaries.

## 👨‍💻 Author

Created as a beginner-friendly Python programming project.

## 📄 License

This project is available for learning and educational purposes.
