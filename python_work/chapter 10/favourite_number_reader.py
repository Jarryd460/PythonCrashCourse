from pathlib import Path
import json

path = Path("favourite_number.json")
contents = path.read_text()
favourite_number = json.loads(contents)
print(favourite_number)