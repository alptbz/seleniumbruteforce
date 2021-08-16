
words = []

numberOfElements = 3

with open('words.txt') as f:
    words = f.read().splitlines()

currentPassword = []

for i in range(numberOfElements):
    currentPassword.append(-1)

numberOfWords = len(words)

numberOfPasswords = 0

for i in range(numberOfWords):
    numberOfPasswords += pow(i + 1, numberOfElements)

print("Number of words: ", numberOfWords)
print("Number of possible passwords: ", numberOfPasswords)

outputfile = open("dictionary.txt", "w")

pos = 0
currentPassword[0] = 0

while pos < numberOfPasswords:
    password = ""
    capitalizedFirst = ""
    capitalizedAll = ""
    for i in currentPassword:
        if i != -1:
            password += words[i]
            capitalizedAll += words[i].capitalize()
    capitalizedFirst = password.capitalize()
    currentPassword[0] += 1
    for k in range(len(currentPassword)):
        if currentPassword[k] >= numberOfWords:
            currentPassword[k] = -1
            if len(currentPassword) > (k + 1):
                currentPassword[k + 1] += 1
    outputfile.write(password)
    outputfile.write('\n')
    outputfile.write(capitalizedFirst)
    outputfile.write('\n')
    outputfile.write(capitalizedAll)
    outputfile.write('\n')
    pos += 1

outputfile.close()