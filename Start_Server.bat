@echo off
call %HOMEPATH%\.virtualenvs\djangotut\scripts\activate
py manage.py runserver
cmd /k