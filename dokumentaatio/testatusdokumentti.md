# Sovelluksen testaaminen

Ohjelmasta on suoritettu yksikkö-, integraatio- ja järjestelmätestaus. Yksikkö- ja integraatiotestit on suoritettu automaattisesti. Järjestelmätestaus on suoritettu manuaalisesti.

## Yksikkötestaus
Yksikkötestein on testattu entiteettien luokat `BNF`, `Rule`, `Sequence` ja `Symbol` sekä BNF-mallin syntaksitarkastus. Luokkien osalta yksikkötesteissä on luotu luokkien instansseja useilla eri tavoilla ja tarkastamalla on konstruktio tapahtunut oikein eli tulostaako luokan `__str__()`-funktio oikean tulostuksen. Lisäksi BNF-mallin syntaksitarkastuksen osalta on yksikkötestattu syntaksitarkastus useilla mahdollisilla kombinaatioilla.

Lisäksi yksikkötestein on testattu tietokantaa luokan `Database` testeillä. Tietokannan testaamisessa luodaan väliaikainen tietokanta `temp.db`, johon testit kohdistetaan. Täten se on myös tyhjä jokaiselle yksikkötestille. Yksikkötesteissä testataan jokaisen luokan `BNF`, `Rule`, `Sequence` ja `Symbol` instanssin lisääminen, hakeminen ja poistaminen tietokannasta.

Jokaista luokkaa vastaa sitä testaava testiluokka:
* [TestBNF](../src/tests/bnf_test.py)
* [TestRule](../src/tests/rule_test.py)
* [TestSequence](../src/tests/seequence_test.py)
* [TestSymbol](../src/tests/symbol_test.py)
* [TestDatabase](../src/tests/database_test.py)

## Integraatiotestaus
Usean luokan testaamista on käytännössä testaamalla koko mallin tallennus, poistaminen ja lataaminen servicen kautta. Testeissä luodaan BNF-malli suoraan tekstistä ja tallennetaan, poistetaan tai ladataan servicen kautta tietokantaan.

Testausta vastaa testiluokka [TestService](../src/tests/service_test.py).

## Järjestelmätestaus

Ohjelman järjestelmätestaus on suoritettu manuaalisesti. Järjestelmätestauksessa on testaus on suoritettu käsin lataamalla Gitlab-release gitlabista, asentamalla ohjelma, ja kokeilemalla käsin vaatimusmäärittelyssä esitetyt asiat käyttöohjeen mukaisesti. Testaus on suoritettu Windows 10:n kautta ajatellu Windows Subsystem Linuxilla Xlaunchin avulla sekä xxxxxx.

## Yksikkö- ja integraatiotestausten testikattavuudet

Yksikkö- ja integraatiotestausten testikattavuus on alla olevan taulukon mukaisesti 90 prosenttia. Käyttöliittymään liittyvää koodia ([ui.py](../src/ui.py), [view.py](../src/view.py)) ei ole huomioitu testikattavuuteen.

    Name                       Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------------------
    src/database.py               70      9     32      4    87%   73-74, 109-110, 145-146, 174-175, 183
    src/entities/bnf.py           48      0     30      0   100%
    src/entities/rule.py          25      0      8      0   100%
    src/entities/sequence.py      26      0     12      1    97%   52->55
    src/entities/symbol.py        13      0      4      0   100%
    src/main.py                   10     10      2      0     0%   1-14
    src/service.py                61      6     28      3    88%   36, 49, 73-74, 122-123
    ----------------------------------------------------------------------
    TOTAL                        253     25    116      8    90%