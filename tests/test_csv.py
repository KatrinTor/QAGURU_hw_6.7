import csv
import os.path
from conftest import RES_DIR

path_to_csv = os.path.join(RES_DIR, 'eggs.csv')
def test_create_csv():
    with open(path_to_csv, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    assert os.path.exists(path_to_csv)

def test_read_csv():
    with open(path_to_csv) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3
        assert csvreader.line_num == 2
    os.remove(path_to_csv)
