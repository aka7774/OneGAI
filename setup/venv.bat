@echo off

set INSTALL_DIR=%~dp0\..\
cd /d %INSTALL_DIR%
mkdir dl

bitsadmin /transfer nuget https://aka.ms/nugetclidl %INSTALL_DIR%dl\nuget.exe
%INSTALL_DIR%dl\nuget.exe install python -Version 3.10.11 -ExcludeVersion -OutputDirectory .
move python\tools python310
rmdir /s /q python

set PYTHON=%INSTALL_DIR%python310\python.exe
set PATH=%PATH%;%INSTALL_DIR%python310\Scripts
bitsadmin /transfer pip https://bootstrap.pypa.io/get-pip.py %INSTALL_DIR%dl\get-pip.py
%PYTHON% %INSTALL_DIR%dl\get-pip.py

%PYTHON% -m pip install gradio_client gunicorn uvicorn fastapi soundfile psutil pytest pytest-check
