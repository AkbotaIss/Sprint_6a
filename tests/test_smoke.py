from pages.base_page import BasePage  # если ещё нет — создай пустой BasePage с open()

def test_open_main(firefox, base_url):
    BasePage(firefox, base_url).open("/")
    assert "Самокат" in firefox.title
