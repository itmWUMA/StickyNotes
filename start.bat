@echo off

echo Starting Flask backend...
start cmd /k "cd backend && python app.py"

echo Starting Vue frontend...
start cmd /k "cd frontend && npm install && npm run dev"

echo Project started.
echo You can access the frontend at http://localhost:5173/