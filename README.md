# ot-harjoitustyö – BNF-visualisoija

BNF-visualisoijan tarkoituksena on piirtää graafi käyttäjän syöttämästä Backus Naur -muodossa olevasta syötteestä. Ohjelmassa pystyy tallentamaan mallin ja lataamaan aiemmin tallennetun mallin.

## Releaset
* [Viikko 5](https://github.com/simokettunen/ot-harjoitustyo/releases/tag/viikko5)
* [Viikko 6](https://github.com/simokettunen/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio
* [Määrittelydokumentti](dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](dokumentaatio/kayttoohje.md)
* [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

## Ohjelman käyttö
Ohjelman asennus tapahtuu komennolla `poetry install`, jonka jälkeen ohjelman voi suorittaa komennolla `poetry run invoke start`. Ohjeet ohjelman tarkempaan käyttöön on esitetty [käyttöohjeessa](dokumentaatio/kayttoohje.md).

Komentoja:

* Ohjelman yksikkötestien suoritus:

    `poetry run invoke test`

* Ohjelman testiraportin suoritus:
 
    `poetry run invoke coverage-report`

* Pylintin suoritus:

    `poetry run invoke pylint`
