import unittest
from datetime import datetime

from puckdb import filters


class TestGameFilter(unittest.TestCase):
    def test_one_season_range(self):
        from_date = datetime(2014, 10, 22)
        to_date = datetime(2015, 4, 1)
        game_filter = filters.GameFilter(from_date=from_date, to_date=to_date)
        seasons = game_filter.by_season()
        self.assertEqual(1, len(seasons))
        self.assertEqual('20142015', seasons[0])

    def test_season_before_range(self):
        from_date = datetime(2014, 4, 22)
        to_date = datetime(2015, 4, 1)
        game_filter = filters.GameFilter(from_date=from_date, to_date=to_date)
        seasons = game_filter.by_season()
        self.assertEqual(2, len(seasons))
        self.assertEqual('20132014', seasons[0])
        self.assertEqual('20142015', seasons[1])

    def test_season_after_range(self):
        from_date = datetime(2014, 10, 22)
        to_date = datetime(2015, 9, 1)
        game_filter = filters.GameFilter(from_date=from_date, to_date=to_date)
        seasons = game_filter.by_season()
        self.assertEqual(2, len(seasons))
        self.assertEqual('20142015', seasons[0])
        self.assertEqual('20152016', seasons[1])
