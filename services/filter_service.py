class FilterService:

    def pending(

        self,

        tasks

    ):

        return [

            task

            for task in tasks

            if not task.completed

        ]
