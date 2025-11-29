import random  # function for choosing a random word.

# Function for choosing a random word
def choose():
    words = ["SEPARATE", "DEFINITELY", "OCCURRENCE", "CONSENSUS", "ACCEPTABLE",
             "BROCCOLI", "REFERRED", "BUREAUCRACY", "BISHOP", "PROGRAMMING",
             "ENTREPRENEUR", "CONSCIENCE", "PARALLEL", "CENTRE"]
    pick = random.choice(words)
    return pick

# Function to jumble characters of the chosen word
def jumble(word):
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled

# Function for showing final score
def thank(p1name, p2name, p1score, p2score):
    print(p1name, 'Your score is:', p1score)
    print(p2name, 'Your score is:', p2score)
    print('Thanks for playing...')

# Function for declaring the winner
def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("Winner is", player1)
    elif p2score > p1score:
        print("Winner is", player2)
    else:
        print("Draw.. Well Played, everyone!")

# Function for playing the game
def play():
    # Enter player1 and player2 names
    p1name = input("Player 1, please enter your name: ")
    p2name = input("Player 2, please enter your name: ")
    
    # Variables for counting scores
    p1score = 0
    p2score = 0
    # Variable for counting turns
    turn = 0

    print("Use CAPS Only")

    # Game loop
    while True:
        # Choose a random word
        picked_word = choose()
        # Jumble the chosen word
        question = jumble(picked_word)
        print("Jumbled word is:", question)

        # Player 1's turn if turn number is even, otherwise Player 2's turn
        if turn % 2 == 0:
            print(p1name, "Your Turn.")
            answer = input("What is in your mind? ")

            # Check if answer is correct
            if answer == picked_word:
                p1score += 1  # Increment Player 1's score
                print("Correct! Your score is:", p1score)
            else:
                print("Better luck next time...")
            
        else:
            print(p2name, "Your Turn.")
            answer = input("What is in your mind? ")

            # Check if answer is correct
            if answer == picked_word:
                p2score += 1  # Increment Player 2's score
                print("Correct! Your score is:", p2score)
            else:
                print("Better luck next time...")

        # Display the correct word and prompt to continue or quit
        print("Correct word was:", picked_word)
        cont = int(input("Press 1 to continue or 0 to quit: "))

        # Break loop if user chooses to quit
        if cont == 0:
            # Call thank() function to show final score
            thank(p1name, p2name, p1score, p2score)
            # Call check_win() to declare the winner
            check_win(p1name, p2name, p1score, p2score)
            break
        else:
            # Increment the turn count to switch players
            turn += 1

# Driver code
if __name__ == '__main__':
    # Start the game by calling the play function
    play()
