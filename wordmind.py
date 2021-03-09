import random
my_list = ['burn' , 'raid' , 'head' ,  'cane',  'bond', 'nest', 'tidy' , 'deny',  'riot' , 'twin',\
'flow', 'thin', 'body' , 'rain', 'salt', 'jury', 'nail','land', 'rage' ,'lack' ,'soar' ,'last' ,'bang' ,'pray', 'crew', 'home' ,\
 'plot', 'dawn', 'warm', 'raid', 'lost' ,'neck' ,'code' ,'yard' ,'hour' g]
#mylist = ['ruimtereis', 'aap', 'abbonees', 'boekenkast', 'euro', 'journalist', 'nacht', 'puur',  'kwast']
secret_word = random.choice(my_list)
doorgaan = True
#secret_word = input("Choose the secret_word! (Dont let the player know) : ").lower()
secret_word_length = len(secret_word)
#print("")
#print("")
print("Welcome to WORDMIND!")
print("The secret word length is: ")
print("-"*secret_word_length)
print("So the secret word length is: ", secret_word_length, " characters.")
secLetter1Correct = False
procentcorrectstring = "-"*secret_word_length
print_word = ""

number_of_guesses = 0
print("dash(-) means that the letter on that spot is not in the word you are trying to guess.")
print("If you guess a letter correctly that is also in the right spot, then you unlock the letter.")
print("If you guess a letter correctly that is not in the right spot, then it will show a question mark (?)")
while doorgaan:
    print(print_word)
    print_word = ""
    first_guess = input("Guess the word: ").lower()
    first_guess_length = len(first_guess)
    if first_guess_length == secret_word_length:
        number_of_guesses = number_of_guesses + 1
        print("You have guessed" , number_of_guesses, " time(s)!")
        if first_guess == secret_word:
            print("You have won!")
            print("The word was: ", secret_word)
            doorgaan = False
        elif first_guess != secret_word: # else
            for i in range(len(first_guess)):
                if first_guess[i] == secret_word[i]:
                    print_word += secret_word[i]
                    #print("letter" ,i + 1," is in Correct spot, Correct letter.")
                elif first_guess[i] in secret_word:
                    print_word += "?"
                    #print("letter" ,i + 1,"Incorrect spot, Correct letter.")
                else:
                    print_word += "-"
                    #print("letter" ,i + 1,"Incorrect spot, Incorrect letter. Letter", i + 1 ,", is not in this word ")



            #Eerst  letter op goede positie print letter
            #als niet op positie checken of het in een ander positie in het woord zit
            #als ook vals is dan -
        else:
            print("That is incorrect.")
            print("The length of the word is correct.")
    else:
        print("The length of the word is incorrect!")
else:
    print("GAME OVER")