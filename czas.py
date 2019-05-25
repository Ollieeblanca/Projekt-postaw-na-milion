import time

print("Czas start!")
for k in range(1,61):
    print(k)
    time.sleep(1)
    if k == 30:
        print("Minęła połowa czasu")

###
#koło ratunkowe z czasem:
###
koloR=["kolo_R"]
if koloR!=[]:
    print("Skorzystajmy zatem z koła ratunkowego!")
    print("Czas start!")
    for k in range(1,21):
        print(k)
        time.sleep(1)
        if k == 10:
        print("Minęła połowa czasu")
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
          koloR.remove(koloR[0])
          print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
       elif b==0:
           print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
           break
else:
    print("Wykorzystałeś już koło ratunkowe")
    print("Obstawiłeś: A:", a, "B:", b,"C:", c, "D:", d,"E:", e, "F:",f)
    if b!=0:
        print("B to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli ", suma_paczek, "paczek." "Przechodzimy do kolejnego pytania.")
    elif b==0:
        print("Przykro mi, to zła odpowiedź. Niestety, nie udało Ci się wygrać ani złotówki!")
