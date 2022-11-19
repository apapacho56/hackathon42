r1 = input("Enter the current ranking score for Player 1")
r2 = input("Enter the current ranking score for Player 2")
outcome = input("Who won?")
def ranking():
	K = 50
	P = 400
	while not (outcome == 1) and (outcome == 2):
        outcome = input("Please type 1 if Player 1 won, 2 if Player 2 won");
	if outcome == 1:
    	s1 = 1
    	s2 = 0
	elif outcome == 2
   		s1 = 0
    	s2 = 1
    rfinal =(r1+K*(s1-(1 / (1 + 10**((r2-r1)/P)))))
    rfinal =round(rfinal)
    return (rfinal)


print("Player 1's old ranking was " + r1 + "!")
print("Player 2's old ranking was " + r2 + "!")
print("Player 1's current ranking is " + ranking(r1, r2, s1))
print("Player 2's current ranking is " + ranking(r2, r1, s2))