from dataclasses import dataclass

@dataclass
class Task:

    title: str

    priority: str

    completed: bool

    due: str
