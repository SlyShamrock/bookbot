def word_count(text):
    words = text.split()
    return len(words)

def letter_count(book_text):
    letters_dict = {}
    for letter in book_text:
       letter = letter.lower()
       if letter in letters_dict:
            letters_dict[letter] += 1
       else:
            letters_dict[letter] = 1
    return letters_dict        
        

def sorting(count):
    return count["num"]

def sorted_dict(letters_dict):
    new_list = []
    for letter, count in letters_dict.items():
       new_dict = {"char": letter, "num": count}
       new_list.append(new_dict)
    new_list.sort(reverse=True, key=sorting)
    return new_list


