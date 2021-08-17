from selenium.webdriver.common.by import By
from fitternity_task.Settings import BrowserManager
from fitternity_task.page_objects.base.BasePage import Page


class GymPage(Page):

    __HEADER_LIST = []

    def __init__(self):

        Page.__init__(self)

    def get_page_headers(self):
        locator = "//div[@class='srpbreadcrumb']//li"
        self.wait_to_clickable(wait=5, by=By.XPATH, locator=locator)
        for index in range(1, len(BrowserManager.DRIVER.find_elements(By.XPATH, locator)) + 1):
            GymPage.__HEADER_LIST.append(self.get_element(By.XPATH, "({}//a)[{}]".format(locator, index)).text)
        return GymPage.__HEADER_LIST

    def get_outlets_count(self):
        text = self.get_element(By.XPATH, "//div[@class='mui-col-md-9 mui-col-xs-8']//span").text
        return int(text.split()[1])
