import pytest

from pom.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        home_page_nav = HomePageNav(self.driver)
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, f' actual_links: {actual_links} not equal expected_links: {expected_links}'