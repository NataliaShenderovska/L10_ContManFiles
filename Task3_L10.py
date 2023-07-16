import csv
import random

players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
rounds = 100
score_table = []
for round in range(rounds):
    round_scores = [(player, random.randint(0, 1000)) for player in players]
    score_table.extend(round_scores)

with open('player_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    for player, score in score_table:
        writer.writerow([player, score])

print("Score table is saved to player_scores.csv.")
