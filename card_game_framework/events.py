class Event:
    def __init__(self, event_name, *args, **kwargs):
        self.event_name = event_name
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f"EVENT {self.event_name} ({self.args},{self.kwargs})"


class EventsManager:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def notify(self, event: Event):
        for listener in self._listeners:
            listener.notify(event)


events_manager = EventsManager()


def event(func, events_manager=events_manager):
    def event_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        events_manager.notify(Event(func.__name__, *args, **kwargs))
        return result

    return event_wrapper
