elif wylosowana==lista[4]:
    print(wylosowana)
    print("Ile paczek obstawiasz na odpowiedź A?")
    a=int(input())
    print("Ile paczek obstawiasz na odpowiedź B?")
    b=int(input())
    if a!=0:
        print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy. Przechodzimy do kolejnego pytania.")
    elif a==0:
        print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
        break
