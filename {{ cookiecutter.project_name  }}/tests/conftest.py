import os
import pytest
import shutil

from pathlib import Path


@pytest.fixture(scope="session")
def a_fixture():
    return "fixture"


# Common Data Paths
# @pytest.fixture(scope='session')
# def shared_datadir(request, tmpdir_factory):
#     original_shared_path = os.path.join(os.path.dirname(__file__), 'data')

#     tempdir = tmpdir_factory.getbasetemp()
#     temp_path = Path(str(tempdir.join("data")))
#     shutil.copytree(original_shared_path, str(temp_path))
#     request.addfinalizer(lambda: tempdir.remove(rec=1))

#     return temp_path

@pytest.fixture(scope='session')
def shared_datadir():
    original_shared_path = os.path.join(os.path.dirname(__file__), 'data')

    return original_shared_path