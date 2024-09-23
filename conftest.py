import datetime
import time
import pytest

@pytest.fixture(scope='class')
def start_end_time():
    start_time = datetime.datetime.now().time()
    print(f'Test start time is: {start_time}')
    yield
    end_time = datetime.datetime.now().time()
    print(f'\n Test end time is: {end_time}\n')

@pytest.fixture()
def test_exec_time():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f'\n Test execution time is: {end_time - start_time}\n')
