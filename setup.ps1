Write-Host "=== RGPV Result Automation Setup ===" -ForegroundColor Cyan

# Allow script execution (temporary)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Check Python
Write-Host "`nChecking Python..."
$pythonVersion = python --version 2>$null
if (-not $pythonVersion) {
    Write-Host "❌ Python not found. Install it from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
} else {
    Write-Host "✅ Python detected: $pythonVersion" -ForegroundColor Green
}

# Install dependencies
if (Test-Path "requirements.txt") {
    Write-Host "`nInstalling dependencies..."
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed." -ForegroundColor Green
} else {
    Write-Host "⚠️ requirements.txt not found." -ForegroundColor Yellow
}

# Check Tesseract OCR
$tesseractPath = "C:\Program Files\Tesseract-OCR\tesseract.exe"
if (Test-Path $tesseractPath) {
    Write-Host "✅ Tesseract found." -ForegroundColor Green
} else {
    Write-Host "❌ Tesseract not found. Install from: https://github.com/UB-Mannheim/tesseract/wiki" -ForegroundColor Red
}

# Check Edge WebDriver
$edgeDriverPath = "C:\edgedriver_win64\msedgedriver.exe"
if (Test-Path $edgeDriverPath) {
    Write-Host "✅ Edge WebDriver found." -ForegroundColor Green
} else {
    Write-Host "❌ Edge WebDriver missing. Download from:" -ForegroundColor Red
    Write-Host "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
}

Write-Host "`n=== Setup Complete ===" -ForegroundColor Cyan
Write-Host "Run: python main.py" -ForegroundColor Yellow
Pause
