#Test Match 1 :
#Dhoni : 56 , Balaji : 94

#Test Match 2 :
#Balaji : 80 , Dravid : 105

def Max_Score(Matches):
    """Calculates top scorer from nested match dictionary."""
    total_scores = {}
    
    # Iterate and aggregate scores
    for match in Matches.values():
        for player, score in match.items():
            total_scores[player] = total_scores.get(player, 0) + score
    
    # Identify top scorer
    top_player = max(total_scores, key=total_scores.get)
    top_score = total_scores[top_player]
    
    # Return as tuple
    return (top_player, top_score)

#call function match_data
match_data = {
    'test1':{'Dhoni':56, 'Balaji' : 94}, 
    'test2':{'Balaji': 80, 'Dravid':105}
}


print(Max_Score(match_data)) 

#Output ('Balaji', 174)
