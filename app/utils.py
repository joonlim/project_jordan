from datetime import date, timedelta, datetime


def group_into_pairs(items):
    """
    Takes a list as input and pushes every two items of that list into a new
    list as pairs of items and returns the new list. If there is an odd number
    of items, the last pair has only one item in the list.

    Ex: [1,2,3,4,5,6,7] -> [[1,2],[3,4],[5,6],[7]]
    """
    pairs = list()

    i = 0
    while i < len(items):
        pair = list()
        pair.append(items[i])
        # Check for next items
        i += 1
        if i < len(items):
            pair.append(items[i])
        pairs.append(pair)
        i += 1

    return pairs


def sort_list_by_attribute(list, attr, second_attr=None, reverse=True):
    """
    Sorts a list of dicts by an attribute. If a second attribute is given, then
    this list sorted by both attributes (ties are broken with the second
    attribute.)

    This method sorts the given list, it does not return a new list.
    """
    if second_attr is not None:
        list.sort(key=lambda x: (x[attr], x[second_attr]), reverse=reverse)
    else:
        list.sort(key=lambda x: x[attr], reverse=reverse)


def days_before_today(days_to_subtract, format="%Y-%m-%d"):
    """
    Returns yesterday's date as a string(formatted: "YYYY-MM-DD").
    """
    today = date.today()
    prev_day = today - timedelta(days=days_to_subtract)
    return prev_day.strftime(format)


def ratio_string(num, den, digits_passed_decimal_point):
    """
    Returns the ratio num / den with an amount of digits after the decimal
    equal to digits_passed_decimal_point. If den is 0, this returns 0.
    """
    digits = "%." + str(digits_passed_decimal_point) + "f"
    if den == 0:
        return digits % 0
    else:
        ratio = num / den
        return digits % ratio


def is_valid_date(date_string, deli="/"):
    """
    Returns true if date_string is a string representing a date formatted
    DD/MM/YYYY, where the '/' is replaced by deli.
    """
    format = "%m-%d-%Y".replace('-', deli)
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        # raise ValueError("Incorrect data format, should be MM-DD-YYYY")
        return False
