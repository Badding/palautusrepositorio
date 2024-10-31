import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.service = StatisticsService(PlayerReaderStub())
    
    def test_search_found(self):
        player = self.service.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_not_found(self):
        player = self.service.search("Badding")
        self.assertIsNone(player)
    
    def test_filter_by_team(self):
        players = self.service.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")
    
    # test with no sortBy parameter (default is SortBy.POINTS)
    def test_top(self):
        players = self.service.top(2)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
    
    def test_top_by_goals(self):
        players = self.service.top(4, SortBy.GOALS)
        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")
        self.assertEqual(players[3].name, "Gretzky")
        self.assertEqual(players[4].name, "Semenko")

    def test_top_by_assists(self):
        players = self.service.top(4, SortBy.ASSISTS)
        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")
        self.assertEqual(players[3].name, "Kurri")
        self.assertEqual(players[4].name, "Semenko")

    def test_top_by_points(self):
        players = self.service.top(4, SortBy.POINTS)
        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")
        self.assertEqual(players[4].name, "Semenko")
