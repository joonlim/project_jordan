"""
Utility functions related to NBA data.
"""


def format_category(stat):
    """
    Format a category string displayed on the client.
    """
    format_dict = {
        "min": "PTS",
        "fgm": "FGM",
        "fga": "FGA",
        "fg_pct": "FG%",
        "fg3m": "3PM",
        "fg3a": "3PA",
        "fg3_pct": "3P%",
        "ftm": "FTM",
        "fta": "FTA",
        "ft_pct": "FT%",
        "dreb": "DREB",
        "oreb": "DREB",
        "reb": "REB",
        "ast": "AST",
        "stl": "STL",
        "blk": "BLK",
        "tov": "TOV",
        "pf": "PF",
        "pts": "PTS",
        "plus_minus": "+/-",
        "per": "PER"
    }
    return format_dict[stat]


def parse_stat(stat, default):
    if type(stat) is not str:
        return default

    stat = stat.lower()

    switch = {
        "min": "min",
        "minutes": "min",
        "minute": "min",

        "fgm": "fgm",

        "fga": "fga",

        "fg_pct": "fg_pct",
        "fgpct": "fg_pct",
        "fg%": "fg_pct",

        "fg3m": "fg3m",
        "3pm": "fg3m",

        "fg3a": "fg3a",
        "3pa": "fg3a",

        "fg3_pct": "fg3_pct",
        "fg3pct": "fg3_pct",
        "fg3%": "fg3_pct",
        "3p_pct": "fg3_pct",
        "3ppct": "fg3_pct",
        "3p%": "fg3_pct",

        "ftm": "ftm",

        "fta": "fta",

        "ft_pct": "ft_pct",
        "ftpct": "ft_pct",
        "ft%": "ft_pct",

        "oreb": "oreb",
        "o_reb": "oreb",

        "dreb": "dreb",
        "d_reb": "dreb",

        "reb": "reb",
        "rebound": "reb",
        "rebounds": "reb",

        "ast": "ast",
        "assist": "ast",
        "assists": "ast",

        "stl": "stl",
        "steal": "stl",
        "steals": "stl",

        "blk": "blk",
        "block": "blk",
        "blocks": "blk",

        "tov": "tov",
        "to": "tov",
        "turnover": "tov",
        "turnovers": "tov",

        "pf": "pf",
        "foul": "pf",
        "fouls": "pf",

        "pts": "pts",
        "pt": "pts",
        "point": "pts",
        "points": "pts",

        "plus_minus": "plus_minus",
        "plus/minus": "plus_minus",
        "+/-": "plus_minus",
        "+-": "plus_minus",
        "pm": "plus_minus",
        "p/m": "plus_minus",
        "plusminus": "plus_minus",

        "linear_per": "per",
        "linearper": "per",
        "lper": "per",
        "l_per": "per",
        "per": "per"
    }

    return switch.get(stat, default)
