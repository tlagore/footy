class Config:
    @staticmethod
    def getConfigs():
        data = [
                {
                    "url": "http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1",
                    "tables": 
                    [
                        {
                        "table_definition":{
                            "table_name": "goalkeepers",
                            "row_definition": {
                                "key_name": "name",
                                "column_definition": {
                                    "data_description": {
                                        "POS":"position",
                                        "NO":"number",
                                        "NAME":"name",
                                        "AGE":"age",
                                        "APP":"appearances",
                                        "SUBIN":"substitutions" ,
                                        "S":"saves",
                                        "GC":"goals_against",
                                        "A":"assists",
                                        "FC":"fouls",
                                        "FA":"fouls_against",
                                        "YC":"yellow_cards",
                                        "RC":"red_cards"
                                    },
                                    "specific_table":[
                                        ["section", {"class": "Table2__responsiveTable Table2__table-outer-wrap --align-headers goalkeepers"}]],
                                    "player_data":[ 
                                        ["span", "class"]],
                                    "player_details":[
                                        ["a", {"href" : "http://www.espnfc.com/player/"}]]
                                    }
                                }
                            }
                        },
                        {
                        "table_definition":{
                            "table_name": "players",
                            "row_definition": {
                                "key_name": "name",
                                "column_definition": {
                                    "data_description": {
                                        "POS":"position",
                                        "NO":"number",
                                        "NAME":"name",
                                        "AGE":"age",
                                        "APP":"appearances",
                                        "SUBIN":"substitutions" ,
                                        "S":"saves",
                                        "GC":"goals_against",
                                        "A":"assists",
                                        "FC":"fouls",
                                        "FA":"fouls_against",
                                        "YC":"yellow_cards",
                                        "RC":"red_cards"
                                    },
                                    "specific_table":[
                                        ["section", {"class": "Table2__responsiveTable Table2__table-outer-wrap --align-headers outfield players"}]],
                                    "player_data":[ 
                                        ["span", "class"]],
                                    "player_details":[
                                        ["a", {"href" : "http://www.espnfc.com/player/"}]]
                                    }
                                }
                            }
                        }
                    ]
                }
            ]
        return data

