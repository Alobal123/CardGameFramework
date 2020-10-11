from war_game.war_game import WarGame
from war_game.rules import ChangeZonesEffect

def test_war_game_setup():
    game = WarGame()
    assert game.number_of_players == 2
    #print(game)


def test_war_rule():
    game = WarGame()
    for i in range(game.number_of_players):
        card = WarGame().zones[WarGame.get_hand_zone_name(i)][i]
        eff = ChangeZonesEffect()
        card.add_effect(eff)
        eff.apply(dest_zone=game.zones['battlefield'])

