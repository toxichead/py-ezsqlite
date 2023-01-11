# Py-EzSQLite
Want easy work with SQLite3 in Python? This simple facade can help you!

Simple usage:
```python
from ezsqlite import EzSQLite
db = EzSQLite("mybrandnew.db")
```

Query usage:
```python
# ...
query = db.query("...")
if query['status'] == True:
  # doing something with query when all 's okay
  # if you use SELECT, query returns selected info in 'details' index
else:
  # if something went wrong query will return error in 'details' index
```
