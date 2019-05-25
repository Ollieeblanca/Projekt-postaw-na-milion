elif wylosowana==lista[2]:
            print(wylosowana)
            print("Czas start!")
            time.sleep(60)
            print("Koniec czasu.")
            print("Ile paczek obstawiasz na odpowiedź A?")
            a=int(input())
            print("Ile paczek obstawiasz na odpowiedź B?")
            b=int(input())
            print("Ile paczek obstawiasz na odpowiedź C?")
            c=int(input())
            print("Czy chcesz skorzystać z koła ratunkowego?")
            kolo_ratunkowe=input()
            if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy. Przechodzimy do kolejnego pytania.")
                suma_paczek=suma_paczek-b-c
                dlugosc=dlugosc-1
                lista.remove(wylosowana)
            elif a==0 and kolo_ratunkowe=="Nie"or a==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a==0:
                print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                break
            else:
                print("Skorzystajmy zatem z koła ratunkowego!")
                print("Czas start!")
                time.sleep(20)
                print("Koniec czasu.")
                print("Ile paczek obstawiasz na odpowiedź A?")
                a=int(input())
                print("Ile paczek obstawiasz na odpowiedź B?")
                b=int(input())
                print("Ile paczek obstawiasz na odpowiedź C?")
                c=int(input())
                if a!=0:
                    suma_paczek=suma_paczek-b-c
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy. Przechodzimy do kolejnego pytania.")
                elif a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
