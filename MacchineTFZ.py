# Modulo che salva il database in file "pickle".
import pickle
# Modulo che mantiene una lista ordinata senza dover chiamare una operazione di ordinamento ogni volta che un elemento
# viene aggiunto alla lista.
import bisect
# Modulo per data e ora.
import datetime
# Modulo per la manipolazione del tempo.
import time


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
        self.incl_elica_max_dx = m_incl_elica_dx
        self.incl_elica_max_sx = m_incl_elica_sx
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
        self.incl_elica_max_dx = m_incl_elica_dx

    def set_inclinazione_elica_max_sx(self, m_incl_elica_sx):
        self.incl_elica_max_sx = m_incl_elica_sx

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
    fascia_multipla = None
    incl_elica_dx = 0.0
    incl_elica_sx = 0.0
    inclinazione = 0.0

    def __init__(self, c, d, ls_ut, p_ta, p_f, p_lav, p_prog_multi, mod, fascia, fascia_multi,
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
        self.fascia_multipla = fascia_multi
        self.incl_elica_dx = p_incl_elica_dx
        self.incl_elica_sx = p_incl_elica_sx
        self.inclinazione = incl

    def set_codice(self, c):
        self.codice = c

    def set_diametro(self, d):
        self.diametro = d

    def set_lista_utensili(self, ls_ut):
        self.lista_utensili = ls_ut

    def set_fase(self, fs):
        self.fase = fs

    def set_programma_multiplo(self, p_prog_multi):
        self.programma_multiplo = p_prog_multi

    def set_modulo(self, mod):
        self.modulo = mod

    def set_fascia(self, fascia):
        self.fascia = fascia

    def set_fascia_multipla(self, fascia_multi):
        self.fascia_multipla = fascia_multi

    def set_incl_elica_dx(self, p_incl_elica_dx):
        self.incl_elica_dx = p_incl_elica_dx

    def set_incl_elica_sx(self, p_incl_elica_sx):
        self.incl_elica_sx = p_incl_elica_sx

    def set_inclinazione(self, incl):
        self.inclinazione = incl

    def rimuovi_utensile(self, cod):
        self.lista_utensili.remove(cod)


Macchine_TFZ_Aprilia = []
Utensili = []
Particolari = []

indice_attrezzatura = {1: "palo", 2: "pinza", 3: "pinza alberi", 4: "corpo porta pinza", 5: "manuale",
                       6: "contropunta", 7: "slitta elicoidale", 8: "robot"}

indice_utensili = {1: "creatore", 2: "coltello", 3: "tazza", 4: "gambo"}

indice_lavorazioni = {0: "dentatura finita", 1: "dentatura pre sbarbata", 2: "dentatura pre rettifica",
                      3: "dentatura scanalata", 4: "dentatura conica", 5: "dentatura conica scanalata", 6: "stozza",
                      7: "interna", 8: "stozza elicoidale", 9: "stozza elicoidale bombata"}

lista_fasi_pezzo = ["080", "081", "082", "083", "084", "085", "120", "121", "122", "123", "124", "125", "130",
                    "131", "132", "133", "134", "135"]

Indice_attributi_macchina = {0: "codice", 1: "diametro range", 2: "interasse min", 3: "tipo attrezzatura",
                             4: "tipo utensile", 5: "diametro max utensile", 6: "lavorazione", 7: "modulo max",
                             8: "altezza fascia max", 9: "inclinazione elica max dx",
                             10: "inclinazione elica max sx", 11: "inclinazione tavola",
                             12: "altezza attrezzatura max", 13: "torna indietro"}

Indice_attributi_particolare = {0: "codice", 1: "diametro", 2: "lista codici utensile",
                                3: "lista tipo attrezzatura", 4: "lista tipo utensile", 5: "diametro utensile",
                                6: "fase", 7: "lavorazione", 8: "modulo", 9: "fascia", 10: "fascia multipla",
                                11: "inclinazione elica dx", 12: "inclinazione elica sx", 13: "inclinazione",
                                14: "torna indietro"}

Indice_attributi_utensile = {0: "codice", 1: "tipo", 2: "diametro utensile", 3: "senso elica",
                             4: "inclinazione elica", 5: "torna indietro"}


# Controlla l' altezza attrezzatura del pezzo con l' altezza attrezzatura supportata dalla macchina.
def attrezzatura_altezza_compatibile(p_dict_att, m_alt_att_max):
    for a in list(p_dict_att.values()):
        if minore_uguale(a, m_alt_att_max):
            return True
    return False


# Scorro il dizionario "lista tipo attrezzatura" del particolare, con il metodo .keys() prendo l' indice del
# dizionario, che in questo caso è l' attrezzatura, e con la funzione "oggetto compatibile" verifico se l' indice
# è nella lista "tipo attrezzatura" della macchina.
def attrezzatura_compatibile(p_dict_att, m_ls_att):
    return oggetto_compatibile(list(p_dict_att.keys()), m_ls_att)


# Prende il tipo di lavorazione, se è stozza passa, se invece è una dentatura prende il verso dell' elica sia del pezzo
# che dell' utensile e fa i conti ritornando l' inclinazione esatta da confrontare con la macchina. Se i versi sono
# concordi esegue una differenza, mentre se sono opposti fa una somma. Il risultato è in centesimi.
def calcolo_inclinazione(u_senso_el, u_inc_el, p_lav, p_inc_el_dx, p_inc_el_sx):
    if "dentatura" in p_lav or "dentatura conica" in p_lav:
        if p_inc_el_dx > 0:
            if u_senso_el == "dx":
                inclinazione_dx = float(format(p_inc_el_dx - u_inc_el, ".2f"))
                return inclinazione_dx
            else:
                inclinazione_dx = float(format((p_inc_el_dx + u_inc_el), ".2f"))
                return inclinazione_dx
        elif p_inc_el_sx > 0:
            if u_senso_el == "sx":
                inclinazione_sx = float(format((p_inc_el_sx - u_inc_el), ".2f"))
                return inclinazione_sx
            else:
                inclinazione_sx = float(format((p_inc_el_sx + u_inc_el), ".2f"))
                return inclinazione_sx
        elif p_inc_el_dx == 0 and p_inc_el_sx == 0:
            if u_senso_el == "dx":
                inclinazione_dx = u_inc_el
                return inclinazione_dx
            elif u_senso_el == "sx":
                inclinazione_sx = u_inc_el
                return inclinazione_sx


# Verifico che la lavorazione non sia una stozza, creo una lista di risultati di interassi calcolati e li confronto con
# la macchina.
def calcolo_interasse(p_lista_utensile, diam_pezzo, p_lav, m_int_min):
    ls_r = []
    if "dentatura" in p_lav or "dentatura conica" in p_lav:
        for cod_u in p_lista_utensile:
            x = get_utensile(cod_u).diametro_utensile
            ls_r.append((x + diam_pezzo) / 2)
        for r in ls_r:
            if r >= m_int_min:
                return True
        return False
    return True


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
    return lista_tipo


# Verifica se l' input è scritto in modo corretto, altrimenti, in caso di input errato grazie al ciclo "while", richiede
# l' inserimento dell' input finché non riceve un input riconosciuto. Ritorna una stringa.Il metodo .strip() elimina gli
# spazi.
def check_inserimento_stringhe(lista, tipo):
    scelta = input(f'Inserire {tipo}: ').strip()
    while not valuta_input_testo(scelta, lista):
        scelta = input(f'{tipo.capitalize()} non disponibile. Inserire nuovamente "{tipo}": ').strip()
    return scelta


# Funzione che gestisce le scelte con liste.
def check_scelta_menu(lista, domanda=None):
    try:
        if lista == ["si", "no"]:
            scelta = input(f'{domanda}[si/no]: ').strip().lower()
            while scelta != "si" and scelta != "no":
                scelta = input(f'Scelta errata! Ripetere scelta. {domanda}[si/no]: ').strip().lower()
            return scelta
        elif lista == ["aggiungere", "rimuovere"]:
            print("Vuoi aggiungere o rimuovere?")
            for numero, opzione in enumerate(lista):
                print(f'[{numero}] - {opzione}')
            scelta = int(input("Inserire scelta: "))
            while scelta not in range(len(lista)):
                scelta = int(input("Scelta errata! Inserire scelta: "))
            return lista[scelta]
        else:
            for i, k in enumerate(lista):
                print(f'[{i}] - {k}')
            scelta = int((input("Inserire scelta: ")))
            while scelta not in range(len(lista)):
                scelta = int(input("Scelta errata! Ripetere scelta: "))
            return lista[scelta]
    except (ValueError, AttributeError):
        print("Scelta errata o inesistente. \n")
        menu()


# Funzione che confronta tutti parametri macchina e particolare e controlla se sono compatibili.
def compatibilita_generale(p, m, debug=False):
    if not debug:
        return attrezzatura_compatibile(p.tipo_attrezzatura, m.tipo_attrezzatura) and \
            attrezzatura_altezza_compatibile(p.tipo_attrezzatura, m.altezza_attrezzatura_max) and \
            calcolo_interasse(p.lista_utensili, p.diametro, p.lavorazione, m.interasse_min) and \
            diametro_compatibile(p.diametro, m.diametro_range) and \
            diametro_utensile_compatibile(p.lista_utensili, m.diametro_max_utensile) and \
            inclinazione_compatibile(p.lista_utensili, p.lavorazione, p.incl_elica_dx, p.incl_elica_sx,
                                     m.incl_elica_max_dx, m.incl_elica_max_sx) and \
            minore_uguale(p.modulo, m.modulo_max) and \
            minore_uguale((p.fascia * p.fascia_multipla), m.altezza_fascia_max) and \
            minore_uguale(p.inclinazione, m.inclinazione_tavola) and \
            oggetto_compatibile(p.lavorazione, m.lavorazione) and \
            verifica_programma_multiplo(p.programma_multiplo, m.programma_multiplo)
    else:
        risultati_incompatibili = []
        if not attrezzatura_compatibile(p.tipo_attrezzatura, m.tipo_attrezzatura):
            risultati_incompatibili.append("Attrezzatura")
        if not attrezzatura_altezza_compatibile(p.tipo_attrezzatura, m.altezza_attrezzatura_max):
            risultati_incompatibili.append("Altezza attrezzatura")
        if not calcolo_interasse(p.lista_utensili, p.diametro, p.lavorazione, m.interasse_min):
            risultati_incompatibili.append("Interasse")
        if not diametro_compatibile(p.diametro, m.diametro_range):
            risultati_incompatibili.append("Diametro")
        if not diametro_utensile_compatibile(p.lista_utensili, m.diametro_max_utensile):
            risultati_incompatibili.append("Diametro utensile")
        if not inclinazione_compatibile(p.lista_utensili, p.lavorazione, p.incl_elica_dx, p.incl_elica_sx,
                                        m.incl_elica_max_dx, m.incl_elica_max_sx):
            risultati_incompatibili.append("Inclinazione elica")
        if not minore_uguale(p.modulo, m.modulo_max):
            risultati_incompatibili.append("Modulo")
        if not minore_uguale((p.fascia * p.fascia_multipla), m.altezza_fascia_max):
            risultati_incompatibili.append("Fascia")
        if not minore_uguale(p.inclinazione, m.inclinazione_tavola):
            risultati_incompatibili.append("Inclinazione")
        if not oggetto_compatibile(p.lavorazione, m.lavorazione):
            risultati_incompatibili.append("Lavorazione")
        if not verifica_programma_multiplo(p.programma_multiplo, m.programma_multiplo):
            risultati_incompatibili.append("Programma multiplo")
        if len(risultati_incompatibili) >= 1:
            print(f'Macchina [{m.codice}] risultato: {risultati_incompatibili}')


# Crea un dizionario con indice il tipo di attrezzatura e come valore la sua altezza.
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


# Controlla la lista utensili del particolare e verifica se i diametri sono compatibili con la macchina.
def diametro_utensile_compatibile(lista_utensile, m_diametro_max_utensile):
    for cod_u in lista_utensile:
        diametro_utensile = get_utensile(cod_u).diametro_utensile
        if minore_uguale(diametro_utensile, m_diametro_max_utensile):
            return True
    return False


# Funzione per editare macchine,particolari o utensili.
def edit(cod, tipo, fs=None):
    global indice_attrezzatura
    global indice_utensili
    global indice_lavorazioni
    global lista_fasi_pezzo
    try:
        if tipo == "macchina":
            m = get_macchina(cod)
            if isinstance(m, Macchina):
                stampa_etichetta(Indice_attributi_macchina)
                choice = int(input("Quale voce vuoi modificare?: "))
                # Controllo se la modifica riguarda una lista.
                if choice in [3, 4, 6]:
                    edit_lista(m, choice)
                # Controllo se la modifica riguarda una tupla.
                elif choice == 1:
                    print(f'Valore attuale: {m.diametro_range}')
                    minimo = int(input("Inserire valore minimo:"))
                    massimo = int(input("Inserire valore massimo: "))
                    m.set_diametro((minimo, massimo))
                # Controllo se la modifica è di tipo str.
                elif choice == 0:
                    print(f'Codice attuale: {m.codice}')
                    scelta_utente = input("Inserire la modifica: ")
                    # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                    getattr(m, "set_" + Indice_attributi_macchina[choice].replace(" ", "_"))(scelta_utente)
                # Controllo se la modifica è di tipo int.
                elif choice in [2, 5, 7, 8, 9, 10, 11, 12]:
                    if choice == 2:
                        print(f'Interasse minimo attuale: {m.interasse_min}')
                    elif choice == 5:
                        print(f'Diametro max utensile attuale: {m.diametro_max_utensile}')
                    elif choice == 7:
                        print(f'Modulo max attuale: {m.modulo_max}')
                    elif choice == 8:
                        print(f'Altezza fascia attuale: {m.altezza_fascia_max}')
                    elif choice == 9:
                        print(f'Inclinazione elica max dx attuale: {m.incl_elica_max_dx}')
                    elif choice == 10:
                        print(f'Inclinazione elica max sx attuale: {m.incl_elica_max_sx}')
                    elif choice == 11:
                        print(f'Inclinazione tavola attuale: {m.inclinazione_tavola}')
                    elif choice == 12:
                        print(f'Altezza attrezzatura max attuale: {m.altezza_attrezzatura_max}')
                    scelta_utente = int(input("Inserire la modifica: "))
                    # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                    getattr(m, "set_" + Indice_attributi_macchina[choice].replace(" ", "_"))(scelta_utente)
                elif choice == 13:
                    print(" ")
                    menu()
                else:
                    print(f'Scelta [{choice}] inesistente! Ritorno al menu. ')
                    print(" ")
                    menu()
                stampa_valori_macchina(m)
                print("Modifica completata con successo!")
            else:
                print(f'{tipo.capitalize()} [{cod}] inesistente. Verificare presenza nel database.')
                print("")
                menu()
        elif tipo == "particolare":
            p = get_particolare(cod.codice, fs)
            if isinstance(p, Particolare):
                # Stampo l' indice attributi particolare rimuovendo le voci che riguardano l' utensile. Con la funzione
                # .pop rimuovo quello che non mi serve.
                i_a_p_temp = Indice_attributi_particolare.copy()
                i_a_p_temp.pop(4)
                i_a_p_temp.pop(5)
                i_a_p_temp.pop(11)
                i_a_p_temp.pop(12)
                i_a_p_temp.pop(13)
                stampa_etichetta(i_a_p_temp)
                scelta = int(input("Quale voce vuoi modificare?: "))
                # Controllo se la modifica riguarda un dizionario.
                if scelta in [3]:
                    edit_dizionario_attrezzatura_particolare(p)
                # Controllo se la modifica riguarda una lista.
                elif scelta in [2, 7]:
                    edit_lista(p, scelta)
                # Controllo se la modifica è di tipo int.
                elif scelta in [1, 8, 9, 10]:
                    if scelta == 1:
                        print(f'Diametro attuale: {p.diametro}')
                    elif scelta == 8:
                        print(f'Modulo attuale: {p.modulo}')
                    elif scelta == 9:
                        print(f'Fascia attuale: {p.fascia}')
                    elif scelta == 10:
                        print(f'Pezzi accoppiati attualmente: {p.fascia_multipla}')
                    scelta_utente = int(input("Inserire la modifica: "))
                    # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                    getattr(p, "set_" + Indice_attributi_particolare[scelta].replace(" ", "_"))(scelta_utente)
                # Controllo se la modifica è di tipo str.
                elif scelta in [0, 6]:
                    if scelta == 0:
                        print(f'Codice attuale: {p.codice}')
                    elif scelta == 6:
                        print(f'Fase attuale: {p.fase}')
                    scelta_utente = input("Inserire la modifica: ")
                    # Questa voce prende l' attributo, che scelgo tramite input [scelta], da un dizionario.
                    getattr(p, "set_" + Indice_attributi_particolare[scelta].replace(" ", "_"))(scelta_utente)
                elif scelta == 14:
                    print(" ")
                    menu()
                else:
                    print(f'Scelta [{scelta}] inesistente! Ritorno al menu.')
                    print(" ")
                    menu()
                stampa_valori_particolare(p)
                print("Modifica completata con successo!")
            else:
                print(f'{tipo.capitalize()} [{cod.codice}] inesistente. Verificare presenza nel database.')
                print("")
                menu()
        elif tipo == "utensile":
            u = get_utensile(cod)
            if isinstance(u, Utensile):
                stampa_etichetta(Indice_attributi_utensile)
                scelta = int(input("Quale voce vuoi modificare?: "))
                if scelta == 1:
                    stampa_etichetta(indice_utensili)
                    scelta_utente = check_inserimento_indice(indice_utensili, "utensile")
                    getattr(u, "set_" + Indice_attributi_utensile[scelta].replace(" ", "_"))(scelta_utente)
                elif scelta == 3:
                    print(f'Senso elica attuale: {u.senso_elica}')
                    scelta_utente = input("Inserire senso elica(dx o sx): ")
                    getattr(u, "set_" + Indice_attributi_utensile[scelta].replace(" ", "_"))(scelta_utente)
                elif scelta in [0, 2, 4]:
                    if scelta == 0:
                        print(f'Codice attuale: {u.codice}')
                    elif scelta == 2:
                        print(f'Diametro attuale: {u.diametro_utensile}')
                    elif scelta == 4:
                        print(f'Inclinazione attuale: {u.inclinazione_elica}')
                    scelta_utente = int(input("Inserire la modifica: "))
                    getattr(u, "set_" + Indice_attributi_utensile[scelta].replace(" ", "_"))(scelta_utente)
                elif scelta == 5:
                    print(" ")
                    menu()
                else:
                    print(f'Scelta [{scelta}] inesistente! Ritorno al menu.')
                    print(" ")
                    menu()
                stampa_valori_utensile(u)
                print("Modifica completata con successo!")
            else:
                print(f'{tipo.capitalize()} [{cod}] inesistente. Verificare presenza nel database.')
                print("")
                menu()
    except (ValueError, AttributeError):
        print("Scelta errata o inesistente. \n")
        menu()


# Modifica il dizionario "tipo attrezzatura" del particolare.
def edit_dizionario_attrezzatura_particolare(particolare):
    operazione = check_scelta_menu(["aggiungere", "rimuovere"])
    if operazione == "aggiungere":
        stampa_etichetta(indice_attrezzatura)
        print(f'Attrezzatura attuale')
        for att in particolare.tipo_attrezzatura:
            print(f' -  {att}')
        valore = check_inserimento_indice(indice_attrezzatura, "attrezzatura")[0]
        alt_att = float(sostituzione_virgola(input(f'Inserire altezza attrezzatura ({valore}): ')))
        particolare.tipo_attrezzatura[valore] = alt_att
    elif operazione == "rimuovere":
        dict_att = {}
        # Con la funzione enumerate creo una lista con indice (i) e valore (k)
        for i, k in enumerate(particolare.tipo_attrezzatura):
            dict_att[i] = k
        stampa_etichetta(dict_att)
        valore = check_inserimento_indice(dict_att, "attrezzatura")[0]
        particolare.tipo_attrezzatura.pop(valore)


# Funzione che modifica gli attributi di tipo lista per macchina e particolare.
def edit_lista(oggetto, choice):
    if isinstance(oggetto, Macchina):
        operazione = check_scelta_menu(["aggiungere", "rimuovere"])
        # Scelta lista attrezzatura per la macchina.
        if choice == 3:
            if operazione == "aggiungere":
                stampa_etichetta(indice_attrezzatura)
                print(f'Attrezzatura attuale')
                for att in oggetto.tipo_attrezzatura:
                    print(f' -  {att}')
                valore = check_inserimento_indice(indice_attrezzatura, "attrezzatura")
                for i in valore:
                    oggetto.tipo_attrezzatura.append(i)
            elif operazione == "rimuovere":
                dict_att = {}
                for i, k in enumerate(oggetto.tipo_attrezzatura):
                    dict_att[i] = k
                stampa_etichetta(dict_att)
                valore = check_inserimento_indice(dict_att, "attrezzatura")
                for i in valore:
                    oggetto.tipo_attrezzatura.remove(i)
        # Scelta tipo utensile per la macchina
        elif choice == 4:
            if operazione == "aggiungere":
                stampa_etichetta(indice_utensili)
                print(f'Tipo utensili attuali')
                for ut in oggetto.tipo_utensile:
                    print(f' -  {ut}')
                valore = check_inserimento_indice(indice_utensili, "utensile")
                for i in valore:
                    oggetto.tipo_utensile.append(i)
            elif operazione == "rimuovere":
                dict_ut = {}
                for i, k in enumerate(oggetto.tipo_utensile):
                    dict_ut[i] = k
                stampa_etichetta(dict_ut)
                valore = check_inserimento_indice(dict_ut, "utensile")
                for i in valore:
                    oggetto.tipo_utensile.remove(i)
        # Scelta tipo lavorazione per la macchina.
        elif choice == 6:
            if operazione == "aggiungere":
                stampa_etichetta(indice_lavorazioni)
                print(f'Lavorazioni attuali')
                for lav in oggetto.lavorazione:
                    print(f' -  {lav}')
                valore = check_inserimento_indice(indice_lavorazioni, "lavorazioni")
                for i in valore:
                    oggetto.lavorazione.append(i)
            elif operazione == "rimuovere":
                dict_lav = {}
                for i, k in enumerate(oggetto.lavorazione):
                    dict_lav[i] = k
                stampa_etichetta(dict_lav)
                valore = check_inserimento_indice(dict_lav, "lavorazioni")
                for i in valore:
                    oggetto.lavorazione.remove(i)
    elif isinstance(oggetto, Particolare):
        operazione = check_scelta_menu(["aggiungere", "rimuovere"])
        # Scelta lista tipo utensili del particolare.
        if choice == 2:
            scelta = int(input("Quanti utensili devi associare al particolare?: "))
            ls_ut = []
            for i in range(scelta):
                u = get_utensile(input("Inserire codice utensile: "))
                count = 0
                while u is None:
                    u = get_utensile(input("Codice errato.Inserire codice utensile: "))
                    count += 1
                    if count == 3:
                        print("Codice errato. Probabile che l' utensile non sia presente nel database.")
                        quit()
                ls_ut.append(u.codice)
            oggetto.set_lista_utensili(ls_ut)
        # Scelta tipo lavorazione per il particolare.
        if choice == 7:
            if operazione == "aggiungere":
                stampa_etichetta(indice_lavorazioni)
                print(f'Lavorazioni attuali')
                for lav in oggetto.lavorazione:
                    print(f' -  {lav}')
                valore = check_inserimento_indice(indice_lavorazioni, "lavorazioni")
                for i in valore:
                    oggetto.lavorazione.append(i)
            elif operazione == "rimuovere":
                dict_lav = {}
                for i, k in enumerate(oggetto.lavorazione):
                    dict_lav[i] = k
                stampa_etichetta(dict_lav)
                valore = check_inserimento_indice(dict_lav, "lavorazioni")
                for i in valore:
                    oggetto.lavorazione.remove(i)


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


# Calcola l' inclinazione tra pezzo e utensile e ritorna il risultato creando un dizionario con il codice utensile
# e il risultato dell 'inclinazione. Lo fa per ogni utensile nella lista utensili. Dopo prende i risultati e li
# confronta con i valori della macchina ritornando True o False.
def inclinazione_compatibile(lista_utensili, p_lav, p_inc_el_dx, p_inc_el_sx, incl_elica_max_dx, incl_elica_max_sx):
    inclinazione_utensili = {}
    for cod_ut in lista_utensili:
        u = get_utensile(cod_ut)
        risultato_inclinazione = calcolo_inclinazione(u.senso_elica, u.inclinazione_elica,
                                                      p_lav, p_inc_el_dx, p_inc_el_sx)
        inclinazione_utensili[u.codice] = risultato_inclinazione
    # Qua controllo il risultato dell' inclinazione con l' inclinazione della macchina.
    valore_maggiore_inclinazione = sorted(list(inclinazione_utensili.values()))[-1]
    if valore_maggiore_inclinazione is None:
        valore_maggiore_inclinazione = 0
    if p_inc_el_dx != 0 and p_inc_el_sx == 0:
        return valore_maggiore_inclinazione <= incl_elica_max_dx
    elif p_inc_el_sx != 0 and p_inc_el_dx == 0:
        return valore_maggiore_inclinazione <= incl_elica_max_sx
    elif p_inc_el_dx == 0 and p_inc_el_sx == 0:
        for cod_ut in lista_utensili:
            u = get_utensile(cod_ut)
            if u.senso_elica == "dx" and valore_maggiore_inclinazione > incl_elica_max_dx:
                return False
            if u.senso_elica == "sx" and valore_maggiore_inclinazione > incl_elica_max_sx:
                return False
        return True


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
        if tipo == "macchina":
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
                inc_el_max_dx = int(input("Inserire inclinazione elica dx massima (inserire 30 "
                                          "(per le dentatrici) o 0 (per le stozze) se non necessario): "))
                inc_el_max_sx = int(input("Inserire inclinazione elica dx massima (inserire 30 "
                                          "(per le dentatrici) o 0 (per le stozze) se non necessario): "))
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
        if tipo == "particolare":
            y = get_particolare(cod, fs)
            if isinstance(y, Particolare):
                print(f'Il particolare "{cod}" è presente nel database.')
            else:
                print(f'Inserire valori particolare "{cod}"')
                print("-----   Dati utensile   -----")
                scelta = int(input("Quanti utensili devi associare al particolare?: "))
                ls_ut = []
                for i in range(scelta):
                    u = get_utensile(input("Inserire codice utensile: "))
                    count = 0
                    while u is None:
                        u = get_utensile(input("Codice errato.Inserire codice utensile: "))
                        count += 1
                        if count == 3:
                            print("Codice errato. Probabile che l' utensile non sia presente nel database. Inserire"
                                  " prima l' utensile e poi il particolare.")
                            quit()
                    ls_ut.append(u.codice)
                print("-----   Dati pezzo   -----")
                d = float(sostituzione_virgola(input("Inserire diametro pezzo: ")))
                mod = float(sostituzione_virgola(input("Inserire modulo: ")))
                h = float(sostituzione_virgola(input("Inserire fascia: ")))
                fascia_multi = int(input("Quanti particolari vanno lavorati insieme?: "))
                stampa_etichetta(indice_lavorazioni)
                lav = check_inserimento_indice(indice_lavorazioni, "lavorazione")
                inc_el_dx = 0.0
                inc_el_sx = 0.0
                inc = 0.0
                # Lavorazione è sempre una lista da 1 elemento.
                if lav[0] == "stozza" or lav[0] == "interna" or lav[0] == "dentatura conica":
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
                elif lav[0] == "stozza elicoidale" or lav[0] == "stozza elicoidale bombata":
                    elica = scelta_elica()
                    if elica[0] == "dx":
                        inc_el_dx = elica[1]
                    else:
                        inc_el_sx = elica[1]
                p_m = input("Il particolare ha più dentature da lavorare con lo stesso ciclo?(si,no): ").strip()
                while p_m != "si" and p_m != "no":
                    p_m = input("Scelta errata! Ripetere la scelta. "
                                "Il particolare ha più dentature da lavorare con lo stesso ciclo?(si,no): ").strip()
                p_m = True if p_m == "si" else False
                print("-----   Dati attrezzatura   -----")
                stampa_etichetta(indice_attrezzatura)
                ta = check_inserimento_indice(indice_attrezzatura, "attrezzatura")
                ta = crea_dizionario_attrezzatura(ta, lav)
                p = Particolare(cod, d, ls_ut, ta, fs, lav, p_m, mod, h, fascia_multi, inc_el_dx, inc_el_sx, inc)
                stampa_valori_particolare(p)
                scelta = input("I valori inseriti sono corretti?(si, no): ")
                if scelta == "si":
                    Particolari.append(p)
                    print("Inserimento completato con successo")
                elif scelta == "no":
                    print("Inserimento errato. Programma interrotto")
                else:
                    print("Scelta sbagliata")
        if tipo == "utensile":
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
    except (TypeError, AttributeError):
        print("Codice errato o inesistente")


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
        if input_codice == p.codice[-3:] or input_codice == p.codice[-4:] or input_codice == p.codice:
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
def macchine_compatibili(ls_part, ls_macc, fs=None, debug=False):
    lista_risultati = []
    for p in ls_part:
        for m in ls_macc:
            if fs is None:
                if compatibilita_generale(p, m, debug):
                    lista_risultati.append(m)
            else:
                if p.fase == fs:
                    if compatibilita_generale(p, m, debug):
                        lista_risultati.append(m)
        for macchina in lista_risultati:
            risultato_robot = robot_compatibile(macchina.tipo_attrezzatura, p.tipo_attrezzatura.keys())
            if risultato_robot is not None:
                print(f'   {macchina.codice} - {risultato_robot}')
            else:
                print(f'   {macchina.codice}')


# Valore (a) maggiore o uguale a (b).
def maggiore_uguale(a, b):
    if a is None or b is None:
        return True
    return a >= b


# Funzione menu.
def menu():
    lista_opzioni = ["Verifica compatibilità", "Stampa database", "Modifica database", "Uscita"]
    lista_verifica = ["Compatibilità generale",  "Confronta macchina con particolare",
                      "Verifica particolari lavorati dall' utensile", "Incompatibilità generale", "Torna indietro"]
    lista_stampa_db = ["Stampa attributi macchina", "Stampa attributi particolare", "Stampa attributi utensile",
                       "Stampa database macchine", "Stampa database particolari", "Stampa database utensili",
                       "Torna indietro"]
    lista_modifica = ["Inserimento", "Modifica", "Rimozione", "Torna indietro"]
    scelta = None
    while scelta != "Uscita":
        print("Cosa desideri fare?")
        scelta = check_scelta_menu(lista_opzioni)
        if "Verifica compatibilità" == scelta:
            scelta = check_scelta_menu(lista_verifica)
            if scelta == "Compatibilità generale":
                verifica_compatibilita()
            elif scelta == "Confronta macchina con particolare":
                verifica_se_macchina_lavora_particolare()
            elif scelta == "Verifica particolari lavorati dall' utensile":
                verifica_particolari_lavorati_da_utensile(input("Inserire codice utensile: "))
            elif scelta == "Incompatibilità generale":
                # Passando il valore debug, compatibilità generale mi ritorna i risultati falsi.
                verifica_compatibilita(True)
            elif scelta == "Torna indietro":
                menu()
        elif "Stampa database" == scelta:
            scelta = check_scelta_menu(lista_stampa_db)
            if scelta == "Stampa attributi macchina":
                scelta = input("Inserire codice macchina: ").replace("-", "_")
                m = get_macchina(scelta)
                stampa_valori_macchina(m)
            elif scelta == "Stampa attributi particolare":
                scelta_particolare = input("Inserire codice particolare ( inserire codice completo o "
                                           "ultime 3 o 4 cifre): ")
                scelta_fase_particolare = input("Inserire fase particolare: ")
                scelta_particolare = lista_particolari(scelta_particolare, Particolari)
                p = None
                for part in scelta_particolare:
                    if part.fase == scelta_fase_particolare:
                        p = part
                stampa_valori_particolare(p)
            elif scelta == "Stampa attributi utensile":
                scelta = input("Inserire codice utensile: ")
                u = get_utensile(scelta)
                stampa_valori_utensile(u)
            elif scelta == "Stampa database macchine":
                stampa_database(Macchine_TFZ_Aprilia)
            elif scelta == "Stampa database particolari":
                stampa_database(Particolari)
            elif scelta == "Stampa database utensili":
                stampa_database(Utensili)
            elif scelta == "Torna indietro":
                menu()
        elif "Modifica database" == scelta:
            scelta = check_scelta_menu(lista_modifica)
            scelta_tipo_inserimento(scelta)
        elif "Uscita" == scelta:
            scelta = check_scelta_menu(["si", "no"], "Vuoi salvare?")
            if scelta == "si":
                save_db("macchine")
                save_db("particolari")
                save_db("utensili")
            else:
                print("Database non salvati!")
            time.sleep(3)
            quit()
        print("")


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


# Aggiunge eventuali attributi alle classi.
def reinizializza_database(db):
    global Macchine_TFZ_Aprilia
    global Utensili
    global Particolari
    new_db = []
    # Impostata per modificare in int interasse_min.
    if isinstance(db[0], Macchina):
        for m in db:
            print(m.codice)
            incl_elica_max_dx = int(input("Inserire valore: "))
            new_m = Macchina(m.codice, m.diametro_range, m.tipo_attrezzatura, m.tipo_utensile, m.diametro_max_utensile,
                             m.lavorazione, m.programma_multiplo, m.modulo_max, m.altezza_fascia_max, m.interasse_min,
                             incl_elica_max_dx, m.incl_elica_max_sx, m.inclinazione_tavola,
                             m.altezza_attrezzatura_max)
            new_db.append(new_m)
        Macchine_TFZ_Aprilia = new_db
    if isinstance(db[0], Utensile):
        # Funzione non ancora implementata.
        pass
    # Impostata per aggiungere l' attributo "fascia_multipla".
    if isinstance(db[0], Particolare):
        for p in db:
            print(p.codice)
            fascia_multipla = int(input("Inserire valore: "))
            new_p = Particolare(p.codice, p.diametro, p.lista_utensili, p.tipo_attrezzatura, p.fase, p.lavorazione,
                                p.programma_multiplo, p.modulo, p.fascia, fascia_multipla, p.incl_elica_dx,
                                p.incl_elica_sx, p.inclinazione)
            new_db.append(new_p)
        Particolari = new_db


# Rimuove una macchina, un particolare o un utensile dalla lista.
def remove(cod, tipo, fs=None):
    if tipo == "macchina":
        x = get_macchina(cod)
        if isinstance(x, Macchina):
            Macchine_TFZ_Aprilia.remove(x)
            print(f'Macchina [{x.codice}] eliminata con successo')
        else:
            print(f'{tipo.capitalize()} [{cod.codice}] inesistente. Verificare presenza nel database.')
    elif tipo == "particolare":
        x = get_particolare(cod.codice, fs)
        if isinstance(x, Particolare):
            Particolari.remove(x)
            print(f'Codice [{x.codice}] eliminato con successo.')
        else:
            print(f'{tipo.capitalize()} [{cod.codice}] inesistente. Verificare presenza nel database.')
    elif tipo == "utensile":
        verifica_particolari_lavorati_da_utensile(cod)
        u = get_utensile(cod)
        scelta = check_scelta_menu(["si", "no"], "Vuoi procedere alla rimozione?")
        if scelta == "si":
            ls_p = particolari_usati_da_utensile(u.codice)
            for p in ls_p:
                p.rimuovi_utensile(cod)
                if len(p.lista_utensili) == 0:
                    print(f'{p.codice} - [{p.fase}] non ha più utensili associati.')
                scelta = input("Vuoi aggiungere un utensile?(si o no): ")
                while scelta != "si" and scelta != "no":
                    scelta = input("Scelta errata. Vuoi aggiungere un utensile?(si o no):")
                if scelta == "si":
                    edit(p.codice, "p", p.fase)
            Utensili.remove(u)
            print(f'Utensile [{u.codice}] eliminato con successo')
        elif scelta == "no":
            print("Modifica annullata.")
        else:
            print(f'{tipo.capitalize()} [{cod.codice}] inesistente. Verificare presenza nel database.')


# Verifica se il pezzo ha l' attrezzatura per essere lavorato con il robot.
def robot_compatibile(m_lista_attrezzatura, p_lista_attrezzatura):
    for m_att in m_lista_attrezzatura:
        if m_att == "robot":
            for p_att in p_lista_attrezzatura:
                if p_att == "corpo porta pinza" or "palo" or "pinza":
                    return f'Utilizzo robot disponibile'
                elif p_att != "corpo porta pinza" or "palo" or "pinza":
                    return f'Utilizzo robot non disponibile'


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


# Scelgo che tipo di operazione devo fare (inserimento, modifica, rimozione) e in base alla scelta chiamo la funzione
# appropriata.
def scelta_tipo_inserimento(scelta):
    if scelta == "Torna indietro":
        menu()
    lista_tipo = ["macchina", "utensile", "particolare"]
    if scelta == "Inserimento":
        print("Vuoi inserire una macchina, un utensile o un particolare?")
        scelta_tipo = check_scelta_menu(lista_tipo)
        scelta_fase = 0
        if scelta_tipo == "particolare":
            scelta_codice = input("Inserire codice particolare: ")
            scelta_fase = check_inserimento_stringhe(lista_fasi_pezzo, "fase")
        else:
            scelta_codice = input("Inserire codice: ").replace("-", "_")
        insert_database(scelta_codice, scelta_tipo, scelta_fase)
    elif scelta == "Modifica":
        print("Vuoi modificare una macchina, un utensile o un particolare?")
        scelta_tipo = check_scelta_menu(lista_tipo)
        if scelta_tipo == "particolare":
            scelta_codice = input("Inserire codice particolare (inserire codice completo o ultime 3 o 4 cifre): ")
            scelta_fase = input("Inserire fase: ")
            scelta_codice = lista_particolari(scelta_codice, Particolari)
            if len(scelta_codice) == 1:
                scelta_codice = scelta_codice[0]
            else:
                for part in scelta_codice:
                    if part.fase == scelta_fase:
                        scelta_codice = part
            continua = "si"
            while continua == "si":
                edit(scelta_codice, scelta_tipo, scelta_fase)
                continua = check_scelta_menu(["si", "no"], "Desideri effettuare altre modifiche?")
        else:
            scelta_codice = input("Inserire codice: ").replace("-", "_")
            continua = "si"
            while continua == "si":
                edit(scelta_codice, scelta_tipo)
                continua = check_scelta_menu(["si", "no"], "Desideri effettuare altre modifiche?")
    elif scelta == "Rimozione":
        print("Vuoi rimuovere una macchina, un utensile o un particolare?")
        scelta_tipo = check_scelta_menu(lista_tipo)
        if scelta_tipo == "particolare":
            scelta_codice = input("Inserire codice particolare (inserire codice completo o ultime  3 o 4 cifre): ")
            scelta_fase = input("Inserire fase: ")
            scelta_codice = lista_particolari(scelta_codice, Particolari)
            if len(scelta_codice) == 1:
                scelta_codice = scelta_codice[0]
            else:
                for part in scelta_codice:
                    if part.fase == scelta_fase:
                        scelta_codice = part
            remove(scelta_codice, scelta_tipo, scelta_fase)
        else:
            scelta_codice = input("Inserire codice: ").replace("-", "_")
            remove(scelta_codice, scelta_tipo)


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
    for i in db:
        print(i)


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
# Utilizzo il if one line.
        print(f'Programma multiplo: \n {"Si" if m.programma_multiplo is True else "No"} \nModulo max: \n {m.modulo_max}'
              f'\nAltezza fascia max: \n {m.altezza_fascia_max} '
              f'\nInterasse min: \n {"-----" if m.interasse_min == 0 else m.interasse_min} \n'
              f'Inclinazione elica dx max: \n {"-----" if m.incl_elica_max_dx == 0 else m.incl_elica_max_dx} '
              f'\nInclinazione elica sx max: \n {"-----" if m.incl_elica_max_sx == 0 else m.incl_elica_max_sx} '
              f'\nInclinazione tavola: \n {"-----" if m.inclinazione_tavola ==0 else m.inclinazione_tavola} '
              f'\nAltezza attrezzatura max: \n {m.altezza_attrezzatura_max} ')
    except (TypeError, AttributeError):
        print("Codice errato o inesistente")


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
              f'Fascia: \n {p.fascia} \nPezzi lavorati contemporaneamente: \n {p.fascia_multipla}'
              f' \nInclinazione elica dx: \n {"-----" if p.incl_elica_dx == 0.0 else p.incl_elica_dx} \n'
              f'Inclinazione elica sx: \n {"-----" if p.incl_elica_sx == 0.0 else p.incl_elica_sx} \n'
              f'Inclinazione conica: \n {"-----" if p.inclinazione == 0.0 else p.inclinazione}')
    except (TypeError, AttributeError):
        print("Codice errato o inesistente")


