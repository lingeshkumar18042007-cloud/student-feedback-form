import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages
DB_FILE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            department TEXT NOT NULL,
            year TEXT NOT NULL,
            semester TEXT NOT NULL,
            subject TEXT NOT NULL,
            faculty_name TEXT NOT NULL,
            teaching_quality INTEGER NOT NULL,
            subject_understanding INTEGER NOT NULL,
            communication INTEGER NOT NULL,
            course_content INTEGER NOT NULL,
            overall_rating INTEGER NOT NULL,
            comments TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            student_name = request.form['student_name']
            student_id = request.form['student_id']
            department = request.form['department']
            year = request.form['year']
            semester = request.form['semester']
            subject = request.form['subject']
            faculty_name = request.form['faculty_name']
            teaching_quality = int(request.form['teaching_quality'])
            subject_understanding = int(request.form['subject_understanding'])
            communication = int(request.form['communication'])
            course_content = int(request.form['course_content'])
            overall_rating = int(request.form['overall_rating'])
            comments = request.form['comments']

            conn = get_db_connection()
            conn.execute('''
                INSERT INTO feedback (student_name, student_id, department, year, semester, subject, faculty_name, teaching_quality, subject_understanding, communication, course_content, overall_rating, comments)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (student_name, student_id, department, year, semester, subject, faculty_name, teaching_quality, subject_understanding, communication, course_content, overall_rating, comments))
            conn.commit()
            conn.close()
            
            flash('Feedback submitted successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('index'))
            
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    
    # Handle search/filter
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        feedbacks = conn.execute('''
            SELECT * FROM feedback 
            WHERE student_id LIKE ? OR department LIKE ? OR subject LIKE ? OR faculty_name LIKE ?
            ORDER BY created_at DESC
        ''', ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%')).fetchall()
    else:
        feedbacks = conn.execute('SELECT * FROM feedback ORDER BY created_at DESC').fetchall()
    
    # Calculate stats
    total_feedbacks = len(feedbacks)
    average_rating = 0
    if total_feedbacks > 0:
        total_rating = sum([f['overall_rating'] for f in feedbacks])
        average_rating = round(total_rating / total_feedbacks, 1)

    conn.close()
    return render_template('dashboard.html', feedbacks=feedbacks, total_feedbacks=total_feedbacks, average_rating=average_rating, search_query=search_query)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_feedback(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM feedback WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Feedback deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
