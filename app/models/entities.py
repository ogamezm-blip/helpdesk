class Ticket:
    def __init__(self, id: int, title: str, description: str, category: str, priority: str, requester_id: int):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.requester_id = requester_id
        self.assignee_id = None
        self.status = "open"