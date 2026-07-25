from models.task import Task
from data.sample_tasks import TASKS

class TaskRepository:

    def load(self):

        return [

            Task(**task)

            for task in TASKS

        ]
