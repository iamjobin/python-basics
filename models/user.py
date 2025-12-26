from dataclasses import dataclass, field
from typing import Optional

@dataclass #It has everything and skips the boilerplate codes, if @dataclass(frozen=True) than it acts like Java final
class User:
    name: str 
    age: Optional[str] = None
    messages: list = field(default_factory=list)

    def have_messages(self):
        return (len(self.messages)>0)

u = User('test', messages=['h'])

print(u)
