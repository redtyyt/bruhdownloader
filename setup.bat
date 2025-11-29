@echo off
setlocal

echo This batch file should be used to install required libs, softwares and modules. Please answer correctly to the questions or the app could crash.

:Prompt
set /p userIn="Do you have python installed on your pc? (y/n) >> "

if "%userIn%"=="y" ()
else if "%userIn%"=="n" (
  echo Installing python for you with winget.

  winget install -e --id Python.Python.3.11 --scope machine
) else (
  echo Invalid input. Write y or n for yes or no.
  goto Prompt
)

endlocal
