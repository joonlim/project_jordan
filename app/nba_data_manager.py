from random import shuffle
from app.nba_database import NBAMongoDB

HOST = "23.23.23.23"
PORT = 27017


class NBADataManager:
    """
    Manages the data of all the players, player seasons, teams, games, etc.

    Attributes:
        db          The NBADatabase object.
    """
    def __init__(self):
        self.db = NBAMongoDB(HOST, PORT)

    def get_player_by_id(self, id):
        """
        Given a player id, return a dict with information about the player with
        that id.
        """
        player = self.db.get_player_by_id(id)

        # Format dict to be returned.
        player_info = self.__parse_player_info(player)
        return player_info

    def get_players_by_id(self, ids):
        """
        Given a list of player ids, return a list of dicts with information
        about the players with those ids.
        """
        players_info_list = list()
        for id in ids:
            # Format dict to be returned.
            player_info = self.get_player_by_id(id)
            players_info_list.append(player_info)

        return players_info_list

    def __format_headshot_img_file_path(self, name):
        """
        Given a player's name (format: Firstname Lastname), return the path
        of the player's headshot image.
        """
        headshot_img_file = self.__format_img_alt(name) + ".png"
        headshot_img_path = "img/player_headshots/" + headshot_img_file
        return headshot_img_path

    def __format_img_alt(self, name):
        """
        Given a player's name (format: Firstname Lastname), return an alternate
        name for any of the player's images.
        """
        alt = name.lower().replace(' ', '_').replace('.', '')\
            .replace("'", "")
        return alt

    def __parse_player_info(self, player_doc):
        """
        Given a player document, create a dict representing player information
        to be returned to a client.

        player_doc format:

        {
            "_id": Integer,
            "last_updated": String,
            "first_name": String,
            "last_name": String,
            "birthdate": String,
            "school": String,
            "country": String,
            "height": String,
            "weight": String,
            "jersey": String,
            "position": String,
            "roster_status": String,
            "team": {
                "name": String,
                "city": String,
                "abbrev": String
            },
            "from_year": Integer,
            "to_year": Integer,
            "played_this_season": Boolean
        }
        """

        name = player_doc['first_name'] + " " + player_doc['last_name']
        link = name.replace(' ', '_')
        headshot_img_path = self.__format_headshot_img_file_path(name)
        headshot_img_alt = self.__format_img_alt(name)

        return {
            "_id": player_doc['_id'],
            "link": link,
            "name": name,
            "headshot_img": {
                "path": headshot_img_path,
                "alt": headshot_img_alt
            },
            "birthdate": player_doc['birthdate'],
            "school": player_doc['school'],
            "country": player_doc['country'],
            "height": player_doc['height'],
            "weight": player_doc['weight'],
            "jersey": player_doc['jersey'],
            "position": player_doc['position'],
            "team": player_doc['team'],
            "from_year": player_doc['from_year'],
            "to_year": player_doc['to_year'],
        }


data_manager = NBADataManager()
