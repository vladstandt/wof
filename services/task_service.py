from utils.date_utils import sort_key

class TaskService:

    def sort(

        self,

        tasks

    ):

        return sorted(

            tasks,

            key=sort_key

        )
