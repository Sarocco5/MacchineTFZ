import pickle


class Macchina:
    nome = None
    diametro = ()
    interasse_min = None
    tipo_attrezzatura = []
    tipo_utensile = []
    diametro_max_utensile = None
    lavorazione = []
    modulo_max = None
    altezza_fascia_max = None
    incl_elica_max_dx = None
    incl_elica_max_sx = None
    inclinazione_tavola = None

    def __init__(self, n, d, m_ta, m_tu, d_max_ut, m_lav, mod_max, h_fascia_max,
                 int_min=0, m_incl_elica_dx=0, m_incl_elica_sx=0, incl_tav=0):
        self.nome = n
        self.diametro = d
        self.tipo_attrezzatura = m_ta
        self.tipo_utensile = m_tu
        self.diametro_max_utensile = d_max_ut
        self.lavorazione = m_lav
        self.modulo_max = mod_max
        self.altezza_fascia_max = h_fascia_max
        self.interasse_min = int_min
        self.incl_elica_max_dx = m_incl_elica_dx
        self.incl_elica_max_sx = m_incl_elica_sx
        self.inclinazione_tavola = incl_tav

    def set_diametro(self, d):
        self.diametro = d

    def set_tipo_attrezzatura(self, m_ta):
        self.tipo_attrezzatura = m_ta

    def set_tipo_utensile(self, m_tu):
        self.tipo_utensile = m_tu

    def set_diametro_max_utensile(self, d_max_ut):
        self.diametro_max_utensile = d_max_ut

    def set_lavorazione(self, m_lav):
        self.lavorazione = m_lav

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


class Particolare:
    nome = None
    diametro = None
    interasse = None
    tipo_attrezzatura = None
    tipo_utensile = []
    diametro_utensile = None
    fase = []
    lavorazione = []
    modulo = ()
    fascia = None
    incl_elica_dx = None
    incl_elica_sx = None
    inclinazione = None

    def __init__(self, c, d, p_ta, p_tu, d_ut, p_f, p_lav, mod, fascia,
                 p_incl_elica_dx=0, p_incl_elica_sx=0, incl=0):
        self.codice = c
        self.diametro = d
        self.interasse = calcolo_interasse(d, d_ut)
        self.tipo_attrezzatura = p_ta
        self.tipo_utensile = p_tu
        self.diametro_utensile = d_ut
        self.fase = p_f
        self.lavorazione = p_lav
        self.modulo = mod
        self.fascia = fascia
        self.incl_elica_dx = p_incl_elica_dx
        self.incl_elica_sx = p_incl_elica_sx
        self.inclinazione = incl


# Ritorna true, se il valore del diametro è contenuto nella tupla (min, max).
def diametro_compatibile(valore, tupla):
    return tupla[0] <= valore <= tupla[1]


# Definisco che tipo ti lavorazione è.
def tipo_lavorazione(p_lav, m_lav):
    return p_lav in m_lav


# Funzione che prende 2 dati, esegue la somma e il risultato lo divide per 2.
def calcolo_interasse(diam_pezzo, diam_ute):
    return (diam_pezzo + diam_ute) / 2


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def attrezzatura_compatibile(p_ta, m_ta):
    for attrezzatura in p_ta:
        return attrezzatura in m_ta


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def utensile_compatibile(p_tu, m_tu):
    return p_tu in m_tu


# Valore A minore o uguale a B.
def minore_uguale(a, b):
    return a <= b


# creo una lista vuota da riempire con il codice che metto tramite l'input, che mi servirà per vedere se il codice è
# è presente nel database_particolari.
def lista_particolari(input_codice, db_particolari):
    lp = []
    for particolare in db_particolari:
        if input_codice == particolare.codice:
            lp.append(particolare)
    return lp


# Crea una mini lista che riempe prendendo le fasi dalla lista particolari.
def lista_fasi(particolari):
    l_f = []
    for pa in particolari:
        l_f.append(pa.fase)
    return l_f


# Controlla se un dato in "macchina" è presente anche in "particolare", se si mi ritorna True.
def fase_compatibile(fs_macchina, fs_pezzo):
    if fs_macchina == fs_pezzo:
        return True
    return False


# Funzione che confronta tutti parametri macchina e particolare e controlla se sono compatibili.
def compatibilita_generale(m, p):
    return diametro_compatibile(p.diametro, m.diametro) and \
        utensile_compatibile(p.tipo_utensile, m.tipo_utensile) and \
        tipo_lavorazione(p.lavorazione, m.lavorazione) and \
        attrezzatura_compatibile(p.tipo_attrezzatura, m.tipo_attrezzatura) and \
        minore_uguale(p.modulo, m.modulo_max) and \
        minore_uguale(p.fascia, m.altezza_fascia_max) and \
        minore_uguale(p.incl_elica_dx, m.incl_elica_max_dx) and \
        minore_uguale(p.incl_elica_sx, m.incl_elica_max_sx) and \
        minore_uguale(p.inclinazione, m.inclinazione_tavola)


# Funzione che scorre le 2 liste del database (macchine e particolari), e ,usando la funzione "compatibilità_generale",
# mi stampa su quali macchine il particolare in questione è lavorabile. In questa funzione è presente anche la verifica
# della fase del pezzo.
def macchine_compatibili(ls_macc, ls_part, fs=None):
    for p in ls_part:
        for m in ls_macc:
            if fs is None:
                if compatibilita_generale(m, p):
                    print(m.nome)
            else:
                if p.fase == fs:
                    if compatibilita_generale(m, p):
                        print(m.nome)


