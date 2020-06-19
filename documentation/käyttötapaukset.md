# Käyttötapaukset / SQL-lauseet

## Käyttäjät  
- Käyttäjän luominen / poistaminen

```sql
INSERT INTO user (username, password, role, date_created, date_modified)
VALUES (?, ?, 'USER', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
```   

```sql
DELETE FROM user WHERE user.id = ?
```   

- Admin käyttäjä pystyy lisätä admin oikeudet muille käyttäjille

## Taskit  
- Käyttäjä luoda itselleen taskeja.  

```sql
INSERT INTO task (user_id, name, active, archived, deadline, description , data_created, date_modified)
VALUES (user.id, ?, 0, 0, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
```   

- Käyttäjä voi päivittää olemassa olevia taskeja.  

```sql
UPDATE task  
SET (name = ?, state = ?, labels = ?, deadline = ?, description = ?, data_modified = CURRENT_TIMESTAMP)
WHERE task.id = ?, task.user_id = user.id
```   

- Käyttäjä voi poistaa olemassa olevia taskeja. 

```sql
DELETE FROM task WHERE task.id = ?
```   

- Käyttäjä voi arkistoida valmiita taskeja.

```sql
UPDATE task
SET (archived = 1)
WHERE task.id = ?, task.user_id = user.id
```   

- Taskeja voidaan kategorisoida tageilla.

- Taskeille voi asettaa aikarajoja.

## Projektit
- Taskeista voidaan luoda yhteisiä kokonaisuuksia eli projekteja. 

```sql
INSERT INTO project (user_id, name, active, date_created, date_modified)
VALUES (user.id, ?, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
```   

- Projektille voi lisätä taskeja sekä poistaa taskeja.  

```sql
UPDATE project  
SET (project.task_id = ?)
WHERE project.id = ?
```   

- Käyttäjä voi listata projektilla olevat taskit.  

```sql
SELECT task.id, task.name, task.deadline, task.state, task.description, COUNT(task.id) AS count FROM project
INNER JOIN task ON (task.project_id = project.id)
WHERE (task.project_id = project_id)
GROUP BY task.id, task.name, task.deadline, task.state
```   

- Käyttäjä voi poistaa projektejaan.

```sql
DELETE FROM project WHERE project.id = ?
```   

- Profiili sivulta käyttäja pystyy tarkastamaan omien taskien ja projektien määrän.  

```sql
SELECT COUNT(id) AS count FROM task
WHERE (user_id = ?)
```   

```sql
SELECT COUNT(id) AS count FROM project
WHERE (user_id = ?)
```   

- Admin-oikeuksilla käyttäjä voi listata kaikki sovelluksen käyttäjät sekä heidän projektinsa ja niissä olevien taskien määrät  

```sql
SELECT name, role FROM user
```   

```sql
SELECT COUNT(project.id), project.name, COUNT(task.id) FROM project
LEFT JOIN task ON task.project_id = project.id
WHERE (project.user_id = user_id) 
GROUP BY project.id, project.name
```   
