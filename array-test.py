# list these 3 are all the same
test = ["j", "n", "J", "N", "ja", "Ja", 'jA', "JA"]
test = ("j", "n", "J", "N", "ja", "Ja", 'jA', "JA")
test = {"j", "n", "J", "N", "ja", "Ja", 'jA', "JA"}

# static array (tuple)
test = "j", "n", "J", "N", "ja", "Ja", 'jA', "JA"

ja = input("Voer een ja in: ")
if ja in test:
    print("Goede ja")
else:
    print("Foute ja")