import re
import time

from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    expect(page).to_have_title(re.compile("OrangeHRM"))


def test_has_header(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()


def test_has_credentials(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    expect(page.locator("//div[@class='orangehrm-login-error']//p[1]")).to_have_text("Username : Admin")
    expect(page.locator("//div[@class='orangehrm-login-error']//p[2]")).to_have_text("Password : admin123")


def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")).to_have_text("Required")
    time.sleep(2)