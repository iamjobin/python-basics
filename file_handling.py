import json
from pathlib import Path

# Read Files
with open('data.txt', 'r') as file:
    content = file.read() # Read Lines -> readLine(), readLines()

with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

print(content)


# Write Files
# 1. Overwrite
with open('data.txt', 'w') as file:
    file.write('test\n')

# 2. Append
with open('data.txt', 'a') as file:
    file.write('demo\n')

# Json with files
data = {
    "user": "Jobin",
    "role": "Engineer"
}

with open('config.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('config.json', 'r') as file:
    config = json.load(file)

print(config['user'])


#Sample Agent code
MEMORY_FILE = Path('memory.json')

def save_memory(data):
    with open(MEMORY_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def load_memory():
    if not MEMORY_FILE.exists():
        return {}
    with open(MEMORY_FILE) as file:
        return json.load(file)
    
save_memory(config)
print(load_memory())