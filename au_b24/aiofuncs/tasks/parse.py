import inspect
from typing import Callable, Literal
from ...aioreqs import post
from ..exceptions import StopParsing

def parse_tasks(fn: Callable):
    def wrapper(filters: dict, select: list, order: Literal['asc', 'desc'] = 'asc', **kwargs):
        async def async_wrapper():
            if not isinstance(filters, dict):
                raise ValueError("Filters must be a dict")
            if not select:
                raise ValueError("Select is not provided")
            if not isinstance(select, list):
                raise ValueError("Select must be a list")
            if order not in ('asc', 'desc'):
                raise ValueError("Order must be 'asc' or 'desc")
            if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
                raise ValueError("id filtering can't be used with '<', '>', '>=' and '<='")
            filters_copy = filters.copy()
            if order == "asc":
                filters_copy.update({">ID": 0})
                id_key = ">ID"
            else:
                filters_copy.update({"<ID": 2**32})
                id_key = "<ID"
            counter = 0
            while True:
                response = await post("tasks.task.list", {"filter": filters_copy, "select": select, 'order': {"ID": order}, "start": "-1"})
                if not response or not "tasks" in response:
                    break
                tasks = response["tasks"]
                if not tasks or not isinstance(tasks, list):
                    break
                for task in tasks:
                    if not task or not isinstance(task, dict):
                        continue
                    filters_copy[id_key] = task["id"]
                    try:
                        counter += 1
                        if inspect.iscoroutinefunction(fn):
                            await fn(task, counter=counter, **kwargs)
                        else:
                            fn(task, counter=counter, **kwargs)
                    except StopParsing:
                        return
        return async_wrapper()
    return wrapper
