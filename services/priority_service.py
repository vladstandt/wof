class PriorityService:

    order = {

        "High": 1,

        "Medium": 2,

        "Low": 3

    }

    def highest(

        self,

        tasks

    ):

        return sorted(

            tasks,

            key=lambda t:

            self.order[t.priority]

        )
