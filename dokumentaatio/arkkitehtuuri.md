# Arkkitehtuurikuvaus

## Rakenne

Ohjelman ylätason rakenne on kuvattu alla olevassa kuvassa. Ohjelma sisältää käyttöliittymän, joka hyödyntää BNF-serviceä, josta on tietokantayhteys. BNF-service sisältää myös viittauksen BNF-mallin olioon.

![structure](./imgs/structure.png)

## Käyttöliittymä

Käyttöliittymässä on kaksi näkymää, jotka ovat aloitussivu ja visualisointisivu. Aloitussivulta käyttäjä voi aloittaa uuden mallin visualisoimisen tai mallin lataamisen tietokannasta. Kummallakin tavalla käyttäjä siirtyy visualisointisivulle, jossa käyttäjä voi syöttää BNF-mallin mukaisen määrittelyn sille varattuun tekstikenttään, visualisoida määrittelyn ja tallentaa BNF-mallin tietokantaan.

Aloitussivusta vastaa luokka `StartView` ja visualisointisivusta luokka `EditModeView`, jotka kummatkin perivät luokan `View`. Koko käyttöliittymästä vastaa luokka `UI`.

## Sovelluslogiikka

Alla olevassa kuvassa on esitetty sovelluksen tämän hetkinen luokkakaavio. Ohjelman sovelluslogiikka sisältää neljä luokkaa: `BNF`, `Rule`, `Sequence` ja `Symbol`. Luokalla `BNF` löytyy seuraavat julkiset metodit:
* `create_from_string`
* `check_unassigned_nonterminals`

Luokat `Rule`, `Sequence` ja `Symbol` sisältävät julkisina vain konstruktorin `__init__` ja `__str__`-metodin.

Lisäksi löytyy luokkaan `BNF` kuulumaton erillinen, mutta vahvasti luokan yhteyteen kuuluva funktio `check_syntax`, jolla voi tarkistaa BNF-määrittelyn syntaksin oikeellissuuden.

![class diagram](./imgs/class_diagram.png)

## Toiminallisuudet

### Mallin lataaminen

Alla olevassa kuvassa on esitetty sekvenssikaavio, kun BNF-malli ladataan tietokannasta. Käyttäjä valitsee käyttöliittymästä aiemmin tallennetun mallin, ja painaa painiketta *load model*. Tällöin luokassa `Service` aloitetaan tallennetun mallin lataaminen tietokannasta. Ensin ladataan tiedot BNF-mallista ja luodaan olio, joka on luokan `BNF` instanssi. Tämän jälkeen ladataan tiedot säännöistä ja luodaan olioita, jotka ovat luokan `Rule` instansseja. Kullekin `Rule`-luokan objektille ladataan tietokannasta tiedot lausekkeista ja luodaan olioit, jotka ovat luokan `Sequence` olioita. Kullekin `Sequence`-luokan oliolle ladataan tiedot tietokannasta symboleista ja luodaan näitä vastaavat oliot, jotka ovat luokan `Symbol` instansseja.

![Sequence diagram of loading model](./imgs/loading_model.png)

### Mallin tallennus

Alla olevassa kuvassa on esitetty sekvenssikaavio, kun BNF-malli tallennetaan tietokantaan. Käyttäjä painaa käyttöliittymässä painiketta *save drawn model*. Tällöin luokassa `Service` aloitetaan BNF-mallin tallennus. Jos tietokannasta löytyy malli, jolla on sama id kuin tallennettavalla mallilla, poistetaan tietokannasta malli ja siihen liittyvät tiedot säännöistä, lausekkeista ja symboleista. Tämän jälkeen uuden malli, ja siihen liittyvät säännöt, lausekkeet ja symbolit tallennetaan tietokantaan.

![Squence diagram of saving model](./imgs/saving_model.png)

### Mallin visualisointi

Alla olevassa kuvassa on esitetty sekvenssikaavio, kun BNF-malli luodaan. Käyttäjä kirjoittaa käyttöliittymässä BNF-mallin mukaisen määrittelyn sille varattuun tekstikenttään, ja painaa painiketta *draw*. Tällöin BNF-mallin määrittelevä teksti siirtyy käyttöliitymässä luokan `Service` instanssille, joka ensimmäiseksi tarkistaa, onko syntaksi oikein. Jos syntaksi on oikein, luodaan ensin olio, joka on luokan `BNF` instanssi. BNF-olio muodostaa tarvittavat oliot säännöille, jotka ovat luokan `Rule` instansseja, nämä luovat tarvittavat oliot lausekkeille, jotka ovat luokan `Sequence` instansseja, jotka vielä luovat tarvittavat oliot symboleille, jotka ovat luokan `Symbol` instansseja. BNF-olio palautuu lopulta servicelle, johon käyttöliittymällä on pääsy.

![Sequence diagram of visualizing model](./imgs/visualizing_model.png)

## Tietojen tallennus

Tiedot tallennetaan SQL-tietokantaan. Tietokanta alustetaan luokassa `Database` ja se annetaan syötteenä luokalle `Service`. Tietojen tallennuksesta, lataamisesta ja poistamisesta huolehtii luokka `Service`, joka välittää käskyt tietokantaluokalle `Database`.

Jokaisella luokalla `BNF`, `Rule`, `Sequence` ja `Symbol` on tietokannassa omat taulunsa. Tietokantaan tallennetaan näistä luokista seuraavat tiedot:

BNF
* id (avain): BNF-mallin id UUID:nä

Rule
* id (avain): Säännön id UUID:nä
* bnf: BNF-mallin UUID, johon sääntö liittyy
* symbol: Symbolin teksti, jolle sääntö on määritetty

Sequence
* id (avain): Lausekkeen id UUID:nä
* rule: Säännön UUID, johon lauseke liittyy

Symbol
* id (avain): Symbolin id UUID:nä
* sequence: Lausekkeen UUID, johon symboli liittyy
* type: symbolin tyyppi
* label: symbolin teksti