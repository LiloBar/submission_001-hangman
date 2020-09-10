#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    my_file = open(file_name,'r')
    word = my_file.readlines()
    my_file.close()

    return word


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    rand = random.randint(0, len(words) -1) #here I am asking for the 
    ran_word = words[rand]
    random_number = random.randint(0, len(ran_word)-1)
    list_underscore = list(ran_word)
    list_underscore[random_number] = '_'
    string_hint = ''.join(list_underscore)

    print("Guess the word: " + string_hint)

    return ran_word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    put_name = input('Guess the missing letter: ')
    return put_name


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

