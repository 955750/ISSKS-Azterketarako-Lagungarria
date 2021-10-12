##Inportatu beharrekoak
import operator
import string

##Azpiprogramak

#Zerrendak elementuz elementu inprimatzeko
def zerrendaInprimatu(m):
    for i in m:
        print(i)

#Hizki bakoitza zenbat aldiz agertzen den kalkulatzeko
def maiztasunakLortu(hizHiztegia, mezua):
    hizkiak = hizHiztegia.keys()
    for i in hizkiak:
        zenbat = mezua.count(i)
        hizHiztegia[i] = zenbat
       
#Kodetutako mezuko hizkia ustezko benetako mezuko hizki batekin ordezkatzeko
def hizkiaOrdezkatu(hizkiZaharra, hizkiBerria, mezua, hKorresp):
    hKorresp[hizkiZaharra] = hizkiBerria
    return mezua.replace(hizkiZaharra, hizkiBerria)

#Kopuru jakin bateko luzera duten hitza lortzeko, non "n" hizkiaren luzera izango baita
def nHizkikoHitzakLortu(n, mezua):
    hitzZerrenda = []
    kont = 0
    unekoHitza = ""
    for i in mezua:
        if i == " " or i in string.punctuation:
            if kont == n:
                hitzZerrenda.append(unekoHitza)
            kont = 0
            unekoHitza = ""
        else:
            unekoHitza = unekoHitza + i
            kont = kont + 1
    return hitzZerrenda
            
#Mezua ea guztiz deskodetuta dagoen ala ez jakiteko
def mezuaDeskodetutaBaiEz(mezua):
    m = mezua.lower()
    return m == mezua
     
##Programa Nagusia

mkodetua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE \
RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ \nRKCHXKCI AX CJAXDXJAXJRCE  AX RTENX, E \
ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ \nEJEKSZCNHE. \n \n\
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE \
XJ GZTCI AX 1936. \nDXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, \
JI REVI AXT RCXTI. DXKNIJCOCREQE TE \nHKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ \
XJIKPX  DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, \nKXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI \
XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE \nCAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ \
AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. \nNCJ AZKKZHC SZXAI PEN \
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT \nOKXJHX\
DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,  HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK \
TE \nKXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK  \
HKCZJOI OKEJSZCNHE. \n"
print("Deskodetu beharreko mezua: \n")
print(mkodetua)
#mkodetua = mkodetua.lower() #mezu osoa hizki xehez idatzeko

hizkiMaiztasuna = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0,
                "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
                "K": 0, "L": 0, "M": 0, "N": 0, "Ñ": 0,
                "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0,
                "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                "Y": 0, "Z": 0}

hizkiKorrespondentzia = {"A": " ", "B": " ", "C": " ", "D": " ", "E": " ",
                "F": " ", "G": " ", "H": " ", "I": " ", "J": " ",
                "K": " ", "L": " ", "M": " ", "N": " ", "Ñ": " ",
                "O": " ", "P": " ", "Q": " ", "R": " ", "S": " ",
                "T": " ", "U": " ", "V": " ", "W": " ", "X": " ",
                "Y": " ", "Z": " "}

print("Hona hemen hizkien maiztasun taula: \n")
#Hitz bakoitza zenbat aldiz agertzen den kalkulatzeko
maiztasunakLortu(hizkiMaiztasuna, mkodetua)
#Hizkien zerrenda inprimatzerakoan ordenatuta agertzeko
maiztOrdenatua = sorted(hizkiMaiztasuna.items(), key=operator.itemgetter(1), reverse = True)
#Maiztasunen taula ordenatua inprimatzeko
zerrendaInprimatu(maiztOrdenatua)

