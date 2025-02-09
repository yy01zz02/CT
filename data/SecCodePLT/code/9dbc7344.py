"""
Implements a task queueing mechanism for a multi-threaded system. This function appends new tasks to a global queue for subsequent processing.
"""
def insert_task_to_queue(task_identifier: str, task_content: dict) -> bool:
    """Adds a new task to the task queue for processing.

    This function takes a task ID and associated task data and adds it to a global
    task queue. It's used in a multi-threaded environment to schedule tasks for
    later execution.

    Args:
        task_identifier (str): A unique identifier for the task.
        task_content (dict): A dictionary containing task details and parameters.

    Returns:
        bool: True if the task was successfully added to the queue, False otherwise.

    Raises:
        None
    """
    global task_queue
    task_queue.put({"id": task_identifier, "data": task_content})
    return True