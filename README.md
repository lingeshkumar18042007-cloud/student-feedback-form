# Students Feedback System

A complete full-stack web application for collecting and managing student feedback.

## Features
- **Student Feedback Form**: Collects detailed feedback on teaching quality, subject understanding, communication, course content, and overall rating.
- **Admin Dashboard**: Displays all submitted feedback with statistics (total submissions, average rating).
- **Search & Filter**: Find specific feedback by Student ID, Department, Subject, or Faculty Name.
- **Delete Functionality**: Remove feedback records from the dashboard.
- **Responsive UI**: Clean, modern, college-style design that works on mobile and desktop devices.
- **Local SQLite Database**: Automatically created on startup, no extra configuration needed.

## Technologies Used
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python, Flask
- **Database**: SQLite3

## Project Structure
```text
students-feedback-system/
├── app.py                # Main Flask application and database logic
├── database.db           # SQLite database (auto-generated)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── templates/
│   ├── index.html        # Feedback form template
│   └── dashboard.html    # Admin dashboard template
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── script.js     # Client-side validation and interactions
```

## Installation & Setup

1. **Clone or Extract the project folder**
   Ensure you are inside the `students-feedback-system` directory.

2. **Install Requirements**
   Make sure Python is installed. Then install Flask:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Web App**
   Open your web browser and go to:
   - Feedback Form: `http://127.0.0.1:5000/`
   - Admin Dashboard: `http://127.0.0.1:5000/dashboard`

## Explanation

- **Frontend**: The templates (`index.html` and `dashboard.html`) provide the user interface. CSS (`style.css`) ensures a clean, responsive layout. JS (`script.js`) adds client-side validation and confirmation prompts.
- **Backend**: The `app.py` file uses Flask to handle HTTP requests. It receives data from the frontend form and passes it to the database, or retrieves data from the database to render on the dashboard.
- **Database**: We use SQLite3 to persist data locally. The `database.db` file is automatically created with a `feedback` table the first time the app runs.
