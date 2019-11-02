import unittest, pywikibot, mwparserfromhell
from ..library.SearchEngine import SearchEngine

class SearchEngineTest(unittest.TestCase):

    # def setUp(self):
    #     self.se = SearchEngine()
    #     pass


    def test_getByCategory(self):
        self.se = SearchEngine()
        pages = self.se.getByCategory('1985_video_games')
        titles = []
        for page in pages:
            titles.append(page.title())
        
        assert len(titles) > 0
        print(f"\npages found: {len(titles)}")
        pass