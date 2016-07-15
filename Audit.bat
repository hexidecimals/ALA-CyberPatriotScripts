@echo off
Auditpol /set /category:"Account Logon" /Success:enable /failure:enable
Auditpol /set /category:"Logon/Logoff" /Success:enable /failure:enable
Auditpol /set /category:"Account Management" /Success:enable /failure:enable
Auditpol /set /category:"DS Access" /Success:enable /failure:enable
Auditpol /set /category:"Object Access" /Success:enable /failure:enable
Auditpol /set /category:"policy change" /Success:enable /failure:enable
Auditpol /set /category:"Privilege use" /Success:enable /failure:enable
Auditpol /set /category:"System" /Success:enable /failure:enable
Auditpol /set /category:"Process Tracking" /Success:enable /failure:enable
net accounts /MINPWLEN:8
net accounts /MAXPWAGE:30
net accounts /UNIQUEPW:5
net accounts /MINPWAGE:15
echo Set Lockout threshold!!!

pause
exit