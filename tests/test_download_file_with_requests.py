import os
from conftest import TMP_DIR
import requests

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path_to_file = os.path.abspath(os.path.join(TMP_DIR, 'selenium_logo.png'))

def test_doeload_with_requests(tmp_dir_manager):
    response = requests.get(url)
    with open('selenium_logo.png', 'wb') as file:
        file.write(response.content)

    assert response.status_code == 200

    size = os.path.getsize('selenium_logo.png')
    assert 30803 == size
