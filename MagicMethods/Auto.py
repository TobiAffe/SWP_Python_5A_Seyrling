class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __len__(self):
        return int(self.ps)

    def __add__(self, other):
        if isinstance(other, Auto):
            return Auto(self.ps + other.ps)
        raise TypeError("Addition ist nur zwischen Auto-Objekten erlaubt.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return Auto(self.ps - other.ps)
        raise TypeError("Subtraktion ist nur zwischen Auto-Objekten erlaubt.")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Auto(self.ps * other)
        raise TypeError("Multiplikation ist nur mit einer Zahl erlaubt.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return NotImplemented

    def __str__(self):
        return f"Auto mit {self.ps} PS"


# Testzeilen
if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    # len
    print(len(a1))  # Ausgabe: 50

    # Addition
    a3 = a1 + a2
    print(a3)  # Ausgabe: Auto mit 110 PS

    # Subtraktion
    a4 = a2 - a1
    print(a4)  # Ausgabe: Auto mit 10 PS

    # Multiplikation
    a5 = a1 * 2
    print(a5)  # Ausgabe: Auto mit 100 PS

    # Typüberprüfung
    try:
        a1 + 10
    except TypeError as e:
        print(e)  # Ausgabe: Addition ist nur zwischen Auto-Objekten erlaubt.

    # Vergleich
    print(a1 == a2)  # Ausgabe: False
    print(a1 < a2)  # Ausgabe: True
    print(a1 > a2)  # Ausgabe: False

    # Kombinierte Operationen
    a6 = (a1 + a2) * 2
    print(a6)  # Ausgabe: Auto mit 220 PS
