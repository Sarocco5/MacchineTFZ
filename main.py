import pickle
import bisect


class Macchina:
    codice = None
    diametro_range = ()
    tipo_attrezzatura = []
    tipo_utensile = []
    diametro_max_utensile = None
    lavorazione = []
    programma_multiplo = None
    modulo_max = None
    altezza_fascia_max = None
    interasse_min = None
    incl_elica_max_dx = None
    incl_elica_max_sx = None
    inclinazione_tavola = None
    altezza_attrezzatura_max = None

    def __init__(self, c, d, m_ta, m_tu, d_max_ut, m_lav, m_prog_multi, mod_max, h_fascia_max,
                 int_min=0, m_incl_elica_dx=30, m_incl_elica_sx=30, incl_tav=10, m_alt_att_max=300):
        self.codice = c
        self.diametro_range = d
        self.tipo_attrezzatura = m_ta
        self.tipo_utensile = m_tu
        self.diametro_max_utensile = d_max_ut
        self.lavorazione = m_lav
        self.programma_multiplo = m_prog_multi
        self.modulo_max = mod_max
        self.altezza_fascia_max = h_fascia_max
        self.interasse_min = int_min
        self.inclinazione_elica_max_dx = m_incl_elica_dx
        self.inclinazione_elica_max_sx = m_incl_elica_sx
        self.inclinazione_tavola = incl_tav
        self.altezza_attrezzatura_max = m_alt_att_max

    def set_codice(self, c):
        self.codice = c

    def set_diametro(self, d):
        self.diametro_range = d

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

    def set_inclinazione_elica_max_dx(self, m_incl_elica_dx):
        self.inclinazione_elica_max_dx = m_incl_elica_dx

    def set_inclinazione_elica_max_sx(self, m_incl_elica_sx):
        self.inclinazione_elica_max_sx = m_incl_elica_sx

    def set_inclinazione_tavola(self, incl_tav):
        self.inclinazione_tavola = incl_tav

    def set_altezza_attrezzatura_max(self, m_alt_att_max):
        self.altezza_attrezzatura_max = m_alt_att_max


class Utensile:
    codice = None
    tipo = None
    diametro_utensile = None
    senso_elica = None
    inclinazione_elica = None

    def __init__(self, c, t, d, senso_el, inc_el=0.0):
        self.codice = c
        self.tipo = t
        self.diametro_utensile = d
        self.senso_elica = senso_el
        self.inclinazione_elica = float(inc_el)

    def set_codice(self, c):
        self.codice = c

    def set_tipo(self, t):
        self.tipo = t

    def set_diametro_utensile(self, d):
        self.diametro_utensile = d

    def set_senso_elica(self, senso_el):
        self.senso_elica = senso_el

    def set_inclinazione_elica(self, inc_el):
        self.inclinazione_elica = inc_el


class Particolare:
    codice = None
    diametro = None
    lista_utensili = []
    tipo_attrezzatura = {}
    fase = None
    lavorazione = []
    programma_multiplo = None
    modulo = None
    fascia = None
    incl_elica_dx = 0.0
    incl_elica_sx = 0.0
    inclinazione = 0.0

    def __init__(self, c, d, ls_ut, p_ta, p_f, p_lav, p_prog_multi, mod, fascia,
                 p_incl_elica_dx, p_incl_elica_sx, incl):
        self.codice = c
        self.diametro = d
        self.lista_utensili = ls_ut
        self.tipo_attrezzatura = p_ta
        self.fase = p_f
        self.lavorazione = p_lav
        self.programma_multiplo = p_prog_multi
        self.modulo = mod
        self.fascia = fascia
        self.incl_elica_dx = p_incl_elica_dx
        self.incl_elica_sx = p_incl_elica_sx
        self.inclinazione = incl

    def set_codice(self, c):
        self.codice = c

    def set_diametro(self, d):
        self.diametro = d

    def set_fase(self, fs):
        self.fase = fs

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


Macchine_TFZ_Aprilia = []
Utensili = []
Particolari = []

indice_attrezzatura = {1: "palo", 2: "pinza", 3: "corpo porta pinza", 4: "manuale",
                       5: "contropunta", 6: "slitta elicoidale"}

indice_utensili = {1: "creatore", 2: "coltello", 3: "tazza", 4: "gambo"}

indice_lavorazioni = {1: "dentatura", 2: "dentatura conica", 3: "stozza", 4: "interna", 5: "stozza elicoidale",
                      6: "stozza elicoidale bombata"}

lista_fasi_pezzo = ["080", "081", "082", "083", "084", "085", "120", "121", "122", "123", "124", "125", "130",
                    "131", "132", "133", "134", "135"]

