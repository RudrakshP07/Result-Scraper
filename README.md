Absolutely! Here’s a complete **README.md** for your project, fully updated with setup instructions, dependencies, and usage:

````markdown
# RGPV Result Automation

A Python automation script to fetch student results from RGPV's result portal, process CAPTCHA using OCR, and save the results to a CSV file.

---

## Features

- Reads roll numbers from a CSV file (`Students_Record.csv`)
- Automates form submission on the RGPV result portal
- Captures and solves CAPTCHA using Tesseract OCR
- Fetches student result data:
  - Name
  - Roll Number
  - Result Status
  - SGPA
  - CGPA
- Saves all results to a CSV file (`Students_Result_Output.csv`)
- Supports Microsoft Edge browser via Selenium WebDriver

---

## Prerequisites

- Windows OS
- Python 3.8 or higher
- Microsoft Edge browser
- Edge WebDriver matching your Edge version
- Tesseract OCR installed

---

## Files

| File | Description |
|------|-------------|
| `main.py` | Main automation script |
| `requirements.txt` | Python dependencies |
| `Students_Record.csv` | Input CSV with roll numbers |
| `Students_Result_Output.csv` | Output CSV where results will be saved |
| `setup.ps1` | Windows setup script |

---

## Setup Instructions (Windows)

1. **Clone or download** the project folder.  
2. **Open PowerShell** in the project directory.  
3. Run the following command to temporarily allow script execution and launch the setup script:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup.ps1
````

The setup script will:

* Install all Python dependencies from `requirements.txt`
* Verify Python installation
* Check for Tesseract OCR
* Check for Edge WebDriver

After setup completes successfully, run the program with:

```powershell
python main.py
```

---

## Usage

1. Prepare a CSV file (`Students_Record.csv`) with roll numbers in the **first column**.
2. Run the script:

```powershell
python main.py
```

3. The script will:

* Open Microsoft Edge
* Submit each roll number to the RGPV result portal
* Solve CAPTCHA automatically
* Fetch results (Name, Roll No., Result Status, SGPA, CGPA)
* Save results to `Students_Result_Output.csv`

4. Once all roll numbers are processed, close the browser when prompted.

---

## Python Dependencies

All required dependencies are listed in `requirements.txt`:

```text
selenium
pillow
pytesseract
```

They can be installed manually with:

```powershell
pip install -r requirements.txt
```

---

## Notes

* Ensure the **paths to Edge WebDriver and Tesseract** in `main.py` are correct:

```python
edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

* If CAPTCHA is not recognized correctly, check Tesseract installation and image quality.

* Reset button is clicked after each roll number to prepare the form for the next input.

---

## License

This project is open for personal and educational use.

```

---

If you want, I can also **update `requirements.txt` and the setup instructions** so the project can be set up in **one command**, fully ready for Windows users.  

Do you want me to do that?
```
