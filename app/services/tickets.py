from app.models.entities import Ticket
from app.models.enums import TicketStatus

class TicketService:
    def __init__(self):
        self._tickets = []
        self._next_id = 1

    def create(self, title: str, description: str, category: str, priority: str, requester_id: int) -> Ticket:
        ticket = Ticket(self._next_id, title, description, category, priority, requester_id)
        self._tickets.append(ticket)
        self._next_id += 1
        return ticket

    def assign_technician(self, ticket_id: int, technician_id: int) -> Ticket | None:
        for ticket in self._tickets:
            if ticket.id == ticket_id:
                ticket.assignee_id = technician_id
                return ticket
        return None

    def assign_technician(self, ticket_id: int, technician_id: int) -> Ticket | None:
        for ticket in self._tickets:
            if ticket.id == ticket_id:
                ticket.assignee_id = technician_id
                return ticket
        return None

    def list_by_technician(self, technician_id: int) -> list[Ticket]:
        return [ticket for ticket in self._tickets if ticket.assignee_id == technician_id]

    def list_by_category(self, category: str) -> list[Ticket]:
        return [ticket for ticket in self._tickets if ticket.category == category]

    def list_by_status(self, status: str | TicketStatus) -> list[Ticket]:
        target_status = status.value if isinstance(status, TicketStatus) else status
        return [
            ticket for ticket in self._tickets 
            if (ticket.status.value if isinstance(ticket.status, TicketStatus) else ticket.status).lower() == target_status.lower()
        ]