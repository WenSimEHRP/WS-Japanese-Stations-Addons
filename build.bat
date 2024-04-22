@echo off
:start
py src\stations\generated_stations\templates\generate_templates.py
py get_date.py
py generate_stations.py
py combine.py
gcc -E -x c -o wins.nml wins.pnml
gcc -E -x c -P -o lang\english.lng lang\anglische.lng.template
nmlc wins.nml
rem nmlc -s wins.nml

:: move to newgrf directory
copy wins.grf D:\Data\Documents\OpenTTD\newgrf
pause
:: debug purpose, goto start to run again
goto start