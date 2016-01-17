from random import shuffle


class NBADataManager:
    def sample_team(self):
        sample_team = {
            "players": [
                {
                    "name": "Stephen Curry",
                    "link": "/Stephen_Curry",
                    "img_path": "img/players/Stephen_Curry.png",
                    "img_alt": "stephen-curry"
                },
                {
                    "name": "Draymond Green",
                    "link": "/Draymond_Green",
                    "img_path": "img/players/Draymond_Green.png",
                    "img_alt": "draymond-green"
                },
                {
                    "name": "Hassan Whiteside",
                    "link": "/Hassan Whiteside",
                    "img_path": "img/players/Hassan_Whiteside.png",
                    "img_alt": "hassan-whiteside"
                },
                {
                    "name": "Andrew Wiggins",
                    "link": "/Andrew_Wiggins",
                    "img_path": "img/players/Andrew_Wiggins.png",
                    "img_alt": "andrew-wiggins"
                },
                {
                    "name": "Isaiah Thomas",
                    "link": "/Isaiah_Thomas",
                    "img_path": "img/players/Isaiah_Thomas.png",
                    "img_alt": "isaiah-thomas"
                },
                {
                    "name": "DeMar Derozan",
                    "link": "/DeMar_Derozan",
                    "img_path": "img/players/DeMar_Derozan.png",
                    "img_alt": "demar-derozan"
                },
                {
                    "name": "Dirk Nowitzki",
                    "link": "/Dirk_Nowitzki",
                    "img_path": "img/players/Dirk_Nowitzki.png",
                    "img_alt": "dirk-nowitzki"
                },
                {
                    "name": "C.J. McCollum",
                    "link": "/CJ_McCollum",
                    "img_path": "img/players/CJ_McCollum.png",
                    "img_alt": "cj-mccollum"
                },
                {
                    "name": "Thaddeus Young",
                    "link": "/Thaddeus_Young",
                    "img_path": "img/players/Thaddeus_Young.png",
                    "img_alt": "thaddeus-young"
                },
                {
                    "name": "Marcin Gortat",
                    "link": "/Marcin_Gortat",
                    "img_path": "img/players/Marcin_Gortat.png",
                    "img_alt": "marcin-gortat"
                },
                {
                    "name": "Deron Williams",
                    "link": "/Deron_Williams",
                    "img_path": "img/players/Deron_Williams.png",
                    "img_alt": "deron-williams"
                },
                {
                    "name": "Joakim Noah",
                    "link": "/Joakim_Noah",
                    "img_path": "img/players/Joakim_Noah.png",
                    "img_alt": "joakim-noah"
                },
                {
                    "name": "Kristaps Porzingis",
                    "link": "/Kristaps_Porzingis",
                    "img_path": "img/players/Kristaps_Porzingis.png",
                    "img_alt": "kristaps-porzingis"
                },
            ]
        }
        shuffle(sample_team['players'])
        return sample_team


data_manager = NBADataManager()
