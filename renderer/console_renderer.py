class ConsoleRenderer:

    def display(

        self,

        tasks,

        stats

    ):

        print()

        print("Task List\n")

        for task in tasks:

            mark = "x" if task.completed else " "

            print(

                f"[{mark}] {task.title}"

            )

            print(

                f"Priority: {task.priority}"

            )

            print(

                f"Due: {task.due}"

            )

            print()

        print("Summary\n")

        print(

            f"Total: {stats['total']}"

        )

        print(

            f"Completed: {stats['completed']}"

        )

        print(

            f"Pending: {stats['pending']}"

        )
