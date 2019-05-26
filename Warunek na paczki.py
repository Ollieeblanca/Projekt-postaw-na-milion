@@ -0,0 +1,53 @@
	    if wylosowana== lista[0]:
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
	            print("Ile paczek obstawiasz na odpowiedź F?")
	            f=int(input())
	            if a+b+c+d+e+f<= suma_paczek:
	                print("Czy chcesz skorzystać z koła ratunkowego?")
	                kolo_ratunkowe=input()
	                if  b!=0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b!=0 or kolo_ratunkowe=="NIE" and b!=0:
	                    print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy")
	                    suma_paczek=suma_paczek-a-c-d-e-f
	                    dlugosc=dlugosc-1
	                    lista.remove(wylosowana)
	                elif b==0 and kolo_ratunkowe=="nie" or kolo_ratunkowe=="Nie"and b==0 or kolo_ratunkowe=="NIE" and b==0:
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
	                    print("Ile paczek obstawiasz na odpowiedź F?")
	                    f=int(input())
	                    if b!=0:
	                        suma_paczek=suma_paczek-a-c-d-e-f
	                        dlugosc=dlugosc-1
	                        lista.remove(wylosowana)
	                        print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy.Przechodzimy do kolejnego pytania.")
	                    elif b==0:
	                        print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
	                        break
