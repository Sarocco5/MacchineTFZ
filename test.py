#Indice_attributi_particolare = {0: "codice", 1: "diametro", 2: "interasse", 3: "tipo_attrezzatura",
                                    #4: "tipo_utensile", 5: "diametro_utensile", 6: "fase", 7: "lavorazione",
                                    #8: "modulo", 9: "fascia", 10: "incl_elica_dx", 11: "incl_elica_sx",
                                    #12: "inclinazione"}

#x = (c)

#getattr(x, )

class Particolare:
    nome = None
    diametro = None
    interasse = None
    tipo_attrezzatura = []
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
        self.incl_elica_max_dx = p_incl_elica_dx
        self.incl_elica_max_sx = p_incl_elica_sx
        self.inclinazione = incl


def calcolo_interasse(diam_pezzo, diam_ute):
    return (diam_pezzo + diam_ute) / 2


if __name__ == '__main__':

    part1 = Particolare("752/3534368", 150, ["palo", "pinza"], "creatore", 160, "120", "dentatura", 3, 20,
                        p_incl_elica_dx=22)
    part2 = Particolare("607", 120, ["palo", "manuale"], "creatore", 160, "120", "dentatura", 1.5, 40)
    part3 = Particolare("495", 150, ["manuale"], "creatore", 160, "120", "dentatura", 4, 20, p_incl_elica_sx=14)
    part4 = Particolare("81/87553312", 75, ["pinza"], "coltello", 120, "081", "stozza_elicoidale", 3, 22)
    part5 = Particolare("81/87553312", 80, ["pinza"], "coltello", 160, "082", "stozza", 2.5, 45)
    part6 = Particolare("752/3534368", 60, ["pinza"], "coltello", 160, "080", "stozza", 4, 10, incl=8)
    Particolari = [part1, part2, part3, part4, part5, part6]


x = part1

print(x.codice[7:])
