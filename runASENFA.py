import sys
import subprocess
import time
import os

"""
That File for run sender and reciver and open Two Cmd the frist for Reciver and second For sender
"""
# Add PyInstaller temp folder to path when running EXE
if getattr(sys, 'frozen', False):
    sys.path.append(sys._MEIPASS)
# Detect real Python interpreter
python = sys.executable
if python.lower().endswith(".exe") and "python" not in os.path.basename(python).lower():
    # running as compiled .exe, so force use of python.exe
    python = "python"

# Start receiver in a new cmd window
subprocess.Popen(
    f'start "" cmd /k "{python} -c \"from ASENFA import receiver; receiver()\""',
    shell=True
)

time.sleep(1)

# Start sender in another new cmd window
subprocess.Popen(
    f'start "" cmd /k "{python} -c \"from ASENFA import sender; sender()\""',
    shell=True
)
