import stdio
import stdrandom

# Set a variable(rank) to a random int from [2, 14].
rank = stdrandom.uniformInt(2, 15)

# The if statement to turn the rank of cards into a string
# (11 for Jack, 12 for Queen, and so on).
if rank == 11:
    rank = "Jack"
elif rank == 12:
    rank = "Queen"
elif rank == 13:
    rank = "King"
elif rank == 14:
    rank = "Ace"

# Set a variable(suit) to a random int from [1, 4].
suit = stdrandom.uniformInt(1, 5)

# The if statement to turn the suit of cards into a string
# (1 for Clubs, 2 for Diamonds, 3 for Hearts, and 4 for Spades).
if suit == 1:
    suit = "Clubs"
elif suit == 2:
    suit = "Diamonds"
elif suit == 3:
    suit = "Hearts"
elif suit == 4:
    suit = "Spades"

# Write the output
stdio.writeln(str(rank) + ' of ' + str(suit))
