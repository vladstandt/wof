import json

class JsonExporter:

    def export(

        self,

        tasks,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                [

                    task.__dict__

                    for task

                    in tasks

                ],

                file,

                indent=4

            )
