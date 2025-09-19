# EDEN Meeting Notes App Launcher
Write-Host "Starting EDEN Meeting Notes App..." -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "Warning: .env file not found" -ForegroundColor Yellow
    Write-Host "Please copy env.template to .env and add your Gemini API key" -ForegroundColor Yellow
    Write-Host ""
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& "venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host ""
Write-Host "Starting the application..." -ForegroundColor Green
python app.py

Read-Host "Press Enter to exit"
