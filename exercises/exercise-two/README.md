# Exercise Two

## Summary

The objective of this exercise is to spin up a Python Flask application and a postgres database all as part of one command using a Docker Compose file. When the application is hit in the browser it should return a string with a value stored in a table in the postgres database.

NOTE: In order to run the database initialisation script you will need to delete the pg-data directory first.

```
docker-compose up --build
```