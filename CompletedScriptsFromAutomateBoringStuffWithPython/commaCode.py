spam = ['apples', 'bananas', 'tofu', 'cats']
newSpam = ['']

def someFunction(spam):
    for i in range(spam[len(spam) -2]):
        newSpam.append(str(spam[i] + ", "))

newSpam.append(" and " + str(spam[len(spam) -1]))

print(someFunction(spam))
