r'''
Alex Yazdani
10 July 2025

filter_long_words.py
Write a Python function called filter_long_words(input_file, output_file, min_length) that does the following:
    Opens the file specified by input_file, which contains one word per line.
    Filters out all words that are shorter than min_length characters.
    Sorts the remaining words alphabetically.
    Writes the sorted words to output_file, with one word per line.
'''


def filter_long_words(infile, outfile, cnt):
    with open(infile, "r") as fin:
        inwords = fin.read().strip().split("\n")
        outwords = sorted([word for word in inwords if len(word)>=cnt])
    with open(outfile, "w") as fout:
        for word in outwords:
            fout.write(f"{word}\n")



if __name__ == "__main__":
    filter_long_words("input_files/words_in.txt", "output_files/words_out.txt", 5)
    with open("output_files/words_out.txt", "r") as f:
        print(f.read().strip().split("\n"))
