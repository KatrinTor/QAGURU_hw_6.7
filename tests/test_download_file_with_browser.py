import os
import time
from conftest import TMP_DIR
from selenium import webdriver
from selene import browser

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
browser.config.driver_options = options

def test_download_with_requests(tmp_dir_manager):
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(5)

    assert os.path.exists(os.path.join(TMP_DIR, 'pytest-main.zip'))
