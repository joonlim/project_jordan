from app.nba_database import NBAMongoDB
import app.utils as utils
from app.static.teams import teams

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

    def get_player_by_name(self, name):
        """
        Given a player's full name, return a dict with information about the
        player with that name (ignore case).
        """
        player = self.db.get_player_by_name(name)
        if player is None:
            return

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

    def get_player_season_by_id(self, id, season):
        """
        Given a player id and a season (format: "2014-15"), return a dict with
        information all the games the player has played in the season.
        """
        player_season = self.db.get_player_season_by_id(id, season)

        # Format dict to be returned.
        player_season_info = self.__parse_player_season_info(player_season)
        return player_season_info

    def get_all_player_games_on_date(self, date, season):
        """
        Given a list of player ids, a date (format: "YYYY-MM-DD"), and the
        matching season, return a list of dicts that map a player's id to their
        game information on the given date.
        """
        seasons = self.db.get_seasons(season)

        # Create a dict of ids mapped to games of the given date.
        player_dict = dict()  # map id to game
        for s in seasons:
            games = s["games"]
            for game in games:
                if game["date"] == date:
                    id = s["_id"]
                    player_dict[id] = game

        player_games_on_date_list = list()
        for id in player_dict:
            # Format dicts to be returned.
            game = player_dict[id]
            player_game_info = self.__parse_game_stats(game)
            player_games_on_date_list.append({
                "_id": id,
                "game": player_game_info
            })

        return player_games_on_date_list

    def get_team_by_abbrev(self, abbrev):
        """
        Given a team abbreviation (format: "GSW"), return a dict with static
        team information, which includes the full name and colors.
        """
        abbrev_lower = abbrev.lower()
        return teams[abbrev_lower]

    def __format_headshot_img_file_path(self, name):
        """
        Given a player's name (format: "Firstname Lastname"), return the path
        of the player's headshot image.
        """
        headshot_img_file = self.__format_img_alt(name) + ".png"
        headshot_img_path = "img/player_headshots/" + headshot_img_file
        return headshot_img_path

    def __format_team_logo_img_file_path(self, name):
        """
        Given a team's full name (format: "City Name"), return the path of the
        team's logo image.
        """
        headshot_img_file = self.__format_img_alt(name) + ".png"
        headshot_img_path = "img/team_logos/" + headshot_img_file
        return headshot_img_path

    def __format_img_alt(self, name):
        """
        Given a player's name (format: "Firstname Lastname"), return an
        alternate name for any of the player's images.
        """
        alt = name.lower().replace(' ', '_').replace('.', '')\
            .replace("'", "")
        return alt

    def __parse_game_stats(self, game_doc):
        """
        Given a player_info dict and game document, create a dict representing
        the player stats of the game to be returned to the client.

        game_doc format:

        {
            "id": String,
            "date": String,
            "home": String,
            "away": String,
            "winner": String,
            "statistics": {
                "min": Integer,
                "fgm": Integer,
                "fga": Integer,
                "fg_pct": Float,
                "fg3m": Integer,
                "fg3a": Integer,
                "fg3_pct": Float,
                "ftm": Integer,
                "fta": Integer,
                "ft_pct": Float,
                "oreb": Integer,
                "dreb": Integer,
                "reb": Integer,
                "ast": Integer,
                "stl": Integer,
                "blk": Integer,
                "tov": Integer,
                "pf": Integer,
                "pts": Integer,
                "plus_minus": Integer,
                "linear_PER": Float
            }
        }
        """
        home = game_doc.get("home", "NOT A GAME")
        if home != "NOT A GAME":
            date = game_doc["date"].replace("-", "/")
            formatted_date = date[5:] + "/" + date[:4]
            home = game_doc["home"]
            away = game_doc["away"]
            matchup = away + " @ " + home
            winner = game_doc["winner"]
            if winner == "Undecided":
                wl = "Ongoing"
            else:
                wl = "W" if home == winner else "L"

            stats = game_doc["statistics"]
        else:
            formatted_date = ""
            matchup = ""
            wl = ""

            stats = game_doc

        fgm = stats["fgm"]
        fga = stats["fga"]
        fg_pct = utils.ratio_string(fgm, fga, 3)
        fg3m = stats["fg3m"]
        fg3a = stats["fg3a"]
        fg3_pct = utils.ratio_string(fg3m, fg3a, 3)
        ftm = stats["ftm"]
        fta = stats["fta"]
        ft_pct = utils.ratio_string(ftm, fta, 3)

        return {
            "date": formatted_date,
            "matchup": matchup,
            "wl": wl,
            "min": stats["min"],
            "fgm": fgm,
            "fga": fga,
            "fg_pct": fg_pct,
            "fg3m": fg3m,
            "fg3a": fg3a,
            "fg3_pct": fg3_pct,
            "ftm": ftm,
            "fta": fta,
            "ft_pct": ft_pct,
            "dreb": stats["dreb"],
            "oreb": stats["oreb"],
            "reb": stats["reb"],
            "ast": stats["ast"],
            "stl": stats["stl"],
            "blk": stats["blk"],
            "tov": stats["tov"],
            "pf": stats["pf"],
            "pts": stats["pts"],
            "plus_minus": stats["plus_minus"],
            "per": stats["linear_PER"]
        }

    def __parse_player_season_info(self, player_season_doc):
        """
        Given a player season document, create a dict representing information
        information of the season.
        create a dict representing

        season_doc format:

        document = {
            "_id": Integer,
            "last_updated": String,
            "games": game_doc list,
            "total": game_doc,
            "average": game_doc
        }

        game_doc format:

        {
            "id": String,
            "date": String,
            "home": String,
            "away": String,
            "winner": String,
            "statistics": {
                "min": Integer,
                "fgm": Integer,
                "fga": Integer,
                "fg_pct": Float,
                "fg3m": Integer,
                "fg3a": Integer,
                "fg3_pct": Float,
                "ftm": Integer,
                "fta": Integer,
                "ft_pct": Float,
                "oreb": Integer,
                "dreb": Integer,
                "reb": Integer,
                "ast": Integer,
                "stl": Integer,
                "blk": Integer,
                "tov": Integer,
                "pf": Integer,
                "pts": Integer,
                "plus_minus": Integer,
                "linear_PER": Float
            }
        }
        """

        games = list()
        for game in player_season_doc['games']:
            game_stats = self.__parse_game_stats(game)
            games.append(game_stats)

        total = self.__parse_game_stats(player_season_doc['total'])
        average = self.__parse_game_stats(player_season_doc['average'])

        return {
            "_id": player_season_doc['_id'],
            "games": games,
            "total": total,
            "average": average
        }

    def __parse_player_info(self, player_doc):
        """
        Given a player document, create a dict representing player information
        to be returned to the client.

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
