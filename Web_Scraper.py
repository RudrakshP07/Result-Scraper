import csv
import time
import traceback
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Specify the path to the EdgeDriver executable
edge_driver_path = r"C:\Web Driver\msedgedriver.exe"  # Update with the actual path to EdgeDriver

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update with the actual path to Tesseract executable

# Specify the path to the CSV file containing roll numbers
csv_file_path = r"D:\Web Scraper\Students_Record_Cyber_2ndyear.csv"  # Absolute path to the CSV file

# Create options and service
edge_options = Options()
service = EdgeService(edge_driver_path)

# Create the Edge WebDriver instance
driver = webdriver.Edge(service=service, options=edge_options)

# Function to read roll numbers from the first column of a CSV file
def read_roll_numbers(file_path):
    roll_numbers = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Assuming roll numbers are in the first column
            roll_numbers.append(row[0].strip())  # Append roll numbers from the first column
    return roll_numbers

try:
    # Read roll numbers from the specified CSV file
    roll_numbers = read_roll_numbers(csv_file_path)

    # Iterate through each roll number
    for roll_number in roll_numbers:
        try:
            # Open the URL
            url = "http://result.rgpv.ac.in/Result/ProgramSelect.aspx"
            driver.get(url)

            # Locate and click the radio button
            radio_button = driver.find_element(By.ID, 'radlstProgram_1')
            radio_button.click()

            # Wait for the page to redirect and load completely
            WebDriverWait(driver, 10).until(EC.url_changes(url))

            ############################ PAGE 2 ############################  
            # Interact with the new page after redirection
            # Locate the text input field and enter the roll number
            text_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtrollno')))
            text_input.send_keys(roll_number)

            # Locate the dropdown and select a value
            dropdown = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_drpSemester')
            select = Select(dropdown)
            select.select_by_value("3")

            # Locate the CAPTCHA image element using an XPath expression
            captcha_image = driver.find_element(By.XPATH, '//img[contains(@src, "CaptchaImage.axd")]')
            
            # Define the path to save the CAPTCHA screenshot
            captcha_screenshot_path = "captcha_screenshot.png"

            # Take a screenshot of the CAPTCHA element and save it to a file
            captcha_image.screenshot(captcha_screenshot_path)
            print(f"CAPTCHA screenshot saved to {captcha_screenshot_path}")

            # Convert the CAPTCHA screenshot to text using OCR (pytesseract)
            captcha_image_pil = Image.open(captcha_screenshot_path)
            captcha_answer = pytesseract.image_to_string(captcha_image_pil).strip()

            # Remove spaces from the CAPTCHA answer
            captcha_answer = captcha_answer.replace(" ", "")
            captcha_answer = captcha_answer.replace(".", "")
            captcha_answer = captcha_answer.replace(",", "")
            captcha_answer = captcha_answer.replace(";", "")
            captcha_answer = captcha_answer.replace("'", "")
            # captcha_answer = captcha_answer.replace("", "")

            # Delay for 7 seconds before entering the CAPTCHA answer
            time.sleep(7)

            # Locate the CAPTCHA input field
            captcha_input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TextBox1')

            # Enter the CAPTCHA answer and simulate pressing Enter to submit the form
            captcha_input.send_keys(captcha_answer + Keys.ENTER)
            
            ############################ PAGE 3 ############################  
            # Delay for 7 seconds before clicking the reset button
            time.sleep(7)

            # Locate the reset button and click it
            reset_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnReset'))
            )
            reset_button.click()
            
        except Exception as ex:
            # Handle exceptions during roll number processing
            print(f"An error occurred with roll number {roll_number}: {ex}")
            # Skip the current roll number and continue with the next one
            continue

    # Pause the script to observe the action
    print("Pause: observe the action")
    input("Press Enter to close the browser...")

except Exception as e:
    print("An error occurred:", e)
    print(traceback.format_exc())

finally:
    # Close the browser
    driver.quit()
