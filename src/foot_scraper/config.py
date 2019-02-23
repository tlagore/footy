class Config:
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
                    #these locations are for getting the most accurate table as some of them seem to be garbage
                    "goalie_table_loc": "2", 
                    "player_table_loc": "8",
                    "header_loc": "0",
                    #Key: tag, Value:class
                    "tags_to_remove":[
                            ["span", {"class" : "pl2"}]
                    ]
                },
                {
                    "urls" : [
                        "https://fbref.com/en/squads/b8fd03ef/2018-2019/Manchester-City"
                    ],
                    "goalie_table_loc": "0",
                    "player_table_loc": "0",
                    "header_loc": "1",
                    "tags_to_remove":[

                    ]

                }
                ]
        return data

