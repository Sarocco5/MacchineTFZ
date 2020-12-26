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


# Ritorna true, se il valore del diametro è contenuto nella tupla (min, max)
def diametro_compatibile(valore, tupla):
    return tupla[0] <= valore <= tupla[1]


# Definisco che tipo ti lavorazione è
def tipo_lavorazione(p_lav, m_lav):
    return p_lav in m_lav


def calcolo_interasse(diam_pezzo, diam_ute):
    return (diam_pezzo + diam_ute) / 2


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def attrezzatura_compatibile(p_ta, m_ta):
    for attrezzatura in p_ta:
        return attrezzatura in m_ta


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def utensile_compatibile(p_tu, m_tu):
    return p_tu in m_tu


def minore_uguale(a, b):
    return a <= b


# creo una lista vuota da riempire con il codice che metto tramite l'input, che mi servirà per vedere se il codice è
# è presente nel database_particolari
def lista_particolari(input_codice, db_particolari):
    lp = []
    for particolare in db_particolari:
        if input_codice == particolare.codice:
            lp.append(particolare)
    return lp


def lista_fasi(particolari):
    l_f = []
    for pa in particolari:
        l_f.append(pa.fase)
    return l_f


def fase_compatibile(fs_macchina, fs_pezzo):
    if fs_macchina == fs_pezzo:
        return True
    return False


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


# ls_macc= lista macchine; ls_part= lista particolari; fs= fase.
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


def get_macchina(nome_macchina):
    for m in Macchine_TFZ_Aprilia:
        if m.nome == nome_macchina:
            return m


def get_particolare(codice_particolare, fs=None):
    for p in Particolari:
        if p.codice == codice_particolare:
            if fs is None:
                return p
            elif p.fase == fs:
                return p


def stampa_valori(v):
    print(vars(v))


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


# mettere opzioni di scelta per tipo lavorazione e
# attrezzatura
def insert_database(cod, tipo, fs=None):
    if tipo == "m":
        x = get_macchina(cod)
        if isinstance(x, Macchina):
            print(f'La macchina "{cod}" è presente nel database.')
        else:
            print(f'Inserire valori macchina "{cod}"')
            d_min = int(input("Inserire diametro minimo: "))
            d_max = int(input("Inserire diametro massimo: "))
            d = (d_min, d_max)
            att = input("Inserire il tipo di attrezzatura compatibile: ")
            t_u = input("Inserire il tipo di utensile: ")
            d_max_u = int(input("Inserire il diametro massimo dell'utensile: "))
            lav = input("Inserire tipo di lavorazioni: ")
            mod_max = int(input("Inserire modulo massimo: "))
            h_max = int(input("Inserire altezza massima: "))
            int_min = int(input("Inserire interasse minimo: "))
            inc_el_max_dx = int(input("Inserire inclinazione elica dx massima: "))
            inc_el_max_sx = int(input("Inserire inclinazione elica sx massima: "))
            inc_tav = int(input("Inserire inclinazione tavola: "))
            print("Inserimento completato con successo")
            m = Macchina(cod, d, att, t_u, d_max_u, lav, mod_max, h_max, int_min, inc_el_max_dx, inc_el_max_sx, inc_tav)
            Macchine_TFZ_Aprilia.append(m)
    else:
        pass
    if tipo == "p":
        y = get_particolare(cod)
        if isinstance(y, Particolare):
            print(f'Il particolare "{cod}" è presente nel database.')
        else:
            print(f'Inserire valori particolare "{cod}"')
            d = int(input("Inserire diametro pezzo: "))
            att = input("Inserire tipo attrezzatura: ")
            t_u = input("Inserire tipo utensile: ")
            d_u = int(input("Inserire diametro utensile: "))
            fs = input("Inserire fase: ")
            lav = input("Inserire tipo lavorazione: ")
            m = input("Inserire modulo: ")
            h = input("Inserire fascia: ")
            inc_el_dx = input("Inserire elica pezzo: ")
            inc_el_sx = input("Inserire elica pezzo: ")
            inc = input("Inserire inclinazione pezzo:")
            print("Inserimento completato con successo")
            p = (d, att, t_u, d_u, fs, lav, m, h, inc_el_dx, inc_el_sx, inc)
            Particolari.append(p)


