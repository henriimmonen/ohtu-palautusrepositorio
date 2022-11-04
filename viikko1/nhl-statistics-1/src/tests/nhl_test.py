import unittest
from statistics import Statistics, SortBy
from player import Player

class playerReaderStub():
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(playerReaderStub())
    
    def test_setUp(self):
        kurri = self.statistics.search('Kurri')
        self.assertEqual(kurri.name, 'Kurri')

    def test_search_by_team(self):
        detroit = self.statistics.team('DET')
        self.assertEqual(detroit[0].name, 'Yzerman')

    def test_top_points(self):
        top_player = self.statistics.top(1, SortBy.POINTS)
        self.assertEqual(top_player[0].name, 'Gretzky')

    def test_not_found(self):
        player = self.statistics.search('Väyrynen')
        self.assertIsNone(player)

    def test_top_goals(self):
        top_goals = self.statistics.top(1, SortBy.GOALS)
        self.assertEqual(top_goals[0].name, 'Lemieux')

    def test_top_assists(self):
        top_goals = self.statistics.top(1, SortBy.ASSISTS)
        self.assertEqual(top_goals[0].name, 'Gretzky')