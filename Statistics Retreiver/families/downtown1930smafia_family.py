from __future__ import absolute_import, division, unicode_literals

from pywikibot import family
from pywikibot.tools import deprecated

class Family(family.Family):
    name = 'downtown1930smafia'  # Your chosen family name

    langs = {
        'en': 'downtown1930smafia.fandom.com',
    }

    def scriptpath(self, code):
        return {
            'en': '',
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return '1.39.3'

    def protocol(self, code):
        return 'https'
