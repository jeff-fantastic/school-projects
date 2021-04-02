#######################################################
#   Simulation game of traveling out west in 1800's   #
#######################################################

  ###################################################
  # I had fun making this, and learned some new     #
  # stuff while I was at it. Never played this      #
  # classic game myself so I took some creative     #
  # liberties when it came to what happened in it.  #
  # Code is also available on my github page! Check #
  # out my other endeavors into C and whatnot       #
  # there if you're interested.                     #
  ###################################################

#######################################################
# https://github.com/jefftasticgames/school-projects/ #
#######################################################

import random
from random import randint

welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
		   3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
		   2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck, and see you in Oregon!"

# Model -- variables that collectivel represent the state
# of the game
miles_traveled = 0
food_remaining = 500
health_level = 5
appetite = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
random_events_this_month = 0
player_name = None

# Constants -- parameters that define the rules of the game,
# but which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 90
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

MIN_DAYS_PER_RANDOM_EVENT = 1
MAX_DAYS_PER_RANDOM_EVENT = 10
MIN_FOOD_PER_RANDOM_EVENT = 1
MAX_FOOD_PER_RANDOM_EVENT = 100

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
	'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
	'August', 'September', 'October', 'November', 'December'
]


# Converts are numeric date into a string.
# input: m - a month in the range 1-12
# input: d - a day in the range 1-31
# output: a string like "December 24".
# Note: this function does not enforce calendar rules. It's happy to output
# impossible strings like "June 95" or "February 31"
def date_as_string(m, d):
	return str(NAME_OF_MONTH[m]) + " " + str(d)

def miles_remaining():
	return MILES_BETWEEN_NYC_AND_OREGON - miles_traveled

# Returns the number of days in the month (28, 30, or 31).
# input: an integer from 1 to 12. 1=January, 2=February, etc.
# output: the number of days in the month. If the input is not in
#   the required range, returns 0.
def days_in_month(m):
	if m in MONTHS_WITH_28_DAYS:
		return 28
	elif m in MONTHS_WITH_30_DAYS:
		return 30
	elif m in MONTHS_WITH_31_DAYS:
		return 31
	else:
		return 0
 
# Calculates whether a sickess occurs on the current day based
# on how many days remain in the month and how many sick days have
# already occured this month. If there are N days left in the month, then
# the chance of a sick day is either 0, 1 out of N, or 2 out of N, depending
# on whether there have been 2 sick days so far, 1 sick day so far, or no
# sick days so far.
#
# This system guarantees that there will be exactly
# 2 sick days each month, and incidentally that every day of the month
# is equally likely to be a sick day (proof left to the reader!)
def random_sickness_occurs():
	global month
	global day
	days_left = days_in_month(month) - day
	rand_sick = 1
	if (days_left >= 1):
		rand_sick = randint(0, days_left)
	if (sicknesses_suffered_this_month == 0):
		if (rand_sick < 2):
			handle_sickness()
	elif (sicknesses_suffered_this_month == 1):
		if (rand_sick < 1):
			handle_sickness()

def handle_sickness():
	global health_level
	global sicknesses_suffered_this_month
	sicknesses_suffered_this_month += 1
	health_level -= 1
	print("\nYOW! You got sick and lost a health point.")

def consume_food():
	global food_remaining
	global appetite
	food_remaining -= appetite

# YOW! Random events are meant to be fun little things that happen from time to
# time on your adventure. Pretty much you always have a 1/50 chance of having
# a random event happening once a month. If you're lucky, you can scathe away
# and not deal with any incidents!
#
# Incidents include: flooding, dysentery, mugging, stash discovery

def random_event_occurs():
	global random_events_this_month
	if (random_events_this_month == 0):
		if (randint(1, 25) == 1):
			handle_random_event()

def handle_random_event():
	global health_level
	global food_remaining
	global random_events_this_month
	random_event = randint(1, 4)
	if (random_event == 1): # flood
		rand_days = randint(MIN_DAYS_PER_RANDOM_EVENT, MAX_DAYS_PER_RANDOM_EVENT)
		rand_food = randint(MIN_FOOD_PER_RANDOM_EVENT, MAX_FOOD_PER_RANDOM_EVENT)
		food_remaining -= rand_food
		advance_game_clock(rand_days)
		print("\nA rain shower came through and flooded your wagon. You lost", str(rand_food), "pounds of food and took", str(rand_days), "days to recover.")
	elif (random_event == 2): # dysentery
		rand_days = randint(MIN_DAYS_PER_RANDOM_EVENT, MAX_DAYS_PER_RANDOM_EVENT)
		rand_health = randint(0, 2)
		health_level -= rand_health
		advance_game_clock(rand_days)
		print("\nYou fell sick to dysentery and lost", str(rand_health), "health and took", str(rand_days), "days to recover.")
	elif (random_event == 3): # mugging
		rand_food = randint(MIN_FOOD_PER_RANDOM_EVENT, MAX_FOOD_PER_RANDOM_EVENT)
		mugging_prompt = input("\nOutlaws approach your wagon. Do you let them take your food? (Y/N) -->")
		if mugging_prompt == "N":
			print("\nYou pull out your hunting rifle to defend yourself.")
			rand_defense = randint(0, 1)
			if rand_defense == 0:
				health_level -= 3
				print("\nYou get shot and lose 3 health.")
			else:
				food_remaining += rand_food
				print("\nYou shoot the outlaws and gain", str(rand_food), "pounds of food.")
		else:
			food_remaining -= rand_food
			print("\nYou let the outlaws take your food. You lost", str(rand_food), "pounds of food.")
	else: # stash
		rand_food = randint(MIN_FOOD_PER_RANDOM_EVENT, MAX_FOOD_PER_RANDOM_EVENT)
		food_remaining += rand_food
		print("\nLucky day! You found a stash containing", str(rand_food), "pounds of food! What a steal!")
	random_events_this_month += 1

