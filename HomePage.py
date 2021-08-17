from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from fitternity_task.Settings import BrowserManager
from fitternity_task.page_objects.base.BasePage import Page


class HomePage(Page):

    CHOSE_LOCALITY_DROPDOWN = "//div[@class='mui-col-md-12 mui-col-xs-12 top-location-box']"
    CHOSE_FITNESS_FORM = "//div[@class='mui-col-md-12 mui-col-xs-12 top-category-box']"
    INPUT_FIELD = "(//input[@type= 'select-one'])[{}]"
    INPUT_VALUE = "//div[@class='selectize-dropdown-content']//div[text()='{}']"
    EXPLORE = "//a[text()=' Explore']"
    GLOBAL_SEARCH = "//input[@id='global-search-input']"
    GLOBAL_SEARCH_ELEM = "//div[@class='easy-autocomplete-container']//li[{}]//div[@class='mui-row']//div"

    def __init__(self):

        Page.__init__(self)

    def click_chose_locality(self):
        WebDriverWait(BrowserManager.DRIVER, self.WAIT_THRESHOLD).until(EC.element_to_be_clickable((
            By.XPATH, HomePage.CHOSE_LOCALITY_DROPDOWN)))
        BrowserManager.DRIVER.find_element(By.XPATH, HomePage.CHOSE_LOCALITY_DROPDOWN).click()
        return self

    def select_locality(self, locality=None):
        self.get_element(By.XPATH, HomePage.INPUT_FIELD.format(1)).send_keys(locality)
        element = self.get_element(By.XPATH, HomePage.INPUT_VALUE.format(locality))
        ActionChains(driver=BrowserManager.DRIVER).move_to_element(to_element=element)\
            .send_keys(Keys.ENTER).perform()
        return self

    def click_chose_fitness_form(self):
        self.get_element(By.XPATH, HomePage.CHOSE_FITNESS_FORM).click()
        return self

    def select_fitness_form(self, form=None):
        self.get_element(By.XPATH, HomePage.INPUT_FIELD.format(2)).send_keys(form)
        element = self.get_element(By.XPATH, HomePage.INPUT_VALUE.format(form))
        ActionChains(driver=BrowserManager.DRIVER).move_to_element(to_element=element).send_keys(
            Keys.ENTER).perform()
        from fitternity_task.page_objects.GymPage import GymPage
        return GymPage()

    def input_global_search(self, input_text=None):
        self.wait_to_clickable(wait=2, by=By.XPATH, locator=HomePage.GLOBAL_SEARCH)
        self.get_element(By.XPATH, HomePage.GLOBAL_SEARCH).send_keys(input_text)
        return self

    def select_global_search_item(self, index=1):
        self.wait_to_clickable(wait=2, by=By.XPATH, locator=HomePage.GLOBAL_SEARCH_ELEM.format(index))
        self.get_element(By.XPATH, HomePage.GLOBAL_SEARCH_ELEM.format(index)).click()
        from fitternity_task.page_objects.GymPage import GymPage
        return GymPage()

    def get_selected_text(self, index=1):
        self.wait_to_clickable(wait=2, by=By.XPATH, locator=HomePage.GLOBAL_SEARCH_ELEM.format(index))
        return self.get_element(By.XPATH, HomePage.GLOBAL_SEARCH_ELEM.format(index)).text
