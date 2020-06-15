# Taulujen luonti skriptit  

- User-taulu:

```sql
CREATE TABLE user (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        username VARCHAR(30) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        role VARCHAR(5) NOT NULL, 
        PRIMARY KEY (id)
);
```
