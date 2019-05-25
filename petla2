elif wylosowana== lista[1]:
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
            print("Ile paczek obstawiasz na odpowiedź D?")
            d=int(input())
            print("Ile paczek obstawiasz na odpowiedź E?")
            e=int(input())
            print("Czy chcesz skorzystać z koła ratunkowego?")
            kolo_ratunkowe=input()
            if a!=0 and kolo_ratunkowe=="Nie"or a!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="NIE"and a!=0:
                suma_paczek=suma_paczek-b-c-d-e
                dlugosc=dlugosc-1
                print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")

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
                print("Ile paczek obstawiasz na odpowiedź D?")
                d=int(input())
                print("Ile paczek obstawiasz na odpowiedź E?")
                e=int(input())
                if a!=0:
                    suma_paczek=suma_paczek-b-c-d-e
                    dlugosc=dlugosc-1
                    lista.remove(wylosowana)
                    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")
                elif a==0:
                    print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
                    break
