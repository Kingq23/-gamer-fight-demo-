from json import load
import os,other,random
with open('database?/armor.json') as f:
  armor = load(f)
	
with open('database?/enemys.json') as f:
	enemy = load(f)

with open('database?/weapon.json') as f:
  weapon = load(f)
	
def encouter(enemy_stat,weapon_stat,armor_stat):
	enemy_hp = enemy[enemy_stat]["hp"]
	enemy_def = enemy[enemy_stat]["defence"]
	enemy_atk = enemy[enemy_stat]["damage"]
	player_hp = armor[armor_stat]["ad-hp"]
	player_atk = weapon[weapon_stat]["damage"]
	player_def = armor[armor_stat]["defence"]
	while True:
		
		def_turn = 0
		print("1.attack 2.defend")
		print(f"your hp:{player_hp} enemy hp:{enemy_hp}")
		action = input()
		if action == "1":
			print(f"you did {enemy_hp - player_atk}")
			enemy_hp = enemy_hp - player_atk
		elif action == "2":
			player_def = player_def + 5
			def_turn = 2
		def_chance = random.randint(1,20)
		if def_chance <=player_def:
			print(f"they missed most of the damage and did {(enemy_atk / 2)}")
			player_hp = player_hp - (enemy_atk / 2)
		else:
			print(f"they did {enemy_atk}")
			player_hp = player_hp - enemy_atk
		if enemy_hp <=0:
			os.system("clear")
			
			other.write("the enemy died")
			break
		elif player_hp <=0:
			os.system("clear")
			other.write("YOU died")
			break
default = ["gooblin","slime"]

encouter(random.choice(default), "stick", "ancient clothes")