Indice_attributi_macchina = {0: "codice", 1: "diametro range", 2: "interasse min", 3: "tipo attrezzatura",
                             4: "tipo utensile", 5: "diametro max utensile", 6: "lavorazione", 7: "modulo max",
                             8: "altezza fascia max", 9: "inclinazione elica max dx",
                             10: "inclinazione elica max sx", 11: "inclinazione tavola",
                             12: "altezza attrezzatura massima"}

Indice_attributi_particolare = {0: "codice", 1: "diametro", 2: "lista codici utensile", 3: "interasse",
                                4: "lista tipo attrezzatura", 5: "lista tipo utensile", 6: "diametro utensile",
                                7: "fase", 8: "lavorazione", 9: "modulo", 10: "fascia", 11: "inclinazione elica dx",
                                12: "inclinazione elica sx", 13: "inclinazione"}

Indice_attributi_utensile = {0: "codice", 1: "tipo", 2: "diametro utensile", 3: "senso elica",
                             4: "inclinazione elica"}


# Prende il tipo di lavorazione, se è stozza passa, se invece è una dentatura prende il verso dell' elica sia del pezzo
# che dell' utensile e fa i conti ritornando l' inclinazione esatta da confrontare con la macchina. Se i versi sono
# concordi esegue una differenza, mentre se sono opposti fa una somma. Il risultato è in centesimi.
def calcolo_inclinazione(u_senso_el, u_inc_el, p_lav, p_inc_el_dx, p_inc_el_sx):
    if "dentatura" in p_lav or "dentatura conica" in p_lav:
        if p_inc_el_dx > 0:
            if u_senso_el == "dx":
                inclinazione_dx = format(p_inc_el_dx - u_inc_el, ".2f")
                return inclinazione_dx
            else:
                inclinazione_dx = format((p_inc_el_dx + u_inc_el), ".2f")
                return inclinazione_dx
        elif p_inc_el_sx > 0:
            if u_senso_el == "sx":
                inclinazione_sx = format((p_inc_el_sx - u_inc_el), ".2f")
                return inclinazione_sx
            else:
                inclinazione_sx = format((p_inc_el_sx + u_inc_el), ".2f")
                return inclinazione_sx
        elif p_inc_el_dx == 0 and p_inc_el_sx == 0:
            if u_senso_el == "dx":
                inclinazione_dx = u_inc_el
                return inclinazione_dx
            elif u_senso_el == "sx":
                inclinazione_sx = u_inc_el
                return inclinazione_sx


# Calcola l' inclinazione tra pezzo e utensile e ritorna il risultato creando un dizionario con il codice utensile
# e il risultato dell 'inclinazione. Lo fa per ogni utensile nella lista utensili.
def calcolo_inclinazione_per_utensile(lista_utensili, p_lav, p_inc_el_dx, p_inc_el_sx):
    inclinazione_utensili = {}
    for u in lista_utensili:
        risultato_inclinazione = calcolo_inclinazione(u.senso_elica, u.inclinazione_elica,
                                                      p_lav, p_inc_el_dx, p_inc_el_sx)
        inclinazione_utensili[u.codice] = risultato_inclinazione
    return inclinazione_utensili


# Verifico che la lavorazione non sia una stozza e calcolo l' interasse.
def calcolo_interasse(utensile, diam_pezzo, p_lav):
    r = 0.0
    if "dentatura" in p_lav or "dentatura conica" in p_lav:
        r = (utensile.diametro_utensile + diam_pezzo) / 2
    return r


# Creo un dizionario con indice l' attrezzatura e associo l' altezza.
def calcolo_interasse_per_utensile(lista_utensili, diametro_pezzo, lavorazione):
    interasse_utensili = {}
    for u in lista_utensili:
        risultato_interasse = calcolo_interasse(u, diametro_pezzo, lavorazione)
        interasse_utensili[u.codice] = risultato_interasse
    return interasse_utensili


