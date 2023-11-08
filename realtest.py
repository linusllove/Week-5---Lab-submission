from logic import get_winner
#test None
test = [[None,"O","X"], ["O",None,"X"],["O","X","O"]]
winner = get_winner (test)
print(winner)

#test X
test = [["O",None,"X"], ["X","X","O"],["X","X","O"]]
winner = get_winner (test)
print(winner)
