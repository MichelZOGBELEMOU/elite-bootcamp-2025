"""A module that defines a basic task hierarchy """
from datetime import datetime

# Standardization of statuses
ALLOWED_STATUSES = {"todo", "processing", "done"}
class Task:
    """Represents a simple task with a name and status"""
    def __init__(self, name: str, status: str = "todo")->None:
        """Initialize a task with a name and status"""
        self.name = name
        if status.lower() not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status: {status}. Choose from {ALLOWED_STATUSES}")
        self.status = status.lower()

    def __repr__(self) -> str:
        return f"Task({self.name!r}, {self.status!r})"

    def mark_done(self) ->None:
        """Mark the task as completed by setting its status to done"""
        self.status = "done"

    def __str__(self) -> str:
        return f"Task({self.name}, {self.status})"


class RecurringTask(Task):
    """Represents a recurring task that repeats at a given interval"""
    def __init__(self, name: str, status: str = "todo", interval: str = "daily")->None:
        """Initialize a recurring task with a name, status and interval"""
        super().__init__( name, status)
        self.interval = interval

    def __repr__(self) -> str:
        return f"RecurringTask({self.name!r}, {self.status!r}, {self.interval!r})"

    def __str__(self) -> str:
        return f"RecurringTask({self.name}, {self.status}, {self.interval})"

class TimedTask(Task):
    """Represents a task with a specific deadline"""
    def __init__(self, name: str, status: str = "todo", deadline: datetime| None = None) -> None:
        super().__init__(name, status)
        self.deadline = deadline or datetime.now()

    def is_overdue(self) -> bool:
        """return True if the deadline has passed"""
        return datetime.now() > self.deadline

    def __repr__(self) -> str:
        return f"TimedTask({self.name!r}, {self.status!r}, {self.deadline!r})"

    def __str__(self) -> str:
        return f"TimedTask({self.name}, {self.status}, {self.deadline.isoformat()})"


def main() -> None:
    """Demonstrate the task hierarchy."""
    my_task = Task("C++", "Processing")
    my_recurring_task = RecurringTask("C", "Processing", "weekly")
    my_timed_task= TimedTask("Python", "Processing", datetime.now())

    for t in (my_task, my_recurring_task, my_timed_task):
        print(t)

    for t in (my_task, my_recurring_task, my_timed_task):
        t.mark_done()
        print(t)

if __name__ == "__main__":
    main()
