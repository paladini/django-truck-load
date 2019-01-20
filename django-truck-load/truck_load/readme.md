
## Importing datasets to database

In order to import `trucks.csv` and `cargos.csv` into our PostgreSQL database, run the following commands:

```
python manage.py populate_trucks "../../challenge/trucks.csv"
python manage.py populate_loads "../../challenge/cargo.csv"
```