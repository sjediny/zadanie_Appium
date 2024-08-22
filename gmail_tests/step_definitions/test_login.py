import pytest
from pytest_bdd import scenarios, given, when, then
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import TimeoutException

from pages.welcome_page import WelcomePage
from pages.addresses_list_page import AddressesListPage
from pages.login_page import LoginPage
from pages.set_up_email_page import SetUpEmailPage
from pages.password_page import PasswordPage
from pages.email_welcome_page import EmailWelcomePage
from pages.google_services_page import GoogleServicesPage
from pages.setting_page import SettingPage
from pages.accounts_page import AccountsPage
from pages.account_page import AccountPage
from pages.notification_bar_page import NotificationBarPage
from pages.pop_up_page import PopUpPage
from pages.inbox_page import InboxPage

from configuration.configuration import Config

scenarios('../features/login.feature')

@pytest.fixture
def appium_driver():
    from appium import webdriver
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.google.android.gm",
        "appActivity": "com.google.android.gm.ConversationListActivityGmail",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(desired_caps))
    yield driver
    step_delete_account(driver)
    driver.quit()

def step_delete_account(appium_driver):
    appium_driver.open_notifications()
    NotificationBarPage(appium_driver).pull_down_notification_bar()
    NotificationBarPage(appium_driver).navigate_to_setting()

    SettingPage(appium_driver).visible_setting_page()
    SettingPage(appium_driver).navigate_to_accounts()

    AccountsPage(appium_driver).visble_accounts_page()
    AccountsPage(appium_driver).navigate_to_account(Config().email)

    AccountPage(appium_driver).visible_account_page()
    AccountPage(appium_driver).remove_account()

@given('the Gmail app is launched')
def step_gmail_launched(appium_driver):
        WelcomePage(appium_driver).visible_welcome()
        WelcomePage(appium_driver).click_gotit()

@when('a new email address is entered')
def step_enter_email(appium_driver):
    AddressesListPage(appium_driver).visible_adresses_list()
    AddressesListPage(appium_driver).click_new_email_address()

    SetUpEmailPage(appium_driver).visible_set_up_email()
    SetUpEmailPage(appium_driver).click_google()

    LoginPage(appium_driver).visible_login()
    LoginPage(appium_driver).enter_email(Config().email)
    LoginPage(appium_driver).click_next_button()

@when('the correct password is provided')
def step_enter_password(appium_driver):
    PasswordPage(appium_driver).visible_password_page()
    PasswordPage(appium_driver).enter_password(Config().password)
    PasswordPage(appium_driver).click_next_button()

    EmailWelcomePage(appium_driver).visible_welcome()
    EmailWelcomePage(appium_driver).click_agree()

    GoogleServicesPage(appium_driver).visible_google_sercvices()
    GoogleServicesPage(appium_driver).click_accetp()

@when('navigating to the inbox')
def step_navigate_to_inbox(appium_drive):
    AddressesListPage(appium_driver).visible_adresses_list()
    AddressesListPage(appium_driver).navigate_to_inbox()

@when('permission is "{decision}"')
def step_handle_permission(appium_driver, decision):
    PermissionPage(appium_driver).visible_permission()
    PermissionPage(appium_driver).click_permission_decision(decision)

@when('the pop-up news window is closed')
def step_close_pop_up_news(context):
    PopUpPage(appium_driver).visible_pop_up()
    PopUpPage(appium_driver).close_pop_up

@then('the inbox should be displayed')
def step_verify_inbox_displayed(context):
    assert InboxPage(appium_driver).is_inbox_display(), "Inbox is not displayed"

@then('the account should be displayed in the addresses list')
def check_account(appium_driver):
    AddressesListPage(appium_driver).visible_adresses_list()
    assert AddressesListPage(appium_driver).is_account_displayed()
    actual_name = AddressesListPage(appium_driver).get_account_name()
    expected_name = Config.name
    assert actual_name == expected_name, f"Expected account name to be '{expected_name}', but got '{actual_name}'"
    actual_email = AddressesListPage(appium_driver).get_acount_email()
    expected_email = Config.email
    assert actual_email == expected_email, f"Expected account email to be '{expected_email}', but got '{actual_email}'"
