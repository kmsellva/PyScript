#import region
import csv
import datetime
import time
import webbrowser
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException,
                                        ElementNotInteractableException,
                                        MoveTargetOutOfBoundsException,
                                        InvalidElementStateException)

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import Select, WebDriverWait
from bs4 import BeautifulSoup

#endRegion

#inputRegion

url  = "https://www.makemytrip.com/flights/"

#scriptControl
wd  =   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#due to UTC time saturday is added to weekday
we =    ['Sunday']
to =    datetime.utcnow().strftime('%d/%m/%Y')
ti =    datetime.utcnow().strftime('%H:%M:%S')
day =   datetime.utcnow().strftime('%A')

def daytime():
    if day in wd:
        #no dayLight saving enable below 4 timings
        uptime      =   '10:31:00'
        uptime1     =   '23:59:00'
        uptime2     =   '00:00:00'
        downtime    =   '05:01:00'
        #if dayLight saving enable below 4 timings
        # uptime      =   '11:31:00'
        # uptime1     =   '23:59:00'
        # uptime2     =   '00:00:00'
        # downtime    =   '06:01:00'
        if day  ==  'Monday':
                    #no dayLight saving enable below 1 timings
                    downtime      =   '04:01:00'
                    #no dayLight saving enable below 1 timings
                    # downtime      =   '05:01:00'
        if ti>uptime and ti<=uptime1 or ti>=uptime2 and ti<downtime:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print(to+ " - " +day+ " - " +ti+ " UTC: Application is available, hence proceeding with transaction....")
            return True

        else:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print(to+ " - " +day+ " - " +ti+ " UTC: Application is unavailable, hence script terminated.")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            return True

    if day in we:
        #no dayLight saving enable below 3 timings
        uptime       =   '12:31:00'
        downtime     =   '23:59:00'
        downtime1    =   '04:01:00'
        #if dayLight saving enable below 3 timings
        # uptime       =   '12:31:00'
        # downtime     =   '23:59:00'
        # downtime1    =   '05:01:00'
        if ti<downtime1 or ti>uptime and ti<downtime:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print(to+ " - " +day+ " - " +ti+ " UTC: Application is available, hence proceeding with transaction....")
            return True

        else:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print(to+ " - " +day+ " - " +ti+ " UTC: Application is unavailable, hence script terminated.")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            return False

#end scriptControl

