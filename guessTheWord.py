import random

# A list of words that someone can guess
potential_words = ["example", "words", "someone", "can", "guess"]
word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word

for i in range (len(word)):  # appends the same number of "_" as there are letters
	current_word.append("_")
#print(current_word)




# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	print(current_word)
	if "_" not in current_word:
		print("You win! The word was", word.upper())
		break
	guess = input("Guess a letter: ")


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	if guess in current_word:
		print("you already guessed that letter, try again!")

	for i in range(len(current_word)): # letter is the arbitrary variable we use in a for loop
		if guess == word[i]: # if the guess you made equals a letter in the word
			current_word[i] = guess # the "_" will be replaced with the guessed letter


	if  guess not in word:
		if guess in guesses:
			print("you already guessed that letter, try again!")
		else:
			fails = fails+1
			print("You have " + str(maxfails - fails) + " tries left!")
			guesses.append(guess)

if fails == maxfails:
	print("Out of guesses. Your word was", word.upper())
