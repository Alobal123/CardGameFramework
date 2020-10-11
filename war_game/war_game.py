from card_game_framework.card import Card
from card_game_framework.zone import Zone
from war_game.rules import ChangeZonesEffect, WarRule
from card_game_framework.events import events_manager

class WarGame:

    @staticmethod
    def get_hand_zone_name(player_number):
        return f'hand_{player_number}'

    @staticmethod
    def get_discard_zone_name(player_number):
        return f'discard_pile_{player_number}'

    def __init__(self):
        self.zones = {}
        self._setup()

    def _setup(self, number_of_players: int = 2):
        self.number_of_players = number_of_players
        self._setup_zones()
        self._setup_players()
        self._setup_cards()
        self._setup_rules()

    def _setup_zones(self):
        def add_zone(name):
            self.zones[name] = Zone(name)

        for player_number in range(self.number_of_players):
            add_zone(self.get_hand_zone_name(player_number))
            add_zone(self.get_discard_zone_name(player_number))
        add_zone('battlefield')

    def _setup_players(self):
        pass

    def _setup_cards(self):
        for player_number in range(self.number_of_players):
            zone = self.zones[self.get_hand_zone_name(player_number)]
            for card_value in range(10):
                zone.append(Card(str(card_value),{'value':card_value}, zone=zone))

    def _setup_rules(self):
        events_manager.add_listener(WarRule(number_of_players=self.number_of_players))

    def __repr__(self):
        rt = []
        for name, zone in self.zones.items():
            rt.append(f'ZONE------------{name}-------------ZONE')
            if not zone:
                rt.append('ZONE EMPTY')
            for card in zone:
                rt.append(str(card))
        return '\n'.join(rt)
