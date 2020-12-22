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
    lavorazione = []
    fase = []
    modulo = ()
    fascia = None
    incl_elica_max_dx = None
    incl_elica_max_sx = None
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
        self.incl_elica_max_dx = p_incl_elica_dx
        self.incl_elica_max_sx = p_incl_elica_sx
        self.inclinazione = incl


# Ritorna true, se il valore del diametro è contenuto nella tupla (min, max)
def diametro_compatibile(tupla, valore):
    if tupla[0] <= valore <= tupla[1]:
        return True
    return False


# Definisco che tipo ti lavorazione è
def tipo_lavorazione(p_lav, m_lav):
    if p_lav in m_lav:
        return True
    return False


def calcolo_interasse(diam_pezzo, diam_ute):
    return (diam_pezzo + diam_ute) / 2


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def attrezzatura_compatibile(p_ta, m_ta):
    for attrezzatura in p_ta:
        if attrezzatura in m_ta:
            return True
    return False


# Scorro una lista e vedo se l'oggetto è presente nella lista.
def utensile_compatibile(p_tu, m_tu):
    if p_tu in m_tu:
        return True
    return False


def diametro_utensile(d_max_ut, d_ut):
    if d_ut >= d_max_ut:
        return True
    return False


# Modulo
def modulo_compatibile(mod_max, mod):
    if mod <= mod_max:
        return True
    return False


def fascia_compatibile(fascia, h_fascia_max):
    if fascia <= h_fascia_max:
        return True
    return False


# Il valore di un dato particolare è maggiore o uguale ad un dato macchina
def inclinazione_elica_compatibile_dx(p_incl_elica_dx, m_incl_elica_dx):
    if p_incl_elica_dx <= m_incl_elica_dx:
        return True
    return False


def inclinazione_elica_compatibile_sx(p_incl_elica_sx, m_incl_elica_sx):
    if p_incl_elica_sx <= m_incl_elica_sx:
        return True
    return False


def inclinazione_compatibile(incl, incl_tav):
    if incl <= incl_tav:
        return True
    return False


# creo una lista vuota da riempire con il codice che metto tramite l'input, che mi servirà per vedere se il codice è
# è presente nel database_particolari
def lista_particolari(input_codice, db_particolari):
    lp = []
    for particolare in db_particolari:
        if input_codice == particolare.codice:
            lp.append(particolare)
    return lp


def lista_fasi(particolari):
    lf = []
    for pa in particolari:
        lf.append(pa.fase)
    return lf


def fase_compatibile(fs_macchina, fs_pezzo):
    if fs_macchina == fs_pezzo:
        return True
    return False


def compatibilita_generale(macchina, pezzo):
    return diametro_compatibile(macchina.diametro, pezzo.diametro) and \
            utensile_compatibile(pezzo.tipo_utensile, macchina.tipo_utensile) and \
            diametro_utensile(pezzo.diametro_utensile, macchina.diametro_max_utensile) and \
            tipo_lavorazione(pezzo.lavorazione, macchina.lavorazione) and \
            modulo_compatibile(macchina.modulo_max, pezzo.modulo) and \
            fascia_compatibile(pezzo.fascia, macchina.altezza_fascia_max) and \
            attrezzatura_compatibile(pezzo.tipo_attrezzatura, macchina.tipo_attrezzatura) and \
            inclinazione_elica_compatibile_dx(pezzo.incl_elica_max_dx, macchina.incl_elica_max_dx) and \
            inclinazione_elica_compatibile_sx(pezzo.incl_elica_max_sx, macchina.incl_elica_max_sx) and \
            inclinazione_compatibile(pezzo.inclinazione, macchina.inclinazione_tavola)


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


if __name__ == '__main__':
    m1 = Macchina("15_24", (120, 300), ["palo", "pinza"], ["creatore"], 200,
                  ["dentatura"],
                  6, 100, int_min=100, m_incl_elica_dx=30, m_incl_elica_sx=30)
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
        lf = lista_fasi(mini_lista)
        print(lf)
        fase = input("Selezionare fase: ")
        while fase not in lf:
            fase = input("Fase non presente. Selezionare nuovamente la fase: ")
        macchine_compatibili(Macchine_TFZ_Aprilia, mini_lista, fase)
    else:
        print("Particolare non presente nel database.")
