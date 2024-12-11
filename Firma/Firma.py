from PIL import Image

class Firma:
    def __init__(self, name, abteilungen):
        self.name = name
        self.abteilungen = abteilungen

    def abteilungs_count(self):
        return len(self.abteilungen)

    def abteilungsleiter_count(self):
        return len([a for a in self.abteilungen if isinstance(a.leiter, Leiter)])

    def mitarbeiter_count(self):
        return sum(len(a.mitarbeiter) + (1 if a.leiter else 0) for a in self.abteilungen)

    def mitarbeiter_strength(self):
        return max(self.abteilungen, key=lambda a: len(a.mitarbeiter) + (1 if a.leiter else 0))

    def gender_count(self, gender):
        return sum(
            len([m for m in a.mitarbeiter if m.gender == gender])
            + (1 if a.leiter and a.leiter.gender == gender else 0)
            for a in self.abteilungen
        )


class Abteilung:
    def __init__(self, name, mitarbeiter, leiter):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.leiter = leiter


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender  # True: male, False: female


class Mitarbeiter(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)


class Leiter(Mitarbeiter):
    def __init__(self, name, gender):
        super().__init__(name, gender)


# Testdaten
def main():

    # Mitarbeiter erstellen
    mitarbeiter_1 = Mitarbeiter("Max Mustermann", True)
    mitarbeiter_2 = Mitarbeiter("Lisa Müller", False)
    mitarbeiter_3 = Mitarbeiter("John Doe", True)
    mitarbeiter_4 = Mitarbeiter("Anna Schmidt", False)
    mitarbeiter_5 = Mitarbeiter("Karl Meyer", True)
    mitarbeiter_6 = Mitarbeiter("Sophia Klein", False)

    # Leiter erstellen
    leiter_1 = Leiter("Dr. Hans Leiter", True)
    leiter_2 = Leiter("Frau Petra Leitung", False)

    # Abteilungen erstellen
    abteilung_1 = Abteilung("Verwaltung", [mitarbeiter_1, mitarbeiter_2], leiter_1)
    abteilung_2 = Abteilung("Entwicklung", [mitarbeiter_3, mitarbeiter_4, mitarbeiter_5], leiter_2)
    abteilung_3 = Abteilung("Vertrieb", [mitarbeiter_6], None)

    # Firma erstellen
    firma = Firma("Seyrling GmbH", [abteilung_1, abteilung_2, abteilung_3])

    print(f"Anzahl der Abteilungen: {firma.abteilungs_count()}")
    print(f"Anzahl der Abteilungsleiter: {firma.abteilungsleiter_count()}")
    print(f"Anzahl der Mitarbeiter: {firma.mitarbeiter_count()}")
    print(f"Abteilung mit der höchsten Mitarbeiterzahl: {firma.mitarbeiter_strength().name}")
    print(f"Anzahl der männlichen Mitarbeiter: {firma.gender_count(True)}")
    print(f"Anzahl der weiblichen Mitarbeiter: {firma.gender_count(False)}")

    im = Image.open("./Grafik/Firma_UML.png")
    im.show()

if __name__ == '__main__':
    main()
