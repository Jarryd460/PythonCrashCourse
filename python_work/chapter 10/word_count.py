from pathlib import Path

def count_words(path):
    """Count the approximate words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        # Count the approximate words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ["python_work/chapter 10/alice.txt", "python_work/chapter 10/siddhartha.txt", "python_work/chapter 10/moby_dick.txt", "python_work/chapter 10/little_woman.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)