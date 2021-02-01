import pickle


class Macchina:
    nome = None
    diametro = ()
    interasse_min = None
    tipo_attrezzatura = []
    tipo_utensile = []
    diametro_max_utensile = None
    lavorazione = []
    programma_multiplo = None
    modulo_max = None
    altezza_fascia_max = None
    incl_elica_max_dx = None
    incl_elica_max_sx = None
    inclinazione_tavola = None
    altezza_attrezzatura_max = None

    def __init__(self, n, d, m_int_min, m_ta, m_tu, d_max_ut, m_lav, m_prog_multi, mod_max, h_fascia_max,
                 int_min=0, m_incl_elica_dx=0, m_incl_elica_sx=0, incl_tav=0, m_alt_att_max=0):
        self.nome = n
        self.diametro = d
        self.interasse_min = m_int_min
        self.tipo_attrezzatura = m_ta
        self.tipo_utensile = m_tu
        self.diametro_max_utensile = d_max_ut
        self.lavorazione = m_lav
        self.programma_multiplo = m_prog_multi
        self.modulo_max = mod_max
        self.altezza_fascia_max = h_fascia_max
        self.interasse_min = int_min
        self.incl_elica_max_dx = m_incl_elica_dx
        self.incl_elica_max_sx = m_incl_elica_sx
        self.inclinazione_tavola = incl_tav
        self.altezza_attrezzatura_max = m_alt_att_max

    def set_nome(self, n):
        self.nome = n

    def set_diametro(self, d):
        self.diametro = d

    def set_interasse_minimo(self, m_int_min):
        self.interasse_min = m_int_min

    def set_diametro_max_utensile(self, d_max_ut):
        self.diametro_max_utensile = d_max_ut

    def set_programma_multiplo(self, m_prog_multi):
        self.programma_multiplo = m_prog_multi

    def set_modulo_max(self, mod_max):
        self.modulo_max = mod_max

    def set_altezza_fascia_max(self, m_fascia_max):
        self.altezza_fascia_max = m_fascia_max

    def set_interasse_min(self, int_min):
        self.interasse_min = int_min

    def set_incl_elica_max_dx(self, m_incl_elica_dx):
        self.incl_elica_max_dx = m_incl_elica_dx

    def set_incl_elica_max_sx(self, m_incl_elica_sx):
        self.incl_elica_max_sx = m_incl_elica_sx

    def set_inclinazione_tavola(self, incl_tav):
        self.inclinazione_tavola = incl_tav

    def set_altezza_attrezzatura_max(self, m_alt_att_max):
        self.altezza_attrezzatura_max = m_alt_att_max


class Particolare:
    codice = None
    diametro = None
    interasse = None
    tipo_attrezzatura = []
    tipo_utensile = []
    diametro_utensile = None
    fase = None
    lavorazione = []
    programma_multiplo = None
    modulo = None
    fascia = None
    incl_elica_dx = None
    incl_elica_sx = None
    inclinazione = None
    altezza_attrezzatura = None

    def __init__(self, c, d, p_ta, p_tu, d_ut, p_f, p_lav, p_prog_multi, mod, fascia,
                 p_incl_elica_dx=0, p_incl_elica_sx=0, incl=0,  p_alt_att=0):
        self.codice = c
        self.diametro = d
        self.interasse = calcolo_interasse(d, d_ut)
        self.tipo_attrezzatura = p_ta
        self.tipo_utensile = p_tu
        self.diametro_utensile = d_ut
        self.fase = p_f
        self.lavorazione = p_lav
        self.programma_multiplo = p_prog_multi
        self.modulo = mod
        self.fascia = fascia
        self.incl_elica_dx = p_incl_elica_dx
        self.incl_elica_sx = p_incl_elica_sx
        self.inclinazione = incl
        self.altezza_attrezzatura = p_alt_att

    def set_codice(self, c):
        self.codice = c

    def set_diametro(self, d):
        self.diametro = d

    def set_fase(self, fs):
        self.fase = fs

    def set_diametro_utensile(self, d_ut):
        self.diametro_utensile = d_ut

    def set_programma_multiplo(self, p_prog_multi):
        self.programma_multiplo = p_prog_multi

    def set_modulo(self, mod):
        self.modulo = mod

    def set_fascia(self, fascia):
        self.fascia = fascia

    def set_incl_elica_dx(self, p_incl_elica_dx):
        self.incl_elica_dx = p_incl_elica_dx

    def set_incl_elica_sx(self, p_incl_elica_sx):
        self.incl_elica_sx = p_incl_elica_sx

    def set_inclinazione(self, incl):
        self.inclinazione = incl

    def set_altezza_attrezzatura(self, p_alt_att):
        self.altezza_attrezzatura = p_alt_att


