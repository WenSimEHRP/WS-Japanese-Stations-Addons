@echo off
:start
py get_date.py
py combine.py
py generate_stations.py
gcc -E -x c -o wsjps.nml wsjps_indexes.pnml
gcc -E -x c -P -o lang\english.lng lang\anglische.lng.template
::nmlc wsjps.nml

:: move to newgrf directory
rem copy wsjps.grf D:\Data\Documents\OpenTTD\newgrf
pause
:: debug purpose, goto start to run again
goto start