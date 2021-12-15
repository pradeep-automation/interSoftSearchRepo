import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\PRADEEP\\Desktop\\Selenium\\chromedriver.exe")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("https://github.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
