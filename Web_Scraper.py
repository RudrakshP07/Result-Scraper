import csv
import time
import traceback
import requests
from io import BytesIO
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ===================== CONFIGURATION =====================

# Path to Edge WebDriver executable
edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"  # Update if needed

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to input CSV (with roll numbers)
csv_file_path = r"J:\Git\Students_Record.csv"

# Path to output CSV (where results will be saved)
output_csv = r"J:\Git\Students_Result_Output.csv"

# ==========================================================

# Create options and service for Edge
edge_options = Options()
service = EdgeService(edge_driver_path)

# Create the Edge WebDriver instance
driver = webdriver.Edge(service=service, options=edge_options)


# ------------------ FUNCTION DEFINITIONS ------------------

def read_roll_numbers(file_path):
    """Read roll numbers from the first column of a CSV file."""
    roll_numbers = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row and row[0].strip():
                roll_numbers.append(row[0].strip())
    return roll_numbers


def save_result_to_csv(roll, name, result_status, sgpa, cgpa, output_path):
    """Append a student's result data to the output CSV file."""
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["Roll No", "Name", "Result Status", "SGPA", "CGPA"])
        writer.writerow([roll, name, result_status, sgpa, cgpa])


# ------------------ MAIN SCRIPT EXECUTION ------------------

try:
    roll_numbers = read_roll_numbers(csv_file_path)

    for roll_number in roll_numbers:
        try:
            print(f"\n🔹 Processing roll number: {roll_number}")

            # Open the result website
            url = "http://result.rgpv.ac.in/Result/ProgramSelect.aspx"
            driver.get(url)

            # Select radio button for program
            radio_button = driver.find_element(By.ID, 'radlstProgram_1')
            radio_button.click()

            # Wait for page to redirect
            WebDriverWait(driver, 10).until(EC.url_changes(url))

            # ================= PAGE 2 =================
            # Enter roll number
            text_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtrollno'))
            )
            text_input.send_keys(roll_number)

            # Select semester
            dropdown = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_drpSemester')
            select = Select(dropdown)
            select.select_by_value("6")

            # ===================== CAPTCHA FETCHING =====================
            try:
                # Locate the captcha container div
                captcha_div = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_pnlCaptcha'))
                )

                # Find the <img> element inside the div
                captcha_img = captcha_div.find_element(By.TAG_NAME, 'img')

                # Get the image source URL
                captcha_src = captcha_img.get_attribute("src")

                # If the src is relative, make it absolute
                if captcha_src.startswith("/"):
                    base_url = driver.current_url.split("/Result")[0]
                    captcha_src = base_url + captcha_src

                # Download the image from the src
                response = requests.get(captcha_src)
                captcha_image_pil = Image.open(BytesIO(response.content))

                # Optional: save locally for debugging
                captcha_image_pil.save("captcha_downloaded.png")
                print(f"🖼️ CAPTCHA image downloaded from {captcha_src}")

                # Extract text using pytesseract
                captcha_answer = pytesseract.image_to_string(captcha_image_pil).strip()

                # Clean OCR result
                for ch in [" ", ".", ",", ";", "'", "\""]:
                    captcha_answer = captcha_answer.replace(ch, "")

                print(f"🔠 CAPTCHA interpreted as: '{captcha_answer}'")

            except Exception as captcha_ex:
                print(f"⚠️ CAPTCHA download or OCR failed: {captcha_ex}")
                continue

            # Delay before entering CAPTCHA
            time.sleep(7)

            # Enter CAPTCHA and submit
            captcha_input = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_TextBox1')
            captcha_input.send_keys(captcha_answer + Keys.ENTER)

            # ================= PAGE 3 =================
            # Wait for result to load
            time.sleep(7)

            try:
                # Grab result details
                name_elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_lblNameGrading'))
                )
                roll_elem = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_lblRollNoGrading')
                result_status_elem = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_lblResultNewGrading')
                sgpa_elem = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_lblSGPA')
                cgpa_elem = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_lblcgpa')

                # Extract text
                name = name_elem.text.strip()
                roll = roll_elem.text.strip()
                result_status = result_status_elem.text.strip()
                sgpa = sgpa_elem.text.strip()
                cgpa = cgpa_elem.text.strip()

                # Print result to console
                print(f"✅ Result for {roll}: {name}")
                print(f"Result Status: {result_status}, SGPA: {sgpa}, CGPA: {cgpa}")

                # Save result to CSV
                save_result_to_csv(roll, name, result_status, sgpa, cgpa, output_csv)
                print(f"📁 Data saved to {output_csv}")

            except Exception as data_ex:
                print(f"⚠️ Could not fetch result data for roll {roll_number}: {data_ex}")

            # ================= RESET FORM =================
            reset_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnReset'))
            )
            reset_button.click()

        except Exception as ex:
            print(f"❌ Error occurred for roll number {roll_number}: {ex}")
            continue

    print("\n🎉 All roll numbers processed.")
    input("Press Enter to close the browser...")

except Exception as e:
    print("❌ Fatal error:", e)
    print(traceback.format_exc())

finally:
    driver.quit()
    print("🚪 Browser closed.")
