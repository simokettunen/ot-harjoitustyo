# ot-harjoitustyö – BNF-visualisoija

BNF-visualisoijan tarkoituksena on piirtää graafi käyttäjän syöttämästä Backus Naur -muodossa olevasta syötteestä. Ohjelmassa pystyy tallentamaan mallin ja lataamaan aiemmin tallennetun mallin.

## Dokumentaatio
* [Määrittelydokumentti](dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
* [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

## Ohjelman käyttö
Ohjelman asennus tapahtuu komennolla `poetry install`, jonka jälkeen ohjelman voi suorittaa komennolla `poetry run invoke start`.

Ohjelman yksikkötestien suoritus onnistuu komennolla `poetry run invoke test` ja testiraportin saa komennolla `poetry run invoke coverage-report`. Pylintin suoritus onnistuu komennolla `poetry run invoke pylint`.

### Syntaksi BNF-mallin kirjoittamiseen
TODO

Esimerkkejä:

    <a> ::= <b> <c> | <d>
    <b> ::= "abc"
    <c> ::= <b> <c> | "r"
    <d> ::= "x"
    