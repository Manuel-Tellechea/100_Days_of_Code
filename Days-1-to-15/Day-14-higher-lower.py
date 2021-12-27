from art14 import logo, vs
from game_data14 import data
import random

game_over = False
counter = 0

while not game_over:

  choices_to_compare = random.choices(data, k=2)
  name1 = choices_to_compare[0]['name']
  description1 = choices_to_compare[0]['description']
  country1 = choices_to_compare[0]['country']
  follower_count1 = choices_to_compare[0]['follower_count']

  name2 = choices_to_compare[1]['name']
  description2 = choices_to_compare[1]['description']
  country2 = choices_to_compare[1]['country']
  follower_count2 = choices_to_compare[1]['follower_count']

  print(logo)
  print(f"Compare A: {name1}, {description1}, from {country1}")

  print(vs)
  print(f"Compare B: {name2}, {description2}, from {country2}")
  selection = input("Who has more followers? Type 'A' or 'B': ")

  if follower_count1 > follower_count2:
    winner = 'A'
  else:
    winner = 'B'

  if selection == winner:
    counter += 1
    print(f"You're right! Current score: {counter}.")
  else:
    counter = 0
    game_over = True
    print("Game Over")