# Verifica se l' input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto. Ritorna una lista. Il metodo .strip() elimina gli
# spazi.
def check_inserimento_dati(lista, tipo):
    scelta = input(f'Inserire {tipo} (utilizzare virgola per scelte multiple): ').strip()
    while not valuta_input_testo(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente il tipo di {tipo}: ').strip()
    return crea_lista_da_stringa(scelta)


# Funzione che lavora con i dizionari. Crea una lista con le scelte numeriche, poi crea una lista vuota che riempe con
# le scelte se sono presenti nel dizionario. Ritorna la lista riempita con le scelte.
def check_inserimento_indice(indice, tipo):
    scelta = input(f'Inserire {tipo} (inserire il numero corrispondente ed utilizzare virgola per scelte multiple): ')
    scelte = crea_lista_da_stringa(scelta)
    lista_tipo = []
    for scelta in scelte:
        q = indice.get(int(scelta))
        if q is not None:
            lista_tipo.append(q)
    print(lista_tipo)
    return lista_tipo


# Verifica se l' input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto. Ritorna una stringa.Il metodo .strip() elimina gli
# spazi.
def check_inserimento_stringhe(lista, tipo):
    scelta = input(f'Inserire {tipo}: ').strip()
    while not valuta_input_testo(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente "{tipo}": ').strip()
    return scelta


# Funzione che confronta tutti parametri macchina e particolare e controlla se sono compatibili.
def compatibilita_generale(p, m):
    return diametro_compatibile(p.diametro, m.diametro_range) and \
        oggetto_compatibile(p.tipo_attrezzatura, m.tipo_attrezzatura) and \
        oggetto_compatibile(p.lavorazione, m.lavorazione) and \
        maggiore_uguale(p.interasse, m.interasse_min) and \
        minore_uguale(p.modulo, m.modulo_max) and \
        minore_uguale(p.fascia, m.altezza_fascia_max) and \
        minore_uguale(p.incl_elica_dx, m.incl_elica_max_dx) and \
        minore_uguale(p.incl_elica_sx, m.incl_elica_max_sx) and \
        minore_uguale(p.inclinazione, m.inclinazione_tavola) and \
        minore_uguale(p.altezza_attrezzatura, m.altezza_attrezzatura_max) and \
        verifica_programma_multiplo(p.programma_multiplo, m.programma_multiplo)


# Crea un dizionario con indice il tipo di attrezzatura e come valore la sua altezza
def crea_dizionario_attrezzatura(lista_tipo_attrezzatura, lista_lavorazioni):
    dict_alt_att = {}
    stozza_elicoidale = False
    slitta_elicoidale = False
    for r in lista_lavorazioni:
        if r == "stozza elicoidale":
            stozza_elicoidale = True
    for i in lista_tipo_attrezzatura:
        if i == "slitta elicoidale":
            slitta_elicoidale = True
        else:
            x = float(sostituzione_virgola(input(f'Inserire altezza attrezzatura ({i}): ')))
            dict_alt_att[i] = x
    if stozza_elicoidale is True:
        if slitta_elicoidale is True:
            dict_alt_att["slitta elicoidale"] = "disponibile"
        else:
            dict_alt_att["slitta elicoidale"] = "non disponibile"
    return dict_alt_att


# Prima toglie eventuali spazi e poi spezza in lista per ogni virgola.
def crea_lista_da_stringa(scelta):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return scelta


# Ritorna true, se il valore del diametro è contenuto nella tupla (min, max).
def diametro_compatibile(valore, tupla):
    return tupla[0] <= valore <= tupla[1]


# Funzione per editare macchine,particolari o utensili.
def edit(cod, tipo, fs=None):
    global indice_attrezzatura
    global indice_utensili
    global indice_lavorazioni
    global lista_fasi_pezzo
    if tipo == "m":
        m = get_macchina(cod)
        if isinstance(m, Macchina):
            stampa_etichetta(Indice_attributi_macchina)
            choice = int(input("Quale voce vuoi modificare?: "))
            # Controllo se la modifica riguarda una lista.
            if choice in [3, 4, 6]:
                edit_lista(m, choice)
            # Controllo se la modifica riguarda una tupla.
            elif choice == 1:
                minimo = input("Inserire valore minimo:")
                massimo = input("Inserire valore massimo: ")
                m.set_diametro((minimo, massimo))
            # Altrimenti la modifica è di tipo stringa o numero.
            else:
                scelta_utente = input("Inserire la modifica: ")
                # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                getattr(m, "set_" + Indice_attributi_macchina[choice].replace(" ", "_"))(scelta_utente)
            stampa_valori_macchina(m)
            print("Modifica completata con successo!")
    elif tipo == "p":
        p = get_particolare(cod, fs)
        if isinstance(p, Particolare):
            stampa_etichetta(Indice_attributi_particolare)
            scelta = int(input("Quale voce vuoi modificare?: "))
            # Controllo se la modifica riguarda un dizionario.
            if scelta in [4]:
                edit_dizionario_attrezzatura_particolare(p)
            # Controllo se la modifica riguarda una lista.
            elif scelta in [8]:
                edit_lista(p, scelta)
            # Scelta non gestibili perché relative ad utensili.
            elif scelta in [2, 3, 5, 6, 11, 12]:
                pass
            # Altrimenti la modifica è di tipo stringa o numero.
            else:
                scelta_utente = int(input("Inserire la modifica: "))
                # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                getattr(p, "set_" + Indice_attributi_macchina[scelta].replace(" ", "_"))(scelta_utente)
            stampa_valori_particolare(p)
            print("Modifica completata con successo!")
    elif tipo == "u":
        u = get_utensile(cod)
        if isinstance(u, Utensile):
            stampa_etichetta(Indice_attributi_utensile)
            scelta = int(input("Quale voce vuoi modificare?: "))
            scelta_utente = int(input("Inserire la modifica: "))
            # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
            getattr(u, "set_" + Indice_attributi_macchina[scelta].replace(" ", "_"))(scelta_utente)
            stampa_valori_utensile(u)
            print("Modifica completata con successo!")


# Modifica il dizionario "tipo attrezzatura" del particolare.
def edit_dizionario_attrezzatura_particolare(particolare):
    operazione = input("Vuoi aggiungere o rimuovere?: ")
    while operazione != "aggiungere" and operazione != "rimuovere":
        operazione = input("Scelta errata!Vuoi aggiungere o rimuovere?: ")
    if operazione == "aggiungere":
        stampa_etichetta(indice_attrezzatura)
        valore = check_inserimento_indice(indice_attrezzatura, "attrezzatura")[0]
        alt_att = float(sostituzione_virgola(input(f'Inserire altezza attrezzatura ({valore}): ')))
        particolare.tipo_attrezzatura[valore] = alt_att
    elif operazione == "rimuovere":
        dict_att = {}
        for i, k in enumerate(particolare.tipo_attrezzatura):
            dict_att[i] = k
        stampa_etichetta(dict_att)
        valore = check_inserimento_indice(dict_att, "attrezzatura")[0]
        particolare.tipo_attrezzatura.pop(valore)


# Funzione che modifica gli attributi di tipo lista per macchina e particolare.
def edit_lista(oggetto, choice):
    if isinstance(oggetto, Macchina):
        operazione = input("Vuoi aggiungere o rimuovere?: ")
        while operazione != "aggiungere" and operazione != "rimuovere":
            operazione = input("Scelta errata!Vuoi aggiungere o rimuovere?: ")
        # Scelta lista attrezzatura per la macchina.
        if choice == 3:
            if operazione == "aggiungere":
                stampa_etichetta(indice_attrezzatura)
                valore = check_inserimento_indice(indice_attrezzatura, "attrezzatura")[0]
                oggetto.tipo_attrezzatura.append(valore)
            elif operazione == "rimuovere":
                dict_att = {}
                for i, k in enumerate(oggetto.tipo_attrezzatura):
                    dict_att[i] = k
                stampa_etichetta(dict_att)
                valore = check_inserimento_indice(dict_att, "attrezzatura")[0]
                oggetto.tipo_attrezzatura.remove(valore)
        # Scelta tipo utensile per la macchina
        elif choice == 4:
            if operazione == "aggiungere":
                stampa_etichetta(indice_utensili)
                valore = check_inserimento_indice(indice_utensili, "utensile")[0]
                oggetto.tipo_utensile.append(valore)
            elif operazione == "rimuovere":
                dict_ut = {}
                for i, k in enumerate(oggetto.tipo_utensile):
                    dict_ut[i] = k
                stampa_etichetta(dict_ut)
                valore = check_inserimento_indice(dict_ut, "utensile")[0]
                oggetto.tipo_utensile.remove(valore)
        # Scelta tipo lavorazione per la macchina.
        elif choice == 6:
            if operazione == "aggiungere":
                stampa_etichetta(indice_lavorazioni)
                valore = check_inserimento_indice(indice_lavorazioni, "lavorazioni")[0]
                oggetto.lavorazione.append(valore)
            elif operazione == "rimuovere":
                dict_lav = {}
                for i, k in enumerate(oggetto.lavorazione):
                    dict_lav[i] = k
                stampa_etichetta(dict_lav)
                valore = check_inserimento_indice(dict_lav, "lavorazioni")[0]
                oggetto.lavorazione.remove(valore)
    elif isinstance(oggetto, Particolare):
        operazione = input("Vuoi aggiungere o rimuovere?: ")
        while operazione != "aggiungere" and operazione != "rimuovere":
            operazione = input("Scelta errata!Vuoi aggiungere o rimuovere?: ")
        # Scelta lista lavorazione per il particolare.
        if choice == 8:
            if operazione == "aggiungere":
                stampa_etichetta(indice_lavorazioni)
                valore = check_inserimento_indice(indice_lavorazioni, "lavorazioni")[0]
                oggetto.lavorazione.append(valore)
            elif operazione == "rimuovere":
                dict_lav = {}
                for i, k in enumerate(oggetto.lavorazione):
                    dict_lav[i] = k
                stampa_etichetta(dict_lav)
                valore = check_inserimento_indice(dict_lav, "lavorazioni")[0]
                oggetto.lavorazione.remove(valore)


# Controlla se il valore fase(int) nella macchina è uguale anche nel particolare.
def fase_compatibile(fs_macchina, fs_pezzo):
    return fs_macchina == fs_pezzo


# Scorre la lista macchine e mi ritorna la macchina.
def get_macchina(codice_macchina):
    for m in Macchine_TFZ_Aprilia:
        if m.codice == codice_macchina:
            return m


# Come "get_macchina" con la differenza che questa funzione controlla anche la fase, in caso ci siano particolari
# presenti nel database con più fasi.
def get_particolare(codice_particolare, fs):
    for p in Particolari:
        if p.codice == codice_particolare and p.fase == fs:
            return p


# Scorre la lista utensili e mi ritorna l' utensile.
def get_utensile(codice_utensile):
    for u in Utensili:
        if u.codice == codice_utensile:
            return u


# Associa l' uso del programma multiplo alla macchina o al particolare in fase di insert.
def inserimento_programma_multiplo(scelta):
    return True if scelta == "si" else False


# Funzione che inserisce una macchina, un particolare o un utensile nel database.
def insert_database(cod, tipo, fs=None):
    global indice_attrezzatura
    global indice_utensili
    global indice_lavorazioni
    global lista_fasi_pezzo
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
                stampa_etichetta(indice_attrezzatura)
                att = check_inserimento_indice(indice_attrezzatura, "attrezzatura")
                stampa_etichetta(indice_utensili)
                t_u = check_inserimento_indice(indice_utensili, "utensile")
                d_max_u = int(input("Inserire il diametro massimo dell' utensile: "))
                stampa_etichetta(indice_lavorazioni)
                lav = check_inserimento_indice(indice_lavorazioni, "lavorazione")
                p_m = input("La macchina può eseguire più lavorazioni con lo stesso ciclo?(si o no)").strip()
                while p_m != "si" and p_m != "no":
                    p_m = input("Scelta errata! Ripetere la scelta. "
                                "Il particolare ha più dentature da lavorare con lo stesso ciclo?(si,no): ").strip()
                p_m = True if p_m == "si" else False
                mod_max = int(input("Inserire modulo massimo: "))
                h_max = int(input("Inserire altezza fascia massima: "))
                int_min = int(input("Inserire interasse minimo (inserire 0 se non necessario): "))
                inc_el_max_dx = int(input("Inserire inclinazione elica dx massima (inserire 30 se non necessario): "))
                inc_el_max_sx = int(input("Inserire inclinazione elica sx massima (inserire 30 se non necessario): "))
                inc_tav = int(input("Inserire inclinazione tavola (inserire 0 se non necessario): "))
                alt_att_max = int(input("Inserire altezza attrezzatura massima(inserire 300 se non necessario): "))
                m = Macchina(cod, d, att, t_u, d_max_u, lav, p_m,  mod_max, h_max,
                             int_min, inc_el_max_dx, inc_el_max_sx, inc_tav, alt_att_max)
                stampa_valori_macchina(m)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Macchine_TFZ_Aprilia.append(m)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
        if tipo == "p":
            y = get_particolare(cod, fs)
            if isinstance(y, Particolare):
                print(f'Il particolare "{cod}" è presente nel database.')
            else:
                print(f'Inserire valori particolare "{cod}"')
                d = float(sostituzione_virgola(input("Inserire diametro pezzo: ")))
                scelta = int(input("Quanti utensili devi associare al particolare?: "))
                ls_ut = []
                for i in range(scelta):
                    u = get_utensile(input("Inserire codice utensile: "))
                    while u is None:
                        u = get_utensile(input("Codice errato.Inserire codice utensile: "))
                    ls_ut.append(u.codice)
                fs = check_inserimento_stringhe(lista_fasi_pezzo, "fase")
                stampa_etichetta(indice_lavorazioni)
                lav = check_inserimento_indice(indice_lavorazioni, "lavorazione")
                stampa_etichetta(indice_attrezzatura)
                ta = check_inserimento_indice(indice_attrezzatura, "attrezzatura")
                ta = crea_dizionario_attrezzatura(ta, lav)
                p_m = input("Il particolare ha più dentature da lavorare con lo stesso ciclo?(si,no): ").strip()
                while p_m != "si" and p_m != "no":
                    p_m = input("Scelta errata! Ripetere la scelta. "
                                "Il particolare ha più dentature da lavorare con lo stesso ciclo?(si,no): ").strip()
                p_m = True if p_m == "si" else False
                mod = float(sostituzione_virgola(input("Inserire modulo: ")))
                h = float(sostituzione_virgola(input("Inserire fascia: ")))
                inc_el_dx = 0.0
                inc_el_sx = 0.0
                inc = 0.0
                # Lavorazione è sempre una lista da 1 elemento.
                if lav[0] == "stozza" or lav[0] == "interna":
                    inc = float(sostituzione_virgola(
                        input("Inserire inclinazione pezzo (inserire gradi in centesimi): ")))
                elif lav[0] == "dentatura" or lav[0] == "dentatura conica":
                    scelta = input("Dentatura dritta o elicoidale?: ").strip()
                    while scelta != "dritta" and scelta != "elicoidale":
                        scelta = input("Scelta errata! Ripetere la scelta. Dritta o elicoidale?:").strip()
                    if scelta != "dritta":
                        elica = scelta_elica()
                        if elica[0] == "dx":
                            inc_el_dx = elica[1]
                        else:
                            inc_el_sx = elica[1]
                p = Particolare(cod, d, ls_ut, ta, fs, lav, p_m, mod, h, inc_el_dx, inc_el_sx, inc)
                stampa_valori_particolare(p)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Particolari.append(p)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
        if tipo == "u":
            z = get_utensile(cod)
            if isinstance(z, Utensile):
                print(f'Utensile "{cod}" presente nel database.')
            else:
                print(f'Inserire valori utensile "{cod}"')
                d = float(sostituzione_virgola(input("Inserire diametro: ")))
                stampa_etichetta(indice_utensili)
                t = check_inserimento_indice(indice_utensili, "utensile")
                sens_el = input("Inserisci senso elica(Inserire 'dx', 'sx' o 'dritto'): ").strip()
                inc_el = 0
                while sens_el != "dx" and sens_el != "sx" and sens_el != "dritto":
                    sens_el = input("Valore errato, inserisci nuovamente il verso: ")
                if sens_el == "dx":
                    inc_el = float(sostituzione_virgola(
                        input("Inserisci gradi inclinazione elica dx (inserire gradi in centesimi): ")))
                elif sens_el == "sx":
                    inc_el = float(sostituzione_virgola(
                        input("Inserisci gradi inclinazione elica sx (inserire gradi in centesimi): ")))
                u = Utensile(cod, t, d, sens_el, inc_el)
                stampa_valori_utensile(u)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Utensili.append(u)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
    except ValueError:
        print("Valore errato. Hai inserito un carattere invece che un numero.")
        # menu()


# Crea una lista dove mette i diametri degli utensili presenti nel particolare.
def lista_diametro_utensile(codice_utensili):
    lu = []
    for indice in codice_utensili:
        u = get_utensile(indice)
        d = u.diametro_utensile
        lu.append(d)
    return lu


# Crea una mini lista che riempe prendendo le fasi dalla lista particolari.
def lista_fasi(particolari):
    l_f = []
    for pa in particolari:
        l_f.append(pa.fase)
    return l_f


# Creo una lista vuota da riempire con il codice che metto tramite l' input, che mi servirà per vedere se il codice è
# è presente nel database_particolari. Se nella lp risultano più particolari con le cifre finali uguali, mi crea una
# lista_codici_particolari_simili e mi stampa i codici presenti nella lista per intero, così da poter scegliere quello
# giusto. Una volta scelto rimuove gli altri da lp.
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


# Funzione per il caricamento del database.
def load_db():
    global Macchine_TFZ_Aprilia
    global Particolari
    global Utensili
    try:
        with open(f'db_macchine.pickle', 'rb') as handle:
            print('Database macchine caricato')
            Macchine_TFZ_Aprilia = pickle.load(handle)
    except FileNotFoundError:
        print("...db macchine non trovato")
    try:
        with open(f'db_particolari.pickle', 'rb') as handle:
            print('Database particolari caricato')
            Particolari = pickle.load(handle)
    except FileNotFoundError:
        print("...db particolari non trovato")
    try:
        with open(f'db_utensili.pickle', 'rb') as handle:
            print('Database utensili caricato')
            Utensili = pickle.load(handle)
    except FileNotFoundError:
        print("...db utensili non trovato")


# Funzione che scorre le 2 liste del database (macchine e particolari), e ,usando la funzione "compatibilità_generale",
# mi stampa su quali macchine il particolare in questione è lavorabile. In questa funzione è presente anche la verifica
# della fase del pezzo.
def macchine_compatibili(ls_part, ls_macc, fs=None):
    for p in ls_part:
        for m in ls_macc:
            if fs is None:
                if compatibilita_generale(p, m):
                    print(m.codice)
            else:
                if p.fase == fs:
                    if compatibilita_generale(p, m):
                        print(m.codice)


# Valore (a) maggiore o uguale a (b).
def maggiore_uguale(a, b):
    if a is None or b is None:
        return True
    return a >= b


# Valore (a) minore o uguale a (b).
def minore_uguale(a, b):
    if a is None or b is None:
        return True
    return a <= b


# Confronta il contenuto di una lista (a) con un valore fisso (b).
def minore_uguale_lista(lista, b):
    minore = True
    for a in lista:
        if a > b:
            minore = False
    return minore


# Scorro 2 liste e vedo se l' attributo dell' oggetto è in entrambe le liste.
def oggetto_compatibile(ls_attributi_p, ls_attributi_m):
    for p in ls_attributi_p:
        for m in ls_attributi_m:
            if p == m:
                return True
    return False


# Scorre la lista dei particolari, controlla in quali particolari è usato l' utensile selezionato e crea una lista
# con quei particolari.
def particolari_usati_da_utensile(cod_ut):
    list_part_use_ut = []
    for p in Particolari:
        if cod_ut in p.lista_utensili:
            list_part_use_ut.append(p)
    return list_part_use_ut


# Rimuove una macchina, un particolare o un utensile dalla lista.
def remove(cod, tipo, fs=None):
    if tipo == "m":
        x = get_macchina(cod)
        if isinstance(x, Macchina):
            Macchine_TFZ_Aprilia.remove(x)
            print("Macchina eliminata con successo")
    elif tipo == "p":
        x = get_particolare(cod, fs)
        if isinstance(x, Particolare):
            Particolari.remove(x)
            print("Codice eliminato con successo")
    elif tipo == "u":
        u = get_utensile(cod)
        if isinstance(u, Utensile):
            ls_p = particolari_usati_da_utensile(u.codice)
            if len(ls_p) > 0:
                print(f'Utensile utilizzato da {len(ls_p)} {"particolare" if len(ls_p) == 1 else "particolari"}.')
                [print(f' - {i.codice}') for i in ls_p]
                scelta = input("Vuoi procedere alla rimozione?(si o no): ")
                while scelta != "si" and scelta != "no":
                    input("Scelta errata. Vuoi procedere alla rimozione?(si o no):")
                if scelta == "si":
                    ls_p.remove(u.codice)
                    Utensili.remove(u)
                    print("Utensile eliminato con successo.")
                elif scelta == "no":
                    print("Modifica annullata.")


# Funzione per il salvataggio del database.
def save_db(tipo):
    print(f'   ... salvataggio database {tipo}.')
    with open(f'db_{tipo}.pickle', 'wb') as handle:
        if tipo == "macchine":
            pickle.dump(Macchine_TFZ_Aprilia, handle, protocol=pickle.HIGHEST_PROTOCOL)
        elif tipo == "particolari":
            pickle.dump(Particolari, handle, protocol=pickle.HIGHEST_PROTOCOL)
        elif tipo == "utensili":
            pickle.dump(Utensili, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            print(f'Errore! Valore {tipo} non valido!')


# Se il particolare, in fase di inserimento, presenta una dentatura/stozza elicoidale, con questa funzione posso
# selezionare il verso dell' elica e poi inserire il valore.
def scelta_elica():
    valore_elica = None
    elica = input("Inserire senso elica (dx, sx): ")
    while elica != "dx" and elica != "sx":
        elica = input("Senso errato! Inserire nuovamente il senso dell' elica: ")
    if elica == "dx":
        valore_elica = float(sostituzione_virgola(input("Inserire elica pezzo dx "
                                                        "(inserire il valore in centesimi): ")))
    elif elica == "sx":
        valore_elica = float(sostituzione_virgola(input("Inserire elica pezzo sx "
                                                        "(inserire il valore in centesimi) : ")))
    return elica, valore_elica


# Funzione per numeri decimali, elimina la virgola e la sostituisce con il punto.
def sostituzione_virgola(scelta):
    if "," in scelta:
        scelta = scelta.replace(',', '.')
    return scelta


# Permette di dividere in "numero" e "valore" la stampa degli attributi della macchina o del particolare.
def stampa_etichetta(indice):
    for numero, valore in indice.items():
        print(f'[{numero}] - {valore}')


# Controlla se un oggetto è in una lista e stampa gli oggetti che trova nella lista.
def stampa_lista(lista):
    for item in lista:
        print("   " + item)


# Stampa il database.
def stampa_database(lista):
    db = []
    if isinstance(lista[0], Particolare):
        for indice in lista:
            # Dato che con i particolari ad una o due cifre prima dello slash dava problemi di ordinamento, con questo
            # metodo prima uso "split" e divido il codice in 2 dallo slash, aggiungo gli zeri mancati per portare tutti
            # i codici a tre cifre prima dello slash e poi, mentre la scorro, ordino la nuova lista con "bisect".
            s = indice.codice.split("/")[0]
            k = len(s)
            if k < 3:
                for i in range(3 - k):
                    indice.codice = "0" + indice.codice
            bisect.insort(db, indice.codice + " fase [" + indice.fase + "]")
    elif isinstance(lista[0], Utensile):
        for indice in lista:
            bisect.insort(db, indice.codice)
    elif isinstance(lista[0], Macchina):
        for indice in lista:
            bisect.insort(db, indice.codice)
    print(db)


# Stampa gli attributi della macchina.
def stampa_valori_macchina(m):
    try:
        print(f'Codice: \n {m.codice} \nDiametro min-max: \n{m.diametro_range} \nLista attrezzatura: ')
        for a in m.tipo_attrezzatura:
            print(f' {a}')
        print(f'Lista utensili: ')
        for u in m.tipo_utensile:
            print(f' {u}')
        print(f'Diametro utensile max: \n {m.diametro_max_utensile} \nLavorazione: ')
        for lav in m.lavorazione:
            print(f' {lav}')
        print(f'Programma multiplo: \n {"Si" if m.programma_multiplo is True else "No"} \nModulo max: \n {m.modulo_max}'
              f'\nAltezza fascia max: \n {m.altezza_fascia_max} \nInterasse min: \n {m.interasse_min} \n'
              f'Inclinazione elica dx max: \n {m.incl_elica_max_dx} \nInclinazione elica sx max: \n '
              f'{m.incl_elica_max_sx} \nInclinazione tavola: \n '
              f'{m.inclinazione_tavola} \nAltezza attrezzatura max: \n {m.altezza_attrezzatura_max} ')
    except TypeError:
        print("Codice macchina errato")


# Stampa gli attributi del particolare.
def stampa_valori_particolare(p):
    try:
        print(f'Codice: \n {p.codice} \nDiametro: \n {p.diametro} \nLista utensili: ')
        for cod_u in p.lista_utensili:
            print(f' {cod_u}')
        print(f'Lista attrezzatura: ')
        for a in p.tipo_attrezzatura:
            print(f' {a}: {p.tipo_attrezzatura.get(a)}')
        print(f'Fase: \n {p.fase} \nLavorazione: ')
        for lav in p.lavorazione:
            print(f' {lav}')
        print(f'Programma multiplo: \n {"Si" if p.programma_multiplo is True else "No" } \nModulo: \n {p.modulo} \n'
              f'Fascia: \n {p.fascia} \nInclinazione elica dx: \n '
              f'{"-----" if p.incl_elica_dx == 0.0 else p.incl_elica_dx} \n'
              f'Inclinazione elica sx: \n {"-----" if p.incl_elica_sx == 0.0 else p.incl_elica_sx} \n'
              f'Inclinazione: \n {"-----" if p.inclinazione == 0.0 else p.inclinazione}')
    except TypeError:
        print("Codice particolare errato")


# Stampa gli attributi dell' utensile.
def stampa_valori_utensile(u):
    try:
        print(f'Codice: \n {u.codice} \nTipo: \n {u.tipo} \nDiametro: \n {u.diametro_utensile} \nSenso elica: \n'
              f' {u.senso_elica} \nInclinazione elica: \n {u.inclinazione_elica}')
    except TypeError:
        print("Codice utensile errato")


# Prima toglie lo spazio dalla scelta e poi lo spezza in lista per ogni virgola,
# ritorna True se la scelta è contenuta nella lista.
def valuta_input_testo(scelta, lista):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return set(scelta) <= set(lista)


# Verifica se il particolare richiede un programma multiplo e ritorna True
def verifica_programma_multiplo(p_pm, m_pm):
    if not p_pm:
        return True
    elif m_pm:
        return True
    return False


if __name__ == '__main__':
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