# Stampa gli attributi dell' utensile.
def stampa_valori_utensile(u):
    try:
        print(f'Codice: \n {u.codice} \nTipo: \n {u.tipo} \nDiametro: \n {u.diametro_utensile} \nSenso elica: \n'
              f' {u.senso_elica} \nInclinazione elica: \n {u.inclinazione_elica}')
    except (TypeError, AttributeError):
        print("Codice errato o inesistente")


# Prima toglie lo spazio dalla scelta e poi lo spezza in lista per ogni virgola,
# ritorna True se la scelta è contenuta nella lista.
def valuta_input_testo(scelta, lista):
    scelta = scelta.replace(' ', '')
    scelta = scelta.split(',')
    return set(scelta) <= set(lista)


# Usa macchine compatibili per verificare su quali macchine è possibile lavorare il particolare.
def verifica_compatibilita(debug=False):
    codice = input("Inserire codice particolare (inserire codice completo o ultime 3 o 4 cifre): ")
    mini_lista = lista_particolari(codice, Particolari)
    if len(mini_lista) == 1:
        macchine_compatibili(mini_lista, Macchine_TFZ_Aprilia, fs=None, debug=debug)
    elif len(mini_lista) > 1:
        print("Il codice presenta più fasi. Quale intendi scegliere?")
        li_fa = lista_fasi(mini_lista)
        for fs in li_fa:
            print("   " + fs)
        fase = check_inserimento_stringhe(li_fa, "fase")
        if fase in li_fa:
            for particolare in mini_lista:
                if particolare.fase == fase:
                    macchine_compatibili([particolare], Macchine_TFZ_Aprilia, fase, debug)
    else:
        print("Particolare non presente nel database.")


