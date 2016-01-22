from flask import render_template, url_for
from app import app
from flask import request

import app.utils as utils
import app.nba_utils as nba

from app.website_manager import website_manager as wm
from app.nba_data_manager import data_manager as dm
from app.user_manager import user_manager as um

# Order of buttons on navigation bar.
SEASON = 0
DAILY = 1
COMPARE = 2

CURRENT_SEASON = "2015-16"


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    """
    Home page
    """
    website = wm.info()
    page = wm.new_page("Home")
    navbar = wm.nav_bar_pages()

    # Fake user for now
    user = um.fake_user()

    player_ids = user['players']
    players = dm.get_players_by_id(player_ids)

    # Create rows of two players each for the website's home page.
    player_rows = utils.group_into_pairs(players)

    return render_template("index.html",
                           website=website,
                           page=page,
                           navbar=navbar,
                           user=user,
                           player_rows=player_rows)


@app.route('/date')
@app.route('/date.html')
@app.route('/daily')
@app.route('/daily.html')
def daily():
    """
    Games of players who played on a given date.
    """
    website = wm.info()
    navbar = wm.nav_bar_pages(DAILY)

    # Fake user for now
    user = um.fake_user()

    # Check if there is a date, stat, and secondary stat
    # ex: ?date=2016-01-07&stat=AST&secondstat=PER
    date = request.args.get('date')
    stat = request.args.get('stat')
    stat2 = request.args.get('stat2')

    # Default date and stat. secondstat defaults to None.
    if not utils.is_valid_date(date, "-"):
        date = utils.days_before_today(1, "%m-%d-%Y")  # Yesterday's date

    stat = nba.parse_stat(stat, "per")   # If stat is incorrect form or empty, it defaults to per.
    stat2 = nba.parse_stat(stat2, None)  # If stat is incorrect form or empty, it defaults to None.

    page = wm.new_page("Games on " + date.replace("-", "/"))

    # Format date to YYYY-MM-DD
    formatted_date = date[6:] + "-" + date[:5]
    games_maps_list = dm.get_all_player_games_on_date(formatted_date, CURRENT_SEASON)  # TODO: season name

    if stat2 is not None:
        games_maps_list.sort(key=lambda x: (x['game'][stat], x['game'][stat2]), reverse=True)
    else:
        games_maps_list.sort(key=lambda x: x['game'][stat], reverse=True)

    top_players = list()
    num_top_players = len(games_maps_list) if len(games_maps_list) <= 2 else 3
    if num_top_players != 0:
        top_div = 12 // num_top_players
    else:
        top_div = 0

    players = list()
    for i in range(len(games_maps_list)):
        player = dm.get_player_by_id(games_maps_list[i]['_id'])
        game = games_maps_list[i]['game']
        players.append({
            "player": player,
            "game": game
        })
        if i < 3:
            top_players.append(players[i])

    chosen_stat = nba.format_category(stat)

    return render_template("daily.html",
                           website=website,
                           page=page,
                           navbar=navbar,
                           user=user,
                           date=date,
                           stat=stat,
                           stat2=stat2,
                           chosen_stat=chosen_stat,
                           top_players=top_players,
                           players=players,
                           top_div=top_div)


@app.route('/compare')
@app.route('/compare.html')
def compare():
    """
    Compare two players in a given date range.
    """
    website = wm.info()
    navbar = wm.nav_bar_pages(COMPARE)
    page = wm.new_page("Compare Players")

    # Fake user for now
    user = um.fake_user()

    # Check if there is a start, end, player1, and player2
    start = request.args.get('start')
    end = request.args.get('end')
    player1 = request.args.get('player1')
    player2 = request.args.get('player2')

    # Default date and stat. secondstat defaults to None.
    if not utils.is_valid_date(start, "-"):
        start = utils.days_before_today(2, "%m-%d-%Y")  # Two days before today
    if not utils.is_valid_date(end, "-"):
        end = utils.days_before_today(1, "%m-%d-%Y")  # Yesterday's date

    # TODO LOGIC, by game or by week, etc

    return render_template("compare.html",
                           website=website,
                           page=page,
                           navbar=navbar,
                           user=user,
                           start=start,
                           end=end,
                           player1=player1,
                           player2=player2)


