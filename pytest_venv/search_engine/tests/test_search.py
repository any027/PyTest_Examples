from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    #Given DDG home page is splayed
    search_page.load()

    search_page.search("panda")

    #Given the DuckDuckGo home page is displayed
    assert "panda" in result_page.title()

    #When the user searches ofr "Panda"
    assert "panda" == result_page.search_input_value()

    #Then the search result title contains "Panda"
    assert result_page.result_count_for_phrase("panda") > 0

    assert True