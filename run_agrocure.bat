@echo off
echo ======================================================================
echo  AGROCURE AI - AI-Based Plant Disease Detection System
echo  CSE College Final Year Project
echo  Supported Crops: Tomato (10), Potato (3), Capsicum (2), Grapes (4)
echo  Languages: English, Hindi, Kannada, Marathi, Tamil
echo ======================================================================
echo.
cd /d "%~dp0"
echo Starting AGROCURE AI Server at http://127.0.0.1:5000 ...
python -m uvicorn backend.app_server:app --host 127.0.0.1 --port 5000 --reload
pause
