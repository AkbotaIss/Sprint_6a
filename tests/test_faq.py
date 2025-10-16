import pytest
import allure
from pages.main_page import MainPage

FAQ_IDS = [
    "Сколько это стоит? И как оплатить?",
    "Хочу сразу несколько самокатов! Так можно?",
    "Как рассчитывается время аренды?",
    "Можно ли заказать самокат прямо на сегодня?",
    "Можно ли продлить заказ или вернуть самокат раньше?",
    "Вы привозите зарядку вместе с самокатом?",
    "Можно ли отменить заказ?",
    "Я живу за МКАДом, привезёте?",
]

@pytest.mark.ui
@pytest.mark.parametrize("i", list(range(8)), ids=FAQ_IDS)
@allure.title("FAQ: вопрос «{id}» открывается и содержит текст")
def test_faq_item_has_text(firefox, base_url, i, request):
    page = MainPage(firefox, base_url)
    page.open_and_accept()
    text = page.expand_faq_and_get_text(i)
    # Проверяем, что соответствующий ответ появился и не пустой
    assert text != ""
