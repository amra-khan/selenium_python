from selenium.webdriver.common.by import By
from fitternity_task.Settings import BrowserManager
from fitternity_task.page_objects.base.BasePage import Page


class LoginPage(Page):

    LOG_IN = "//span[@class='login-text']"
    LOGIN_POPUP = "//div[@class='login-popup']"
    USERNAME_FIELD = "//input[@id='phone']"
    PSWD_FIELD = "//input[@type='password']"
    LOGIN_BUTTON = "//button[text()='LOGIN']"
    ERROR_FIELD = "//li[@class='messenger-message-slot messenger-shown messenger-first messenger-last']"
    SIGN_UP = "//button[text()='Sign up']"
    CLOSE_POPUP = "//button[@class='mfp-close']"

    def __init__(self, mobile_num=None, email_id=None, pswd=None):

        Page.__init__(self)

        if mobile_num:
            self.mobile_num = int(mobile_num)
        else:
            self.email_id = email_id
        self.pswd = pswd

    def click_login_button(self):
        BrowserManager.DRIVER.find_element(By.XPATH, LoginPage.LOG_IN).click()
        return self

    def enter_username(self, username=None):
        self.wait_to_clickable(by=By.XPATH, locator=LoginPage.LOGIN_POPUP)
        self.get_element(By.XPATH, LoginPage.USERNAME_FIELD).send_keys(username)
        return self

    def enter_password(self, pswd=None):
        self.get_element(By.XPATH, LoginPage.PSWD_FIELD).send_keys(pswd)
        return self

    def login_account(self):
        self.get_element(By.XPATH, LoginPage.LOGIN_BUTTON).click()
        assert not self.exists(by=By.XPATH, locator="{}//div[text()='Please Enter Valid Email ID']".format(LoginPage.ERROR_FIELD)),\
            "invalid email id"
        if self.exists(by=By.XPATH, locator="{}//div[text()='Customer Doesnt Exist. Sign Up to create your account']"):
            assert self.exists(by=By.XPATH, locator=LoginPage.SIGN_UP), "doesnt automatically land on sign up page"
        else:
            """
            couldn't get the otp to register on the site , tried several times so leaving the verification
            part after login but the code would work in both the case
            """
            pass
        return self

    def close_popup(self):
        self.get_element(By.XPATH, LoginPage.CLOSE_POPUP).click()
        assert not self.exists(by=By.XPATH, locator=LoginPage.LOGIN_POPUP), "popup doesnt go away"
        return self


