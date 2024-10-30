from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

def get_short_url(tag, cookies_json, asin):
    # Load cookies from JSON
    cookies = json.loads(cookies_json)

    # Set up the WebDriver (you may need to adjust options based on your browser)
    options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(options=options)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=options)


    try:
        # Navigate to the Amazon page for the given ASIN
        driver.get(f'https://www.amazon.com/dp/{asin}')

        # Add cookies to the browser
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Refresh the page to apply the cookies
        driver.refresh()
        
        # Wait for the "Get Link" button to be present and click it
        element_to_click = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.ID, "amzn-ss-get-link-button"))
        )
        element_to_click.click()
        time.sleep(2)

        # Select the tracking ID dropdown
        select_element = driver.find_element(By.ID, "amzn-ss-tracking-id-dropdown-text")
        driver.execute_script("arguments[0].scrollIntoView(true);", select_element)
        time.sleep(1)

        # Use JavaScript to click the dropdown
        driver.execute_script("arguments[0].click();", select_element)
        time.sleep(2)

        # Select the appropriate tag from the dropdown
        tags = select_element.find_elements(By.CSS_SELECTOR, "option")
        for t in tags:
            if t.text.strip() == tag:
                driver.execute_script("arguments[0].click();", t)
                time.sleep(2)
                break

        # Click the button to get the short URL
        driver.find_element(By.ID, "amzn-ss-get-link-btn-text-announce").click()
        time.sleep(2)

        # Retrieve the short URL
        short_url = driver.find_element(By.ID, "amzn-ss-text-shortlink-textarea").text.strip()
        return short_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Close the browser
        driver.quit()

# Example usage
cookies_json =open("cookies.json").read()
short_url = get_short_url("foodlyai-20", cookies_json, "B071L7V8YH")
print(short_url)
