@echo off
:loop
echo Please confirm the directory of gitbook
echo Your current directory is %cd%
set /p confirm=input (yes/no):
echo %confirm%
if %confirm% EQU yes (goto :yes) else (goto :no)
:no
echo Invalid input, please try again
goto loop

rem if yes break the loop, else return to the loop
:yes
echo You have confirmed the directory of gitbook %CD%

rem create your summary file
python md_to_gitbook.py
echo SUMMARY.md has been created

if exist "docs" (rmdir /s /q "docs")

gitbook init && gitbook build && ren "_book" "docs"