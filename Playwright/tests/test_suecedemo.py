import re
from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name", "problem_user")
    page.fill("input#password", "secret_sauce")
    page.click("//input[@id='login-button'][1]")
    expect(page.click("//input[@id='login-button'][1]")).to_have_id("login-button")

