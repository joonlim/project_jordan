# test

from nba_data_manager import data_manager as dm
import utils as utils

# Check if there is a date, stat, and secondary stat
# ex: ?date=2016-01-07&stat=AST&secondstat=PER
date = ""
stat = ""
stat2 = ""

# Default date and stat. secondstat defaults to None.
if date == "" or date is None:
    date = utils.days_before_today(1)  # Yesterday's date
if stat == "" or stat is None:
    stat = 'linear_PER'
if stat2 == "" or stat2 is None:
    stat2 = None

games = dm.get_player_games_on_date(date, "2015-16")  # TODO: season name

utils.sort_list_by_attribute(games, stat, stat2)

print(games)
