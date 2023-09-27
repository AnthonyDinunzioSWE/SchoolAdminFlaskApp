# Imports
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy and Migrate extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    date_of_birth = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    min_students = db.Column(db.Integer)
    max_students = db.Column(db.Integer)
    active = db.Column(db.String(200), nullable=False)


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(600), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float)


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))


class ProfessorAssignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    professor = db.relationship('Professor', backref=db.backref('assignments', lazy=True))
    course = db.relationship('Course', backref=db.backref('assignments', lazy=True))


class AdminPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))


a_password = AdminPassword
a_password.password = "testpass123"


def create_tables():
    db.create_all()


# Login Route (Admin Password Entry)
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("USER ENTERED AN ADMIN PASSWORD TO ATTEMPT LOGIN")
        entered_password = request.form['admin']
        if entered_password == a_password.password:
            print("YOU ENTERED THE RIGHT PASSWORD MOVING YOU TO THE DASHBOARD")
            return render_template("dashboard.html")
        else:
            print("THE PASSWORD YOU ENTERED WAS INCORRECT TRY AGAIN!")
            return render_template('error.html'), 400

    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    num_students = Student.query.count()
    num_professors = Professor.query.count()
    num_courses = Course.query.count()

    current_date = datetime.now().strftime("%Y-%m-%d")

    return render_template("dashboard.html", num_students=num_students, num_professors=num_professors,
                           num_courses=num_courses, current_date=current_date)


@app.route("/students")
def students():
    students = Student.query.all()
    return render_template("students.html", students=students)


@app.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("courses.html", courses=courses)


@app.route("/professors")
def professors():
    professors = Professor.query.all()
    return render_template("professors.html", professors=professors)



@app.route("/register_student", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        # Get data from the form
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        date_of_birth = request.form.get("date_of_birth")
        address = request.form.get("address")
        phone_number = request.form.get("phone_number")

        # Create a new Student object and add it to the database
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            address=address,
            phone_number=phone_number,
        )
        db.session.add(new_student)
        db.session.commit()

        # Redirect to the Students page after registration
        return redirect("/students")

    return render_template("register_student.html")


@app.route("/register_course", methods=["GET", "POST"])
def register_course():
    if request.method == "POST":
        # Get data from the form
        name = request.form.get("name")
        min_students = int(request.form.get("min_students"))
        max_students = int(request.form.get("max_students"))
        active = request.form.get("active")

        # Create a new course object and add it to the database
        course = Course(name=name, min_students=min_students, max_students=max_students, active=active)
        db.session.add(course)
        db.session.commit()

        # Redirect to the courses page after registration
        return redirect(url_for("courses"))

    return render_template("register_course.html")


@app.route("/register_professor", methods=["GET", "POST"])
def register_professor():
    if request.method == "POST":
        # Get data from the form
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        date_of_birth = request.form.get("date_of_birth")
        address = request.form.get("address")
        phone_number = request.form.get("phone_number")
        salary = float(request.form.get("salary"))

        # Create a new professor object and add it to the database
        professor = Professor(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, address=address, phone=phone_number, salary=salary)
        db.session.add(professor)
        db.session.commit()

        # Redirect to the professors page after registration
        return redirect(url_for("professors"))

    return render_template("register_professor.html")



@app.route("/enroll_student", methods=["GET", "POST"])
def enroll_student():
    if request.method == "POST":
        # Get the selected course and student IDs from the form
        course_id = request.form.get("course")
        student_id = request.form.get("student")

        # Check if the enrollment relationship already exists
        existing_enrollment = Enrollment.query.filter_by(course_id=course_id, student_id=student_id).first()

        if existing_enrollment:
            # Enrollment relationship already exists, you can handle this case as needed
            # For now, we'll redirect to the students page
            return redirect(url_for("students"))
        else:
            # Create a new enrollment relationship in the database
            enrollment = Enrollment(course_id=course_id, student_id=student_id)
            db.session.add(enrollment)
            db.session.commit()

            # Redirect to the students page after enrollment
            return redirect(url_for("students"))

    # Fetch the courses and students from the database for the dropdowns
    courses = Course.query.all()
    students = Student.query.all()

    return render_template("enroll_student.html", courses=courses, students=students)


@app.route("/assign_professor", methods=["GET", "POST"])
def assign_professor():
    if request.method == "POST":
        # Get the selected course and professor IDs from the form
        course_id = request.form.get("course")
        professor_id = request.form.get("professor")

        # Check if the assignment relationship already exists
        existing_assignment = ProfessorAssignments.query.filter_by(course_id=course_id, professor_id=professor_id).first()

        if existing_assignment:
            # Assignment relationship already exists, you can handle this case as needed
            # For now, we'll redirect to the courses page
            return redirect(url_for("courses"))
        else:
            # Create a new assignment relationship in the database
            assignment = ProfessorAssignments(course_id=course_id, professor_id=professor_id)
            db.session.add(assignment)
            db.session.commit()

            # Redirect to the courses page after assignment
            return redirect(url_for("courses"))

    # Fetch the courses and professors from the database for the dropdowns
    courses = Course.query.all()
    professors = Professor.query.all()

    return render_template("assign_professor.html", courses=courses, professors=professors)


@app.route("/delete_student/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect("/students")


@app.route("/edit_student/<int:student_id>")
def edit_student(student_id):
    student = Student.query.get(student_id)
    if student:
        # Redirect to the registration page with the student data pre-filled
        return render_template("register_student.html", student=student)
    else:
        # Handle the case where the student does not exist
        return "Student not found", 404


if __name__ == '__main__':
    with app.app_context():
        create_tables()
        app.run(debug=True)

