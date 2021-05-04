import re

print("Hello there! Let's play Madlib :D")

user_inputs = []

with open("madlib.txt") as f:
    content = f.read()

    words = content.split()

    for word in words:
        if word[0] == '{':
            user_inputs.append(word)


answers = []
    
for phrase in user_inputs:
    print(f"Please enter : {phrase}")

    answer = input("> ")

    answers.append(answer)



regex = r"\{[a-z|A-Z|0-9|_|\-|']{1,}\}"

new_content = re.sub(regex, answers[0], content, count = 1)

for i in range(1, len(answers)):
    new_content = re.sub(regex, answers[i], new_content, count = 1)


with open("answered_madlib.txt", 'w') as f:
    f.write(new_content)


with open("answered_madlib.txt") as f:
    end_game = f.read()

print(end_game)

print("Thanks for playing Madlib!")