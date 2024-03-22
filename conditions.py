from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_preconditions(driver):
    # Open the website
    driver.get("https://www.calkoo.com/en/vat-calculator")

    # Handle additional consent button
    try:
        consent_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]]"))
        )
        consent_button.click()
    except:
        pass

    try:
        additional_consent_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button"))
        )
        additional_consent_button.click()
    except:
        pass

    # Handle cookie agreement popup
    try:
        cookie_popup = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cc-window"))
        )
        accept_button = cookie_popup.find_element_by_xpath("//a[@aria-label='dismiss cookie message']")
        accept_button.click()
    except:
        pass

    # Choose Portugal in Country field
    country_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="vatcalculator"]/div[2]/div[2]/select'))
    )
    country_dropdown.send_keys("Portugal")


def test_postcondition(driver):
    # Click on Reset button
    reset_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "clear"))
    )
    reset_button.click()

    # Close the browser
    driver.quit()
