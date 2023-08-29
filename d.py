import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import random
import time

months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]

def main(bot, username, password, timeout):
    try:
        day = Select(bot.find_element_by_xpath('//*[@id="DayDropdown"]'))
    except:
        main(bot, username, password, timeout)
    month = Select(bot.find_element_by_xpath('//*[@id="MonthDropdown"]'))
    year = Select(bot.find_element_by_xpath('//*[@id="YearDropdown"]'))
    usernameInput = bot.find_element_by_xpath('//*[@id="signup-username"]')
    passwordInput = bot.find_element_by_xpath('//*[@id="signup-password"]')
    register = bot.find_element_by_xpath('//*[@id="signup-button"]')

    # Dob - Day Selector
    dayVal = random.randint(1, 27)
    if dayVal < 10:
        dayVal = "0" + str(dayVal)
    day.select_by_value(str(dayVal))

    # Dob - Month Selector
    monthVal = random.choice(months)
    month.select_by_visible_text(str(monthVal))

    # Dob - Year Selector
    yearVal = random.randint(1960, 2010)
    year.select_by_visible_text(str(yearVal))

    # Username
    usernameInput.clear()
    usernameInput.send_keys(username)

    # Password
    passwordInput.clear()
    passwordInput.send_keys(password)

    # Register
    register.click()
    time.sleep(timeout)

def login(username: str, password: str, timeout: int, proxyList, headless: bool = True) -> None:
    options = Options()
    options.headless = headless

    if proxyList != None:
        proxy = random.choice(proxyList)
        options.add_argument(f'--proxy-server={proxy}')
        time.sleep(12)

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    bot = webdriver.Chrome(chrome_options=options)
    bot.get("https://roblox.com")

    try:
        bot.find_element_by_xpath('//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]')
    except:
        try:
            bot.find_element_by_xpath('//*[@id="DayDropdown"]')
        except:
            login(username, password, timeout, proxyList, headless)
        login(username, password, timeout, proxyList, headless)

    if len(username) > 20:
        username = str(username[:20])

    try:
        main(bot, username, password, timeout)
    except:
        bot.close()
