from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=rosuzaini.database.windows.net;"
    "DATABASE=FAcloud;"
    "UID=rosuzaini;"
    "PWD=admin@1234;"
)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        student_id = request.form["student_id"]
        attendance = request.form["attendance"]
        quiz = request.form["quiz"]

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Performance (StudentID, Attendance, QuizScore)
            VALUES (?, ?, ?)
        """, student_id, attendance, quiz)
        conn.commit()

        return redirect("/")

    return render_template("form.html")

