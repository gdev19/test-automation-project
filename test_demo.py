import re
from playwright.sync_api import Page, expect
from testuff.client import TestuffClient
from testuff.models import Test
from os import getenv
from time import perf_counter

def test_has_correct_title(page: Page, testuff_client: TestuffClient) -> None:
    try:
        first_test = list(testuff_client.get(Test, id=getenv("HOME_PAGE_TEST1_ID")))
        lab_name = "Results"
        start = perf_counter()
        page.goto("https://codeff.nl/")
        expect(page).to_have_title(re.compile("Codeff"))
        testuff_client.add_automation(token=getenv("TOKEN"), lab_name=lab_name, automation_id=first_test[0].automation_id, branch_id=first_test[0].branch_id, name="Home Page Accessible", status='passed', seconds=int(perf_counter() - start), comment="Checked with Playwright")
    except Exception as e:
        testuff_client.add_automation(token=getenv("TOKEN"), lab_name=lab_name, automation_id=first_test[0].automation_id, branch_id=first_test[0].branch_id, name="Home Page Accessible", status='failed', seconds=int(perf_counter() - start), comment=f"Checked with Playwright. Error: {e}")
        raise e
