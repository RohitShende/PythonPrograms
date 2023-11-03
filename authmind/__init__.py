"""
Get data from the file
Filter only unique sentences and remove duplicates
Print only those sentences that are palindromes

Optimized for a bigger file
Handle exceptions if the file is not present
Handle the case where the file is empty

"""


def get_unique_palindrome_sentences(file):
    # read a file line by line
    # and not load the entire file in memory
    # to handle bigger files
    # use the variable "file" to read the file

    with open(file) as f:
        while True:
            sentence = f.readline()

            if not sentence:
                break

            # clean the sentence
            sentence = sentence.strip()

            # print("sentence:", sentence)

            N = len(sentence)
            is_palindrome = True
            for i in range(N//2):
                if sentence[i].lower() != sentence[N-i-1].lower():
                    is_palindrome = False

            if is_palindrome:
                print(sentence)

    # print("Completed")


if __name__ == '__main__':
    get_unique_palindrome_sentences(file="data.txt")
