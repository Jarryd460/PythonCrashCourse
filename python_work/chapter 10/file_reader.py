from pathlib import Path

path = Path("python_work/chapter 10/pi_digits.txt")
# Remove the trailing whitespace that python adds when reading the file
contents = path.read_text().rstrip()

# Split the contents of the file into separate lines as it is stored in the file
for line in contents.splitlines():
    print(line)