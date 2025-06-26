from stats import get_book_text, get_word_count_from_text, get_each_character_count, sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"{get_word_count_from_text(path_to_file)}")
        print("--------- Character Count -------")
        for total_char in sorted_list(get_each_character_count(path_to_file)):
            print(f"{total_char["char"]}: {total_char["num"]}")
        print("============= END ===============")

if __name__ == "__main__":
    main()