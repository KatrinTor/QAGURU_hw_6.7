import os
import glob
import pytest

RES_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../resources')
)

TMP_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../tmp')
)

@pytest.fixture(scope='function', autouse=False)
def tmp_dir_manager():
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)

    yield

    files = glob.glob(os.path.join(TMP_DIR, '*'))
    for f in files:
        os.remove(f)
