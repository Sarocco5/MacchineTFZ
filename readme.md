# MacchineTFZ

qui scrivi la descrizione del programma

## Descrizione classi

### Macchina
**Attributo** | **Tipo** | **Descrizione**
--- | --- | ---
codice | str | codice identificativo della macchina
diametro | float | diametro della macchina
tipo attrezzatura | lista str | lista delle attrezzature supportate dalla macchina
lista utensili | lista str | lista degli utensili supportati dalla macchina
diametro max utensile | float | diametro massimo che può avere l'utensile per essere montato sulla macchina
lavorazione | lista str | lista delle lavorazioni eseguite dalla macchina
programma multiplo | boolean | indica se la macchina ha la possibilità di eseguire più programmi con lo stesso ciclo
modulo max | float | modulo massimo supportato dalla macchina
altezza fascia max | float | fascia massima che può lavorare la macchina
interasse min | float | interasse minimo supportato dalla macchina
inclinazione max dx | float | inclinazione massima supportata dalla macchina
inclinazione max sx | float | inclinazione massima supportata dalla macchina
inclinazione tavola | float | inclinazione massima supportata dalla macchina
altezza attrezzatura max | float |

### Utensile
**Attributo** | **Tipo** | **Descrizione**
--- | --- | ---
codice | str | codice identificativo dell'utensile
tipo | str | tipo di utensile
diametro utensile | float | diametro dell'utensile
senso elica | str | senso elica dell'utensile
inclinazione elica | float | inclinazione dell'utensile

### Particolare
**Attributo** | **Tipo** | **Descrizione**
--- | --- | ---
codice | str | codice identificativo del particolare
diametro |float | diametro del particolare
lista utensili | lista di str | lista di utensili usati dal particolare
tipo attrezzatura | dict{lista attrezzature : altezza attrezzature} | lista di attrezzatura usate dal particolare e la loro altezza
fase | str | codice identificativo della fase
lavorazione | lista di str | tipo di lavorazione del particolare
programma multiplo | boolean | indica se nel particolare ci sono più lavorazioni da fare con lo stesso ciclo
modulo | float | modulo del particolare
fascia | float | aletezza fascia del particolare
fascia multipla | float | indica quanti particolari vengono lavorati contemporaneamente
inclinazione dx | float | inclinazione elica destra del particolare
inclinazione sx | float | inclinazione elica sinistra del particolare
inclinazione | float | inclinazione del particolare
