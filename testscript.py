import pytest
from datetime import datetime
from utils.driver_setup import get_driver, quit_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCrashApp:
    driver = None  # Explicitly declare the driver class variable

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self):
        # Initialize the driver from our helper class
        TestCrashApp.driver = get_driver()  # Assigning the driver to the class variable
        print(f"Driver initialized at: {datetime.now()}")

        if not TestCrashApp.driver:
            pytest.fail("Driver initialization failed.")

        yield  # This will run the test methods
        quit_driver(TestCrashApp.driver)  # Quitting driver after the tests are complete

    def test_enable_crash_and_next(self):
        print("=== Starting test: Enable crash and click Next ===")
        print(f"Test started at: {datetime.now()}")

        try:
            print("Waiting for the 'Enable crash' checkbox to be visible...")
            # Wait until the element is visible
            enable_crash_checkbox = WebDriverWait(TestCrashApp.driver, 60).until(
                EC.visibility_of_element_located((AppiumBy.ID, "com.kobiton.sample.crashsample:id/rbtnEnableCrash"))
            )
            print(f"Found the 'Enable crash' checkbox at: {datetime.now()}")

            # Click the checkbox
            enable_crash_checkbox.click()
            print(f"Clicked the 'Enable crash' checkbox at: {datetime.now()}")

            # Now locate and click the 'Next' button
            next_button = WebDriverWait(TestCrashApp.driver, 30).until(
                EC.element_to_be_clickable((AppiumBy.ID, "com.kobiton.sample.crashsample:id/btnNext"))
            )
            next_button.click()
            print(f"Clicked the 'Next' button at: {datetime.now()}")

        except Exception as e:
            print(f"Test failed due to error: {e}")
            pytest.fail(str(e))
