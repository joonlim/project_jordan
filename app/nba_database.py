from pymongo import MongoClient

DB_NAME = 'nba_db'
PLAYERS_COL = 'players'  # nba_db.players collection
TEAMS_COL = 'teams'
CURRENT_SEASON = "2015-16"  # nba_db.2015-16 collection and current season


class NBADatabase:
    """
    Interface that describes the methods of an NBADatabase.
    """
    def get_players(self):
        """
        Return a list of players.
        """
        return

    def get_seasons(self, season):
        """
        Given a season (ex: "2015-16"), return a list of seasons of each
        player.
        """
        return

    def get_teams(self):
        """
        Return a list of teams.
        """
        return

    def get_player_by_id(self, id):
        """
        Given a player id, return the player with that id.
        """
        return

    def get_player_by_name(self, full_name):
        """
        Given a player's full name, return the player with that name.
        """
        return


class NBAMongoDB(NBADatabase):
    """
    An NBADatabase Implementation that uses a MongoDB database.

    Attributes:
        db          The MongoDB database created from a MongoClient.
    """
    def __init__(self, host, port):
        client = MongoClient(host, port)
        self.db = client[DB_NAME]

    def get_players(self):
        """
        Return a list of players.
        """
        players_collection = self.db[PLAYERS_COL]
        return players_collection

    def get_seasons(self, season):
        """
        Given a season (ex: "2015-16"), return a list of seasons of each
        player.
        """
        # TODO: change db name to "2015_16"
        season_col_name = "season" + season
        season_collection = self.db[season_col_name]
        return season_collection

    def get_player_by_id(self, id):
        """
        Given a player id, return the player with that id.
        """
        players_collection = self.get_players()
        player = players_collection.find({"_id": id})[0]
        return player
