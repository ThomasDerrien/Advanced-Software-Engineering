class DomainEvent:
    """
    Base class for all domain events.
    """
    def publish(self):
        """
        Publishes the event. Extend this to integrate with an event bus.
        """
        print(f"Event published: {self}")
