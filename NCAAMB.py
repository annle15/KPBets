from sportradar.api import API
import os


class NCAAMB(API):

    def __init__(self, api_key='mvychbfvhmngbatf8ba7pege', format_='json', language='en',
                 access_level='trial', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = 8
        self.prefix = f'ncaamb/{self.access_level}/v{self.version}/{self.language}/'


    def get_league_hierarchy(self):
        """get rankings for the entire league"""
        return self._make_request(f'{self.prefix}league/hierarchy')
    # Inside the NCAAMB class in NCAAMB.py
    def get_team_statistics(self, season_year, season_type, team_id):
        endpoint = f"{self.prefix}seasons/{season_year}/{season_type}/teams/{team_id}/statistics"
        return self._make_request(endpoint)



