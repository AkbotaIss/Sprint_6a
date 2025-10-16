import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

# --- наши тестовые данные ---
DATASETS = [
    dict(first="Акбота", last="Исина", address="Москва, Тверская 1",
         metro="Тверская", phone="79990001122", day=20, term="двое суток",
         color="чёрный", comment="Позвоните за 15 минут"),

    dict(first="Мария", last="Смирнова", address="Москва, Пушкина 10",
         metro="Пушкинская", phone="79995553322", day=21, term="сутки",
         color="серый", comment="Код 12"),
]


@pytest.mark.ui
@pytest.mark.parametrize("data", DATASETS, ids=["Набор 1", "Набор 2"])
@allure.title("Позитивный сценарий заказа самоката ({data})")
def test_order_positive_flow(firefox, base_url, data):
    main = MainPage(firefox, base_url)
    order = OrderPage(firefox, base_url)

    # 1. Открыть главную и принять cookies
    main.open_and_accept()

    # 2. Кликнуть «Заказать» (верхняя кнопка)
    main.click_order("top")

    # 3. Заполнить форму шаг 1
    order.fill_step1(
        data["first"], data["last"], data["address"],
        data["metro"], data["phone"]
    )

    # 4. Заполнить форму шаг 2
    order.fill_step2(
        data["day"], data["term"], data["color"], data["comment"]
    )

    # 5. Подтвердить заказ
    order.confirm()

    # 6. Проверить, что появилось окно об успешном создании заказа
    modal = order.success_modal_visible()
    assert modal is not None, "Не появилось сообщение об успешном заказе"
