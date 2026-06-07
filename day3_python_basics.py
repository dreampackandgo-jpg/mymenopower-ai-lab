# Variables
imie = "Dora"
wiek = 47
energia = 7.5

# List
pytania_menopauzy = [
    "Czy miewasz uderzenia gorąca?",
    "Jak śpisz?",
    "Jaki masz poziom energii rano?"
]

# Dictionary
profil_klientki = {
    "imie": "Anna",
    "wiek": 52,
    "glowny_problem": "brak energii",
    "faza": "perimenopauza"
}

print(imie, "ma", wiek, "lat")
print("Pytania:", pytania_menopauzy)
print("Profil:", profil_klientki)

# Functions i loops
def powitaj_klientke(imie, problem):
    return f"Cześć {imie}! Pomogę Ci z: {problem}"

pytania = [
    "Jak śpisz?",
    "Jak oceniasz energię (1-10)?",
    "Kiedy ostatnio miałaś dobry dzień bez mgły mózgowej?",
    "O której godzinie masz spadek energii?"
]

for i, pytanie in enumerate(pytania, 1):
    print(f"Pytanie {i}: {pytanie}")

wynik = powitaj_klientke("Marta", "huśtawki nastroju")
print(wynik)
