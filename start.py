# Libraries
from commands import *
from player_stats import *
from monster_stats import *
import random
import time

# Variables

ran_drops = random.choice

# Player Class
classes = ["Warrior", "Mage", "Healer"]
print(classes)
choose_class = input("Choose your class from the above: ")

if choose_class == "Warrior":
	melee_weapon = "Bloody Axe"
	print(f"Your main weapon is: {melee_weapon}")
elif choose_class == "Mage":
	melee_weapon = "Gamma Spear"
	print(f"Your main weapon is: {melee_weapon}")
elif choose_class == "Healer":
	melee_weapon = "Spear"
	print(f"Your main weapon is: {melee_weapon}")

name = input("What will you go by Warrior? ")

# Funny
if name == "louvie":
	if choose_class == "Mage":
		player_gold += 1000
		print(f"Here you go mommy louv. 1000 gold")

print(f"NAME : {name}")

# tutorial
time.sleep(2)

print("You wonder around to discover a Goblin.\nFight it.")

time.sleep(1)
while True:
	print(f"Goblin Health: {goblin_health}")

	if choose_class == "Warrior":
		print("Attacks:\n1) Blood Swing")
	elif choose_class == "Mage" or "Healer":
		print("Attacks:\n1) Jab")	
	player_fight = input("")

	if player_fight == "1":
		goblin_health -= 5
	if goblin_health == 0:
		break

# Victory

print("Congratulations on beating your first enemy!")
player_gold += goblin_gold_drop
print(f"You have recieved {goblin_gold_drop} gold!")

# Game

while True:
	print("If you're stuck type 'help' or '?' for a list of commands")
	cmds = input(">")

	if cmds in help_commands:
		print(f"Commands\nHelp Prefixes: {help_commands}\nShop Prefixes: {shop_commands}")

	if cmds in shop_commands:
		print(f"")