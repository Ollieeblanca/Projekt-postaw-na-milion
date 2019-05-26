suma_pieniędzy=1000000
suma_paczek=40

if a!=0:
    suma_paczek=suma_paczek-b-c-d-e
    dlugosc=dlugosc-1
    print("A to poprawna odpowiedź! Masz teraz", a*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")
   
if b!=0:
    suma_paczek=suma_paczek-a-c-d-e
    dlugosc=dlugosc-1
    print("A to poprawna odpowiedź! Masz teraz", b*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")

if c!=0:
    suma_paczek=suma_paczek-a-b-d-e
    dlugosc=dlugosc-1
    print("A to poprawna odpowiedź! Masz teraz", c*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")
    
if d!=0:
    suma_paczek=suma_paczek-a-b-c-e
    dlugosc=dlugosc-1
    print("A to poprawna odpowiedź! Masz teraz", d*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")
 
 if e!=0:
    suma_paczek=suma_paczek-a-b-c-d
    dlugosc=dlugosc-1
    print("A to poprawna odpowiedź! Masz teraz", e*25000, "pieniędzy, czyli: ", suma_paczek, "paczek. Przechodzimy do kolejnego pytania.")
