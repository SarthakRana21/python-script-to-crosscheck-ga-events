import difflib
import re

# Open the two text files check readme for more info
with open("{path of textfile1}", "r") as f1, open("{path of textfile2}", "r") as f2:
    file1_contents = f1.read()
    file2_contents = f2.read()

file1_lines = file1_contents.splitlines()
file2_lines = file2_contents.splitlines()

file1_words = set()

for line in file1_lines:
    line = re.sub(r"[^\w\s]", "", line)
    line = re.sub(r"\(|\)|\[|\]|{|}|<|>|,|;", "", line)
    line = re.sub(r"dynamic", "", line)
    line = re.sub(r"static", "", line)
    #line = re.sub(r"", "", line)
    line = line.lower()
    words = line.split()
    file1_words.update(words)

file2_words = set()

for line in file2_lines:
    line = re.sub(r"[^\w\s]", "", line)
    line = re.sub(r"\(|\)|\[|\]|{|}|<|>|,|;", "", line)
    line = line.lower()
    words = line.split()
    file2_words.update(words)

missing_words = file1_words - file2_words

print(missing_words)
