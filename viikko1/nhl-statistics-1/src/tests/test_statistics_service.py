import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_search(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)

    def test_search_none(self):
        player = self.stats.search("NotExist")
        self.assertIsNone(player)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in edm_players))

    def test_top(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4) 

    def test_player_string(self):
        player = Player("Semenko", "EDM", 4, 12)
        expected_string = "Semenko EDM 4 + 12 = 16"
        self.assertEqual(str(player), expected_string)