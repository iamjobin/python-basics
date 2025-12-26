import utils as math
from utils import open_file
from pathlib import Path

print(math.add(10,10))

print(Path.cwd()) 
path = Path('memory.json')
print(path.resolve())
print(open_file(path))
