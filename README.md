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
## Domain class diagram
![UML class](https://user-images.githubusercontent.com/78094325/165640172-543216b6-a0ca-4888-bc11-d639ede2dc14.png)
## Design class diagram
![design class](https://user-images.githubusercontent.com/78094325/165640025-67368872-354b-4a0b-a1f2-35769a7424c5.png)
## Package class diagram
![package class](https://user-images.githubusercontent.com/78094325/165644105-1a0c02b5-48d9-470e-ae5e-76b94bcce30d.png)
