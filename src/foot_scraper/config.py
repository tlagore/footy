class Config:
    @staticmethod
    def getConfigs():
        data = [
                {
                    "urls" :[
                        "http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                        "http://www.espn.com/soccer/team/squad/_/id/382/manchester%20city",
                        "http://www.espn.com/soccer/team/squad/_/id/364/liverpool",
                        "http://www.espn.com/soccer/team/squad/_/id/367/tottenham-hotspur"
                    ],
                    "goalie_table_loc": "2",
                    "player_table_loc": "8",
                    "header_loc": "0",
                    "footer_loc": "0"
                },
                {
                    "urls" : [
                        "https://fbref.com/en/squads/b8fd03ef/2018-2019/Manchester-City"
                    ],
                    "goalie_table_loc": "0",
                    "player_table_loc": "0",
                    "header_loc": "0",
                    "footer_loc": "1"
                }
                ]
        return data

