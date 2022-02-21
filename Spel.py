# Text baserat python spel
# importera alla nödvändiga filer
import sys
import time
import os
import random
import winsound

# Sleep funktion
def wait():
    time.sleep(2)

# Fråga om användaren vill starta programmet
start = input("Starta spel?: ")
if start == "ja":
    os.system('cls')
else:
    print("Avlustar Program.")
    time.sleep(2)
    exit()

winsound.PlaySound("Win.wav", winsound.SND_ASYNC)

# Spel Intro
words = """
Skapat av --

───░█ ───░█ ░█─░█ 
─▄─░█ ─▄─░█ ░█▀▀█ 
░█▄▄█ ░█▄▄█ ░█─░█
"""
# Skrolla igenom alla karaktärer i JJH
for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()


# Spel banner
os.system('cls')
filenames = ["1.txt", "2.txt"]
frames = []
# Öppna två filer och läs in innehållet använd sedan cls
for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(5):
    for frame in frames:
        print("".join(frame))
        time.sleep(0.8)
        os.system('cls')


# De olika karaktärerna i spelet
# krigare
class krigare (object):
    health = 10
    strength = 20
    defence = 10
    magic = 5

# magiker

class magiker (object):
    health = 50
    strength = 10
    defence = 15
    magic = 40

# tank

class tank (object):
    health = 200
    strength = 15
    defence = 30
    magic = 5


# fiende karaktärer
class goblin (object):
    name = "Goblin"
    health = 20
    strength = 10
    defence = 15
    loot = random.randint(0, 2)

# häxa

class witch (object):
    name = "Häxa"
    health = 50
    strength = 15
    defence = 15
    loot = random.randint(0, 2)

# troll

class troll (object):
    name = "Troll"
    health = 100
    strength = 20
    defence = 20
    loot = random.randint(0, 2)


# När spelarens liv når noll och spelet tar slut
def gameOver(character, score):
    if character.health < 1:
        os.system('cls')
        winsound.PlaySound("Curb.wav", winsound.SND_ASYNC)
        print("Du har ingen hälsa kvar!")
        time.sleep(3)
        print("\n")
        print("Spelet är nu över...")
        time.sleep(3)
        print("//////////////////////////////////////////")
        print("/ Skapat av Joacim, Johan och Hugo TE18A /")
        print("//////////////////////////////////////////")
        time.sleep(3)
        print("Tack för att du spelat!")
        time.sleep(3)
        print("\n")
        print("Ditt poäng blev: ", score)
        time.sleep(3) 
        print("\n")
        name = input("Vad heter du? ")
        writeScore(score, name)
        # Skriver namn och poäng till en text-fil
        print("\n")
        time.sleep(1)
        print("Adjö!", name)
        time.sleep(2)
        exit()


# Skriv data till en text fil
def writeScore(score, name):
    file = open("score.txt", "a")
    file.write("Namn: ")
    file.write(str(name))
    file.write(",")
    file.write("Poäng: ")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


# Välj en klass av hjälte
def heroselect():
    print("Välj din hjälte")
    print("---------------")
    selection = input("1. Krigare \n2. Magiker \n3. Tank \n ")
    if selection == "1":
        character = krigare
        print("Du har valt krigaren! \n ")
        wait()
        print("Hälsa - ", character.health)
        print("Styrka - ", character.strength)
        print("Försvar - ", character.defence)
        print("Magi - ", character.magic)
        # Se till att spelaren är säker på sitt val
        confirm = input("Är du säker?: ")
        if confirm == "nej":
            print("\n")
            heroselect()
        else:
            print("\n")
        return character

    elif selection == "2":
        character = magiker
        print("Du har valt magikern!\n ")
        wait()
        print("Hälsa - ", character.health)
        print("Styrka - ", character.strength)
        print("Försvar - ", character.defence)
        print("Magi - ", character.magic)
        # Se till att spelaren är säker på sitt val
        confirm = input("Är du säker?: ")
        if confirm == "nej":
            print("\n")
            heroselect()
        else:
            print("\n")
        return character

    elif selection == "3":
        character = tank
        print("Du har valt Tank!\n ")
        wait()
        print("Häsla - ", character.health)
        print("Styrka - ", character.strength)
        print("Försvar - ", character.defence)
        print("Magi - ", character.magic)
        # Se till att spelaren är säker på sitt val
        confirm = input("Är du säker?: ")
        if confirm == "nej":
            print("\n")
            heroselect()
        else:
            print("\n")
        return character

    else:
        print("Inte ett giltigt alternativ, välj ett av alternativen som finns!\n ")
        heroselect()

# välj fiende


def enemyselect(goblin, witch, troll):
    enemyList = [goblin, witch, troll]
    chance = random.randint(0, 2)
    enemy = enemyList[chance]
    return enemy

# när fienden tappar något

def loot():
    loot = ["dryck", "svärd", "sköld"]
    lootChance = random.randint(0, 2)
    lootDrop = loot[lootChance]
    return lootDrop

# Ger spelaren extra effekt om något hittas.


