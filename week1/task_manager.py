"""A module that defines a basic task hierarchy """
from datetime import datetime
class Task:
    """Represent a simple task with a name and status"""
    def __init__(self, name: str, status: str):
        """Initialize attributes"""
        self.name = name
        self.status = status

    def mark_done(self):
        """Update the status to done"""
        self.status = "done"

    def __str__(self):
        return f"Task({self.name}, {self.status})"


class RecurringTask(Task):
    """Initialize by calling super"""
    def __init__(self, name: str, status: str, interval: str):
        """Initialize"""
        super().__init__( name, status)
        self.interval = interval

    def __str__(self):
        return f"RecurringTask({self.name}, {self.status}, {self.interval})"

class TimedTask(Task):
    """a timed task class"""
    def __init__(self, name: str, status: str, deadline: datetime):
        super().__init__(name, status)
        self.deadline = deadline

    def __str__(self):
        return f"Task({self.name}, {self.status}, {self.deadline.isoformat()})"


def main():
    """Entry point"""
    my_task = Task("C++", "Processing")
    print(my_task)
    my_recurring_task = RecurringTask("C", "Processing", "weekly")
    print(my_recurring_task)
    my_timed_task= TimedTask("Python", "Processing", datetime.now())
    print(my_timed_task)
    my_task.mark_done()
    my_recurring_task.mark_done()
    my_timed_task.mark_done()
    print(my_task)
    print(my_recurring_task)
    print(my_timed_task)

if __name__ == "__main__":
    main()