Macchine_TFZ_Aprilia = []
Particolari = []


# todo cancellare alla consegna
def init_db_test():
    m1 = Macchina("15_24", (120, 300), 90, ["palo", "pinza", "contropunta", "corpo porta pinza"],  ["creatore"],
                  200, ["dentatura", "dentatura_conica"], True,
                  6, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m2 = Macchina("15_25", (100, 200), 90, ["palo", "pinza", "contropunta", "corpo porta pinza"], ["creatore"],
                  200,  ["dentatura", "dentatura_conica"], True,
                  4, 100, int_min=100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m3 = Macchina("15_16", (100, 200), 80, ["palo", "contropunta"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], True,
                  4, 100, m_incl_elica_dx=13, m_incl_elica_sx=21)
    m4 = Macchina("15_17", (100, 200), 80, ["palo", "contropunta"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], True,
                  4, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m5 = Macchina("15_15", (100, 200), 80, ["palo", "contropunta"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], False,
                  4, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m6 = Macchina("15-52", (100, 380), 80, ["contropunta", "corpo porta pinza"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], True,
                  8, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m7 = Macchina("15-54", (100, 380), 80, ["contropunta", "corpo porta pinza"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], True,
                  8, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m8 = Macchina("15_29", (100, 320), 80, ["contropunta", "corpo porta pinza", "manuale"], ["creatore"], 200,
                  ["dentatura", "dentatura_conica"], False,
                  7, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m9 = Macchina("20_52", (40, 380), 80, ["contropunta", "corpo porta pinza"], ["coltello", "tazza", "gambo"], 200,
                  ["stozza", "interna", "stozza elicoidale", "stozza elicoidale bombata"], False,
                  6, 50, incl_tav=10)
    m10 = Macchina("20_53", (40, 380), 80, ["contropunta", "corpo porta pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna", "stozza elicoidale", "stozza elicoidale bombata"], False,
                   6, 50, incl_tav=10)
    m11 = Macchina("15_18", (100, 250), 90, ["palo", "contropunta", "corpo porta pinza"], ["creatore"], 200,
                   ["dentatura", "dentatura_conica"], True,
                   5, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m12 = Macchina("15_10", (100, 320), 80, ["contropunta", "corpo porta pinza", "manuale"], ["creatore"], 200,
                   ["dentatura"], False,
                   6, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m13 = Macchina("15_26", (100, 200), 80, ["palo", "corpo porta pinza"], ["creatore"], 200,
                   ["dentatura", "dentatura_conica"], False,
                   5, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m14 = Macchina("20_13", (40, 200), 80, ["pinza", "corpo porta pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"], False,
                   5, 50, incl_tav=10)
    m15 = Macchina("20_12", (40, 200), 80, ["pinza", "corpo porta pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"], False,
                   5, 50)
    m16 = Macchina("20_51", (40, 200), 80, ["pinza", "contropunta", "corpo porta pinza"],
                   ["coltello", "tazza", "gambo"], 200, ["stozza", "interna", "stozza elicoidale"], False,
                   5, 50, incl_tav=10, m_alt_att_max=280)
    m17 = Macchina("20_04", (40, 200), 80, ["pinza", "contropunta", "corpo porta pinza"],
                   ["coltello", "tazza", "gambo"], 200, ["stozza", "interna", "stozza elicoidale"], False,
                   5, 60, )
    m18 = Macchina("20_10", (40, 200), 80, ["pinza", "corpo porta pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"], False,
                   5, 50, incl_tav=10, m_alt_att_max=280)
    m19 = Macchina("15_51", (40, 200), 80, ["pinza", "corpo porta pinza"], ["coltello"], 150,
                   ["stozza"], False,
                   5, 50, incl_tav=10)
    m20 = Macchina("20_08", (40, 200), 80, ["manuale"], ["coltello", "gambo"], 200,
                   ["stozza", "interna"], False,
                   5, 50)
    global Macchine_TFZ_Aprilia
    Macchine_TFZ_Aprilia = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]

    part1 = Particolare("752/3534368", 108.65, ["palo", "corpo porta pinza"], ["creatore"], 110, "120", ["dentatura"],
                        False, 3.75, 28, p_incl_elica_sx=20)
    part2 = Particolare("81/47823607", 119.4, ["palo", "manuale"], ["creatore"], 80, "120", ["dentatura_conica"],
                        False, 2, 53.5)
    part3 = Particolare("752/3535495", 105.3, ["manuale"], ["creatore"], 80, "120", ["dentatura"], False, 4, 20,
                        p_incl_elica_dx=24)
    part4 = Particolare("81/87553312", 75, ["corpo porta pinza"], ["coltello"], 120, "081", ["stozza elicoidale"],
                        False, 3, 22)
    part5 = Particolare("81/87553312", 80, ["corpo porta pinza"], ["coltello"], 160, "082", ["stozza"], False, 2.5, 45)
    part6 = Particolare("752/3534368", 60, ["pinza", "corpo porta pinza"], ["coltello"], 160, "080", ["stozza"], False,
                        4, 10, incl=8)
    part7 = Particolare("453/32106060", 74.9, ["palo"], ["creatore"], 100, "120", ["dentatura"],
                        False, 2.5, 22, p_incl_elica_sx=20)
    part8 = Particolare("81/84560087", 104.5, ["corpo porta pinza"], ["coltello"], 127.5, "080", ["stozza"],
                        False, 2.5, 10, p_alt_att=286)
    part9 = Particolare("81/87553311", 153.5, ["palo", "corpo porta pinza"], ["creatore"], 100, "121", ["dentatura"],
                        True, 2.75, 23, p_incl_elica_sx=20)
    part10 = Particolare("81/87553311", 131.5, ["palo", "corpo porta pinza"], ["creatore"], 100, "122", ["dentatura"],
                         True, 2.75, 23, p_incl_elica_sx=22)
    global Particolari
    Particolari = [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10]
    save_db("macchine")
    save_db("particolari")


# Ritorna true, se il valore del diametro è contenuto nella tupla (min, max).
def diametro_compatibile(valore, tupla):
    return tupla[0] <= valore <= tupla[1]


# Funzione che prende 2 dati, esegue la somma e il risultato lo divide per 2.
def calcolo_interasse(diam_pezzo, diam_ute):
    return (diam_pezzo + diam_ute) / 2


# Scorro 2 liste e vedo se l'oggetto è in entrambe le liste.
def oggetto_compatibile(ls_p, ls_m):
    for p in ls_p:
        for m in ls_m:
            if p == m:
                return True
    return False


# Valore (a) minore o uguale a (b).
def minore_uguale(a, b):
    if a is None or b is None:
        return True
    return a <= b


# Valore (a) maggiore o uguale a (b).
def maggiore_uguale(a, b):
    return a >= b


# Verifica se il particolare richiede un programma multiplo e ritorna True
def verifica_programma_multiplo(p_pm, m_pm):
    if not p_pm:
        return True
    elif m_pm:
        return True
    return False


# Creo una lista vuota da riempire con il codice che metto tramite l'input, che mi servirà per vedere se il codice è
# è presente nel database_particolari.
def lista_particolari(input_codice, db_particolari):
    lp = []
    lista_codice_particolari_simili = []
    for p in db_particolari:
        if input_codice == p.codice[8:] or input_codice == p.codice[7:] or input_codice == p.codice:
            lp.append(p)
    # Da qui controllo se lp contiene codici diversi con parte finale uguale.
    if len(lp) > 1:
        for item in lp:
            if item.codice not in lista_codice_particolari_simili:
                lista_codice_particolari_simili.append(item.codice)
    if len(lista_codice_particolari_simili) > 1:
        print("Quale codice è quello giusto?")
        for item in lista_codice_particolari_simili:
            print("   " + item)
        scelta = check_inserimento_stringhe(lista_codice_particolari_simili, "codice per intero")
        for item in lp:
            if item.codice != scelta:
                lp.remove(item)
    return lp


# Crea una mini lista che riempe prendendo le fasi dalla lista particolari.
def lista_fasi(particolari):
    l_f = []
    for pa in particolari:
        l_f.append(pa.fase)
    return l_f


# Controlla se il valore fase(int) nella macchina è uguale anche nel particolare.
def fase_compatibile(fs_macchina, fs_pezzo):
    return fs_macchina == fs_pezzo


# Funzione che confronta tutti parametri macchina e particolare e controlla se sono compatibili.
def compatibilita_generale(p, m):
    return diametro_compatibile(p.diametro, m.diametro) and \
        oggetto_compatibile(p.tipo_attrezzatura, m.tipo_attrezzatura) and \
        oggetto_compatibile(p.tipo_utensile, m.tipo_utensile) and \
        oggetto_compatibile(p.lavorazione, m.lavorazione) and \
        minore_uguale(p.modulo, m.modulo_max) and \
        maggiore_uguale(p.interasse, m.interasse_min) and \
        minore_uguale(p.fascia, m.altezza_fascia_max) and \
        minore_uguale(p.incl_elica_dx, m.incl_elica_max_dx) and \
        minore_uguale(p.incl_elica_sx, m.incl_elica_max_sx) and \
        minore_uguale(p.inclinazione, m.inclinazione_tavola) and \
        minore_uguale(p.altezza_attrezzatura, m.altezza_attrezzatura_max) and \
        verifica_programma_multiplo(p.programma_multiplo, m.programma_multiplo)


# Funzione che scorre le 2 liste del database (macchine e particolari), e ,usando la funzione "compatibilità_generale",
# mi stampa su quali macchine il particolare in questione è lavorabile. In questa funzione è presente anche la verifica
# della fase del pezzo.
def macchine_compatibili(ls_part, ls_macc, fs=None):
    for p in ls_part:
        for m in ls_macc:
            if fs is None:
                if compatibilita_generale(p, m):
                    print(m.nome)
            else:
                if p.fase == fs:
                    if compatibilita_generale(p, m):
                        print(m.nome)


# Scorre la lista macchine e mi ritorna la macchina.
def get_macchina(nome_macchina):
    for m in Macchine_TFZ_Aprilia:
        if m.nome == nome_macchina:
            return m
    else:
        print("Macchina non trovata")


# Come "get_macchina" con la differenza che questa funzione controlla anche la fase, in caso ci siano particolari
# presenti nel database con più fasi.
def get_particolare(codice_particolare, fs):
    for p in Particolari:
        if p.codice == codice_particolare and p.fase == fs:
            return p
    else:
        print("Codice non trovato")


# Stampa gli attributi della macchina o del particolare. Esempio: { 'nome': '15_24', 'diametro': (120, 300) } ecc...
def stampa_valori(v):
    try:
        print(vars(v))
    except TypeError:
        print("Testo non corretto")


# Permette di dividere in "numero" e "valore" la stampa degli attributi della macchina o del particolare.
def stampa_etichetta(indice):
    for numero, valore in indice.items():
        print(f'[{numero}] - {valore}')


# Controlla se un oggetto è in una lista e stampa gli oggetti che trova nella lista.
def stampa_lista(lista):
    for item in lista:
        print("   " + item)


# Verifica se l'input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto. Ritorna una lista.
def check_inserimento_dati(lista, tipo):
    scelta = input(f'Inserire {tipo} (utilizzare virgola per scelte multiple): ').strip()
    while not valuta_input_testo(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente il tipo di {tipo}: ').strip()
    return crea_lista_da_stringa(scelta)


# Verifica se l'input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto. Ritorna una stringa.
def check_inserimento_stringhe(lista, tipo):
    scelta = input(f'Inserire {tipo}: ').strip()
    while not valuta_input_testo(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente "{tipo}": ').strip()
    return scelta


# Rimuove una macchina dalla lista.
def remove_macchina(nome_macchina):
    x = get_macchina(nome_macchina)
    if isinstance(x, Macchina):
        Macchine_TFZ_Aprilia.remove(x)
        print("Macchina eliminato con successo")


# Rimuove un particolare dalla lista, con opzione per selezionare il tipo di fase.
def remove_particolare(codice_particolare, fs):
    x = get_particolare(codice_particolare, fs)
    if isinstance(x, Particolare):
        Particolari.remove(x)
        print("Codice eliminato con successo")


# Funzione per edit lista attrezzatura, sia per la macchina che per il particolare
def edit_lista(tipo, operazione, valore):
    if operazione == "aggiungere":
        tipo.tipo_attrezzatura.append(valore)
    if operazione == "rimuovi":
        try:
            tipo.tipo_attrezzatura.remove(valore)
        except ValueError:
            print(f'{valore} non presente nella lista attrezzatura!')


# Funzione per editare macchine o particolari
def edit(cod, tipo, fs=None):
    if tipo == "m":
        m = get_macchina(cod)
        if isinstance(m, Macchina):
            stampa_etichetta(Indice_attributi_macchina)
            choice = int(input("Quale voce vuoi modificare?: "))
            # Controllo se la modifica riguarda una lista
            if choice in [3, 4, 6]:
                tipo_modifica = input("Vuoi aggiungere o rimuovere?: ")
                if tipo_modifica != "aggiungere" or "rimuovere":
                    print("Scelta errata!")
                valore_modifica = input("Inserisci la modifica: ")
                edit_lista(m, tipo_modifica, valore_modifica)
            # Controllo se la modifica riguarda una tupla
            elif choice == 1:
                minimo = input("Inserire valore minimo:")
                massimo = input("Inserire valore massimo: ")
                m.set_diametro((minimo, massimo))
            # Altrimenti la modifica è di tipo stringa o numero
            else:
                scelta_utente = input("Inserire la modifica: ")
                # Questa voce mi prendere l' attributo, che scelgo tramite input [scelta], da un dizionario
                getattr(m, "set_" + Indice_attributi_macchina[choice])(scelta_utente)
            stampa_valori(m)
            print("Modifica completata con successo!")
    elif tipo == "p":
        p = get_particolare(cod, fs)
        if isinstance(p, Particolare):
            stampa_etichetta(Indice_attributi_particolare)
            scelta = int(input("Quale voce vuoi modificare?: "))
            # Controllo se la modifica riguarda una lista
            if scelta in [3, 4]:
                tipo_modifica = input("Vuoi aggiungere o rimuovere?: ")
                if tipo_modifica != "aggiungere" or "rimuovere":
                    print("Scelta errata!")
                valore_modifica = input("Inserisci la modifica: ")
                edit_lista(p, tipo_modifica, valore_modifica)
            # Altrimenti la modifica è di tipo stringa o numero
            else:
                scelta_utente = int(input("Inserire la modifica: "))
                # Questa voce mi prendere l' attributo, che scelgo tramite input [scelta], da un dizionario
                getattr(p, "set_" + Indice_attributi_macchina[scelta])(scelta_utente)
            stampa_valori(p)
            print("Modifica completata con successo!")


# Prima toglie lo spazio dalla scelta e poi lo spezza in lista per ogni virgola,
# ritorna True se la scelta è contenuta nella lista
def valuta_input_testo(scelta, lista):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return set(scelta) <= set(lista)


# Prima toglie eventuali spazi e poi spezza in lista per ogni virgola.
def crea_lista_da_stringa(scelta):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return scelta


# Se il particolare, in fase di inserimento, presenta una dentatura/stozza elicoidale, con questa funzione posso
# selezionare il verso dell'elica e poi inserire il valore.
def scelta_elica():
    valore_elica = None
    elica = input("Inserire verso dell'elica (dx, sx): ")
    if elica == "dx":
        valore_elica = int(input("Inserire elica pezzo(dx): "))
    elif elica == "sx":
        valore_elica = int(input("Inserire elica pezzo(sx): "))
    else:
        print("Inserimento errato. Consentiti solo 'dx' e 'sx'")
        quit()
    return elica, valore_elica


# Funzione che inserisce una macchina o un particolare nel database.
def insert_database(cod, tipo, fs=None):
    lista_attrezzatura = ["palo", "pinza", "corpo porta pinza" "manuale", "contropunta"]
    lista_utensili = ["creatore", "coltello", "tazza", "gambo"]
    lista_lavorazioni = ["dentatura", "dentatura conica", "stozza", "stozza elicoidale", "stozza elicoidale bombata"]
    lista_fasi_pezzo = ["080", "081", "082", "083", "084", "085", "120", "121", "122", "123", "124", "125"]
    try:
        if tipo == "m":
            x = get_macchina(cod)
            if isinstance(x, Macchina):
                print(f'La macchina "{cod}" è presente nel database.')
            else:
                print(f'Inserire valori macchina "{cod}"')
                d_min = int(input("Inserire diametro minimo: "))
                d_max = int(input("Inserire diametro massimo: "))
                d = (d_min, d_max)
                input("Inserisci interasse minimo: ")
                stampa_lista(lista_attrezzatura)
                att = check_inserimento_dati(lista_attrezzatura, "attrezzatura")
                stampa_lista(lista_utensili)
                t_u = check_inserimento_dati(lista_utensili, "utensile")
                d_max_u = int(input("Inserire il diametro massimo dell'utensile: "))
                stampa_lista(lista_lavorazioni)
                lav = check_inserimento_dati(lista_lavorazioni, "lavorazione")
                mod_max = int(input("Inserire modulo massimo: "))
                h_max = int(input("Inserire altezza fascia massima: "))
                int_min = int(input("Inserire interasse minimo: "))
                inc_el_max_dx = int(input("Inserire inclinazione elica dx massima: "))
                inc_el_max_sx = int(input("Inserire inclinazione elica sx massima: "))
                inc_tav = int(input("Inserire inclinazione tavola: "))
                m = Macchina(cod, d, int_min, att, t_u, d_max_u, lav, mod_max, h_max, int_min,
                             inc_el_max_dx, inc_el_max_sx,
                             inc_tav)
                stampa_valori(m)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Macchine_TFZ_Aprilia.append(m)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
        else:
            pass
        if tipo == "p":
            y = get_particolare(cod, fs)
            if isinstance(y, Particolare):
                print(f'Il particolare "{cod}" è presente nel database.')
            else:
                print(f'Inserire valori particolare "{cod}"')
                d = int(input("Inserire diametro pezzo: "))
                stampa_lista(lista_attrezzatura)
                att = check_inserimento_dati(lista_attrezzatura, "attrezzatura")
                stampa_lista(lista_utensili)
                t_u = check_inserimento_dati(lista_utensili, "utensile")
                d_u = int(input("Inserire diametro utensile: "))
                fs = check_inserimento_stringhe(lista_fasi_pezzo, "fase")
                stampa_lista(lista_lavorazioni)
                lav = check_inserimento_stringhe(lista_lavorazioni, "lavorazione")
                inc_el_dx = None
                inc_el_sx = None
                inc = None
                if lav == "stozza":
                    inc = int(input("Inserire inclinazione pezzo: "))
                elif lav == "dentatura":
                    scelta = input("Dentatura dritta o elicoidale?: ")
                    if scelta != "dritta":
                        elica = scelta_elica()
                        if elica[0] == "dx":
                            inc_el_dx = elica[1]
                        else:
                            inc_el_sx = elica[1]
                else:
                    elica = scelta_elica()
                    if elica[0] == "dx":
                        inc_el_dx = elica[1]
                    else:
                        inc_el_sx = elica[1]
                m = int(input("Inserire modulo: "))
                h = int(input("Inserire fascia: "))
                p = Particolare(cod, d, att, t_u, d_u, fs, lav, m, h, inc_el_dx, inc_el_sx, inc)
                stampa_valori(p)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Particolari.append(p)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
    except ValueError:
        print("Valore errato. Hai inserito un carattere invece che un numero.")
        # menu()


# Funzione per il salvataggio del database.
def save_db(tipo):
    print(f'   ... salvataggio database {tipo}.')
    with open(f'db_{tipo}.pickle', 'wb') as handle:
        if tipo == "macchine":
            pickle.dump(Macchine_TFZ_Aprilia, handle, protocol=pickle.HIGHEST_PROTOCOL)
        elif tipo == "particolari":
            pickle.dump(Particolari, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            print(f'Errore! Valore {tipo} non valido!')


# Funzione per il caricamento del database.
def load_db():
    try:
        global Macchine_TFZ_Aprilia
        global Particolari
        with open(f'db_macchine.pickle', 'rb') as handle:
            print('Database macchine caricato')
            Macchine_TFZ_Aprilia = pickle.load(handle)
        with open(f'db_particolari.pickle', 'rb') as handle:
            print('Database particolari caricato')
            Particolari = pickle.load(handle)
        return True
    except FileNotFoundError:
        print("... file db non trovato")
        return False


if __name__ == '__main__':
    Indice_attributi_macchina = {0: "nome", 1: "diametro", 2: "interasse_min", 3: "tipo_attrezzatura",
                                 4: "tipo_utensile", 5: "diametro_max_utensile", 6: "lavorazione", 7: "modulo_max",
                                 8: "altezza_fascia_max", 9: "incl_elica_max_dx", 10: "incl_elica_max_sx",
                                 11: "inclinazione_tavola", 12: "altezza attrezzatura"}
    Indice_attributi_particolare = {0: "codice", 1: "diametro", 2: "interasse", 3: "tipo_attrezzatura",
                                    4: "tipo_utensile", 5: "diametro_utensile", 6: "fase", 7: "lavorazione",
                                    8: "modulo", 9: "fascia", 10: "incl_elica_dx", 11: "incl_elica_sx",
                                    12: "inclinazione", 13: "altezza attrezzatura"}
    load_db()

    codice = input("Inserire codice particolare (inserire codice completo o ultime 4 cifre): ")
    mini_lista = lista_particolari(codice, Particolari)
    if len(mini_lista) == 1:
        macchine_compatibili(mini_lista, Macchine_TFZ_Aprilia)
    elif len(mini_lista) > 1:
        print("Il codice presenta più fasi. Quale intendi scegliere?")
        li_fa = lista_fasi(mini_lista)
        for index in li_fa:
            print("   " + index)
        fase = check_inserimento_stringhe(li_fa, "fase")
        if fase != li_fa:
            macchine_compatibili(mini_lista, Macchine_TFZ_Aprilia, fase)
    else:
        print("Particolare non presente nel database.")
