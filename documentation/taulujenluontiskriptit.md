# Taulujen luonti skriptit  

- User-taulu (tiedot rekistyneistä käyttäjistä):

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

- Task-taulu (tiedot käyttäjien tekemistä taskeista):  

```sql
CREATE TABLE task (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(30) NOT NULL, 
        state VARCHAR(20) NOT NULL, 
        active BOOLEAN NOT NULL, 
        archived BOOLEAN NOT NULL, 
        description VARCHAR(144) NOT NULL, 
        start_date DATETIME, 
        end_date DATETIME, 
        deadline DATETIME, 
        user_id INTEGER NOT NULL, 
        project_id INTEGER, 
        PRIMARY KEY (id), 
        CHECK (active IN (0, 1)), 
        CHECK (archived IN (0, 1)), 
        FOREIGN KEY(user_id) REFERENCES user (id), 
        FOREIGN KEY(project_id) REFERENCES project (id)
);
```  

- Project-taulu (tiedot luoduista projekteista):  

```sql
CREATE TABLE project (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(30) NOT NULL, 
        active BOOLEAN NOT NULL, 
        user_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (active IN (0, 1)), 
        FOREIGN KEY(user_id) REFERENCES user (id)
);
```  

- Label-taulu (tiedot tehdyistä labeleista):  

```sql
CREATE TABLE label (
        id INTEGER NOT NULL, 
        name VARCHAR(30), 
        PRIMARY KEY (id)
);
```  

- TaskLabels-taulu (välitaulu many-to-many Task-Label joinin välille):

```sql
CREATE TABLE tasklabels (
        task_id INTEGER, 
        label_id INTEGER, 
        FOREIGN KEY(task_id) REFERENCES task (id), 
        FOREIGN KEY(label_id) REFERENCES label (id)
);
```  
