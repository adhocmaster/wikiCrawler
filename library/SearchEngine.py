import pywikibot


class SearchEngine:


    def __init__(self, site='wikipedia', lang='en'):
        """[summary]
        
        Keyword Arguments:
            site {optional, url} -- pass url if site is other than wikipedia (default: {None})
        """
           
        self.lang = lang
        self.site = site
        self.source = pywikibot.Site(lange, site)     

        pass


    def search(self, keywords):
        return None

    

