@echo off
:start
py get_date.py
py generate_stations.py
py combine.py
gcc -E -x c -o wsjps.nml wsjps.pnml
gcc -E -x c -P -o lang\english.lng lang\anglische.lng.template
nmlc wsjps.nml

:: move to newgrf directory
copy wsjps.grf D:\Data\Documents\OpenTTD\newgrf
pause
:: debug purpose, goto start to run again
goto start