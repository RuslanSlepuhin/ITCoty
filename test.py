import asyncio

from sites.scraping_epam_anywhere import EpamGetInformation
from sites.scraping_hh import HHGetInformation
from sites.scraping_hhkz import HHKzGetInformation
from sites.scraping_ingamejob import IngameJobGetInformation
from sites.scraping_careerjet import СareerjetGetInformation

sparser = СareerjetGetInformation()
asyncio.run(sparser.get_content())


