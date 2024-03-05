def rate_restaurant(r_scores):
    """Restaurant rating lister."""

    scores = open("scores.txt")
    # r_scores = {}
    for line in scores:
        line = line.rstrip()
        restaurant, score = line.split(":")
        r_scores[restaurant] = int(score)
        

    abc_scores = dict(sorted(r_scores.items()))
    
    for key, value in abc_scores.items():
        print(f"{key} is rated at {value}.")
    
    
def add_restaurant():
    """Asks the user to add one new restaurant to scores.txt"""

    print("Add your favourite restuarant!")
    name = input("Restuarant name: ")
    scores = input("Rating: ")
    r_scores = {}

    r_scores[name] = scores
    rate_restaurant(r_scores)


add_restaurant()