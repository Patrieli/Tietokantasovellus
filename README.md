# ToDoPlanner

Sovellus on tarkoitettu ajanhallintaan ja omien taskien seurantaan.  
Käyttäjä voi luoda sovelluksessa uusia taskeja, asettaa taskeja projekteihin sekä seurata omien taskien edistymistä.  

Sovellus toteutetaan osana Helsingin yliopiston tietojenkäsittelytieteen osaston aineiopintojen harjoitustyötä.

## Dokumentaatio
[Asennusohje](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/asennusohje.md)  
[Käyttöohje](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/kayttoohje.md)  
[Käyttötapaukset](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/k%C3%A4ytt%C3%B6tapaukset.md)  
[SQL-taulujen luontilauseet](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/taulujenluontiskriptit.md)  
[Tietokantakaavio](https://github.com/Patrieli/ToDoPlanner/blob/master/documentation/pictures/tietokantakaavio.jpg) 


## Sovellus herokussa
[ToDoPlanner](https://todoplanneri.herokuapp.com/)

- **Käyttäjätunnukset sovellukseen:**  

	 *Admin-oikeuksilla*:  
  **Username**: admin  
  **Password**: salasana1  

	*Peruskäyttäjä:*  
  **Username**: testaaja  
  **Password**: salasana1  

## Puuttuvat toiminnallisuudet  
Tasks:  
- Taskin labeleiden avulla kategorisointi  
- Taskien järjestäminen nimen, deadlinen tai projektin perusteella  
- Taskien aloitus / lopetuspäivämäärän hyödyntäminen

Projects:  
- Projektin aloitus / lopetuspäivämäärä  

Users:
- Salasanan vaihto  

## Jatkokehytys ideat  
Tasks:  
- Taskien listaus sivuta enemmän kanban tyylinen, taulukko missä taskit näytetään kortteina ja niitä voidaan vedellä taulussa tilasta toiseen.  
- Muistutus jos taskin deadline lähenee  
- Daily tasks sivu, käyttäjä voi listata sivulla päivittäisi taskeja / muistutuksia  

Projects:  
- Rarpotti projektin etenemisestä, esimerkiksi taskien tilojen mukaan  
- Projektin ja taskien tilojen yhdistäminen, mikäli projekti olisi valmis kaikki taskit siirretään valmiiksi  

Users:  
- Kuukausitason raportti mistä näkyy suoritettujen taskien määrä, avoimet taskit, avoimet projektit sekä projektien suoritus prosentti  

Kaverien lisäys:  
- Käyttäjät voivat lisätä toisia kavereiksi ja jakaa projektit ja projektin taskit keskenään

