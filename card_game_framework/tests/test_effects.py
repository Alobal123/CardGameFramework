import pytest

from card_game_framework.card import Card
from card_game_framework.effects import AddStatEffect
from card_game_framework.events import events_manager


@pytest.fixture()
def setup_card(request):
    card = Card('card1')
    effect = AddStatEffect()
    card.add_effect(effect)
    return card, effect


def test_effect(setup_card):
    card, effect = setup_card
    effect.apply(stat_name='color', stat_value='diamond')
    effect.apply(stat_name='value', stat_value=9)
    card.remove_effect(effect)
    assert card.stats['color'] == 'diamond'
    assert card.stats['value'] == 9
    assert len(card.stats) == 2


def test_effect_as_event(setup_card):
    card, effect = setup_card

    class EventListener:
        def notify(self, event):
            if isinstance(event.args[0], AddStatEffect):
                self.color = event.kwargs['stat_value']

    listener = EventListener()
    events_manager.add_listener(listener)
    effect.apply(stat_name='color', stat_value='diamond')
    assert listener.color == 'diamond'
