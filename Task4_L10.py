import csv
player_scores = []
with open('player_scores.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader) 
    for row in reader:
        player_name, score = row
        score = int(score)
        player_scores.append((player_name, score))

highest_scores = {}
for player_name, score in player_scores:
    if player_name not in highest_scores:
        highest_scores[player_name] = score
    else:
        highest_scores[player_name] = max(highest_scores[player_name], score)

sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)

with open('high_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest Score'])
    for player_name, highest_score in sorted_scores:
        writer.writerow([player_name, highest_score])

print("Highest scores saved to high_scores.csv.")