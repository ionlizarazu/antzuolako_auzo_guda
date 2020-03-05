import json
import random
import os
import re
import bs4

def aukeratuMuga():
  with open("mugak.json", "r") as file:
    mugak = json.load(file)
  mugaKopurua = len(mugak)
  return mugak[random.randint(0,mugaKopurua-1)]

def konkistagarria(mugaAukeratua):
    with open("antzuola.json", "r") as file:
        antzuola = json.load(file)["auzoak"]
    for auzoa in antzuola:
        if auzoa["izena"] == mugaAukeratua[0]:
            auzo1 = auzoa
        elif auzoa["izena"] == mugaAukeratua[1]:
            auzo2 = auzoa

    if auzo1["jabea"]==auzo2["jabea"]:
        return False
    else:
        return True

def konkistatu(mugaAukeratua,eguna,historikoa):
    konkistatzaileak = list()
    galtzaileak = list()
    #AUZO ZERRENDA IREKI
    with open("antzuola.json", "r") as file:
        herria = json.load(file)
    for auzoa in herria["auzoak"]:
      if auzoa["izena"]==mugaAukeratua[0]:
        auzoa0izena = auzoa["izena"]
        auzoa0like = auzoa["like"]
      elif auzoa["izena"]==mugaAukeratua[1]:
        auzoa1izena = auzoa["izena"]
        auzoa1like = auzoa["like"]
    if random.randint(1,(100+auzoa0like+auzoa1like)) < (51+auzoa0like):
      konkistatua=1
      konkistatzailea=0
    else:
      konkistatua=0
      konkistatzailea=1
    #MUGAKIDE KONKISTATZAILEA AUKERATU
    '''konkistatzailea = random.randint(0,1)
    if konkistatzailea == 0:
        konkistatua=1
    else:
        konkistatua=0
    '''
    #AUZO KONKISTATZAILEA IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == mugaAukeratua[konkistatzailea]:
            jabea = auzoa["jabea"]
    #KOLOREZTATZEKO KONKISTATZAILEAK IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["jabea"] == jabea:
            konkistatzaileak.append(auzoa["izena"])
    #AUZO GALTZAILEA IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == mugaAukeratua[konkistatua]:
            galtzailea = auzoa["jabea"]
    #KOLOREZTATZEKO GALTZAILEAK IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["jabea"] == galtzailea and auzoa["izena"] != mugaAukeratua[konkistatua]:
            galtzaileak.append(auzoa["izena"])
    #AUZO KONKISTATUA KONKISTATU
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == mugaAukeratua[konkistatua]:
            auzoa["jabea"] = jabea
    if jabea == "Kalebarren":
        jabea = jabea+"e"
    #KOLOREZTATU MAPA
    koloreztatuKonkista(konkistatzaileak,galtzaileak,mugaAukeratua[konkistatua],eguna)
    historikoa = historikoa + 'KONKISTA!  '+jabea+'k '+mugaAukeratua[konkistatua]+' konkistatu du\n\n'
    print("KONKISTA! "+jabea+"k "+mugaAukeratua[konkistatua]+" konkistatu du")
    with open("antzuola.json", "w") as file:
        json.dump(herria, file)
    return historikoa

def gauzatuKonkistaPosiblea(mugaAukeratua,eguna,historikoa):
    auzokideak = list()
    mugaPosibleak = list()
    galtzaileak = list()
    #AUZO ZERRENDA IREKI
    with open("antzuola.json", "r") as file:
        herria = json.load(file)
    #AUZO JABEA IDENTIFIKATU, BIENTZAT BERA DA
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == mugaAukeratua[0]:
            jabea = auzoa["jabea"]
    #AUZO JABEAREN JABETZAK IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["jabea"] == jabea:
            auzokideak.append(auzoa["izena"])
    #MUGA ZERRENDA IREKI
    with open("mugak.json", "r") as file:
        mugak = json.load(file)
    #KONKISTATZEKO MUGA POSIBLEAK IDENTIFIKATU
    for muga in mugak:
        if (muga[0] in auzokideak and muga[1] not in auzokideak) or (muga[1] in auzokideak and muga[0] not in auzokideak):
            mugaPosibleak.append(muga)
    #KONKISTATZEKO MUGA AUKERATU
    aukeratua = random.randint(0,len(mugaPosibleak)-1)
    #HAUTATUTAKO MUGAKIDEA HARTU
    if mugaPosibleak[aukeratua][0] not in auzokideak:
        konkistatua = mugaPosibleak[aukeratua][0]
    else:
        konkistatua = mugaPosibleak[aukeratua][1]
    #AUZO GALTZAILEA IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == konkistatua:
            galtzailea = auzoa["jabea"]
    #KOLOREZTATZEKO GALTZAILEAK IDENTIFIKATU
    for auzoa in herria["auzoak"]:
        if auzoa["jabea"] == galtzailea and auzoa["izena"] != konkistatua:
            galtzaileak.append(auzoa["izena"])
    #AUZO KONKISTATUA KONKISTATU
    for auzoa in herria["auzoak"]:
        if auzoa["izena"] == konkistatua:
            jabeZaharra = auzoa["jabea"]
            auzoa["jabea"] = jabea
            

    if jabea == "Kalebarren":
        jabea = jabea+"e"
    if jabeZaharra != "Kalebarren":
        jabeZaharra = jabeZaharra+"r"
    koloreztatuKonkista(auzokideak,galtzaileak,konkistatua,eguna)
    historikoa = historikoa + "KONKISTA! "+jabea+"k lehen "+jabeZaharra+"en jabetzakoa zen "+konkistatua+" konkistatu du\n\n"
    print("KONKISTA! "+jabea+"k lehen "+jabeZaharra+"en jabetzakoa zen "+konkistatua+" konkistatu du")
    with open("antzuola.json", "w") as file:
        json.dump(herria, file)
    return historikoa

