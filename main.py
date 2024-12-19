

def main():
    book_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count = wordCount(file_contents)
    
    unsort = (counter(file_contents))
    
    sorted = chars_sort(unsort)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()
    
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def wordCount(file_contents):
    words = file_contents.split()
    count = len(words)
    return count
    
def counter(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    return chars


def sort_on(d):
    return d["num"]

def chars_sort(unsort):
    sorted = []
    for ch in unsort:
        sorted.append({"char": ch, "num": unsort[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
        
main()