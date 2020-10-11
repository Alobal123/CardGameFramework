from card_game_framework.effects import Effect
from card_game_framework.events import event, Event
from card_game_framework.zone import Zone


class ChangeZonesEffect(Effect):
    @event
    def apply(self, *, dest_zone: Zone =None):
        source_zone = self.card.zone
        source_zone.remove(self.card)
        self.card.zone = dest_zone
        dest_zone.append(self.card)
        self.card.remove_effect(self)


class WarRule(Effect):

    def __init__(self, number_of_players: int):
        super().__init__()
        self.number_of_players = number_of_players

    def notify(self, event: Event):

        if isinstance(event.args[0], ChangeZonesEffect):
            dest_zone = event.kwargs['dest_zone']
            if dest_zone.name == 'battlefield' and len(dest_zone) == self.number_of_players:
                self.apply(dest_zone)

    @event
    def apply(self, battlefield_zone: Zone):
        pass  # TODO
