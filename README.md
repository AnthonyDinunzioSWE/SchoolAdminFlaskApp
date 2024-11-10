Student Management System | 2024
================================

Live Demo
---------

Explore the live demo of the Student Management System [here](https://anthonydinunzioswe.github.io/SchoolAdminFlaskApp) to see the app in action. Feel free to test the login system, view and manage students, professors, and courses.

[Live Demo](https://anthonydinunzioswe.github.io/SchoolAdminFlaskApp)

Overview
--------

Welcome to the **Student Management System**, a web application designed to help manage students, professors, and courses in a university setting. Built with Flask, SQLite, and HTML, this project demonstrates my proficiency in back-end development, database management, and dynamic web page rendering.

### Project Goals:

-   Create a user-friendly platform for managing students, professors, and courses.
-   Implement a secure login system for admin users.
-   Provide the ability to register students, professors, and courses.
-   Enable enrollment of students in courses.
-   Provide an interactive dashboard with real-time data.

Key Features
------------

This project showcases several essential features that demonstrate my skills in building dynamic web applications:

-   **Admin Login**: Secure login page for the admin to access the dashboard.
-   **Student Management**: Register, view, and list students.
-   **Professor Management**: Register and view professors.
-   **Course Management**: Register and view courses, set student limits.
-   **Enrollment System**: Enroll students into courses, ensuring proper course capacity.
-   **Dashboard**: Displays an overview of the total number of students, professors, and courses.
-   **Responsive Design**: Ensures that the app works seamlessly across mobile and desktop devices.

Challenges Overcome
-------------------

Throughout the development of the Student Management System, I encountered a few challenges that helped enhance my skills:

-   **Database Schema Design**: Structuring the database to handle relationships between students, professors, and courses efficiently.
-   **Form Handling**: Handling various user inputs and ensuring data integrity during form submissions.
-   **Dynamic Web Pages**: Rendering dynamic content based on the data fetched from the database.
-   **Security**: Ensuring secure admin login with password verification.

Installation and Usage
----------------------

### Installation

To set up the Student Management System locally, follow these steps:

1.  Clone the repository:

    bash

    Copy code

    `git clone https://github.com/yourusername/student-management-system.git`

2.  Navigate to the project directory:

    bash

    Copy code

    `cd student-management-system`

3.  Set up the database by running:

    bash

    Copy code

    `flask db init
    flask db migrate
    flask db upgrade`

4.  Run the Flask app:

    bash

    Copy code

    `flask run`

5.  Open the app in your browser at `http://127.0.0.1:5000/`.

### Usage

Once you open the app in your browser, you can:

-   **Admin Login**: Enter the admin password to access the dashboard.
-   **Register Entities**: Register new students, professors, or courses via dedicated forms.
-   **View Records**: View lists of students, professors, and courses on the respective pages.
-   **Dashboard**: Access a summary of the data via the dashboard page.
-   **Enrollment**: Enroll students in courses using the enrollment form.

App Structure
-------------

The structure of the Student Management System app is organized for clarity and simplicity:

### **HTML**

-   `index.html`: Login page for admin access.
-   `dashboard.html`: Displays an overview of the system with data on students, professors, and courses.
-   `students.html`: Displays a list of students in the system.
-   `courses.html`: Displays a list of courses in the system.
-   `professors.html`: Displays a list of professors in the system.
-   `register_student.html`: Form to register a new student.
-   `register_course.html`: Form to register a new course.
-   `register_professor.html`: Form to register a new professor.

### **CSS**

-   `styles.css`: Provides styling for the app, including layout, color scheme, and responsive design.

### **JavaScript**

-   `script.js`: Handles interactivity for form submissions and data rendering (if applicable).

### **Python**

-   `app.py`: The main Flask application handling the routes, database models, and logic for the system.

Technologies Used
-----------------

This project demonstrates proficiency in the following technologies:

-   **Flask**: A lightweight web framework for Python used to build the app.
-   **SQLAlchemy**: For ORM-based database interaction and migrations.
-   **SQLite**: The database used to store students, professors, courses, and other information.
-   **HTML5**: Used for structuring the content and elements of the app.
-   **CSS3**: For styling the app and ensuring it is responsive.
-   **Jinja2**: Templating engine used for rendering dynamic content on web pages.

Why This Project?
-----------------

The Student Management System was created to showcase my ability to develop interactive and practical web applications. It highlights my skills in:

-   Building and managing a database with multiple relationships.
-   Using Flask to handle routing, form submissions, and database queries.
-   Implementing secure login and user management systems.
-   Designing responsive web pages that adapt across devices.

Contributing
------------

I welcome contributions to improve the Student Management System. Feel free to fork the repository, make changes, and submit a pull request. Areas where contributions are especially appreciated include:

-   **UI Improvements**: Suggestions for new features or enhancements to the design.
-   **Bug Fixes**: Reporting any bugs or issues that you come across.
-   **Additional Features**: Implementing new ways to customize courses or improve user experience.

Acknowledgments
---------------

Special thanks to:

-   **Flask Documentation** for providing comprehensive guides and resources.
-   **SQLAlchemy** for their ORM capabilities that made database management easy and efficient.

Contact
-------

For any questions, feedback, or suggestions, feel free to reach out to me at:

-   **Email**: your-email@example.com