# Verifica se il particolare può essere lavorato su una determinata macchina.
def verifica_se_macchina_lavora_particolare():
    scelta_macchina = input("Inserire codice macchina: ").replace("-", "_")
    m = get_macchina(scelta_macchina)
    if isinstance(m, Macchina):
        scelta_particolare = input("Inserire codice particolare ( inserire codice completo o ultime 3 o 4 cifre): ")
        scelta_fase_particolare = input("Inserire fase particolare: ")
        scelta_particolare = lista_particolari(scelta_particolare, Particolari)
        p = get_particolare(scelta_particolare, scelta_fase_particolare)
        if isinstance(p, Particolare):
            x = compatibilita_generale(p, m)
            if x is True:
                return print(f'La {m.codice} può lavorare il particolare {p.codice}')
            else:
                print(f'La {m.codice} non può lavorare il particolare {p.codice}')


# Stampa una lista di particolari che usano l' utensile selezionato.
def verifica_particolari_lavorati_da_utensile(cod):
    u = get_utensile(cod)
    if isinstance(u, Utensile):
        ls_p = particolari_usati_da_utensile(u.codice)
        if len(ls_p) > 0:
            print(f'Utensile utilizzato da {len(ls_p)} {"particolare" if len(ls_p) == 1 else "particolari"}.')
            [print(f' - {i.codice}') for i in ls_p]
    else:
        print(f'Il codice [{cod}] non è nel db')


# Verifica se il particolare richiede un programma multiplo e ritorna True o False.
def verifica_programma_multiplo(p_pm, m_pm):
    if not p_pm:
        return True
    elif m_pm:
        return True
    return False


if __name__ == '__main__':
    utente = input("Inserire nome utente: ")
    load_db()
    data = datetime.datetime.now()
    if data.hour in range(1, 12):
        print(f'   Buongiorno {utente.capitalize()}! Oggi è {data.day}/{data.month}/{data.year} e sono le ore '
              f'{0 if data.hour < 10 else ""}{data.hour}:{0 if data.minute < 10 else ""}{data.minute}')
    elif data.hour in range(12, 16):
        print(f'   Buon pomeriggio {utente.capitalize()}! Oggi è {data.day}/{data.month}/{data.year} e sono le ore '
              f'{0 if data.hour < 10 else ""}{data.hour}:{0 if data.minute < 10 else ""}{data.minute}')
    elif data.hour in range(17, 24):
        print(f'   Buonasera {utente.capitalize()}! Oggi è {data.day}/{data.month}/{data.year} e sono le ore '
              f'{0 if data.hour < 10 else ""}{data.hour}:{0 if data.minute < 10 else ""}{data.minute}')
    menu()
