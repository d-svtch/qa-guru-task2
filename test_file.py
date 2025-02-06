from selene import browser, be, have
import pytest


@pytest.fixture(autouse=True)
def operations_with_browser():
    browser.open('https://google.com')
    yield
    browser.quit()


@pytest.fixture(scope="session")
def browser_configurator():
    browser.config.window_height = 1024
    browser.config.window_width = 1024


def test_valid_result(browser_configurator):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.no.text('ничего не найдено'))


def test_invalid_result():
    browser.element('[name="q"]').should(be.blank).type('ydasdfasdfasdfasdfagsdfgsdfgsdfgsdfgssdfggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))
