# My MenoPower — pierwsze pytania diagnostyczne
# Dzień 3 / 90-Day AI Agent Manager Roadmap

pytania_i_odpowiedzi = {
    "Uderzenia gorąca": "Mogą być spowodowane wahaniami estrogenów. Warto notować częstość i porę dnia.",
    "Problemy ze snem": "Typowe w perimenopauzie. Magnez i chłodna sypialnia często pomagają.",
    "Mgła mózgowa": "Powiązana z poziomem estrogenów i kortyzolu. Ćwiczenia aerobowe są kluczowe.",
    "Huśtawki nastroju": "Wynikają ze zmian hormonalnych. Regularne posiłki stabilizują nastrój.",
    "Spadek energii": "Częsty objaw. Warto sprawdzić tarczycę i poziom żelaza."
}

print("=== My MenoPower — Baza pytań i odpowiedzi ===\n")

for pytanie, odpowiedz in pytania_i_odpowiedzi.items():
    print(f"❓ {pytanie}")
    print(f"💡 {odpowiedz}")
    print()