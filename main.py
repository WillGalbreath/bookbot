

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    wordCount(file_contents)
    
    print(counter(file_contents))
    

def wordCount(file_contents):
    words = file_contents.split()
    count = len(words)
    print(count)
    
def counter(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

        
main()