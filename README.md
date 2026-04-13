# Login_Page
i am creating this login page to solidify my fastapi concepts



🔐 Simple Login Page (FastAPI + HTML + JS)

A basic login system built to understand the core authentication flow between frontend and backend.

This project is intentionally minimal — no frameworks, no database, no overengineering.

🚀 Features
User login form (Email + Password)
Frontend built with HTML, CSS, and JavaScript
Backend built with FastAPI
API communication using fetch()
Hardcoded authentication logic
Displays success/error messages
🧠 Purpose

This project is built to learn:

How frontend sends data to backend
How backend processes requests
How responses are handled in UI
End-to-end login flow (without distractions like databases or frameworks)
📁 Project Structure
project/
│── index.html
│── login_page.css
│── login_page.js
│── main.py   # FastAPI backend
⚙️ How It Works
User enters email and password
JavaScript captures input values
Data is sent to FastAPI using POST request
Backend checks credentials (hardcoded)
Returns success or error response
Frontend displays result
🧪 Sample Credentials
Email: test@gmail.com
Password: 1234
🛠️ Setup & Run
1. Install dependencies
pip install fastapi uvicorn
2. Run FastAPI server
uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000
3. Open frontend

Just open index.html in your browser.

⚠️ Limitations
No database (data is hardcoded)
No password hashing (not secure)
No authentication tokens (JWT/session)
Not production-ready
🔮 Future Improvements
Add database (SQLite/PostgreSQL)
Implement user signup
Hash passwords securely
Add JWT authentication
Build frontend with React
💡 Key Learning

This project focuses on:

Understanding the flow, not building a perfect system.

👨‍💻 Author

Sanidhya Pal
