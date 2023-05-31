import os
def pulisci():
    os.system("cls")

def rappresenta_elenco():
    print("""
    R1-Apparecchiature refrigeranti
    R2-Grandi bianchi
    R3-TV e monitor
    R4-Piccoli elettrodomestici ed elettronica di consumo
    R5-Sorgenti luminose
    uscire
    """)



def apparecchiature_rifrigeranti(f1):
    f1 = open("apparecchiature_rifregeranti.txt", "r+")
    lista = ["Frigorifero","Congelatore","Frigo-bar","Cantinetta per vini","Cellula di raffreddamento","Dispenser per acqua refrigerata","Frigorifero per vini","Frigorifero combinato","Frigorifero side-by-side","Frigorifero a due porte","Frigorifero a tre porte","Frigorifero a quattro porte","Frigorifero da banco","Frigorifero per bevande","Frigorifero per gelati","Ghiacciaia","Vetrina refrigerata","Armadio refrigerato","Banco frigo","Cassettiera refrigerata","Cellula di raffreddamento per ristoranti","Cella frigorifera portatile","Isola refrigerata","Frigo per negozi di alimentari","Frigorifero a scomparsa","Frigorifero per camper","Frigorifero per barche","Frigorifero per ufficio","Frigorifero per laboratorio","Frigorifero per farmacie"]
    pulisci()
    print(lista)
    oggetto_da_buttare = input("inserisci un oggetto da buttare: ")
    for i in range(len(lista)):
        f1.write(lista[i] + "; " + "\n")
    for i in range(len(lista)):
        if oggetto_da_buttare == lista[i]:
            f1.write(f"l'oggeto inserito c'è nella lista, {oggetto_da_buttare}")
            break
        else:
            f1.write(f"l'oggetto inserito non c'è nella lista {oggetto_da_buttare}")
            break
    f1.close()

def grandi_bianchi(f2):
    f2 = open("grandi_bianchi.txt", "r+")
    lista = ["Lavatrice","Lavatrice-asciugatrice","Lavastoviglie","Frigorifero","Congelatore","Frigorifero-congelatore","Frigorifero side-by-side","Frigorifero a doppia porta","Frigorifero con dispenser per acqua e ghiaccio","Frigorifero da incasso","Frigorifero per vini","Cappa aspirante","Piano cottura a gas","Piano cottura elettrico","Forno a gas","Forno elettrico","Forno a microonde","Forno a vapore","Forno a doppia funzione (forno combinato)","Cucina a gas","Cucina elettrica","Cucina a induzione","Piano cottura a induzione","Congelatore verticale","Congelatore orizzontale","Congelatore da incasso","Frullatore","Frullatore ad immersione","Robot da cucina","Macchina per il caffè","Macchina per il caffè espresso","Macchina per il caffè a cialde","Tostapane","Tostapane a 4 fette","Bollitore elettrico","Tostapane per panini","Spremiagrumi","Centrifuga per frutta e verdura","Tritatutto","Tritatutto per alimenti","Tritatutto per ghiaccio","Tritatutto a immersione","Fornetto elettrico","Forno a convezione","Tavolo da stiro","Ferro da stiro","Aspirapolvere","Aspirapolvere a traino","Aspirapolvere a bidone","Aspirapolvere robot","Aspirapolvere a batteria","Aspirapolvere verticale","Aspirapolvere per auto","Asciugatrice","Asciugacapelli","Asciugacapelli professionale","Bilancia da cucina","Bilancia digitale","Bilancia pesapersone","Fornello elettrico","Fornello a gas","Bollitore elettrico","Bollitore ad immersione","Scaldabagno","Scaldabagno elettrico","Scaldabagno a gas","Robot aspirapolvere","Macchina per il pane","Tritatutto a lama","Tritatutto a disco","Tritatutto a centrifuga","Tritatutto a impulsi","Tritatutto multifunzione","Tritatutto a velocità variabile","Tritatutto a immersione professionale","Tritatutto a immersione senza fili","Tritatutto a immersion"]
    pulisci()
    print(lista)
    oggetto_da_buttare = input("inserisci l'oggetto da buttare: ")
    for i in range(len(lista)):
        print(lista[i])
    for i in range(len(lista)):
        if oggetto_da_buttare == lista[i]:
            f2.write(f"l'oggetto inserito c'è nella lista, {oggetto_da_buttare}")
        else:
            f2.write(f"l'oggetto inserito non c'è nella lista, {oggetto_da_buttare}")
    f2.close()

