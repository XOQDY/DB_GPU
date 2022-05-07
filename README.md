# DB_GPU
## Create database and table schema
By using the sqlite3 command
``` 
sqlite3 warehouse.db < gpu_database.schema
```
If you can't use the command above use can try use this code instead
```
sqlite3 warehouse.db -init gpu_database.schema
```
And when you create it successful the command will appear like this
```sql
sqlite> I
```
If it doesn't appear like the above use can open database by the following command
* Open database by using ```sqlite3 warehouse.db```
## Import data from csv to the database
When you done create database and in the sqlite and you need to import the data from ```.csv``` file into a specific table then following the step down belown.
```sql
sqlite> .mode csv
sqlite> .import data/GrapichsCard.csv gpu
sqlite> .import data/Warehouse.csv warehouse
```
## Configure and run the application
For now we don't have GUI or Website to see the result but you can see the query and data by use
```
python main.py run
```
## Project Documents
[Diagram](../../wiki/Diagram)  
[API](../../wiki/Web%20Service%20API)