if daytime() is True:

    #region Browser Stuff
    # driver = webdriver.Ie()
    driver = webdriver.Chrome()

    print("----------------------------------")
    if driver.name == "chrome" or driver.name == "Ie":
        # print(driver.name + " browser version: " + driver.capabilities['version'])
        print(driver.name + " browser version: " + driver.capabilities['browserVersion'])

    print("--------------") 
    driver.set_window_size(1024, 768)
    # driver.maximize_window()
    #endregion

    #functions
    def loop_send_keys(elementName, elementValue):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return driver.find_element_by_xpath(elementName).send_keys(elementValue)
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_select_keys(elementName, elementValue):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return Select(driver.find_element_by_xpath(elementName)).select_by_visible_text(elementValue)
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_send_click(elementName):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return driver.find_element_by_xpath(elementName).click()
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_send_click_css(elementName):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return driver.find_element_by_css_selector(elementName).click()
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_send_click_text(elementName):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return driver.find_element_by_partial_link_text(elementName).click()
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_send_clear(elementName):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return driver.find_element_by_partial_link_text(elementName).clear()
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1

    def loop_locate(elementName):
        attempt = 1
        while True:
            try:
                time.sleep(0.9)
                return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "' + elementName + '")]')))
            except (NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementNotInteractableException,MoveTargetOutOfBoundsException,InvalidElementStateException):
                if attempt == 10:
                    raise
                attempt += 1
    #endregion

    #region Step 01
    step = "Step 01: "
    print(step+ "Load login page and validate.")
    start = time.time()

    driver.get(url)

    time.sleep(5)

    try:
        elementName = "Flights"
        start2 = time.time()
        loop_locate(elementName)
        # driver.switch_to.frame(0)
        driver.save_screenshot("Step 01: A_Screen.png")
        stop2 = time.time()
        print(step+ "Location SLA - " + str(stop2-start2))

    except:
        stop = time.time()
        print(step+ "Exception SLA - " + str(stop-start))
        raise Exception ("Element not found - " +elementName)
        print("--------------")
    
    stop = time.time()
    print(step+ "Step SLA - " + str(stop-start))
    print("--------------")
    #endregion

    #region
    step = "Step 02: "
    print(step+ " ")
    start = time.time()

    try:
        elementName = "//*[@id='SW']/div[1]/div[1]/ul/li[6]"
        loop_send_click(elementName)

        elementName = "//*[@id='fromCity']"
        elementValue = "//*[@id='react-autowhatever-1-section-0-item-7']/div/div[1]/p[1]"
        loop_send_click(elementName)        
        loop_send_click(elementValue)

        elementName = "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[2]/label/span"
        elementValue = "//*[@id='react-autowhatever-1-section-0-item-0']/div/div[1]/p[1]"
        loop_send_click(elementName)
        loop_send_click(elementValue)

        # elementName = "//*[@id='departure']"
        # loop_send_click(elementName)

        elementName = "//*[@id='root']/div/div[2]/div/div/div[2]/p/a"
        loop_send_click(elementName)
        driver.save_screenshot("Step 02: A_Screen.png")

        now = datetime.now()
        tom = (str(now.day+1) + "/" + str(now.month) + "/" + str(now.year))

        # driver.get("https://www.makemytrip.com/flight/search?itinerary=MAA-BOM-"+ tom +"&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E")

        elementName = "Flights from"
        start2 = time.time()
        loop_locate(elementName)
        driver.save_screenshot("Step 02: B_Screen.png")
        stop2 = time.time()
        print(step+ "Location SLA - " +elementName+ " is " + str(stop2-start2))

    except:
        stop = time.time()
        print(step+ "Exception SLA - " + str(stop-start))
        raise Exception ("Element not found - " +elementName)
        print("--------------")
    
    stop = time.time()
    print(step+ "Step SLA - " + str(stop-start))
    print("--------------")
    #endregion

    #region
    step = "Step 03: "
    print(step+ " ")
    start = time.time()

    try:
        for i in range(1, 10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        html = driver.execute_script("return document.documentElement.innerHTML;")

        sp = BeautifulSoup(html, "html.parser")
        # sp = BeautifulSoup(body)

        spanFlightName = sp.findAll("span", {"class": "airways-name"}) 
        pFlightCode = sp.findAll("p", {"class": "fli-code"})
        divDeptTime = sp.findAll("div", {"class": "dept-time"})
        pDeptCity = sp.findAll("p", {"class": "dept-city"})
        pFlightDuration = sp.findAll("p", {"class": "fli-duration"})
        pArrivalTime = sp.findAll("p", {"class": "reaching-time append_bottom3"})
        pArrivalCity = sp.findAll("p", {"class": "arrival-city"})
        # spanFlightCost = sp.findAll("span", {"class": "actual-price"})

        if spanFlightName:
            print(step+ "FlightsData will be saved to file")
        else: raise Exception

    except:
        stop = time.time()
        print(step+ "Exception SLA - " + str(stop-start))
        raise Exception ("No flights found -" +tom)
        print("--------------")
    
    stop = time.time()
    print(step+ "Step SLA - " + str(stop-start))
    print("--------------")
    #endregion

    #region
    step = "Step 04: "
    print(step+ " ")
    start = time.time()

    try:

        # Excel colum
        colum = [["flight_name", "flight_code", "departure_city", "arrival_city", "flight_duration", "departure_time", "arrival_time"]]

        for i in range(0, len(spanFlightName)):
            colum.append([spanFlightName[i].text, pFlightCode[i].text,  pDeptCity[i].text, pArrivalCity[i].text, pFlightDuration[i].text, divDeptTime[i].text, pArrivalTime[i].text])
            
        excel = "FlightsScheduled.csv"
        
        with open(excel, 'w', newline='') as spfile:
            wrtr = csv.writer(spfile)
            wrtr.writerows(colum)
            print (step+ "FlightsData saved to file")

    except:
        stop = time.time()
        print(step+ "Exception SLA - " + str(stop-start))
        raise Exception ("Error in " +step)
        print("--------------")
    
    stop = time.time()
    print(step+ "Step SLA - " + str(stop-start))
    print("--------------")
    print("**End**")
    #endregion