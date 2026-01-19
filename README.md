# Corporate Leave Management System

A role-based Corporate Leave Management System built using FastAPI, MySQL, and a simple frontend.

## Key Features

### Employee
- Apply for leave
- View personal leave history
- View leave balance (total, used, remaining)

### Manager
- Automatically assigned a team of employees (up to 12 per manager)
- Approve or reject leave requests **only for their team**
- View team-specific statistics (team size, pending leaves, employees on leave)
- Separate Manager Dashboard

### HR
- View all employees and managers
- Drill down into individual manager teams
- View employee leave details (dates, reason, status)
- Company-wide leave statistics

### System Features
- Automatic employee-to-manager assignment (batch system)
- Role-based access control (Employee / Manager / HR)
- Leave balance validation
- Team-based approval restrictions
- RESTful APIs
- Automated testing using pytest

## Tech Stack
- Backend: FastAPI, SQLAlchemy
- Database: MySQL (SQLite used for testing)
- Frontend: HTML, CSS, JavaScript
- Testing: pytest

## How to Run

1. Install dependencies  
   ```bash
   pip install -r requirements.txt

2. Run backend
   uvicorn app.main:app --reload

3. Open frontend HTML files in browser

## Testing
Run all tests:
   pytest -v