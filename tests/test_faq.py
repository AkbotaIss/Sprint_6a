
import pytest
import allure

from pages.main_page import MainPage
from data.faq_data import FAQ_IDS, FAQ_TEXTS


@allure.feature("FAQ")
class TestFAQ:

    @allure.title("FAQ: вопрос «{faq_id}» открывается и содержит корректный текст")
    @pytest.mark.parametrize(
        "index, expected, faq_id",
        [
            (i, FAQ_TEXTS[i], FAQ_IDS[i])
            for i in range(len(FAQ_TEXTS))
        ],
        ids=FAQ_IDS,
    )
    def test_faq_item_has_text(self, firefox, base_url, index, expected, faq_id):
        page = MainPage(firefox, base_url)
        page.open_and_accept()


        answer_text = page.expand_faq_and_get_text(index)


        assert expected in answer_text
