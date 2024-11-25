r'''
Alex Yazdani
21 November 2024

reverse_string.py
Reverse the order of words in a string.
'''

# def reverse_string(str):
#     words = str.split()
#     string_out = ""
#     for i in range(len(words)-1, -1, -1):
#         string_out = string_out + words[i] + " "
#     return string_out.strip()

def reverse_string(str):
    return  " ".join(str.split()[::-1])

if __name__ == "__main__":
    print(reverse_string("Hello World!"))
    print(reverse_string("Python is awesome"))
    print(reverse_string("I started a joke"))
    print(reverse_string("One two three four"))
    print(reverse_string(""))
    print(reverse_string("SingleWord"))