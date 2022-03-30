"""
Berechnung einer Variation ohne Wiederholung
"""

# Formel für Variation ohne Zurücklegen: n!/(n-k)!

# Funktion für die Berechnung der Fakultät, nimmt ein Argument n entgegen
def calc_factorial(n):
    # Ergebnis auf 1 setzen, da multipliziert wird nicht auf 0!
    result = 1
    # while-Schleife läuft so lange, bis n 0 ist
    while n > 0:
        # Ergebnis wird mit n multipliziert und Ergebnis zugewiesen
        result *= n
        # n um 1 reduzieren
        n -= 1
    return result

# Eingaben für die Gesamtzahl/ausgewählten Elemente zu Integer gecastet
all_elements = int(input("Bitte geben sie die Gesamtzahl aller Elemente ein: "))
selected_elements = int(input("Bitte geben sie die Anzahl der ausgewählten Elemente ein: "))

# Ausgabe des Ergebnisses in dem Funktion aufgerufen und die entsprechenden Argumente übergeben werden
# calc_factorial(all_elements) entspricht n!
# calc_factorial(all_elements - selected_elements) entspricht (n-k)!
print("Das Ergebnis beträgt: ", calc_factorial(all_elements)/calc_factorial(all_elements - selected_elements))
