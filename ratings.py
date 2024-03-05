def rate_restaurant(ratings):
    """Restaurant rating lister."""

    scores = open("scores.txt")
    r_scores = {}
    for line in scores:
        line = line.rstrip()
        restaurant, score = line.split(":")
        r_scores[restaurant] = int(score)
    
    abc_scores = sorted(r_scores)
    
    for key, value in abc_scores.items():                           # loop over each key value pair in word_counts
        print(f"{key} is rated at {value}.")                                     # print each key value pair on separate lines

    return abc_scores



    # return r_scores