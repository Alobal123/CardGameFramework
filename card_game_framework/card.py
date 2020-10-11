from typing import Dict

from card_game_framework.effects import Effect
from card_game_framework.zone import Zone

repr_template = \
"""Card {name}:
in zone: {zone}
stats:
{stats}"""


class Card:

    def __init__(self, name: str, stats: Dict = None, zone: Zone = None):
        self.name = name
        self.stats = stats if stats else {}
        self.zone = zone
        self._effects = []

    def add_effect(self, effect: Effect):
        effect.card = self
        self._effects.append(effect)

    def remove_effect(self, effect: Effect):
        effect.card = None
        self._effects.remove(effect)

    def add_stat(self, stat_name: str, stat_value):
        self.stats[stat_name] = stat_value

    def __repr__(self):
        return repr_template.format(name=self.name, zone=self.zone.name, stats=self.stats)
