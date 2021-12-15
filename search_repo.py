from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


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

result_repo_list = "//li[contains(@class,'repo-list-item')]"
result_repo_text_xpath = "//li[contains(@class,'repo-list-item')]//div[@class ='f4 text-normal']/a"


driver = webdriver.Chrome(executable_path="C:\\Users\\PRADEEP\\Desktop\\Selenium\\chromedriver.exe")
driver.get("https://github.com")
driver.maximize_window()
driver.implicitly_wait(5)

lnk_login = driver.find_element(By.XPATH,_lnk_login_xpath)
lnk_login.click()

input_login = driver.find_element(By.XPATH,_input_user_xpath)
input_login.send_keys("pradeep-automation")

input_pwd = driver.find_element(By.XPATH,_input_pwd_xpath)
input_pwd.send_keys("Greatindia@1234")

btn_signin = driver.find_element(By.XPATH,_btn_signin_xpath)
btn_signin.click()

box_search = driver.find_element(By.CSS_SELECTOR,_box_search_css)
box_search.send_keys("react",Keys.ENTER)

lnk_advance_seacrh = driver.find_element(By.XPATH, _lnk_advance_search_xpath)
lnk_advance_seacrh.click()

dropdown_user_lang = driver.find_element(By.XPATH,_dropdown_user_language_xpath)
dropdown_user_lang.click()

input_repo_option_stars = driver.find_element(By.XPATH,_input_repo_option_stars)
input_repo_option_stars.send_keys(">45")

dropdown_license = driver.find_element(By.XPATH,_dropdown_license_xpath)
dropdown_license.click()

dropdown_option_state = driver.find_element(By.XPATH,_dropdown_option_state)
sel_state = Select(dropdown_option_state)
sel_state.select_by_value("closed")

input_repo_option_followers = driver.find_element(By.ID,_input_repo_option_followers_id)
input_repo_option_followers.send_keys(">50")

btn_search = driver.find_element(By.XPATH,_btn_search_XPATH)
btn_search.click()

result_list = driver.find_elements(By.XPATH,result_repo_list)
result_list_text = driver.find_element(By.XPATH,result_repo_text_xpath)

assert len(result_list) == 1,"More than one result in the list"
assert result_list_text.text == "mvoloskov/decider", "Text does not match"
print("success")
print(len(result_list))
print(result_list_text.text)

driver.quit()











