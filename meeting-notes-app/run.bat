@echo off
echo Starting EDEN Meeting Notes App...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo Warning: .env file not found
    echo Please copy env.template to .env and add your Gemini API key
    echo.
)

REM Install dependencies if needed
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting the application...
python app.py

pause

