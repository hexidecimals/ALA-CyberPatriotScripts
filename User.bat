@echo off
:neg
set /p x=Unauthorized Name?:
if not defined %%x%% GOTO :one
net localgroup administrators %%x%% /delete
:one
set /p a=Delete User?:
if not defined %%a%% GOTO :two
net user %%a%% /DELETE
:two
set /p b=More users or admin delete?:
IF /I "%%b%%"=="users" GOTO :one
IF /I "%%b%%"=="admin" GOTO :neg