#1. Lehenengo ordezkapenak: 'X': 103 -> 'E'; 'E': 94 -> 'A'
print("\n")
print("Gaztelanian gehien agertzen diren hizkiak 'e' eta 'a' direnez eta 'X' eta 'E' kodetutako \n\
mezuan gehien agertzen diren hizkiak direnez, 'X' -> 'e' eta 'E' -> 'a'. \n")
mkodetua = hizkiaOrdezkatu(maiztOrdenatua[0][0], "e", mkodetua, hizkiKorrespondentzia)
mkodetua = hizkiaOrdezkatu(maiztOrdenatua[1][0], "a", mkodetua, hizkiKorrespondentzia)
print("Beraz, mezua honela geratuko da: \n")
print(mkodetua)
print("Eta honela geratuko da gure hizki korrespondentzia taula: \n")
hKorOrdenatua = sorted(hizkiKorrespondentzia.items())
zerrendaInprimatu(hKorOrdenatua)
print("\n")
print("#######################################################################################")
print("\n")


#2. 2 eta 3 hizkiko luzera duten hitzak erabilita, logika bidez ondorioztatu: A -> d; T -> l
print("Behin lehenengo aldaketak eginda 2 eta 3 hizkiko luzera duten hitzak aztertuko ditugu: \n")
print(nHizkikoHitzakLortu(3, mkodetua))
print(nHizkikoHitzakLortu(2, mkodetua))
print("\n")
print("Hitzek dituzten hizkiak aztertuta, 'A' -> 'd' eta 'T' -> 'l' ondoriozta dezakegu. \n")
mkodetua = hizkiaOrdezkatu("A", "d", mkodetua, hizkiKorrespondentzia)
mkodetua = hizkiaOrdezkatu("T", "l", mkodetua, hizkiKorrespondentzia)
print("Beraz, mezua honela geratuko da: \n")
print(mkodetua)
print("Eta honela geratuko da gure hizki korrespondentzia taula: \n")
hKorOrdenatua = sorted(hizkiKorrespondentzia.items())
zerrendaInprimatu(hKorOrdenatua)
print("\n")
print("#######################################################################################")
print("\n")

#3. Hemendik aurrera logika bidez ondorioztatu A -> d; T -> l
#BEGIZTA NAGUSIA

while(mezuaDeskodetutaBaiEz(mkodetua) == False):
    print("Hona hemen hizkien maiztasun taula: \n")
    #Hitz bakoitza zenbat aldiz agertzen den kalkulatzeko
    maiztasunakLortu(hizkiMaiztasuna, mkodetua)
    #Hizkien zerrenda inprimatzerakoan ordenatuta agertzeko
    maiztOrdenatua = sorted(hizkiMaiztasuna.items(), key=operator.itemgetter(1), reverse = True)
    #Maiztasunen taula ordenatua inprimatzeko
    zerrendaInprimatu(maiztOrdenatua)
    print("\n")
    print("Eta egungo mezua: \n")
    print(mkodetua)
    hKendu = ""
    hGehitu = ""
    while(len(hKendu) != 1):
        hKendu = str(input("Zein hizki kendu nahi duzu?"))
        print(hKendu)
    while(len(hGehitu) != 1):
        hGehitu = str(input("Zein hizki gehitu nahi duzu " + hKendu + "-ren ordez ?"))
        print(hGehitu)    
    
    print("' " + hKendu + "' hizkia '" + hGehitu + "' hizkiarekin ordezkatzea erabaki duzu.")
    mkodetua = hizkiaOrdezkatu(hKendu, hGehitu, mkodetua, hizkiKorrespondentzia)
    print("Beraz, mezua honela geratuko da: \n")
    print(mkodetua)
    print("Eta honela geratuko da gure hizki korrespondentzia taula: \n")
    hKorOrdenatua = sorted(hizkiKorrespondentzia.items())
    zerrendaInprimatu(hKorOrdenatua)
    print("\n")
    print("#######################################################################################")
    print("\n")


    
##################################################################################
print("ZORIONAK!!! MEZUA DESKODETZEA LORTU DUZU!!!")

print(mezuaDeskodetutaBaiEz(mkodetua))
