@echo off
cd C:\
netstat -a -b -f -o > NetworkStatus.txt
tasklist > Tasklist.txt