## RGPV Result Scraper

This project is a web scraper designed to automate the process of retrieving results from the RGPV (Rajiv Gandhi Proudyogiki Vishwavidyalaya) website for a list of roll numbers and saving the results to a CSV file.

### Features

- **Input from CSV**: Reads a list of roll numbers from a CSV file and iterates through each roll number.
- **Automated Web Interaction**: Navigates to the RGPV website, selects the appropriate radio button, and enters each roll number.
- **CAPTCHA Solving**: Automatically solves the CAPTCHA using OCR (Optical Character Recognition) to continue the process.
- **Result Retrieval**: After solving the CAPTCHA, the scraper submits the form and retrieves the result for each roll number.
- **Output to CSV**: Saves the results in a structured CSV file for further analysis and processing.
- **Error Handling**: Uses exception handling to skip problematic roll numbers and continue processing the remaining roll numbers without interruption.

### Prerequisites

- Python 3.x
- Selenium
- PIL (Pillow)
- pytesseract
- Edge WebDriver
- Tesseract-OCR

### Installation and Usage

1. Install the required dependencies using `pip`:
    ```shell
    pip install selenium Pillow pytesseract
    ```

2. Download and install the Edge WebDriver from the [official source](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and specify its path in the script.

3. Download and install Tesseract-OCR from the [official source](https://github.com/tesseract-ocr/tesseract) and specify its path in the script.

4. Prepare a CSV file with roll numbers in the first column. Update the script with the path to the CSV file.

5. Run the script to start scraping results and saving them to a CSV file.

### Usage Instructions

- Provide the path to the CSV file containing roll numbers in the script.
- Specify the output CSV file path to save the results.
- Run the script and observe the process in the console.
- The script will automate the process and save the results in the specified CSV file.

### Notes

- Ensure you have the required permissions to scrape data from the website.
- This script interacts with the website in real-time and may take some time to process each roll number depending on network conditions and website performance.
