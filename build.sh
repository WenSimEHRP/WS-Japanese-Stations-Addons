#!/bin/bash
python3 src/stations/generated_stations/templates/generate_templates.py
python3 get_date.py
python3 generate_stations.py
python3 combine.py
gcc -E -x c -o wins.nml wins.pnml
gcc -E -x c -P -o lang/english.lng lang/anglische.lng.template
nmlc wins.nml