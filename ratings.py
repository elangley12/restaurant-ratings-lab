def rate_restaurant(ratings):
    """Restaurant rating lister."""

    text_file = open(ratings)
    abc_scores = {}

    for line in text_file:                                              # parse through each line of the text file
        line = line.rstrip().split(":")                                 # remove each word, one line at a time
        abc_scores = sorted(abc_scores[line])
        # for word in words:                                            # loop through text file word by word
        #     abc_scores[word] = abc_scores.get(word, 0) + 1            # add one for each word to new dictionary
    
        for key, value in abc_scores.items():                           # loop over each key value pair in word_counts
            print(f"{key} {value}")                                     # print each key value pair on separate lines

    # abc_scores = sorted(abc_scores)

    # return abc_scores
