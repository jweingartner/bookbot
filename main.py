def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    report = generate_report(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    #print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    list = {}
    for character in text:
        lowered = character.lower()
        if lowered in list:
            list[lowered] += 1
        else:
            list[lowered] = 1
    return list

def sort_on(d):
    return d["num"]

def generate_report(num_chars):
    report = []
    for ch in num_chars:
        report.append({"char": ch, "num": num_chars[ch]})
    report.sort(reverse=True, key=sort_on)

    return report


main()