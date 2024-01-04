from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path("python_work/chapter 10/Programming.txt")
path.write_text(contents)