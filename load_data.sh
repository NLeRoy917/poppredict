#!bin/bash

cp assets/schema.db data.db
cd scripts/

python load_tracks.py -n 100000 --db "../data.db"
