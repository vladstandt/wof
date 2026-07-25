from config import EXPORT_FILE

from repository.task_repository import TaskRepository

from services.task_service import TaskService
from services.statistics_service import StatisticsService
from services.priority_service import PriorityService

from renderer.console_renderer import ConsoleRenderer
from exporters.json_exporter import JsonExporter

tasks = TaskRepository().load()

tasks = TaskService().sort(

    tasks

)

tasks = PriorityService().highest(

    tasks

)

stats = StatisticsService().build(

    tasks

)

ConsoleRenderer().display(

    tasks,

    stats

)

JsonExporter().export(

    tasks,

    EXPORT_FILE

)
