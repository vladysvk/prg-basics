import re

sender = ""
recepient = ""
subject = ""
body = ""

with open("email.txt" ) as file:
    email = file.read()

sender = re.search("From: .+ .+ <(.+)>", email)
recepient = re.search("To: .+ .+ <(.+)>", email)
subject = re.search("Subject: (.+)", email)
body = re.search("Content-Transfer-Encoding: 7bit\s+([\s\S]+)", email)
print(sender.group(1))
print(recepient.group(1))
print(subject.group(1))
print(body.group(1))