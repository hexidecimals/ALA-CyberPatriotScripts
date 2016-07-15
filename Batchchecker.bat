@echo off
Forfiles /p C:\ /m *.bat /s /C "cmd /c echo @file @path >> Batch.txt"
Forfiles /p C:\ /m *.php /s /C "cmd /c echo @file @path >> Batch.txt"
Forfiles /p C:\ /m *.cmd /s /C "cmd /c echo @file @path >> Batch.txt"
Forfiles /p C:\ /m *.reg /s /C "cmd /c echo @file @path >> Batch.txt"
start Batch.txt
pause