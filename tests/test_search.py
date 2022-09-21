import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('search_phrase', ['panda', 'python', None, 'polar bear'])
def test_basic_duckduckgo_search(browser, search_phrase):
    search_page = DuckDuckGoSearchPage(browser, search_phrase=search_phrase)
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


def test_more_results_button_expands_results_found(browser):
    search_page = DuckDuckGoSearchPage(browser, search_phrase='waffles')
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    search_page.search()

    more_results_button = result_page.get_more_results_button()
    assert more_results_button

    result_links_titles_before_click = result_page.get_result_links_titles()
    more_results_button.click()
    result_links_titles_after_click = result_page.get_result_links_titles()
    assert result_links_titles_after_click > result_links_titles_before_click

    more_results_button = result_page.get_more_results_button()
    assert more_results_button


def test_is_ad_relevant_to_search_phrase_on_result_page(browser):
    search_page = DuckDuckGoSearchPage(browser, search_phrase='ketchup')
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    search_page.search()

    ad_titles = result_page.get_ads_titles()
    assert len(ad_titles) > 0

    search_phrase = search_page.search_phrase

    ad_title_matching_search_phrase = [
        ad_title
        for ad_title in ad_titles
        if search_phrase in ad_title.lower()
    ]
    assert len(ad_title_matching_search_phrase) > 0


def test_does_show_nothing_found_message_on_result_page_if_nothing_found(browser):
    search_page = DuckDuckGoSearchPage(browser, search_phrase='nsokVsnjdl')
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()
    search_page.search()

    search_phrase = result_page.get_search_phrase()

    result_links_titles = result_page.get_result_links_titles()
    assert len(result_links_titles) == 0

    ad_titles = result_page.get_ads_titles()
    assert len(ad_titles) == 0

    no_results_message = result_page.get_no_results_found_message()
    no_results_message_template = result_page.NO_RESULTS_FOUND_MESSAGE_TEMPLATE
    assert no_results_message == no_results_message_template.format(search_phrase=search_phrase)


def test_autocomplete_options_pertain_to_search_phrase(browser):
    search_page = DuckDuckGoSearchPage(browser, search_phrase='ManBearPig')

    search_page.load()

    autocomplete_suggestions = search_page.get_autocomplete_suggestions()
    search_phrase = search_page.search_phrase
    search_phrase_length = len(search_phrase)

    for autocomplete_suggestion in autocomplete_suggestions:
        assert autocomplete_suggestion.text[:search_phrase_length].lower() == search_phrase.lower()
