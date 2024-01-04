import json
from pathlib import Path

favourite_number = input("What is your favourite number? ")
contents = json.dumps(favourite_number)
path = Path("favourite_number.json")
path.write_text(contents)