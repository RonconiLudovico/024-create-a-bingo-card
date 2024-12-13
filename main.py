# due to the nature of random numbers we import the random library
from random import randint

# first we define the main function in which we create an empty dict and an empty list
# for each letter
def main():
    bingoCard = {}
    B = []
    I = []
    N = []
    G = []
    O = []

# Here we loop until there are 5 elements in each letter list to add a random int, making
# sure not to add same numbers to the lists. After the loop we add the lists to the dict
# using each letter as Key
    while len(B) < 5:
        num = randint(1, 15)
        B.append(num) if num not in B else B.remove(num)
    bingoCard["b"] = B

    while len(I) < 5:
        num = randint(16, 30)
        I.append(num) if num not in I else I.remove(num)
    bingoCard["i"] = I

    while len(N) < 5:
        num = randint(31, 45)
        N.append(num) if num not in N else N.remove(num)
    bingoCard["n"] = N

    while len(G) < 5:
        num = randint(46, 60)
        G.append(num) if num not in G else G.remove(num)
    bingoCard["g"] = G

    while len(O) < 5:
        num = randint(61, 75)
        O.append(num) if num not in O else O.remove(num)
    bingoCard["o"] = O

# finally we return the dictionary
    return bingoCard

# Here we define another function in which we assign the returned value of main()
# to a variable
def display_card():
    bingoCard = main()
    print("\n")
# Then we iterate through every key in the dict printing it followed by a space without any
# newline
    for i in bingoCard.keys():
        print(f"{i.upper()}    ", end="")

# Finally we use f strings to print each value of the same index from all the keys,
# creating a Table
    print(f"\n \n{bingoCard["b"][0]}   {bingoCard["i"][0]}   {bingoCard["n"][0]}   {bingoCard["g"][0]}   {bingoCard["o"][0]}")
    print(f"\n{bingoCard["b"][1]}   {bingoCard["i"][1]}   {bingoCard["n"][1]}   {bingoCard["g"][1]}   {bingoCard["o"][1]}")
    print(f"\n{bingoCard["b"][2]}   {bingoCard["i"][2]}   {bingoCard["n"][2]}   {bingoCard["g"][2]}   {bingoCard["o"][2]}")
    print(f"\n{bingoCard["b"][3]}   {bingoCard["i"][3]}   {bingoCard["n"][3]}   {bingoCard["g"][3]}   {bingoCard["o"][3]}")
    print(f"\n{bingoCard["b"][4]}   {bingoCard["i"][4]}   {bingoCard["n"][4]}   {bingoCard["g"][4]}   {bingoCard["o"][4]}")




if __name__ == "__main__":
    display_card()