@app.route('/player')
@app.route('/player.html')
@app.route('/players')
@app.route('/players.html')
def player():
    """
    Display information on a specific player.
    """
    website = wm.info()
    navbar = wm.nav_bar_pages()

    # Fake user for now
    user = um.fake_user()

    # Check if there is a player name
    name = request.args.get('name')

    if name is not None:
        name = name.replace('_', " ")
        name = name.replace('+', " ")
        player = dm.get_player_by_name(name)
        if player is not None:
            team = dm.get_team_by_abbrev(player['team']['abbrev'])
            page = wm.new_page(player['name'])
            season = dm.get_player_season_by_id(player['_id'], CURRENT_SEASON)
        else:
            team = None
            season = None
            page = wm.new_page("Players")
    else:
        player = None
        team = None
        season = None
        page = wm.new_page("Players")

    # TODO LOGIC, by game or by week, etc

    return render_template("player.html",
                           website=website,
                           page=page,
                           user=user,
                           navbar=navbar,
                           player=player,
                           team=team,
                           season=season)


@app.route('/team')
@app.route('/team.html')
@app.route('/teams')
@app.route('/teams.html')
def team():
    """
    Display information on a specific team.
    """
    website = wm.info()
    navbar = wm.nav_bar_pages()

    # Fake user for now
    user = um.fake_user()

    # Check if there is a team name abbreviation
    abbrev = request.args.get('name')

    if abbrev is not None:
        abbrev = abbrev.replace('_', " ")
        abbrev = abbrev.replace('+', " ")
        team = dm.get_team_by_abbrev(abbrev)
        page = wm.new_page(team['city'] + " " + team['name'])
    else:
        team = None
        page = wm.new_page("Teams")

    return render_template("team.html",
                           website=website,
                           page=page,
                           user=user,
                           navbar=navbar,
                           team=team)

# @app.route('/season_stats')
# @app.route('/season_stats.html')
# def season_stats():
#     user = {
#         'nickname': 'Joon',
#         'password': 'monkey'
#     }
#     local_banners = banners[:]

#     shuffle(local_banners)
#     first_banner = local_banners.pop(0)

#     return render_template("season_stats.html",
#                            user=user,
#                            title='Seasonal Stats',
#                            first_banner=first_banner,
#                            banners=local_banners)


# @app.route('/date')
# @app.route('/date.html')
# @app.route('/games_on_date')
# @app.route('/games_on_date.html')
# def game_stats():
#     user = {
#         'nickname': 'Joon',
#         'password': 'monkey'
#     }
#     local_banners = banners[:]

#     shuffle(local_banners)
#     first_banner = local_banners.pop(0)



#     sorted_players = nba_rank.rank_players_on_date(date, stat, secondstat)
#     # optimize
#     sorted_players = sorted_players.reverse()

#     table_header = {
#         "name": "NAME",
#         "matchup": "MATCHUP",
#         "team": "TEAM",
#         "wl": "W/L",
#         "min": "MIN",
#         "fgm": "FGM",
#         "fga": "FGA",
#         "fg_pct": "FG%",
#         "fg3m": "3PM",
#         "fg3a": "3PA",
#         "fg3_pct": "3P%",
#         "ftm": "FTM",
#         "fta": "FTA",
#         "ft_pct": "FT%",
#         "dreb": "DREB",
#         "oreb": "OREB",
#         "reb": "REB",
#         "ast": "AST",
#         "stl": "STL",
#         "blk": "BL",
#         "tov": "TOV",
#         "pf": "PF",
#         "pts": "PTS",
#         "plus_minus": "+/-",
#         "linear_PER": "PER"
#     }

#     return render_template("game_stats.html",
#                            user=user,
#                            title='Home',
#                            first_banner=first_banner,
#                            banners=local_banners,
#                            table_header=table_header,
#                            table_rows=sorted_players)




# @app.route('/game_stats')
# @app.route('/game_stats.html')
# def game_stats():
#     # Check if there is a date, stat, and secondary stat
#     # ex: ?date=2016-01-07&stat=AST&secondstat=PER
#     # date = request.args.get('date')
#     # stat = request.args.get('stat')
#     # secondstat = request.args.get('secondstat')

#     local_banners = banners[:]

#     shuffle(local_banners)
#     first_banner = local_banners.pop(0)

#     return render_template("game_stats.html",
#                            title='Game Stats',
#                            first_banner=first_banner,
#                            banners=local_banners)
