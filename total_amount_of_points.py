# Our football team has finished the championship.
# Our team's match results are recorded in a collection of strings. 
# Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)

# Solution:

def points(games):
    total_points = 0
    for game in games:
        x,y = map(int, game.split(':'))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
    return total_points

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))