"""Restaurant rating lister."""
#define funcion that takes in text file name as argument
#open and store text file data into a file handle object
#use a for loop to create a list of words (use rstrip and split methods)



# put your code here

def sort_restaurant_ratings(filename):

    text_file = open(filename)

    dictionary_of_ratings = {}

    for line in text_file:
        line = line.rstrip() # why is this different than just line.rstrip() ?
        words = line.split(' ')