import os
import zipfile
from conftest import TMP_DIR, RES_DIR

res_files = os.listdir(RES_DIR)
archive = os.path.join(TMP_DIR, 'test.zip')

def test_create_zip(tmp_dir_manager):
    with zipfile.ZipFile(archive, mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in res_files:
            add_file = os.path.join(RES_DIR, file)
            zf.write(add_file, arcname=file)

    with zipfile.ZipFile(archive) as zf:
        assert len(res_files) == len(zf.infolist())
        for file in res_files:
            info = zf.getinfo(file)
            assert file == info.filename
            orig_file_size = os.stat(os.path.join(RES_DIR, file)).st_size
            assert orig_file_size == info.file_size