def lootEffect(lootDrop, character):
    if lootDrop == "dryck":
        character.health = character.health + 20
        print("Du sveper den magiska drycken, vilket ökar din hälsa med 20")
        print("Din hälsa är nu", character.health)
        return character

    elif lootDrop == "svärd":
        character.strength = character.strength + 5
        print("Du bytter ditt svärd mot ett nyare och vasare svärd")
        print("Din styrka har ökat med 5")
        print("Din nya styrka är nu", character.strength)
        return character

    elif lootDrop == "sköld":
        character.defence = character.defence + 5
        print("Du bytter din sköld mot en starkare sköld")
        print("Ditt försvar har ökat med 5")
        print("Ditt nya försvar är", character.defence)
        return character


# När man slåss
def battlestate(score):
    enemy = enemyselect(goblin, witch, troll)
    print("En fientlig", enemy.name, "har närmat sig!")
    print("Du har 3 val...\n ")
    while enemy.health > 0:
        choice = input("1. Svärd\n2. Magi\n3. Spring!\n ")

        if choice == "1":
            print("Du svingar ditt svärd och attackerar", enemy.name)
            hitchance = random.randint(1, 10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                print("Du träffar fienden!, deras hälsa är nu: ", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - \
                        (enemy.strength / character.defence)
                    print(
                        enemy.name, "attackerar dig, din nya hälsa är: ", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30
                        score = score + 5

                    elif enemy.name == "Häxa":
                        enemy.health = 50
                        score = score + 10

                    elif enemy.name == "Troll":
                        enemy.health = 100
                        score = score + 15

                    print("Du har besgrat", enemy.name)
                    print("Ser ut som att den tappade något")
                    lootDrop = loot()
                    print("Du fick en: ", lootDrop)
                    lootEffect(lootDrop, character)
                    print("poäng:")
                    return score

            else:
                print(
                    "Du tappar grepet på ditt svärd vilket glider ur dina händer och missar")
                print(enemy.name, "träffar dig för full skada")
                character.health = character.health - enemy.strength
                print("Din hälsa är nu: ", character.health)
                gameOver(character, score)

        elif choice == "2":
            print("Du kastar en formel och attackerar", enemy.name)
            hitchance = random.randint(1, 10)
            if hitchance > 2:
                enemy.health = enemy.health - character.magic
                print("Du träffar fienden!, deras hälsa är nu: ", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - \
                        (enemy.strength / character.defence)
                    print(
                        enemy.name, "attackerar dig, din nya hälsa är: ", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 30
                        score = score + 5

                    elif enemy.name == "Häxa":
                        enemy.health = 50
                        score = score + 10

                    elif enemy.name == "Troll":
                        enemy.health = 100
                        score = score + 15

                    print("Du har besgrat", enemy.name)
                    print("Ser ut som att den tappade något")
                    lootDrop = loot()
                    print("Du fick en", lootDrop)
                    lootEffect(lootDrop, character)
                    print("poäng:")
                    return score
            else:
                print("Du snubblar när du kastar formeln och missar")
                print(enemy.name, "träffar dig för full skada")
                character.health = character.health - enemy.strength
                print("Din hälsa är nu", character.health)
                gameOver(character, score)

        elif choice == "3":
            print("Du försöker springa...")
            runchance = random.randint(1, 10)
            if runchance > 2:
                print("Du lyckas komma undan fienden!")
                break
            else:
                print("Du försöker springa men snubblar på en rot!")
                print("Medans du är nere slår fienden dig för full skada")
                character.health = character.health - enemy.strength
                print("Din hälsa är nu", character.health)
                gameOver(character, score)

        else:
            print("Inte ett giltigt alternativ, försök igen")


# Det som körs i programmet
score = 0
#Spela musik fån en wav fil
winsound.PlaySound("Main.wav", winsound.SND_ASYNC)
character = heroselect()
os.system('cls')
# Från den här delen till den första cls är en runda i spelet
# Runda 1
score = battlestate(score)
print(score)
time.sleep(3)
os.system('cls')
# Runda 2
score = battlestate(score)
print(score)
time.sleep(3)
os.system('cls')
# Runda 3
score = battlestate(score)
print(score)
time.sleep(3)
os.system('cls')
# Runda 4
score = battlestate(score)
print(score)
time.sleep(3)
os.system('cls')
# Runda 5
score = battlestate(score)
print(score)
time.sleep(3)
os.system('cls')

# När spelaren klarat alla rundor som finns klarar den spelet med ett visst poäng
winsound.PlaySound("Win.wav", winsound.SND_ASYNC)
print("Du klarade dig!")
time.sleep(3)
print("\n")
print("Spelet är nu över!")
time.sleep(3)
print("//////////////////////////////////////////")
print("/ Skapat av Joacim, Johan och Hugo TE18A /")
print("//////////////////////////////////////////")
time.sleep(3)
print("\n")
print("Tack för att du spelat!")
time.sleep(3)
print("\n")
print("Ditt poäng blev: ", score)
time.sleep(3)
print("\n")
name = input("Vad heter du? ")
writeScore(score, name)
# Skriver namn och poäng till en text-fil
print("\n")
time.sleep(1)
print("Hejdå!", name)
time.sleep(2)
exit()
