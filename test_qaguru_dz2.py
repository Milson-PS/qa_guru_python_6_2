
from selene.support.shared import browser
from selene import be, have

def test_qaguru_auth():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_dz_no_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gewgwegewgee').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу gewgwegewgee ничего не найдено. '))