import random

import pytest

import config

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from pages.home_page import HomePage
from config import environment


@pytest.fixture()
def page() -> Page:
    playwright = sync_playwright().start()
    browser = get_chrome_browser(playwright)
    context = get_context(browser)
    page_data = context.new_page()

    login(page_data)
    page_data.goto(environment.TEST_URL)

    yield page_data

    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE,
        locale=config.playwright.LOCALE
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context


def login(page):
    def random_phone_number():
        phone_code = ["7707", "7708", "7701", "7777", "7747", "7702", "7776"]
        randint = random.randint(0, 9999999)
        randcode = random.choice(phone_code)
        return str(f'{randcode}{randint}')

    # Слушает алерты и берет с них информацию
    auth_code = None

    def handle_dialog(dialog):
        nonlocal auth_code
        print(f"Код для авторизации: {dialog.message}")
        auth_code = dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)

    page.goto(config.environment.TEST_URL)

    login_button = page.get_by_role("button", name="Войти")
    login_button.click()

    number_input = page.get_by_label("Ваш номер телефона")
    code_input = random_phone_number()
    print("Сгенерированный номер: " + str(code_input))
    number_input.fill(str(code_input))

    get_otp = page.get_by_role("button", name="Получить код")
    get_otp.click()

    while auth_code is None:
        page.wait_for_timeout(100)

    enter_code = page.get_by_label("Введите код")
    enter_code.fill(auth_code)

    page.get_by_role("dialog").get_by_role("button", name="Войти").click()

    city_select = page.get_by_role("dialog").get_by_text("Алматы")
    city_select.click()


@pytest.fixture(scope="function")
def setup_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            **p.devices['iPhone 12 Pro']
        )
        page = context.new_page()
        page.goto(environment.TEST_URL)  #
        page.context.add_cookies([{
            "name": "hb",
            "value": "true",
            "url": "https://test5.halykmarket.com"
        }])
        page.reload()
        yield page
        context.close()
        browser.close()
