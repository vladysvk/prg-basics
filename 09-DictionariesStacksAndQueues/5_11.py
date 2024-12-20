import json


try:
    with open("voting.json", encoding="utf-8") as new_file:
        votes = json.load(new_file)
except FileNotFoundError:
    votes = {}
except json.JSONDecodeError:
    votes = {}


person_name = input("Name of the person you are voting for: ").strip()


if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1


with open("voting.json", "w", encoding="utf-8") as file:
    json.dump(votes, file, ensure_ascii=False, indent=4)

print(f"Vote for {person_name} has been recorded.")
