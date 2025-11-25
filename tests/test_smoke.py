from pages.main_page import MainPage

def test_open_main(firefox, base_url):
    MainPage(firefox, base_url).open("/")