def tv_monitor(f3):
    f3 = open("tv_monitor.txt", "r+")
    lista = ["Sony Trinitron","Panasonic CRT TV","Philips CRT TV","Toshiba CRT TV","Samsung CRT TV","LG CRT TV","JVC CRT TV","Sharp CRT TV","RCA CRT TV","Hitachi CRT TV","Mitsubishi CRT TV","Zenith CRT TV","Daewoo CRT TV","Grundig CRT TV","Akai CRT TV","Sanyo CRT TV","Vestel CRT TV","Funai CRT TV","GoldStar CRT TV","Admiral CRT TV","Haier CRT TV","Hisense CRT TV","Konka CRT TV","NEC CRT TV","Orion CRT TV","Polaroid CRT TV","TCL CRT TV","ViewSonic CRT Monitor","Dell CRT Monitor","HP CRT Monitor","IBM CRT Monitor","Compaq CRT Monitor","BenQ CRT Monitor","EIZO CRT Monitor","NEC CRT Monitor","Philips CRT Monitor","Samsung CRT Monitor","Sony CRT Monitor","ViewSonic CRT Monitor","Apple CRT Monitor","AOC CRT Monitor","LG CRT Monitor","Mitsubishi CRT Monitor","Panasonic CRT Monitor","Sharp CRT Monitor","Toshiba CRT Monitor","Hitachi CRT Monitor","JVC CRT Monitor","Zenith CRT Monitor","Konica Minolta CRT Monitor","Sun Microsystems CRT Monitor","Silicon Graphics CRT Monitor","Acer CRT Monitor","Fujitsu CRT Monitor","Gateway CRT Monitor","Iiyama CRT Monitor","Princeton CRT Monitor","LaCie CRT Monitor","Philips Magnavox CRT TV","Proview CRT Monitor","Hyundai CRT Monitor","Envision CRT Monitor","Mitsubishi Diamondtron CRT Monitor","Tatung CRT Monitor","MAG Innovision CRT Monitor","Emachines CRT Monitor","Westinghouse CRT Monitor","HANNSpree CRT Monitor","Princeton Graphics CRT Monitor","KDS CRT Monitor","Optiquest CRT Monitor","Planar CRT Monitor","Sceptre CRT Monitor","Soyo CRT Monitor","V7 CRT Monitor","Polaroid FLM CRT TV","Astar CRT TV","Norcent CRT TV","Maxent CRT TV","Vizio CRT TV","Olevia CRT TV","Curtis Mathes CRT TV","Symphonic CRT TV","Viore CRT TV","Sansui CRT TV","Coby CRT TV","Element CRT TV","Proscan CRT TV","RCA Proscan CRT TV","Emerson CRT TV"]
    pulisci()
    print(lista)
    oggetto_da_buttare = input("inserisci l'oggetto da buttare: ")
    for i in range(len(lista)):
        print(lista)
    for i in range(len(lista)):
        if oggetto_da_buttare == lista[i]:
            f3.write(f"l'oggetto inserito c'è nella lista, {oggetto_da_buttare}")
        else:
            f3.write(f"l'oggetto inserito non c'è nella lista, {oggetto_da_buttare}")
    f3.close()

def picc_elettrodomestici_elettronica_consumo(f4):
    f4 = open("picc_elettrodomestici_elettronica_consumo.txt", "r+")
    lista = ["Smartphone","Tablet","Laptop","Desktop computer","Stampante","Videocamera","Fotocamera digitale","Videocamera di sicurezza","Lettore DVD/Blu-ray","Console per videogiochi","Smart TV","Proiettore","Altoparlante Bluetooth","Auricolari wireless","Radio","Telecomando universale","Router Wi-Fi","Modem","Power bank","Aspirapolvere robot","Robot da cucina","Tostapane","Bollitore elettrico","Macchina per il caffè","Frullatore","Ferro da stiro","Asciugacapelli","Bilancia da cucina","Forno a microonde","Aspirapolvere","Sega circolare","Trapano elettrico","Smerigliatrice","Cacciavite elettrico","Pistola termica","Giocattoli radiocomandati","Console di gioco portatile","Puzzle elettronici","Robot giocattolo","Drone","Luci LED per interni","Lampada da tavolo","Lampada a sospensione","Lampadina LED","Lampada a LED intelligente","Sveglia","Termometro digitale","Misuratore di pressione sanguigna","Glucometro","Tensimetro","Bilancia digitale","Nebulizzatore","Elettrocardiografo (ECG)","Ossimetro","Termometro auricolare","Monitor per la pressione sanguigna","Sfigmomanometro digitale","Monitor per il sonno","Stetoscopio elettronico","Monitor per la frequenza cardiaca","Dispositivo per la terapia del dolore","Cuffia per l'insonorizzazione","Registratori vocali digitali","Cuffie wireless","Ricevitore satellitare","Decoder TV","Telefono fisso","Sistema di allarme domestico","Telecamera di sorveglianza","Auricolare con cancellazione del rumore","Orologio intelligente","Sistema di navigazione GPS","Telecamera di videosorveglianza","Scanner","Stampante 3D","Proiettore portatile","Console per DJ","Mixer audio","Sintetizzatore","Tastiera elettronica","Macchina per karaoke","Ricevitore stereo","Impianto audio surround","Scheda audio esterna","Microfono professionale","Apparecchio per la pulizia del viso","Epilatore","Massaggiatore","Fotocamera di sorveglianza wireless","Monitor per la salute del sonno"]
    pulisci()
    print(lista)
    oggetto_da_buttare = input("inserisci l'oggetto da buttare: ")
    for i in range(len(lista)):
        print(lista[i])
    for i in range(len(lista)):
        if oggetto_da_buttare == lista[i]:
            f4.write(f"l'oggetto inserito c'è nella lista, {oggetto_da_buttare}")
        else:
            f4.write(f"l'oggetto inserito non c'è nella lista, {oggetto_da_buttare}")
        f4.close()


def sorgente_luminosa(f5):
    f5 = open("sorgente_luminosa.txt", "r+")
    lista = []
    print(lista)
    oggetto_da_buttare = input("inserisci l'oggetto da buttare")






def menù():
    f1 = open("apparecchiature_rifregeranti.txt", "w")
    f2 = open("grandi_bianchi.txt", "w")
    f3 = open("tv_monitor.txt" , "w")
    f4 = open("piccolo elettrodomestici ed elettronica di consumo.txt", "w")
    f5 = open("sorgenti_luminose.txt", "w")
    while True:
        rappresenta_elenco()
        numero = int(input("inserisci un numero da 1 a 6: "))
        if numero >=1 and numero <= 6:
            if numero == 1:
                apparecchiature_rifrigeranti(f1)
            elif numero == 2:
                grandi_bianchi(f2)
            elif numero == 3:
                tv_monitor(f3)
            elif numero == 4:
                picc_elettrodomestici_elettronica_consumo(f4)
            elif numero == 5:
                    sorgente_luminosa(f5)
            elif numero == 6:
                break
menù()

