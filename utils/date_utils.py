from datetime import datetime

def sort_key(task):

    return datetime.strptime(

        task.due,

        "%Y-%m-%d"

    )
