# import re
import pytest
from playwright.sync_api import Page, expect
from config import environment
from conftest import page
from pages.home_page import HomePage

errorTextIsNotRight = "Текст не соответствует ожидаемому"


def test_two_type_of_delivery_is_available_on_Web(page: Page):
    home_page = HomePage(page)

    home_page.fillSomethingAndSearch(home_page.search_item)
    expect(page.get_by_text("Доступен самовывоз"), errorTextIsNotRight).to_be_visible()
    expect(page.get_by_text("Получение через Пункт выдачи"), "Доставка ПВЗ не должна отображаться").not_to_be_visible()


def test_new_order_in_city(page: Page):
    home_page = HomePage(page)
    home_page.fillSomethingAndSearch(home_page.search_item)

    select_seller_btn = page.get_by_role("button", name="Выбрать", exact=True)
    select_seller_btn.click()
    time.sleep(5)



def test_four_type_of_delivery_is_available_on_webView(setup_page):
    home_page = HomePage(setup_page)
    home_page.fillSomethingAndSearchMobile(home_page.search_item)
    expect(setup_page.get_by_text("Получение через Пункт выдачи"), "Доставка ПВЗ не отображается").to_be_visible()
