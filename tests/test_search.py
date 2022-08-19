from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    search_page.search()

    search_phrase = search_page.search_phrase

    result_page_links_titles = [title for title in result_page.get_result_links_titles()]
    links_titles_matching_search_phrase = [
        link_title
        for link_title in result_page_links_titles
        if search_phrase in link_title.lower()
    ]

    assert len(links_titles_matching_search_phrase) > 0

    assert result_page.get_search_phrase() == search_phrase

    assert search_phrase in result_page.get_page_title()
