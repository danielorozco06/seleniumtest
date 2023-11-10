from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Set Chrome options for Incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

while True:
    # Opens a Chrome browser in Incognito mode
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # Goes to the desired site
    driver.get("https://www.menti.com/altfkm4gd9wk?source=qr-page")
    sleep(5)

    # Scrolls down the page by sending the PAGE_DOWN key
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)

    # Find the radio button
    radio_button_id = "[object Object]2"
    radio_button = driver.find_element(By.ID, radio_button_id)
    driver.execute_script("arguments[0].click();", radio_button)
    sleep(5)

    # JavaScript to find the button and click it
    script = """
    var buttons = document.querySelectorAll('button');
    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i].textContent.trim() === 'Enviar') {
            buttons[i].click();
            break;
        }
    }
    """
    driver.execute_script(script)
    sleep(10)

    # Safely quit our driver
    driver.quit()