def jabeak(historikoa):
    with open("antzuola.json", "r") as file:
        herria = json.load(file)["auzoak"]
    jabeak = list(list())
    jabeHandiak = list(list())
    jabea = list()
    jabetzak = list()
    
    for auzoa in herria:
        jabea=[]
        exist=False
        for bakarra in jabeak:
            if auzoa["jabea"] in bakarra:
                exist=True
                bakarra[1] += 1
        if not exist:
            jabea.append(auzoa["jabea"])
            jabea.append(1)
            jabeak.append(jabea)
    for j in jabeak:
        if j[1]>1:
          jabetzak.append(j[1])
          jabeHandiak.append(j)
    jabetzak.sort(reverse=True)
    
    
    if len(jabeHandiak)>0:
      print("==> Geratzen diren jabe handiak: ")
      historikoa = historikoa + "==> Geratzen diren jabe handiak:\n"
      for jabeHandia in jabeHandiak:
        historikoa = historikoa + " #" + jabeHandia[0] + " - " + str(jabeHandia[1]) +"\n"
        print(" #" + jabeHandia[0] + " - " + str(jabeHandia[1]))
    if 1<len(jabetzak):
      print("####Diferentzia: "+str(jabetzak[0]-jabetzak[1]))
      historikoa = historikoa + "####Diferentzia: "+str(jabetzak[0]-jabetzak[1])+"\n"
    return historikoa

def independentzia():
    aukera = random.randint(1,100)
    if aukera<6:
        return True
    else:
        return False

def amaiera():
    jabeak = list()
    with open("antzuola.json", "r") as file:
        herria = json.load(file)
    for auzoa in herria["auzoak"]:
        if auzoa["jabea"] not in jabeak:
            jabeak.append(auzoa["jabea"])
    if len(jabeak) == 1:
        return True
    else:
        return False

