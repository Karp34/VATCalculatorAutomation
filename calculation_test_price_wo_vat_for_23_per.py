# 1. Calculation for 23% VAT for Portugal with “Price without VAT” option
#
# Preconditions:
# Open https://www.calkoo.com/en/vat-calculator
# Choose “Portugal” in “Country” field
# 23% option in “VAT rate” field should be chosen automatically
#
# Steps:
# Choose “Price without VAT” option under the “VAT rate” field
# Enter “100” in field against “Price without VAT” field
#
# Expected result:
# “Value-Added Tax” and “Price incl. Vat” are filled automatically.
# “Value-Added Tax” is filled with “23.00” value.
# “Price incl. Vat” is filled with “123.00” value.
# Pie chart appears under the fields.
# Pie chart has areas with 18.7% and 81.3% values.
#
# Postconditions: Click on “Reset” button to clear fields
# Environment: Google Chrome 122.0



from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conditions

def launch_test():
    print("TEST STARTED")
    print("1. Calculation for 23 % VAT for Portugal with “Price without VAT” option")
    test_passed_successfully = True
    # Launch Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()


    conditions.test_preconditions(driver)
    # Enter "100" in Price without VAT field
    price_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "NetPrice"))
    )
    price_input.send_keys("100")

    try:
        # Wait for the input element to be visible
        vat_sum_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "VATsum"))
        )
        # Get the value attribute of the input element
        vat_sum_value = vat_sum_input.get_attribute("value")

        # Check if the value is "20.00"
        if vat_sum_value == "23.00":
            print("The input element has value = 23.00 inside.")
        else:
            test_passed_successfully = False
            print("The input element does not have value = 23.00 inside. Current value:", vat_sum_value)

    except Exception as e:
        print("An error occurred:", str(e))

    try:
        # Wait for the input element to be visible
        vat_sum_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "Price"))
        )
        # Get the value attribute of the input element
        vat_sum_value = vat_sum_input.get_attribute("value")

        # Check if the value is "20.00"
        if vat_sum_value == "123.00":
            print("The input element has value = 123.00 inside.")
        else:
            test_passed_successfully = False
            print("The input element does not have value = 123.00 inside. Current value:", vat_sum_value)

    except Exception as e:
        print("An error occurred:", str(e))

    little_pie_text = driver.find_element(By.CSS_SELECTOR,
                                          "#chart_div > div > div:nth-child(1) > div > svg > g:nth-child(3)").text
    if little_pie_text == "18.7%":
        print("Value found:", little_pie_text)
    else:
        test_passed_successfully = False
        print("The element does not have value = 18.7% inside. Current value:", little_pie_text)

    big_pie_text = driver.find_element(By.CSS_SELECTOR,
                                       "#chart_div > div > div:nth-child(1) > div > svg > g:nth-child(4)").text
    if big_pie_text == "81.3%":
        print("Value found:", big_pie_text)
    else:
        test_passed_successfully = False
        print("The element does not have value = 81.3% inside. Current value:", big_pie_text)

    if test_passed_successfully:
        print("TEST PASSED SUCCESSFULLY\n")
    conditions.test_postcondition(driver)