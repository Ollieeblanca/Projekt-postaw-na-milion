print("Witam serdecznie w programie Postaw na milion! Jest z nami uczestnik gry. Jak masz na imię?")
imie=input()
print("Witamy Cię," ,imie,". Przypominam, że masz możliwość wyboru jednorazowego koła ratunkowego, jakim jest dodatkowe 20 sekund na odpowiedź, a na każdą odpowiedź masz 60 sekund. \nMasz do dyspozycji cały milion złotych! Podzieliliśmy go na 40 paczek po 25000 złotych. W zależności od tego ile obstawisz na poprawną odpowiedź, z taką kwotą przechodzisz do następnego etapu. Pamiętaj, że możesz zatrzymać czas pisząc stop. Czy możemy zaczynać grę?")
zaczynacczynie=input()
if zaczynacczynie=="Tak" or zaczynacczynie=="tak" or zaczynacczynie=="TAK":

else:
    print("W takim razie czy chcesz przerwać grę?")
    przerwac=input()
    if przerwac=="Nie" or przerwac=="nie" or przerwac=="NIE":
        print("Kontynuujemy grę!")
