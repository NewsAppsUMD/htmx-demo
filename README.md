# htmx-demo

1. mkdir static
2. cd static
3. wget https://unpkg.com/htmx.org@1.9.2/dist/htmx.min.js
4. wget https://raw.githubusercontent.com/dwillis/hhs-snapshots/main/data/team_totals_20230417.csv
5. cd ..
6. pip install Flask peewee sqlite-utils
7. sqlite-utils insert wbb.db team_totals static/team_totals_20230417.csv --csv
6. touch app.py