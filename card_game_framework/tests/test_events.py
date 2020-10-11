from card_game_framework import events


@events.event
def event_with_args(fake_self, a: int, b: int):
    return a + b


@events.event
def event_with_kwargs(fake_self, a: int = 0, b: int = 0):
    return a + b


class EventListener:

    def notify(self, event):
        print(f"Event {event.event_name} called with {event.args} and {event.kwargs}")
        if event.event_name == 'event_with_kwargs':
            self.value = event.kwargs['a']


def test_events():
    consumer = EventListener()
    events.events_manager.add_listener(consumer)
    events.Event('basic_event')
    assert event_with_args(None, 1, 2) == 3
    assert event_with_kwargs(None, a=1, b=3) == 4
    assert consumer.value == 1