def koloreztatuKonkista(irabazleak,galtzaileak,konkistatua,eguna):
    #irabazleak = ['Beheko Auzoa','Eguzki Auzoa']
    #galtzaileak = ['Lizarraga Hiribidea','Manarieta']
    #konkistatua = 'Zurrategi'
    
    konkistatua = konkistatua.replace(' ' , '')
    
    i=0
    while i<len(irabazleak):
        irabazleak[i] = irabazleak[i].replace(' ' , '')
        i+=1

    i=0
    while i<len(galtzaileak):
        galtzaileak[i] = galtzaileak[i].replace(' ' , '')
        i+=1
    # load the file
    with open("mapa/tmp.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt,'html.parser')
    konfigOsoa = str(soup)

    #regex
    regKolorea = re.compile(r'ctx.fillStyle = ([\s\S]*?);')
    regErtza = re.compile(r'ctx.strokeStyle = ([\s\S]*?);')
    regErtzaLodiera = re.compile(r'ctx.lineWidth = ([\s\S]*?);')

    #auzo irabazleak
    for irabazlea in irabazleak:
        regIrabazleOsoa = re.compile('#'+irabazlea+'([\s\S]*?)//')
        irabazleZaharra = regIrabazleOsoa.findall(konfigOsoa)
        irabazleKolorea = regKolorea.findall(irabazleZaharra[0])
        ertzIrabazlea = regErtzaLodiera.findall(irabazleZaharra[0])
        irabazleBerria = irabazleZaharra[0].replace("'rgb(0, 0, 0)'","'rgb(0, 255, 0)'")
        irabazleBerria = irabazleBerria.replace(ertzIrabazlea[0],"11.123456")
        konfigOsoa = konfigOsoa.replace(irabazleZaharra[0],irabazleBerria)

    #auzo galtzaileak
    for galtzailea in galtzaileak:
        regGaltzaileOsoa = re.compile('#'+galtzailea+'([\s\S]*?)//')
        galtzaileZaharra = regGaltzaileOsoa.findall(konfigOsoa)
        ertzGaltzailea = regErtzaLodiera.findall(galtzaileZaharra[0])
        galtzaileBerria = galtzaileZaharra[0].replace("'rgb(0, 0, 0)'","'rgb(0, 0, 255)'")
        galtzaileBerria = galtzaileBerria.replace(ertzGaltzailea[0],"11.123456")
        konfigOsoa = konfigOsoa.replace(galtzaileZaharra[0],galtzaileBerria)

    #auzo konkistatua
    regKonkistatuOsoa = re.compile('#'+konkistatua+'([\s\S]*?)//')
    konkistatuZaharra = regKonkistatuOsoa.findall(konfigOsoa)
    konkistatuKolorea = regKolorea.findall(konkistatuZaharra[0])
    ertzKonkistatua = regErtzaLodiera.findall(konkistatuZaharra[0])
    konkistatuBerria = konkistatuZaharra[0].replace(konkistatuKolorea[0],irabazleKolorea[0])
    konkistatuBerria = konkistatuBerria.replace("'rgb(0, 0, 0)'","'rgb(255, 0, 0)'")
    konkistatuBerria = konkistatuBerria.replace(ertzKonkistatua[0],"11.123456")
    konfigOsoa = konfigOsoa.replace(konkistatuZaharra[0],konkistatuBerria)

    with open("mapa/"+str(eguna)+"eguna.html", "w") as file:
        file.write(konfigOsoa)
        
    konkistatuTenporala = konkistatuBerria.replace("11.123456",ertzKonkistatua[0])
    konkistatuTenporala = konkistatuTenporala.replace("'rgb(255, 0, 0)'","'rgb(0, 0, 0)'")
    konfigOsoa = konfigOsoa.replace(konkistatuBerria,konkistatuTenporala)

    #auzo irabazleak
    for irabazlea in irabazleak:
        regIrabazleOsoa = re.compile('#'+irabazlea+'([\s\S]*?)//')
        irabazleBerria = regIrabazleOsoa.findall(konfigOsoa)
        irabazleKolorea = regKolorea.findall(irabazleZaharra[0])
        ertzIrabazlea = regErtzaLodiera.findall(irabazleZaharra[0])
        irabazleTenporala = irabazleBerria[0].replace("11.123456","2.856000")
        irabazleTenporala = irabazleTenporala.replace("'rgb(0, 255, 0)'","'rgb(0, 0, 0)'")
        konfigOsoa = konfigOsoa.replace(irabazleBerria[0],irabazleTenporala)

    #auzo galtzaileak
    for galtzailea in galtzaileak:
        regGaltzaileOsoa = re.compile('#'+galtzailea+'([\s\S]*?)//')
        galtzaileBerria = regGaltzaileOsoa.findall(konfigOsoa)
        galtzaileKolorea = regKolorea.findall(galtzaileZaharra[0])
        ertzGaltzailea = regErtzaLodiera.findall(galtzaileZaharra[0])
        galtzaileTenporala = galtzaileBerria[0].replace("11.123456","2.856000")
        galtzaileTenporala = galtzaileTenporala.replace("'rgb(0, 0, 255)'","'rgb(0, 0, 0)'")
        konfigOsoa = konfigOsoa.replace(galtzaileBerria[0],galtzaileTenporala)

    with open("mapa/tmp.html", "w") as file:
        file.write(konfigOsoa)

def koloreztatuIndependentzia(independentista, kolorea,eguna):
  independentista = independentista.replace(' ' , '')
  # load the file
  with open("mapa/tmp.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt,'html.parser')
  konfigOsoa = str(soup)

  #regex
  regKolorea = re.compile(r'ctx.fillStyle = ([\s\S]*?);')
  regErtza = re.compile(r'ctx.strokeStyle = ([\s\S]*?);')
  regErtzaLodiera = re.compile(r'ctx.lineWidth = ([\s\S]*?);')

  #auzo independentista
  regIndepOsoa = re.compile('#'+independentista+'([\s\S]*?)//')
  indepZaharra = regIndepOsoa.findall(konfigOsoa)
  indepKolorea = regKolorea.findall(indepZaharra[0])
  ertzIndep = regErtzaLodiera.findall(indepZaharra[0])
  indepBerria = indepZaharra[0].replace(indepKolorea[0],kolorea)
  indepBerria = indepBerria.replace("'rgb(0, 0, 0)'","'rgb(0, 255, 0)'")
  indepBerria = indepBerria.replace(ertzIndep[0],"11.123456")
  konfigOsoa = konfigOsoa.replace(indepZaharra[0],indepBerria)

  with open("mapa/"+str(eguna)+"eguna.html", "w") as file:
    file.write(konfigOsoa)
    
  indepTenporala = indepBerria.replace("11.123456",ertzIndep[0])
  indepTenporala = indepTenporala.replace("'rgb(0, 255, 0)'","'rgb(0, 0, 0)'")
  konfigOsoa = konfigOsoa.replace(indepBerria,indepTenporala)

  with open("mapa/tmp.html", "w") as file:
    file.write(konfigOsoa)


#BLOKE OROKORRA
independentziak=0
mugaposibleak=0
barnemugak=0
garailea=''
gudaKop=0
#while (independentziak < 2 or gudaKop < 500):
i=1
independentziak=0
mugaposibleak=0
barnemugak=0
historikoa=''
while not amaiera():
#while i<8:
    historikoa = historikoa + '========================================---['+str(i)+']EGUNA---=========================================\n'
    print("==========================================--- ["+str(i)+"] EGUNA ---===========================================")
    if independentzia() and not amaiera():
        print("##INDEPENDENTZIA")
        independentistak = list()
        with open("antzuola.json", "r") as file:
            herria = json.load(file)
        for auzoa in herria["auzoak"]:
            if auzoa["izena"] != auzoa["jabea"]:
                independentistak.append(auzoa["izena"])
        if len(independentistak)!=0:
            independentziak+=1
            aukeratua = random.randint(0,len(independentistak)-1)
            for auzoa in herria["auzoak"]:
                if auzoa["izena"]==independentistak[aukeratua]:
                    jabeOhia = auzoa["jabea"]
                    auzoa["jabea"]=independentistak[aukeratua]
                    kolorea = auzoa["kolorea"]
            historikoa = historikoa + 'INDEPENDENTZIA!  '+independentistak[aukeratua]+'k independentzia lortu du, lehen '+jabeOhia+'ren jabetzakoa zen\n\n'
            print(independentistak[aukeratua]+"k independentzia lortu du, lehen "+jabeOhia+"ren jabetzakoa zen")
            with open("antzuola.json", "w") as file:
                json.dump(herria, file)
            koloreztatuIndependentzia(independentistak[aukeratua], kolorea, i)
        else:
            i=i-1
            print("##EZ DAGO INDEPENDENTISTARIK HERRIAN")
    elif not amaiera():
        mugaAukeratua = aukeratuMuga()
        if konkistagarria(mugaAukeratua):
            mugaposibleak+=1
            #print("##MUGA EGOKIA")
            historikoa = konkistatu(mugaAukeratua,i,historikoa)
        else:
            barnemugak+=1
            #print("##BARNE MUGA")
            historikoa = gauzatuKonkistaPosiblea(mugaAukeratua,i,historikoa)
    i+=1
    historikoa = jabeak(historikoa)
    print('==========================================--------.---------==========================================')
with open("antzuola.json", "r") as file:
    herria = json.load(file)
garailea = herria["auzoak"][0]["jabea"]
print("==========================================--------.---------==========================================")
print("==========================================-----BUKAERA!-----==========================================")
print("==========================================--------.--------==========================================")
print("==========================================--**************--==========================================")
print("==========================================-->> "+garailea+" <<--==========================================")
print("==========================================--**************--==========================================")
print("DATU INTERESGARRI BATZUK:")
print("- independentziak:",independentziak)
print("- muga posibleak:",mugaposibleak)
print("- barne mugak:",barnemugak)
with open("antzuolaOriginala.json", "r") as file:
    herria = json.load(file)
with open("antzuola.json", "w") as file:
    json.dump(herria, file)
    
with open("mapa/tmp.html") as inf:
  txt = inf.read()
  soup = bs4.BeautifulSoup(txt,'html.parser')
konfigOsoa = str(soup)
with open("mapa/BUKAERA.html", "w") as file:
  file.write(konfigOsoa)

with open("mapa/antzuolaguda.html") as inf:
  txt = inf.read()
  soup = bs4.BeautifulSoup(txt,'html.parser')
konfigOsoa = str(soup)
with open("mapa/tmp.html", "w") as file:
  file.write(konfigOsoa)
gudaKop+=1
      
texto = "KONKISTAREN HISTORIKOA:\n"+historikoa+"IRABAZLEA:\n\n##"+garailea+"##\n\nDATU INTERESGARRI BATZUK: \n- independentziak:" + str(independentziak) + " \n- muga posibleak:" + str(mugaposibleak) + " \n- barne mugak:" + str(barnemugak)
with open("Historikoa.txt", "w") as file:
      file.write(texto)








