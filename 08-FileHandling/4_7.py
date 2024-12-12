import re

text = input("Enter text: ")
regex = "[aeuio]"

vowel_count = re.findall(regex, text)

print(f"Number of vowels {len(vowel_count)}")

