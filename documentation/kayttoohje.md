# Käyttöohje

Sovelluksen url:  
[https://todoplanneri.herokuapp.com/](https://todoplanneri.herokuapp.com/)  
Etusivulta löytyy kuvaus sovelluksesta.

Kirjautuminen vaaditaan kaikkiin sovelluksen toiminnallisuuksiin.  

Rekisteröinti tapahtuu sivulta:  
`https://todoplanneri.herokuapp.com/auth/signup/`  

Rekisteröinnissä tarkistetaan onko käyttäjätunnus validi sekä täsmäävätkö salasanat.  

![Sign Up](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/signup.png)  

Kirjautuminen tapahtuu sivulta:    
`https://todoplanneri.herokuapp.com/auth/login`  

![Sign In](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/signin.png)

Uusi taskin luodaan sivulta:  
`https://todoplanneri.herokuapp.com/tasks/create/`  

![Create Task](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/task_create.png)  

Taskit listataan sivulta:  
`https://todoplanneri.herokuapp.com/tasks`  

Sivulla eritellään käyttäjälle eri statuksella olevat taski:
- To-Dos  
- In Progress  
- Completed  

Sivulla käyttäjä voi siirtää taskeja eri statukselle sekä poistaa taskeja.  
Käyttäjä pääsee muokkaamaan taskia klikkaamalla sen nimeä.  

Taskin muokkaus tapahtuu sivulta:  
`https://todoplanneri.herokuapp.com/tasks/edit/<task_id>`  

Käyttäjä voi luoda omia projekteja sivulta:  
`https://todoplanneri.herokuapp.com/projects/create/`  

![Create Project](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/project_create.png)  

Kun projekti on luotu käyttäjä ohjataan seuraavalle sivulle, josta voidaan lisätä avoimia taskeja projektille:  
`https://todoplanneri.herokuapp.com/projects/`  

![Add_tasks_to_project](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/add_tasks_to_project.png)  
Omat projektit ovat listattuna sivulla:  
`https://todoplanneri.herokuapp.com/projects`  

Arkistoidut taskit ovat listattavissa sivulla:  
`https://todoplanneri.herokuapp.com/tasks/archived`  

Oma profiili löytyy yläpalkin "My Profile" alta:  
`https://todoplanneri.herokuapp.com/profile/`   

Profiili sivulla on listattuna liittymispäivämäärä, omien taskien sekä projektin lukumäärä.  

Mikäli käyttäjällä on admin-oikeudet hänellä näkyy yläpalkissa "Users" valikko:  
`https://todoplanneri.herokuapp.com/users`  

Admin-oikeuksilla käyttäjä pystyy selata kaikki sovelluksen käyttäjät läpi ja päivittää käyttäjien tietoja esimerkiksi vaihtamaan usernamea ja päivittämään muiden käyttäjien oikeuksia.  
Admin-oikeusilla on mahdollista myös poistaa sovellukseen rekisteröityneitä käyttäjiä.  

