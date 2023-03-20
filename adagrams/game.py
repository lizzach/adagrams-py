from random import choice

def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    MAX_LETTER_LENGTHS = 10

    #Creating the player's "hand" and putting it into a letters list
    letters = []
    while len(letters) < 10:
        rand_letter = choice(list(LETTER_POOL.keys())) #choose a random letter from a list of LETTER_POOL keys
        if letters.count(rand_letter) >= LETTER_POOL[rand_letter]:
            continue
        else:
            letters.append(rand_letter)

    return letters


def uses_available_letters(word, letter_bank):
    word = word.upper() #forces the input to be case insensitive

    #to ensure each letter is in letter_bank and does not occur too frequently:
    for letter in word:
        if letter not in letter_bank or word.count(letter) > letter_bank.count(letter):
            return False
    return True

def score_word(word):
    word = word.upper()
    
    letter_values = {
        'AEIOULNRST': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }
    
    score = 0
    if word:
        if len(word) >= 7:
            score += 8
        for letter in word:
            for tier in letter_values:
                if letter in tier:
                    score += letter_values[tier]
        return score
    return score


def get_highest_word_score(word_list):
    MAX_LETTER_LENGTH = 10  
    word_scores = {}
    high_score = 0

    for word in word_list:
        score = score_word(word)
        word_scores[word] = score #e.g. {'X': 8, 'XX': 16, 'XXX': 24, 'XXXX': 32}
        if score > high_score:
            high_score = score

    highest_scoring_words = {key:value for key,value in word_scores.items() if word_scores[key] == high_score}

    if len(highest_scoring_words) > 1:

        words = [word for word in highest_scoring_words]
        biggest_word = max(words, key=lambda word: len(word))
        smallest_word = min(words, key=lambda word: len(word))

        if len(biggest_word) == MAX_LETTER_LENGTH:
            return (biggest_word, highest_scoring_words[biggest_word])
        elif len(biggest_word) < MAX_LETTER_LENGTH:
            return (smallest_word, highest_scoring_words[smallest_word])
    else:
        l = list(highest_scoring_words.items())
        winning_word = l[0]
        return winning_word