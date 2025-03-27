# utils/driver_setup.py
from appium import webdriver
from appium.options.common import AppiumOptions
import json
import os

def get_driver():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)

    kobiton_server_url = config.get('kobitonServerUrl')
    desired_caps = config.get('desiredCaps')

    if not kobiton_server_url or not desired_caps:
        raise ValueError("Invalid configuration in device_config.json")

    try:
        options = AppiumOptions()
        options.load_capabilities(desired_caps)
        driver = webdriver.Remote(kobiton_server_url, options=options)
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        print(f"Failed to initialize driver: {e}")
        return None  # Make sure to return None in case of failure

def quit_driver(driver):
    if driver:
        driver.quit()