# Repairs problematic values in the global (month, day) model where the day is
# larger than the number of days in the month. If this happens, advances to the next
# month and knocks the day value down accordingly. Knows that different months have
# different numbers of days. Doesn't handle cases where the day is more than 28
# days in excess of the limit for that month -- could still end up with an
# impossible date after this function is called.
#
# Returns True if the global month/day values were altered, else False.
def maybe_rollover_month():
	if (day > days_in_month(month)):
		return True
	else:
		return False
	# Enter your code here

# Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness. The sickness rules are quirky: player
# is guaranteed to fall ill a certain number of times each month, so illness
# needs to keep track of month changes.
#
# input: num_days - an integer number of days that elapse.
def advance_game_clock(num_days):
	global month
	global day
	global sicknesses_suffered_this_month
	global random_events_this_month
	while num_days > 0:
		if game_is_over():
			num_days = 0
		day += 1
		if maybe_rollover_month():
			sicknesses_suffered_this_month = 0
			random_events_this_month = 0
			day = 1
			month += 1
		consume_food()
		random_sickness_occurs()
		random_event_occurs()
		num_days -= 1


def handle_travel():
	global miles_traveled
	rand_miles = randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
	rand_days = randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)
	miles_traveled += rand_miles
	appetite = 5
	advance_game_clock(rand_days)
	Rplayer_wins()
	print("\nYou traveled", str(rand_miles), "miles in", str(rand_days) + " days!", "\nOnly", miles_remaining(), "miles remain.")

def handle_rest():
	global health_level
	if (health_level < MAX_HEALTH):
		rand_days = randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)
		appetite = 3
		health_level += HEALTH_CHANGE_PER_REST
		print("\nYou rest for", str(rand_days), "days and gained 1 health.")
		advance_game_clock(rand_days)
	else:
		print("\nNo need to rest! You feel just fine.")

def handle_hunt():
	global food_remaining
	rand_days = randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)
	food_remaining += 100
	appetite = 8
	print("\nYou hunt all day, gathering 100 pounds of food in", str(rand_days), "days!")
	advance_game_clock(rand_days)

def handle_status():
	global food_remaining
	global health_level
	global miles_traveled
	global day
	global month
	print("\nFOOD:", str(food_remaining))
	print("HEALTH:", str(health_level))
	print("DIST TRAVELED:", str(miles_traveled))
	print("DATE:", date_as_string(month, day))

def handle_help():
	print(help_text)

def handle_quit():
	global playing
	playing = False

def handle_invalid_input(response):
	print("'{0}' is not a valid command. Try again.".format(response))

def game_is_over():
	global month
	global day
	global health_level
	if month == 12 and day == 31:
		return True
	elif health_level <= 0 or food_remaining <= 0:
		return True
	elif player_wins():
		return True
	else:
		return False

def player_wins():
	global miles_traveled
	if miles_traveled >= MILES_BETWEEN_NYC_AND_OREGON:
		return True
	else:
		return False

def loss_report():
	global food_remaining
	global health_level
	global miles_traveled
	global day
	global month
	print("\nFOOD:", str(food_remaining))
	print("HEALTH:", str(health_level))
	print("DIST TRAVELED:", str(miles_traveled))

def win_report():
	global food_remaining
	global health_level
	global day
	global month
	print("\nFOOD:", str(food_remaining))
	print("HEALTH:", str(health_level))
	print("DATE OF ARRIVAL:", date_as_string(month, day))


print(welcome_text + help_text + good_luck_text)
player_name = input("\nWhat is your name, player? ")

playing = True
handle_status()
while playing:
	# print(str(random_events_this_month), str(sicknesses_suffered_this_month)) # debug
	action = input("Choose an action, {0} --> ".format(player_name))
	if action == "travel" or action == "t":
		handle_travel()
	elif action == "rest" or action == "r":
		handle_rest()
	elif action == "hunt" or action == "h":
		handle_hunt()
	elif action == "quit" or action == "q":
		handle_quit()
	elif action == "help" or action == "?":
		handle_help()
	elif action == "status" or action == "s":
		handle_status()
	else:
		handle_invalid_input(action)

	if game_is_over():
		playing = False

if player_wins():
	print("\n\nCongratulations you made it to Oregon alive!")
	print(win_report())
else:
	print("\n\nAlas! You lose.")
	print(loss_report())