# Scorre la lista macchine e mi ritorna la macchina.
def get_macchina(nome_macchina):
    for m in Macchine_TFZ_Aprilia:
        if m.nome == nome_macchina:
            return m


# Come "get_macchina" con la differenza che questa funzione controlla anche la fase, in caso ci siano particolari
# presenti nel database con più fasi.
def get_particolare(codice_particolare, fs=None):
    for p in Particolari:
        if p.codice == codice_particolare:
            if fs is None:
                return p
            elif p.fase == fs:
                return p


# Stampa gli attributi della macchina o del particolare. Esempio: { 'nome': '15_24', 'diametro': (120, 300) } ecc...
def stampa_valori(v):
    print(vars(v))


# Permette di dividere in "numero" e "valore" la stampa degli attributi della macchina o del particolare.
def stampa_etichetta(indice):
    for numero, valore in indice.items():
        print(f'[{numero}] - {valore}')


# Controlla se un oggetto è in una lista e stampa gli oggetti che trova nella lista.
def stampa_lista(lista):
    for item in lista:
        print(item)


# Verifica se l'input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto.
def check_inserimento_dati(lista, tipo):
    scelta = input(f'Inserire {tipo} (utilizzare virgola per scelte multiple): ')
    while not valuta_input(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente il tipo di {tipo}: ')
    return scelta


def remove_macchina(nome_macchina):
    x = get_macchina(nome_macchina)
    if isinstance(x, Macchina):
        Macchine_TFZ_Aprilia.remove(x)
        print("Macchina eliminato con successo")
    else:
        print("Macchina non trovata")


def remove_particolare(codice_particolare, fs=None):
    x = get_particolare(codice_particolare, fs)
    if isinstance(x, Particolare):
        Particolari.remove(x)
        print("Codice eliminato con successo")
    else:
        print("Codice non trovato")


def edit(cod, tipo, fs=0):
    if tipo == "m":
        x = get_macchina(cod)
        if isinstance(x, Macchina):
            stampa_etichetta(Indice_attributi_macchina)
            scelta = input("Quale voce vuoi modificare?: ")
            valuta_input_numero(scelta)

    if tipo == "p":
        y = get_particolare(cod, fs)
        if isinstance(y, Particolare):
            stampa_etichetta(Indice_attributi_particolare)
            scelta = input("Quale voce vuoi modificare?: ")
            valuta_input_numero(scelta)


def valuta_input(scelta, lista):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return set(scelta) <= set(lista)


def valuta_input_numero(scelta):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return scelta


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


# mettere opzioni di scelta per tipo lavorazione e
# attrezzatura
def insert_database(cod, tipo, fs=None):
    lista_attrezzatura = ["palo", "pinza", "manuale"]
    lista_utensili = ["creatore", "coltello", "tazza", "gambo"]
    lista_lavorazioni = ["dentatura", "stozza", "stozza elicoidale", "stozza elicoidale bombata"]
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
                print("Inserimento completato con successo")
                m = Macchina(cod, d, att, t_u, d_max_u, lav, mod_max, h_max, int_min, inc_el_max_dx, inc_el_max_sx,
                             inc_tav)
                Macchine_TFZ_Aprilia.append(m)
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
                fs = check_inserimento_dati(lista_fasi_pezzo, "fase")
                stampa_lista(lista_lavorazioni)
                lav = check_inserimento_dati(lista_lavorazioni, "lavorazione")
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


# Funzione per il salvataggio del database
def save_db(tipo):
    print(f'   ... salvataggio database {tipo}.')
    with open(f'db_{tipo}.pickle', 'wb') as handle:
        if tipo == "macchine":
            pickle.dump(Macchine_TFZ_Aprilia, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(Particolari, handle, protocol=pickle.HIGHEST_PROTOCOL)


# Funzione per il caricamento del database
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
    Macchine_TFZ_Aprilia = []
    Particolari = []
    Indice_attributi_macchina = {1: "diametro", 2: "interasse_min", 3: "tipo_attrezzatura", 4: "tipo_utensile",
                                 5: "diametro_max_utensile", 6: "lavorazione", 7: "modulo_max", 8: "altezza_fascia_max",
                                 9: "incl_elica_max_dx", 10: "incl_elica_max_sx", 11: "inclinazione_tavola"}
    Indice_attributi_particolare = {1: "diametro", 2: "interasse", 3: "tipo_attrezzatura", 4: "tipo_utensile",
                                    5: "diametro_utensile", 6: "fase", 7: "lavorazione", 8: "modulo", 9: "fascia",
                                    10: "incl_elica_dx", 11: "incl_elica_sx", 12: "inclinazione"}
    load_db()

    codice = input("Inserire codice particolare: ")
    mini_lista = lista_particolari(codice, Particolari)
    if len(mini_lista) == 1:
        macchine_compatibili(Macchine_TFZ_Aprilia, mini_lista)
    elif len(mini_lista) > 1:
        print("Il codice presenta più fasi. Quale intendi scegliere?")
        li_fa = lista_fasi(mini_lista)
        for index in li_fa:
            print(index)
        fase = check_inserimento_dati(li_fa, "fase")
        macchine_compatibili(Macchine_TFZ_Aprilia, mini_lista, fase)
    else:
        print("Particolare non presente nel database.")
