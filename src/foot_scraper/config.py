class Config:

    """ Template Config 
    {
        "urls:[],
        #for the goalie and player table loc need to trial and error where the best table is in the Panda dataframe
        goalie_table_loc:"0",
        "player_table_loc": "0",
        "header_loc": "0",
        "tags_to_remove":[[tag,class value (treat this as a regex)]]
    }
    """
    @staticmethod
    def getConfigs():
        data = [
                {
                    "urls" :[
                        "http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                        "http://www.espn.com/soccer/team/squad/_/id/382/manchester%20city",
                        "http://www.espn.com/soccer/team/squad/_/id/364/liverpool",
                        "http://www.espn.com/soccer/team/squad/_/id/367/tottenham-hotspur",
                        "http://www.espn.com/soccer/team/squad/_/id/360/",
                        "http://www.espn.com/soccer/team/squad/_/id/363/",
                        "http://www.espn.com/soccer/team/squad/_/id/395/",
                        "http://www.espn.com/soccer/team/squad/_/id/380/",
                        "http://www.espn.com/soccer/team/squad/_/id/371/",
                        "http://www.espn.com/soccer/team/squad/_/id/368/",
                        "http://www.espn.com/soccer/team/squad/_/id/349/",
                        "http://www.espn.com/soccer/team/squad/_/id/380/",
                        "http://www.espn.com/soccer/team/squad/_/id/375/",
                        "http://www.espn.com/soccer/team/squad/_/id/384/",
                        "http://www.espn.com/soccer/team/squad/_/id/331/",
                        "http://www.espn.com/soccer/team/squad/_/id/379/",
                        "http://www.espn.com/soccer/team/squad/_/id/361/",
                        "http://www.espn.com/soccer/team/squad/_/id/347/",
                        "http://www.espn.com/soccer/team/squad/_/id/376/",
                        "http://www.espn.com/soccer/team/squad/_/id/370/",
                        "http://www.espn.com/soccer/team/squad/_/id/335/"
                    ],
                    "goalie_table_loc": "2", 
                    "player_table_loc": "8",
                    "header_loc": "0",
                    "tags_to_remove":[["span", "pl2"]]
                },
                {
                    "urls" : [
                        "https://fbref.com/en/squads/b8fd03ef/2018-2019/Manchester-City",
                        "https://fbref.com/en/squads/822bd0ba/2018-2019/Liverpool",
                        "https://fbref.com/en/squads/361ca564/2018-2019/Tottenham-Hotspur",
                        "https://fbref.com/en/squads/19538871/2018-2019/Manchester-United",
                        "https://fbref.com/en/squads/18bb7c10/2018-2019/Arsenal",
                        "https://fbref.com/en/squads/cff3d9bb/2018-2019/Chelsea",
                        "https://fbref.com/en/squads/2abfe087/2018-2019/Watford",
                        "https://fbref.com/en/squads/8cec06e1/2018-2019/Wolverhampton-Wanderers",
                        "https://fbref.com/en/squads/7c21e445/2018-2019/West-Ham-United",
                        "https://fbref.com/en/squads/4ba7cbea/2018-2019/Bournemouth",
                        "https://fbref.com/en/squads/d3fd31cc/2018-2019/Everton",
                        "https://fbref.com/en/squads/a2d435b3/2018-2019/Leicester-City",
                        "https://fbref.com/en/squads/47c64c55/2018-2019/Crystal-Palace",
                        "https://fbref.com/en/squads/943e8050/2018-2019/Burnley",
                        "https://fbref.com/en/squads/b2b47a98/2018-2019/Newcastle-United",
                        "https://fbref.com/en/squads/d07537b9/2018-2019/Brighton--Hove-Albion",
                        "https://fbref.com/en/squads/75fae011/2018-2019/Cardiff-City",
                        "https://fbref.com/en/squads/33c895d4/2018-2019/Southampton",
                        "https://fbref.com/en/squads/fd962109/2018-2019/Fulham",
                        "https://fbref.com/en/squads/f5922ca5/2018-2019/Huddersfield-Town"
                    ],
                    "goalie_table_loc": "0",
                    "player_table_loc": "0",
                    "header_loc": "1",
                    "tags_to_remove":[["span", "f-i f-*"]]
                }
                ]
        return data