if __name__ == '__main__':
    m1 = Macchina("15_24", (120, 300), ["palo", "pinza"], ["creatore"], 200,
                  ["dentatura"],
                  6, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m2 = Macchina("15_25", (100, 200), ["palo", "pinza"], ["creatore"], 200,
                  ["dentatura"],
                  4, 100, int_min=100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m3 = Macchina("15_16", (100, 200), ["palo"], ["creatore"], 200,
                  ["dentatura"],
                  4, 100, m_incl_elica_dx=13, m_incl_elica_sx=21)
    m4 = Macchina("15_17", (100, 200), ["palo"], ["creatore"], 200,
                  ["dentatura"],
                  4, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m5 = Macchina("15_15", (100, 200), ["palo"], ["creatore"], 200,
                  ["dentatura"],
                  4, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m6 = Macchina("15-52", (100, 380), ["pinza"], ["creatore"], 200,
                  ["dentatura"],
                  8, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m7 = Macchina("15-54", (100, 380), ["pinza"], ["creatore"], 200,
                  ["dentatura"],
                  8, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m8 = Macchina("15_29", (100, 320), ["pinza", "manuale"], ["creatore"], 200,
                  ["dentatura"],
                  7, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m9 = Macchina("20_52", (40, 380), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                  ["stozza", "interna", "stozza_elicoidale", "stozza_elicoidale_bombata"],
                  6, 50, incl_tav=10)
    m10 = Macchina("20_54", (40, 380), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna", "stozza_elicoidale", "stozza_elicoidale_bombata"],
                   6, 50, incl_tav=10)
    m11 = Macchina("15_18", (100, 250), ["palo", "pinza"], ["creatore"], 200,
                   ["dentatura"],
                   5, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m12 = Macchina("15_10", (100, 320), ["pinza", "manuale"], ["creatore"], 200,
                   ["dentatura"],
                   6, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m13 = Macchina("15_26", (100, 200), ["palo", "pinza"], ["creatore"], 200,
                   ["dentatura"],
                   5, 100, m_incl_elica_dx=30, m_incl_elica_sx=30)
    m14 = Macchina("20_13", (40, 200), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"],
                   5, 50, incl_tav=10)
    m15 = Macchina("20_12", (40, 200), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"],
                   5, 50)
    m16 = Macchina("20_51", (40, 200), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna", "stozza_elicoidale"],
                   5, 50, incl_tav=10)
    m17 = Macchina("20_04", (40, 200), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna", "stozza_elicoidale"],
                   5, 60, )
    m18 = Macchina("20_10", (40, 200), ["pinza"], ["coltello", "tazza", "gambo"], 200,
                   ["stozza", "interna"],
                   5, 50, incl_tav=10)
    m19 = Macchina("15_51", (40, 200), ["pinza"], ["coltello"], 150,
                   ["stozza"],
                   5, 50, incl_tav=10)
    m20 = Macchina("20_08", (40, 200), ["manuale"], ["coltello", "gambo"], 200,
                   ["stozza", "interna"],
                   5, 50)
    Macchine_TFZ_Aprilia = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]

    part1 = Particolare("368", 150, ["palo", "pinza"], "creatore", 160, "120", "dentatura", 3, 20,
                        p_incl_elica_dx=22)
    part2 = Particolare("607", 120, ["palo", "manuale"], "creatore", 160, "120", "dentatura", 1.5, 40)
    part3 = Particolare("495", 150, ["manuale"], "creatore", 160, "120", "dentatura", 4, 20, p_incl_elica_sx=14)
    part4 = Particolare("3312", 75, ["pinza"], "coltello", 120, "081", "stozza_elicoidale", 3, 22)
    part5 = Particolare("3312", 80, ["pinza"], "coltello", 160, "082", "stozza", 2.5, 45)
    part6 = Particolare("368", 60, ["pinza"], "coltello", 160, "080", "stozza", 4, 10, incl=8)
    Particolari = [part1, part2, part3, part4, part5, part6]

    codice = input("Inserire codice particolare: ")
    mini_lista = lista_particolari(codice, Particolari)
    if len(mini_lista) == 1:
        macchine_compatibili(Macchine_TFZ_Aprilia, mini_lista)
    elif len(mini_lista) > 1:
        print("Il codice presenta più fasi. Quale intendi scegliere?")
        l_f = lista_fasi(mini_lista)
        print(l_f)
        fase = input("Selezionare fase: ")
        while fase not in l_f:
            fase = input("Fase non presente. Selezionare nuovamente la fase: ")
        macchine_compatibili(Macchine_TFZ_Aprilia, mini_lista, fase)
    else:
        print("Particolare non presente nel database.")

