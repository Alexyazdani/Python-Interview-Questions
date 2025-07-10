r'''
Alex Yazdani
10 July 2025

extract_emails.py
Write a Python function that extracts all unique email addresses from a text file and writes them to a new file in sorted order.
Use regular expressions to extract all valid email addresses.
Ignore duplicate email addresses.
'''

import re

def extract_emails(infile, outfile):
    with open("input_files/emails_in.txt", "r") as fin:
        text = fin.read()
        matches = re.findall(r'\S+@\S+\.(?:com|org)', text)
        unique_emails = sorted(set(matches))
    with open("output_files/emails_out.txt", "w") as fout:
        for email in unique_emails:
            fout.write(f"{email}\n")


if __name__ == "__main__":
    extract_emails("sample_input.txt", "sample_output.txt")
    with open("output_files/emails_out.txt", "r") as f:
        print(f.read())
