from pytest import fixture
from testuff.client import TestuffClient
from os import getenv

@fixture(scope="session")
def testuff_client():
    return TestuffClient(
        email=getenv("username"),
        password=getenv("password"),
    )
