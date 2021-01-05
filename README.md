# Release-1.0
 Opis licencije:
 - Komercijalna upotreba
 - Izmjena
 - Distribucija
 - Privatna upotreba

### Release 2.0.
Podaci se nalaze na hrvatskom jeziku.
### Atributi u tablici:
 - **naziv** označava naziv glazbenog instrumenta
 - **wikipedija** označava link na wikipediju
 - **vrsta_instrumenta** označava vrste instrumenata(kordofon, aerofon, glazbala s tipkama, udaraljke, elektrofon)
 - **zemlja_podrijetla** označava zemlju izumitelja kojem se pripisuje patent instrumenta
 - **stoljeće_pojave** označava vremenski period u kojem se spominje prva pojava instrumenta
 - **glazbeni_žanrovi** označava jedan ili više žanrova u kojima se često pojavljuje taj instrument
 - **dijelovi_označavaju** od kojih se dijelova sastoji instrument te od kojeg je materijala taj dio izrađen
 - **način_sviranja** označava ukratko princim dolaska do tonova instrumentom
 - **najpoznatiji_izvođači** označava neke poznate izvođače koji sviraju na instrumentu
 - **najpoznatiji_proizvođači** označava neke poznate proizvođače koji su nekada ili još uvijek proizvode instrument

### Napravljene web stranice
- **datatable.html** Filtriranje podataka iz baze, link za skinut filtriranu tablicu u csv i json formatu
- **index.html** Opis tablice iz prve laboratorijske vježbe

##Napravljeno pomoću djanga.
Bazu podataka potrebno prilagodit za vlastita računala.
Za pokretanje servera treba instalirati virtual environment npr. venv i pokrenut naredbom "activate.bat".
Potrebo unzipat "glazbeni_instrumenti.zip"
Za pokrenut stranice koristiti naredbu "python manage.py runserver".
Linkovi:
 - http://localhost:8000/index/ za index.html
 - http://localhost:8000/ za datatable.html

Stranica datatable.html i index.html rade bez pokretanja servera, ali bez potrebnih podataka.
 
Smatram da je baza podataka dosta nepotpuna. Način sviranja se može puno bolje opisat. Najpoznatiji izvođači i proizvođači su možda krivi nazivi s obzirom koliko se ljudi nije nabrojalo. Dijelova ima puno više nego što sam nabrojao. Za neka stoljeća pojave nisam siguran u podatak koji sam pronašao na internetu.

### Release 3.0.
##Napravljeno pomoću djanga.
Dodane route za lakši pregled podataka.
 - instrumenti/ za popis svih instrumenata
 - instrument/<id>/ za pregled instrumenta s tim id-om
 - specification/<id>/ za pregled specifikacija instrumenta s tim id-om
 - child/<id>/ za pregled dijelova i od čeka su izrađeni, dodavanje, izmijenu i brisanje dijelova
 - type/<species>/ za pregled svih instrumenata iste vrste
 - doc/ ugrađena funkcionalnost koja vraća djelomičan prikaz openApi specifikacije s mogućnošću skidanja specifikacije, potrebno za nadopunit da bi bila kompletna specifikacija
 
Openapi.json opisuje detaljnije route. 


### Smatram da je implementacija baze dobra i da je treba dalje nadopunjavat što je i svrha otvorenih podataka, da ih se može nadopunit i prepravit.
## **Renato Čiž**
