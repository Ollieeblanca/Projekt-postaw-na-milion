import random
dlugosc=len(lista)
while dlugosc>0:
        wylosowana=random.choice(lista)
        if wylosowana== lista[0]:
            print(wylosowana)
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            print("Ile paczek obstawiasz na odpowiedź F?")
            f=int(input())
            if b!=0:
                    suma_paczek=suma_paczek-a-c-d-e
                    dlugosc=dlugosc-1
                print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli: ", suma_paczek, "paczek.")
            elif b==0:
                print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                break    
