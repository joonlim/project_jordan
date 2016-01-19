from app.banners import banners
from random import shuffle
from flask import Markup


WEBSITE_NAME = "Project Jordan"
ICON = "img/icon.png"
YEAR = "2016"
AUTHOR_NAME = "Joon Lim"
AUTHOR_EMAIL = "joonlim@gmail.com"
AUTHOR_GITHUB = "https://github.com/joonlim/"
HEADER = "Welcome to " + Markup("<br/><strong>" + WEBSITE_NAME + "</strong>")
HEADER_MSG = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
FOOTER = "Site Built By " + AUTHOR_NAME


class WebsiteManager:
    """
    Manages website information.
    """
    def info(self):
        """
        Return information about the website, including its name, icon image,
        and author.
        """
        return {
            "name": WEBSITE_NAME,
            "icon": ICON,
            "year": YEAR,
            "author_name": AUTHOR_NAME,
            "author_email": AUTHOR_EMAIL,
            "author_github": AUTHOR_GITHUB
        }

    def new_page(self, title):
        """
        Return the data for a new page, including its title, header, an footer.
        The returned dict also has a random banner to be used in the carousel.
        """
        return {
            "title": title,
            "banner": self.__random_banner(),
            "header": HEADER,
            "header_msg": HEADER_MSG,
            "footer": FOOTER
        }

    def nav_bar_pages(self, index=None):
        """
        Return a list containing the names of all subpages in order. This does
        not include the home page since the button for home should always be on
        the navigation bar. The index parameter should be the index of the page
        calling this method to be displayed as active. If no index is given,
        then no pages will be set to active.
        """
        nav_bar_pages = [
            {
                "title": "Performance",
                "active": False,
                "link": "date_stats"
            },
            {
                "title": "Compare",
                "active": False,
                "link": "compare_players"
            }
        ]

        if index is not None:
            assert index >= 0 and index < len(nav_bar_pages)
            nav_bar_pages[index]['active'] = True
        return nav_bar_pages

    def __random_banner(self):
        """
        Returns a random banner image.
        """
        local_banners = banners[:]
        shuffle(local_banners)
        return local_banners.pop(0)


website_manager = WebsiteManager()
