import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class GitHub:
    # Locators
    _lnk_login_xpath = "//a[@href='/login']"
    _input_user_xpath = "//input[@name='login']"
    _input_pwd_xpath = "//input[@name='password']"
    _btn_signin_xpath = "//input[@value='Sign in']"
    _box_search_css = ".js-site-search-focus"
    _lnk_advance_search_xpath = "(//a[text()='Advanced search'])[1]"
    _input_repo_option_stars = "//input[@id='search_stars']"
    _input_repo_option_followers_id = "search_followers"
    _dropdown_option_state = "//select[@id='search_state']"
    _dropdown_user_language_xpath = "//select[@id = 'search_language']" \
                                    "/optgroup[@label='Popular']/option[@value='JavaScript']"
    _dropdown_license_xpath = "//select[@id='search_license']/optgroup[@label='Licenses']/option[@value='bsl-1.0']"

    _btn_search_XPATH = "(//button[contains(text(),'Search')])[2]"

    # result_repo_list = "//li[contains(@class,'repo-list-item')]"
    result_repo_list_xpath = "//li[contains(@class,'repo-list-item')]//div[@class ='f4 text-normal']/a"

    def __init__(self,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.XPATH, self._lnk_login_xpath).click()

    def set_user_name(self, username):
        self.driver.find_element(By.XPATH, self._input_user_xpath).clear()
        self.driver.find_element(By.XPATH, self._input_user_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self._input_pwd_xpath).clear()
        self.driver.find_element(By.XPATH, self._input_pwd_xpath).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self._btn_signin_xpath).click()

    def search_box_text_enter(self,expr):
        box_search = self.driver.find_element(By.CSS_SELECTOR, self._box_search_css)
        box_search.send_keys(expr, Keys.ENTER)

    def click_advance_search(self):
        lnk_advance_search = self.driver.find_element(By.XPATH, self._lnk_advance_search_xpath)
        lnk_advance_search.click()

    def select_language(self):
        dropdown_user_lang = self.driver.find_element(By.XPATH, self._dropdown_user_language_xpath)
        dropdown_user_lang.click()

    def set_stars(self,value):
        input_repo_option_stars = self.driver.find_element(By.XPATH, self._input_repo_option_stars)
        input_repo_option_stars.send_keys(value)

    def select_license(self):
        dropdown_license = self.driver.find_element(By.XPATH, self._dropdown_license_xpath)
        dropdown_license.click()

    def select_state(self,value):
        # time.sleep(4)
        dropdown_option_state = self.driver.find_element(By.XPATH, self._dropdown_option_state)
        sel_state = Select(dropdown_option_state)
        sel_state.select_by_value(value)

    def set_followers(self,value):
        # time.sleep(3)
        input_repo_option_followers = self.driver.find_element(By.ID, self._input_repo_option_followers_id)
        input_repo_option_followers.send_keys(value)

    def click_search_btn(self):
        btn_search = self.driver.find_element(By.XPATH, self._btn_search_XPATH)
        btn_search.click()

    def result_list(self):
        result_list = self.driver.find_elements(By.XPATH, self.result_repo_list_xpath)
        return result_list

    def get_read_me_text(self):
        self.driver.find_element(By.XPATH, "//a[text()='README.md']").click()
        readme_txt = self.driver.find_element(By.XPATH, "//div[@id='readme']/article").text
        return readme_txt


