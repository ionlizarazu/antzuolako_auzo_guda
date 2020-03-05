# Antzuolako auzo guda
Antzuolako auzoen arteko guda simulatua da.

## Fitxategiak:
### mugak.json
Antzuolako auzoen arteko muga guztiak daude zerrendatuta. Zerrendako elementu bakoitza bi auzo dira, mugakide direnak.
### antzuolaOriginala.json
Antzuolako jatorrizko egoera adierazten du. Auzo bakoitzak lau atributu ditu:
- izena: auzoaren izena.
- jabea: auzo horren uneko jabea (fitxategi honetan beti izango da izena-ren berdina).
- like: auzoak ausazko guda honetan pisu gehiago izateko aukera du, atributu honen balio altuagoak aukera gehiago emango dizkio guda irabazteko.
- kolorea: auzoak gudarako erabiliko duen kolore bereizgarria (inor konkikstatuz gero, kolore honekin bustiko du)
### antzuola.json
Gudan zehar herriaren egoera gordeko duen fitxategia. Gerra amaitzean antzuolaOriginala.json fitxategiaren edukia jasoko du berriz.
### antzuolaGuda.py
Guda exekutatzen duen fitxategia.
### mapa/antzuolaguda.html
Herriko mapa koloreztatua dago. Hasierako egoera erakusten du eta ez da aldatzen exekuzioan zehar.
### mapa/tmp.html
Gudan zehar momentuko egoerak kudeatzeko erabiltzen den HTML fitxategia.

## Nola erabili:
Python bidez exekutatzen da guda.
```bash
    $ python3 antzuolaGuda.py
```
Terminaletik exekutatzean gudaren prozesua pantailan erakusten joango zaigu.
Bestalde, hainbat fitxategi sortuko dizkigu:
- mapa barruan konkista edo independentzia bakoitzeko HTML fitxategi bat, "egun" bezala identifikatuta eta azkenik BUKAERA.html fitxategi bat guda amaiera nola geratu den ikusteko.
- Historikoa.txt fitxategia sortuko digu terminalean erakusten den testua gordetzeko.
