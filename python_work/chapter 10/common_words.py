from pathlib import Path

path = Path("python_work/chapter 10/common_words.txt")
contents = path.read_text()

print(contents.count("row"))
print(contents.lower().count("row"))