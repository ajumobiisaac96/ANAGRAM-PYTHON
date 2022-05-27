# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    w = word.replace(" ","").lower()
    ana = anagram.replace(" ","").lower()

    if (len(w) == len (ana)):

        sorted_1 = sorted(w)
        sorted_2 = sorted(ana)

        if (sorted_1 == sorted_2):
            print ("\nTrue")
        else:
            print ("\nFalse")
    else: 
        print("invalid input.Try again")

find_anagram ("dormitory", "Dirty Room")


