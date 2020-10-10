import events_manager


@events_manager.event
def basic_event():
    pass


@events_manager.event
def event_with_args(a: int, b: int):
    return a + b


@events_manager.event
def event_with_kwargs(a: int = 0, b: int = 0):
    return a + b


class EventListener:

    def notify(self, event):
        print(f"Event {event.event_name} called with {event.args} and {event.kwargs}")
        if event.event_name == 'event_with_kwargs':
            self.value = event.kwargs['a']

def test_events():
    consumer = EventListener()
    events_manager.events_manager.add_listener(consumer)
    basic_event()
    assert event_with_args(1, 2) == 3
    assert event_with_kwargs(a=1, b=3) == 4
    assert consumer.value == 1