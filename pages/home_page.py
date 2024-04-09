from playwright.sync_api import Page, expect
import time

class HomePage:
    search_item = "Смартфон Apple iPhone 7 128Gb Rose Gold"
    select_seller_btn = "Выбрать продавца"

    def __init__(self, page: Page):
        self.page = page

    def fillSomethingAndSearch(self, selector):
        search_input = self.page.get_by_role("textbox", name="Search")
        search_input.fill(selector)
        submit_button = self.page.get_by_role("button", name="Найти")
        submit_button.click()
        self.page.get_by_role("link", name=selector).click()

    def clickOnButton(self, selector):
        self.page.get_by_role("button", name=selector).click()

    def fillSomethingAndSearchMobile(self, selector):
        search_input = self.page.get_by_placeholder("Найти в Halyk Market")
        search_input.click()
        search_input_field = self.page.locator("#search").get_by_label("Найти")
        search_input_field.fill(selector)
        iphone_item = self.page.get_by_text("Смартфон Apple iPhone 7 128Gb")
        iphone_item.click()
        self.page.get_by_role("link", name="На страницу продукта Смартфон Apple iPhone 7 128Gb Rose Gold").click()

        iphone_item.scroll_into_view_if_needed()
        time.sleep(10)

