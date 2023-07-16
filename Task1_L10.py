import string
import random

file_names = [f"{letter}.txt" for letter in string.ascii_uppercase]

summary = ""
for file_name in file_names:
    random_number = random.randint(1, 100)
    summary += f"{file_name}: {random_number}\n"
    with open(file_name, 'a') as file:
        file.write(f"\n{random_number}")

with open("summary.txt", 'w') as summary_file:
    summary_file.write(summary)

print("Check summary.txt for the list of files and their content")
