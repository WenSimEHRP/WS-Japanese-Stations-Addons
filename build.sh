#!/bin/bash
while true
do
    python3 src/stations/generated_stations/templates/generate_templates.py
    python3 get_date.py
    python3 generate_stations.py
    python3 combine.py
    gcc -E -x c -o wsjps.nml wsjps.pnml
    gcc -E -x c -P -o lang/english.lng lang/anglische.lng.template
    nmlc wsjps.nml

    # move to newgrf directory
    # cp wsjps.grf /D/Data/Documents/OpenTTD/newgrf
    read -p "Press any key to continue . . . "
done