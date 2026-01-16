'''
Author:     Auto Job Applier System

[REMOVED]

'''

from modules.helpers import make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
if stealth_mode:
    import undetected_chromedriver as uc
else: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg

try:
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])

    # Set up WebDriver with Chrome Profile
    options = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    # FORCE CLEAN TEMP PROFILE (DEBUG FIX)
    options.add_argument("--user-data-dir=C:\\temp\\selenium-profile")

    if stealth_mode:
        print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
        driver = uc.Chrome(options=options)
    else: 
        driver = webdriver.Chrome(options=options)

    # 🧪 DEBUG TEST — ADD THESE TWO LINES
    

    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
except Exception as e:
    error_msg = (
        "Chrome failed to start.\n\n"
        "Common causes:\n"
        "- Chrome is already running\n"
        "- Chromedriver version mismatch\n"
        "- Stealth mode instability\n\n"
        "Suggested actions:\n"
        "- Close all Chrome windows\n"
        "- Run setup/windows-setup.bat\n"
        "- Try safe_mode = True\n"
    )

    print_lg(error_msg)
    critical_error_log("Chrome startup failure", e)

    try:
        driver.quit()
    except Exception:
        pass

    raise RuntimeError("Chrome initialization failed") from e

    
