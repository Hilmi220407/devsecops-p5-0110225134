class Task:
    def __init__(self, task_id, title, done=False):
        self.task_id = task_id
        self.title = title
        self.done = done

    def to_dict(self):
        return {"id": self.task_id, "title": self.title, "done": self.done}

    def mark_done(self):
        self.done = True