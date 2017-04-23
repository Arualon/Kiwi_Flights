TASK:

Python víkend v Kiwi.com - vstupní úkol

Pomocí této úlohy nám prokážete, že jste s Pythonem již přišli do styku a znáte jeho základy. Tím pádem by nemělo nic bránit tomu, abyste si workshop užili a nebyl pro vás příliš složitý.

##Limitace

Žádné limitace.

Python2.7 nebo 3
všechny moduly jsou povoleny
##Popis úkolu

Máte data o jednotlivých letech (segmentech) a batožinách. Vaším úkolem je nalézt kombinace jednotlivých letů (itineráře, tzn. minimálně 2 segmenty) pro pasažéry bez batožiny, jedním nebo dvěma kusy batožiny tak, aby segmenty navazovaly s časem na přestup 1-4 hodiny. Jednotlivé sloupce jsou ve vstupních datech pojmenovány:

source, destination vyjadřující kód letiště odletu a příletu
departure, arrival jsou časy odletu a příletu
price je cena za letenku bez batožiny
bags_allowed je počet kusů batožiny které se daji dokoupit
bag_price je cena za kus batožiny přikoupené navíc
flight_number je unikátní identifikátor segmentu
Pro jednoduchou orientaci v nabídce nakombinovaných segmentů by bylo vhodné, aby nabídky letů pro pasažéry s různým počtem batožiny již obsahovaly celkovou cenu za všechny segmenty včetně poplatků za batožinu.

##Vstupní data (csv) (pouze ukázka)

source,destination,departure,arrival,flight_number,price,bags_allowed,bag_price
USM,HKT,2017-02-11T06:25:00,2017-02-11T07:25:00,PV404,24,1,9
USM,HKT,2017-02-12T12:15:00,2017-02-12T13:15:00,PV755,23,2,9
USM,HKT,2017-02-12T21:15:00,2017-02-12T22:15:00,PV729,25,1,14
USM,HKT,2017-02-11T14:50:00,2017-02-11T15:50:00,PV966,21,1,17
USM,HKT,2017-02-12T00:35:00,2017-02-12T01:35:00,PV398,24,1,14
USM,HKT,2017-02-12T05:15:00,2017-02-12T06:15:00,PV870,19,1,13
USM,HKT,2017-02-12T10:00:00,2017-02-12T11:00:00,PV320,22,1,18
USM,HKT,2017-02-12T13:40:00,2017-02-12T14:40:00,PV540,26,2,13
USM,HKT,2017-02-12T09:30:00,2017-02-12T10:30:00,PV290,19,2,8
USM,HKT,2017-02-11T02:40:00,2017-02-11T03:40:00,PV876,25,2,16
USM,HKT,2017-02-12T09:35:00,2017-02-12T10:35:00,PV275,24,2,17
HKT,USM,2017-02-12T10:35:00,2017-02-12T11:30:00,PV996,23,1,15
HKT,USM,2017-02-11T15:45:00,2017-02-11T16:40:00,PV243,22,1,6
HKT,USM,2017-02-11T19:05:00,2017-02-11T20:00:00,PV146,21,2,5
HKT,USM,2017-02-12T16:00:00,2017-02-12T16:55:00,PV634,21,1,12
HKT,DPS,2017-02-12T00:00:00,2017-02-12T03:40:00,PV961,70,1,39
HKT,USM,2017-02-12T00:20:00,2017-02-12T01:15:00,PV101,18,2,7
HKT,DPS,2017-02-11T12:00:00,2017-02-11T15:40:00,PV100,96,1,40
HKT,USM,2017-02-12T22:05:00,2017-02-12T23:00:00,PV672,24,2,5
HKT,USM,2017-02-11T06:30:00,2017-02-11T07:25:00,PV442,17,1,11
HKT,USM,2017-02-12T07:15:00,2017-02-12T08:10:00,PV837,18,1,12
BWN,DPS,2017-02-11T06:10:00,2017-02-11T08:30:00,PV953,48,1,25
BWN,DPS,2017-02-12T14:35:00,2017-02-12T16:55:00,PV388,49,1,30
BWN,DPS,2017-02-11T05:35:00,2017-02-11T07:55:00,PV378,59,1,29
BWN,DPS,2017-02-12T10:35:00,2017-02-12T12:55:00,PV046,50,1,25
BWN,DPS,2017-02-11T13:40:00,2017-02-11T16:00:00,PV883,51,1,26
BWN,DPS,2017-02-12T19:10:00,2017-02-12T21:30:00,PV999,54,2,23
BWN,DPS,2017-02-11T16:15:00,2017-02-11T18:35:00,PV213,55,2,22
BWN,DPS,2017-02-11T02:35:00,2017-02-11T04:55:00,PV873,46,1,34
BWN,DPS,2017-02-11T01:15:00,2017-02-11T03:35:00,PV452,57,1,33
BWN,DPS,2017-02-12T08:45:00,2017-02-12T11:05:00,PV278,41,2,22
BWN,DPS,2017-02-12T22:50:00,2017-02-13T01:10:00,PV042,56,2,31
DPS,HKT,2017-02-12T08:25:00,2017-02-12T12:05:00,PV207,83,1,38
DPS,BWN,2017-02-12T17:15:00,2017-02-12T19:40:00,PV620,43,2,25
DPS,BWN,2017-02-11T13:15:00,2017-02-11T15:40:00,PV478,47,1,23
DPS,HKT,2017-02-11T09:15:00,2017-02-11T12:55:00,PV414,67,1,49
DPS,HKT,2017-02-12T08:25:00,2017-02-12T12:05:00,PV699,78,2,41
DPS,HKT,2017-02-12T15:20:00,2017-02-12T19:00:00,PV974,85,1,38
DPS,HKT,2017-02-11T00:20:00,2017-02-11T04:00:00,PV519,79,2,44
DPS,HKT,2017-02-11T08:50:00,2017-02-11T12:30:00,PV260,89,1,43
DPS,BWN,2017-02-12T16:45:00,2017-02-12T19:10:00,PV451,57,1,24
DPS,BWN,2017-02-11T22:10:00,2017-02-12T00:35:00,PV197,50,1,30
##Výstup

Výstupní data můžou být v jakémkoliv formátu vhodném k dalšímu zpracování.
Ignorovat opakování segmentů (A->B) v kombinaci. A a B představují kód letiště.
A->B->A->B je nevalidní kombinace.
A->B->A je validní kombinace.
##Zpracování

Úkol byl navržený tak, aby začátečníkům poskytl výzvu a možnost vyzkoušet si základní datové typy a kontrolní struktury (if, for atd.), a zdatnějším lidem kteří už dříve programovali v jiném jazyce trvalo zpracování chvilku.
Řešení by mělo být jednoduché
Neočekáváme, že řešení bude optimalizované na výpočetní náročnost nebo využití paměti (pokud vás to však baví a chcete využít matematické znalosti ze školy, můžete)
##Použití

Vstupní data bude program číst ze stdin a bude jej tak možné spustit následujícím způsobem cat input.csv | python find_combinations.py skript poté zapíše výstup na stdout a případné chyby na stderr.

##Kontakt

Posílat můžete jako .py soubor / .zip balík v příloze e-mailu nebo odkaz na GitHub repozitář.
Vyřešené úkoly a otázky nám zasílejte na mike@kiwi.com
