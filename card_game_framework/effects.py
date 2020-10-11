from card_game_framework.events import event, Event


class Effect:
    card: 'Card' = None

    def apply(self, *args, **kwargs):
        raise NotImplemented

    def notify(self, event: Event):
        raise NotImplemented


class AddStatEffect(Effect):
    @event
    def apply(self, *, stat_name: str, stat_value):
        self.card.add_stat(stat_name, stat_value)


