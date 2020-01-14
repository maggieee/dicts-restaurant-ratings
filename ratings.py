"""Restaurant rating lister."""
#define funcion that takes in text file name as argument
#open and store text file data into a file handle object
#use a for loop to create a list of words (use rstrip and split methods)
# 


# put your code here

def sort_restaurant_ratings(filename):

    text_file = open(filename)

    dictionary_of_ratings = {}

    for line in text_file:
        line = line.rstrip()
        words = line.split(':')
        # print(words)

        dictionary_of_ratings[words[0]] = words[1]

        sorted_list_of_keys = sorted(dictionary_of_ratings)

   
    for key in sorted_list_of_keys:
        print(f'{key} is rated at {dictionary_of_ratings[key]}')
        # print("{} is rated at {}".format(key, dictionary_of_ratings[key]))


sort_restaurant_ratings('scores.txt')