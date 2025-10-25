## 📘 README.md

```markdown
# 🧮 RGPV Result Automation Script

This project automates the process of fetching student result details (Name, Roll No, SGPA, CGPA, Result Status) from the **RGPV Result Portal** using **Python + Selenium**.

The script:
- Reads roll numbers from a CSV file  
- Automatically fills in the form on the website  
- Captures and reads CAPTCHA images using OCR  
- Saves extracted results into a separate CSV file  

---

## 🖥️ Features

✅ Automates RGPV result fetching  
✅ Uses OCR (Tesseract) to solve CAPTCHAs  
✅ Saves data in a clean CSV format  
✅ Handles multiple roll numbers automatically  
✅ Error handling and progress tracking built in  

---

## 🗂️ Folder Structure

```

RGPV_Result_Automation/
│
├── main.py                   # Main Python script
├── requirements.txt          # Python dependency list
├── Students_Record.csv       # Input CSV (roll numbers)
├── Students_Result_Output.csv # Output CSV (auto-created)
├── captcha_downloaded.png    # (Optional) saved CAPTCHA for debugging
└── README.md                 # Setup and usage guide

````

---

## ⚙️ Requirements

### 🧩 Software Dependencies
| Tool | Description | Download Link |
|------|--------------|---------------|
| **Python 3.8+** | Required for running the script | [python.org/downloads](https://www.python.org/downloads/) |
| **Tesseract OCR** | Image-to-text engine used for solving CAPTCHAs | [UB Mannheim Build (Windows)](https://github.com/UB-Mannheim/tesseract/wiki) |
| **Microsoft Edge** | Browser automated by Selenium | Pre-installed on Windows |
| **Edge WebDriver** | Required for Selenium to control Edge | [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |

---

## 🧾 Python Libraries

The required Python modules are listed in `requirements.txt`.  
Install them all at once using:

```bash
pip install -r requirements.txt
````

### requirements.txt

```
selenium
pillow
pytesseract
requests
```

---

## 🏗️ Windows Setup Instructions

1. **Install Python**

   * Download and install from [python.org](https://www.python.org/downloads/)
   * During installation, ✅ check **“Add Python to PATH”**

2. **Install Tesseract OCR**

   * Download from [UB Mannheim Tesseract Page](https://github.com/UB-Mannheim/tesseract/wiki)
   * Default installation path:

     ```
     C:\Program Files\Tesseract-OCR\
     ```
   * After installation, verify:

     ```bash
     tesseract --version
     ```

3. **Install Microsoft Edge WebDriver**

   * Check your Edge browser version:
     `edge://settings/help`
   * Download the matching **EdgeDriver** from:
     [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   * Extract it to:

     ```
     C:\edgedriver_win64\
     ```

4. **Install Python dependencies**

   * From your project folder:

     ```bash
     pip install -r requirements.txt
     ```

5. **Prepare CSV Input File**

   * Example `Students_Record.csv`:

     ```
     0123CS201
     0123CS202
     0123CS203
     ```

6. **Run the Script**

   ```bash
   python main.py
   ```

---

## 🧠 How It Works

1. Reads roll numbers from `Students_Record.csv`
2. Opens RGPV result portal automatically
3. Selects program & semester
4. Downloads the CAPTCHA image from the correct location (`ctl00_ContentPlaceHolder1_pnlCaptcha`)
5. Extracts text using OCR (pytesseract)
6. Submits the form and extracts:

   * Name
   * Roll No
   * Result Status
   * SGPA
   * CGPA
7. Appends the data to `Students_Result_Output.csv`

---

## 🧩 Notes

* If the CAPTCHA OCR is inaccurate, you can re-run the script — each attempt downloads a new CAPTCHA.
* The script includes built-in delays to let pages load properly.
* The file `captcha_downloaded.png` is saved for debugging purposes.
* Use a **stable internet connection** for consistent results.

---

## 🧰 Troubleshooting

| Issue                                            | Possible Cause         | Solution                                                        |
| ------------------------------------------------ | ---------------------- | --------------------------------------------------------------- |
| `ModuleNotFoundError`                            | Missing Python library | Run `pip install -r requirements.txt`                           |
| `pytesseract.pytesseract.TesseractNotFoundError` | Wrong Tesseract path   | Update `pytesseract.pytesseract.tesseract_cmd` in `main.py`     |
| CAPTCHA image not clear                          | Website layout change  | Recheck CAPTCHA div ID (`ctl00_ContentPlaceHolder1_pnlCaptcha`) |
| WebDriver error                                  | Edge version mismatch  | Download matching EdgeDriver version                            |

---

## 📄 License

This project is provided **for educational and personal automation use** only.
Use responsibly and in compliance with RGPV’s website policies.

---

## 👨‍💻 Author

Developed by **[Your Name]**
📧 Contact: *[youremail@example.com](mailto:youremail@example.com)*

---

```
