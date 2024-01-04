from pathlib import Path

path = Path("python_work/chapter 10/learning_python.txt")
contents = path.read_text()

print(contents)

for line in contents.splitlines():
    line = line.replace("Python", "C#")
    print(line)