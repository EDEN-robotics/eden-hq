@echo off
echo 🌱 Eden HQ - Quick Update Tool
echo ================================
echo.
echo Choose what to update:
echo 1. Mark TODO item as complete
echo 2. Add new roadmap item
echo 3. Open TODO.md for editing
echo 4. Open ROADMAP.md for editing
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Opening TODO.md for editing...
    start notepad TODO.md
) else if "%choice%"=="2" (
    echo.
    echo Opening ROADMAP.md for editing...
    start notepad ROADMAP.md
) else if "%choice%"=="3" (
    echo.
    echo Opening TODO.md for editing...
    start notepad TODO.md
) else if "%choice%"=="4" (
    echo.
    echo Opening ROADMAP.md for editing...
    start notepad ROADMAP.md
) else if "%choice%"=="5" (
    echo Goodbye!
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto :eof
)

pause
