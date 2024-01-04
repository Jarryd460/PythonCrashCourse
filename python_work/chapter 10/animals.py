from pathlib import Path

filenames = ["python_work/chapter 10/cats.txt", "python_work/chapter 10/dogs.txt", "python_work/chapter 10/mice.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents)
        print()