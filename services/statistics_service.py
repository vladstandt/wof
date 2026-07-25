class StatisticsService:

    def build(

        self,

        tasks

    ):

        completed = sum(

            task.completed

            for task in tasks

        )

        return {

            "total": len(tasks),

            "completed": completed,

            "pending": len(tasks)-completed

        }
