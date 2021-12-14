# Arkkitehtuurikuvaus

## Rakenne

Ohjelman ylätason rakenne on kuvattu alla olevassa kuvassa. Ohjelma sisältää käyttöliittymän, jossa hyödyntää BNF-serviceä, mistä on tietokanta yhteys. BNF-service sisältää myös viittauksen BNF-mallin olioon.

![structure](./imgs/structure.png)

Alla olevassa kuvassa on esitetty sovelluksen tämän hetkinen luokkakaavio. Ohjelman sovelluslogiikka sisältää neljä luokkaa: `BNF`, `Rule`, `Sequence` ja `Symbol`

![class diagram](./imgs/class_diagram.png)

Alla olevassa kuvassa on esitetty sekvenssikaavio, kun BNF-malli ladataan tietokannasta.

![sequence diagram](./imgs/sequence_diagram.png)