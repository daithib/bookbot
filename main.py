def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = sorted_count(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for i in sorted_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    output = {}
    unique = set()
    #Create a list of unique chars
    for char in text:
        unique.add(char)
    #Count instances of each char and add it to the output dict
    for i in unique:
        running_total = 0
        for char in text:
            if char == i:
                running_total += 1
        output[i] = running_total
    return output            

def sorted_count(counts):
    count_list = []
    for i in counts:
        if i.isalpha():
            count_list.append({"char": i, "num": counts[i]})
    
    count_list.sort(reverse=True, key=sort_on)
    return count_list


def sort_on(dict):
    return dict["num"]    
            
    



def get_book_text(path):
    with open(path) as f:
        return f.read()



main()