# Degree voting Page

Aquest és un projecte per construir una pàgina web on els alumnes interessats en estudiar a la Universitat de Lleida puguin consultar la informació dels graus que s'imparteixen, així com les assignatures de les quals aquests consten i el professorat que les imparteix.
Actualment el projecte només disposa de la informació introduïda pels administradors, però en un futur es vol que siguin els actuals alumnes el que qualifiquin tant les assignatures com els professors. Aquests alumnes també podran deixar comentaris.
Actualment el sistema de login ja està en funcionament, tot i que com ja s'ha dit no estan desplegats els serveis de votació i comentaris.

## Autors
* Toni Pacheco Fernández
* Joan Palau Oncins

## Requeriments
```bash
pip3 install -r requirements.txt  
```
Django==2.1.5
django-crispy-forms==1.7.2
django-markdown-deux==1.0.5
markdown2==2.3.7
pytz==2018.9

## Creació de la base de dades
Per tal de poder comprovar el funcionament de l'aplicació es facilita un fitxer que genera automàticament la base de dades i l'omple amb prou entrades per a començar a comprovar el seu funcionament.
Per fer-ho només cal cridar la següent comanda des de l'arrel del projecte.
```bash
bash degree_voting/tools/generate_db.sh
```
La comanda crea també un superusuari per a la pàgina web amb el nom *admin* i la contrasenya *password*.

## Pàgines en funcionament
Actualment les pàgines que estan en funcionament són la *Home*, des d'on es pot navegar a les pàgines de *Degrees*, *Teachers* i *Subjects*.
Una vegada a la pàgina de *Degrees* es pot entrar en la pàgina d'un dels graus i trobar el llistat d'assignatures per cursos.
Actualment, però encara no estan desenvolupades les pàgines de cadascuna de les assignatures de cadascun dels graus, així que aquests enllaços no porten enlloc.
Cal dir també que el panell lateral del *home*, el panell *Create Account* encara no està operatiu, però es poden crear comptes d'usuari, fer login i logout des de la barra superior sense cap problema.
