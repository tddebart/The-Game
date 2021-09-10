print("Welkom bij the game je gaat hierin een geweldige avontuur beleven.")
print("")
print("Je bent in het bos en je doel is om boven op de berg van bergen te komen om het speciale zwaard van goud te verkrijgen."
      " Je hebt een houten zwaard en een hond, je bent aleen zijn naam vergeten.")
hondNaam = input("Hoe heet je hond? ")
print("Oh nu weet ik het mijn hond heet {}.".format(hondNaam))
print("Je loopt rechtdoor met {} en komt bij een splitsing.".format(hondNaam))
splitsing = input("Welke kant ga je op links of rechts? (L/R) ").lower()
print(splitsing)
goudHoeveelheid = 35
if splitsing == "l":
    print("Je denkt er even over na en hebt besloten om naar links te gaan.")
    print("Je bent alleen {} kwijt je roept voor zijn naam maar hij komt niet, je bent hem kwijt :(".format(hondNaam))
    grot = input("Je ziet een grot. Ga je erin?(Y/N) ").lower()
    trollDood = False
    if grot == "y":
        print("Je gaat in de grot en ziet iets glimmends aan het einde en gaat er naar toe")
        print("Onderweg zie je een slapende troll")
        moord = input("Vermoord je hem of laat je hem rustig slapen? (vermoorden/laten) ").lower()
        if moord == "vermoorden":
            print("Je vermoord de troll en ziet dat hij wat goud in zijn zak heeft.")
            print("+25 goud")
            goudHoeveelheid += 25
            print("Je loopt verder")
            trollDood = True
        elif moord == "laten":
            print("Je laat hem slapen en loopt verder")

        print("Je komt bij het glimmends en ziet dat het een kist vol met goud is, je opent de kist en")
        if trollDood:
            print("pakt het goud")
            print("+110 goud")
            print("Je gaat de grot uit")
            goudHoeveelheid += 110
        else:
            print("de troll valt je aan, hij heeft je te pakken in de rug en snijd je in kleine stukjes.")
            print("Je bent dood probeer het opnieuw")
            exit()
    print("Je gaat verder en ziet in de verte een dorp misschien kan ik daar een beter wapen kopen")
    dorp = input("Wil je naar het dorp toe.(Y/N) ").lower()
    if dorp == "y":
        if goudHoeveelheid < 50:
            print("Je komt bij het dorp maar hebt geen geld dus ga je maar terug naar de berg")
            print("Je gaat terug naar de berg en loopt verder op en je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt je hebt geen geld dus kan je hem ook geen geld geven hij vermoord je")
            print("Je bent dood probeer het opnieuw")
            exit()
        print("Je hebt besloten om naar het dorp te gaan. Je komt bij het dorp en er zijn twee winkels")
        winkel = input("Wil je naar de hoeden winkel links of naar de blacksmith recht (L/R) ").lower()
        hkopen = 0
        zkopen = 0
        if winkel == "l":
            print("Je loopt de hoeden winkel in.")
            hkopen = int(input("Wat wil je kopen 1. een hoge hoed, 2. een coole pet, 3. een lief hondje die in de hoek ligt (1/2/3) "))
            if hkopen == 1:
                print("Je koopt de hoge hoed")
                print("er valt hier niet veel meer te doen dus ga je maar terug naar de berg")
                print("Je komt bij de berg maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt je gooit je hoge hoed en die schiet ineens een lazer naar de poema die snijd hem door midden, je hebt hem vermoord.")
            elif hkopen == 2:
                print("Je koopt de coole pet")
                print("er valt hier niet veel meer te doen dus ga je maar terug naar de berg")
                print("Je komt bij de berg maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt je gooit je coole pet maar die doet niks.")
                print("Je bent dood probeer het opnieuw")
                exit()
            elif hkopen == 3:
                print("Je koopt het lief hondje")
                hondNaam = input("Hoe noem je je nieuwe hond? ")
                print("er valt hier niet veel meer te doen dus ga je maar terug naar de berg")
                print("Je komt bij de berg maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt, je hond springt in en bijt het hoofd van de poema af, je hebt hem vermoord.")

        elif winkel == "r":
            print("Je loopt de blacksmith in.")
            zkopen = int(input("Wat wil je kopen 1. een ijzeren zwaard, 2. het zwaard van duizend leugens (1/2) "))
            if zkopen == 1:
                print("Je koopt het ijzeren zwaard")
                print("er valt hier niet veel meer te doen dus ga je maar terug naar de berg")
                print("Je komt bij de berg maar je komt een witte poema tegen, je slaat hem met je ijzeren zwaard en snijd hem recht door midden, je hebt hem vermoord.")
            elif zkopen == 2:
                print("Je koopt het zwaard van duizend leugens")
                print("het zwaard vertelt je dat er achter de winkel goud ligt je gaat kijken en het zwaard duwt je in een eindeloze put")
                print("Je bent dood probeer het opnieuw")
                exit()

        print("Je hebt de poema vermoord en loopt verder de berg op.")
        knop = input("Je ziet een vreemde knop in de muur druk je hem in? (Y/N) ").lower()
        if knop == "y":
            if hkopen == 1:
                print("Je drukt de knop maar die laat een gigantische steen vallen recht boven jou maar je sneed hem doormidden met je hoge hoed lazer")
            elif hkopen == 3:
                print("Je drukt de knop maar die laat een gigantische steen vallen recht boven jou maar {} je hond is zo sterk dat hij hem tegen hield en jou beschermd.".format(hondNaam))
            else:
                print("Je drukt de knop maar die laat een gigantische steen vallen recht boven jou je hebt niks om je te beschermen daartegen dus valt die op je")
                print("Je bent dood probeer het opnieuw")
                exit()

        print("Je loopt verder")
        print("Je komt bij de top van de berg en vindt het speciale gouden zwaard je pakt hem op en nu is het van jou, GEWONNEN")
        exit()

    if dorp == "n":
        print("Je hebt besloten om niet naar het dorp te gaan dus ga je terug naar de berg")
        if goudHoeveelheid < 50:
            print("Je loopt de berg op maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt, je hebt geen geld dus kan je hem niet overkopen, hij vermoord je.")
            print("Je bent dood probeer het opnieuw")
            exit()
        print("Je loopt de berg op maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt, je gooit 50 goud naar hem toe en hij accepteert het en gaat weg, je kan verder gaan")
        print("-50 goud")
        goudHoeveelheid -= 50
        print("Je hebt de poema vermoord en loopt verder de berg op.")
        knop = input("Je ziet een vreemde knop in de muur druk je hem in? (Y/N) ").lower()
        if knop == "y":
            print("Je drukt de knop maar die laat een gigantische steen vallen recht boven jou je hebt niks om je te beschermen daartegen dus valt die op je")
            print("Je bent dood probeer het opnieuw")
            exit()

elif splitsing == "r":
    print("Je denkt er even over na en hebt snel besloten om naar rechts te gaan omdat rechts heeft altijd recht.")
    print("Je loopt de berg op maar je komt een witte poema tegen, je slaat hem met je houten zwaard maar die breekt, je hebt geen geld dus kan je hem niet overkopen, hij vermoord je.")
    print("Je bent dood probeer het opnieuw")
    exit()
