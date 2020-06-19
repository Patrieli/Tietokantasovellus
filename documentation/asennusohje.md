# Asennusohje  

*Sovellus on toteutettu python versiolla 3.6.9.*

Suorita vaiheet järjestyksessä ajamalla alla listatut komennot komentoriviltä.  

### Sovelluksen kloonaus Githubista   
``
git clone https://github.com/Patrieli/ToDoPlanner.git
``

### Sovellus hakemistoon ja virtuaaliympäristö käyttöön    
``
cd ToDoPlanner  
source venv/bin/activate 
``

### Riippuvuuksien asentaminen  
``
pip install requirements.txt
``

### Sovelluksen käynnistäminen ToDoPlanner -kansiosta  
``
python run.py  
``  

Ensimmäisen käynnistyksen aikana tapahtuu tietokannan luonti.  
Sovellus on nyt toiminassa lokaalisti sivulla [http://localhost:5000/](http://localhost:5000/).


## Sovelluksen siirto Herokuun  

Siirry komentorivillä sovelluksen hakemistoon ja käynnistä virtualenv  

``
cd ToDoPlanner  
source venv/bin/activate 
``

Repository sisältää valmiin Procfile:n, tiedostossa on ohjeet Herokua varten sovelluksen käynnistämiseen  

Seuraavaksi tarvitaan Herokun käyttäjätunnus sekä Heroku CLI.  

Sovellukselle paikan luonti Herokuun  
(sovelluksen nimi tulee olla uniikki)  
``
heroku create "sovelluksen nimi"  
``  

Lisää paikalliseen versionhallintaaan tieto Herokusta  

``
git remote add heroku https://git.heroku.com/"sovelluksen nimi"
``  

Projektin lähetys Herokuun  

``
git add .
git commit -m "Initial commit"
git push heroku master
``  

