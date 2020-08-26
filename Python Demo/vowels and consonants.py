vowels = ['a', 'e', 'i', 'o', 'u']

count_vowels = 0
count_consonants = 0

str = "hi i am rohit lets start"


for e in str:
    if e in vowels:
        count_vowels += 1
    else:
        count_consonants += 1


print(count_vowels, count_consonants)
