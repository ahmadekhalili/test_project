from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def setup():
    chrome_options = Options()
    chrome_options.binary_location = r"C:\chrome\chrome-win64\chrome.exe"
    # حالت headless (اختیاری، چون این باینری خودش headless هست)
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    s = Service(r"C:\Users\Admin\.wdm\drivers\chromedriver\win64\135.0.7049.95\chromedriver-win32\chromedriver.exe")
    #driver = webdriver.Chrome(options=chrome_options)
    return webdriver.Chrome(options=chrome_options)
