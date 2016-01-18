from flask import render_template, url_for
from app import app
from flask import request

import app.utils as utils

from app.website_manager import website_manager as wm
from app.nba_data_manager import data_manager as dm
from app.user_manager import user_manager as um


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    """
    Home page
    """
    website = wm.info()
    page = wm.new_page("Home")

    # Fake user for now
    user = um.fake_user()

    player_ids = user['players']
    players = dm.get_players_by_id(player_ids)

    # Create rows of two players each for the website's home page.
    player_rows = utils.group_into_pairs(players)

    return render_template("index.html",
                           website=website,
                           page=page,
                           user=user,
                           player_rows=player_rows)


@app.route('/date')
@app.route('/date.html')
@app.route('/date_stats')
@app.route('/date_stats.html')
def date_stats():
    """
    Games of players who played on a given date.
    """
    website = wm.info()

    # Fake user for now
    user = um.fake_user()

    # Check if there is a date, stat, and secondary stat
    # ex: ?date=2016-01-07&stat=AST&secondstat=PER
    date = request.args.get('date')
    stat = request.args.get('stat')
    stat2 = request.args.get('stat2')

    # Default date and stat. secondstat defaults to None.
    if date == "" or date is None:
        date = utils.days_before_today(1)  # Yesterday's date
    if stat == "" or stat is None:
        stat = 'linear_PER'
    if stat2 == "" or stat2 is None:
        stat2 = None

    page = wm.new_page("Games on " + date)

    games = dm.get_player_games_on_date(date, "2015-16")  # TODO: season name

    utils.sort_list_by_attribute(games, stat, stat2)

    return render_template("date_stats.html",
                           website=website,
                           page=page,
                           user=user,
                           date=date,
                           stat=stat,
                           stat2=stat2,
                           games=games)


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
