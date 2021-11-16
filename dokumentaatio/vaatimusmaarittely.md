# Vaatimusmäärittely

## Sovelluksen tarkoitus

Projektissa kehitettävän sovelluksen tarkoituksena on visualisoida Backus–Naur-muodossa (BNF) esitettyjä kontekstiriippumattomia kieliä. Ohjelma avautuu graafiseen käyttöliittymään, jossa ohjelman käyttäjä pystyy määrittelemään Backus–Naur-muodossa olevia lausekkeita, minkä jälkeen ohjelma piirtää käyttöliittymään näkyviin visuaaliset kaaviot käyttäjän kirjoittaman BNF-määrittelyn pohjalta.

## Käyttäjäroolit

Erillisiä käyttäjärooleja ei sovelluksessa ole.

## Ohjelman ydintoiminnallisuus

Ohjelmassa on graafinen käytttöliittymä. Alustavasti ohjelmalla pystyy toteuttamaan seuraavat ydintoiminnot:

* aloitusruutu
    * käyttäjä pystyy lataamaan aiemmin luodun BNF-mallin tietokannasta
    * käyttäjä pystyy aloittamaan uuden BNF-mallin määrittelyn tyhjälle pohjalle

* BNF-mallin muokkaustila
    * käyttäjä pystyy kirjoittamaan BNF-syntaksin mukaisen määrittelyn tekstiruutuun
    * käyttäjä pystyy visualisoimaan tekstiruutuun kirjoitetun tekstin, jolloin ohjelma piirtää syntaksin mukaiset kaaviot
        * tapahtuu painiketta painamalla, ei piirrä reaaliaikaisesti
    * ohjelma tarkistaa käyttäjän laatiman määrittelyn BNF-mallin oikeellisuuden ja ilmoittaa mahdollisesta virheestä
        * varoitus mikäli käyttäjä viittaa lausekkeeseen jota ei ole olemassa
        * virheilmoitus mikäli määrittelyssä on syntaksivirhe

* BNF-mallin tallennus
    * käyttäjä pystyy tallentamaan luodun BNF-mallin tietokantaan
    * ohjelma varoittaa mikäli käyttäjä yrittää sulkea ohjelman eikä muokattua mallia ole tallennettu
  
## Ohjelman jatkokehitysideat

Ohjelman ydintoiminallisuuden jälkeen mahdollisesti kehitettäviä toimintoja  

* reaaliaikainen visualisointi
* yksittäisen BNF-lausekkeiden tallennus ja lataaminen ohjelmaan
* BNF-mallin vienti kuvatiedostoksi
* BNF-mallin vienti sopivaan tekstiformaattiin, esim. JSON
* BNF-mallin lukeminen sopivasta tekstiformaatista, esim. JSON