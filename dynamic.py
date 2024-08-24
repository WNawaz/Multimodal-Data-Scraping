import sys
import csv
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
#import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# add shareet page flag: if yes add page 2 to last_url in first try line
def write_data_usimin(last_url,outfile):
 try:
  driver.get(last_url)
  #ibrahim added this code....
  wait = WebDriverWait(driver, 3)
  #time.sleep(5)  # Adjust sleep time as needed
  element = driver.find_element(By.CSS_SELECTOR, ".MuiAccordionSummary-content.MuiAccordionSummary-contentGutters.css-17o5nyn")
  driver.execute_script("arguments[0].scrollIntoView();", element)
  #element.click()
  driver.execute_script("arguments[0].click();", element)
  print('clicked ',element.text)
  wait = WebDriverWait(driver, 3)
  #time.sleep(5)  # Adjust sleep time as needed
  element = driver.find_element(By.CLASS_NAME, "list-group-item")
  driver.execute_script("arguments[0].scrollIntoView();", element)
  #element.click()
  driver.execute_script("arguments[0].click();", element)
  print('clicked ',element.text)
  print(driver.current_url)
  wait = WebDriverWait(driver, 10)
  driver.back()
  wait = WebDriverWait(driver, 3)
  driver.execute_script("window.scrollTo(0, 0);")
  wait = WebDriverWait(driver, 2)
  #till here
  print(driver.current_url)
  elements = driver.find_elements(By.XPATH, "//p[contains(@style, 'cursor: pointer')]")
  eletexts=[x.text for x in elements]
  for x in eletexts:
    print(x)
  print('now trying to click')
  for txt in eletexts:
   try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{txt}']")))
    #print(element.text)
    #elements = driver.find_elements(By.XPATH, "//p[contains(@style, 'cursor: pointer')]")
    wait = WebDriverWait(driver, 2)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    #element.click()
    driver.execute_script("arguments[0].click();", element)
    wait = WebDriverWait(driver, 2)
    print(driver.current_url)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.fatwah-ans-cont')))
    #answer
    # Get the inner HTML of the element
    html = element.get_attribute('innerHTML')
    # Use BeautifulSoup to extract the text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    answer=text.strip()
    #question
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.fatwah-ques-cont')))
    # Get the inner HTML of the element
    html = element.get_attribute('innerHTML')
    # Use BeautifulSoup to extract the text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    question=text.strip()
    # title
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.title')))
    # Get the inner HTML of the element
    html = element.get_attribute('innerHTML')
    # Use BeautifulSoup to extract the text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    title=text.strip()
    # categories
    elements = driver.find_elements(By.CLASS_NAME, 'sc-fmRtwQ.dcOjOn')
    cats=[]
    for element in elements:
      # Get the outer text
      outer_text = element.text
      # Print the outer text
      #print('printing category')
      #print(outer_text)
      cats.append(outer_text)
    with open(outfile, 'a', newline='', encoding='utf-8') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow([title,question,answer,driver.current_url]+cats)
    driver.back()
    wait = WebDriverWait(driver, 3)
    driver.execute_script("window.scrollTo(0, 0);")
    wait = WebDriverWait(driver, 2)
    print(driver.current_url)
   except Exception as e:
    print(e)
 except:
   print('outer error')

# select radio program

def dynamic_web_content(prog_url,episode,total_pages,outfile,driver_path='/usr/lib/chromium-browser/chromedriver'):
# alqa shahri
 prog_dict={'new_url':prog_url,'keyword':episode,'tot_pgs':total_pages} 
  # max total pages for episodes # #episode names e.g. 'اللقاء الشهري' prog_url=program url'''

 sys.path.insert(0,driver_path)
 # setup chrome options
 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_argument('--headless') # ensure GUI is off
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')
 # set up the webdriver
 driver = webdriver.Chrome(options=chrome_options)
 #
 for i in range(1,prog_dict['tot_pgs']+1):
  driver.get(prog_dict['new_url']+'#page='+str(i))#
  # Wait for elements to load
  wait = WebDriverWait(driver, 20)
  wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//p[contains(text(), '{prog_dict['keyword']}')]")))
  # Find all elements that contain e.g. 'الشريط رقم' in their text and get their text content
  elements = driver.find_elements(By.XPATH, f"//p[contains(text(), '{prog_dict['keyword']}')]")
  element_texts = [element.text for element in elements]
  print(element_texts)
  urls_list=[]
  for txt in element_texts:
   try:
    ### add leading space for page 1. not for page 2 onwards (the mane page e.g for noor ala darb)
    #if i==1:
    #  clickable_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{txt} ']")))## add leading space for page 1. not for page 2 onwards
    #else:
    clickable_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{txt}']")))## add leading space for page 1. not for page 2 onwards
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", clickable_element)
    # Wait for a moment to ensure scrolling is done
    time.sleep(1)#
    # Use JavaScript to click the element
    driver.execute_script("arguments[0].click();", clickable_element)
    # Wait for the page to load after the click
    time.sleep(1)
    # Capture the new URL
    urls_list.append(driver.current_url)
    driver.back()
    wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//p[contains(text(), '{prog_dict['keyword']}')]")))
   except Exception as e:
    print('not found shareet page')
    print(e)
  for shr_url in urls_list:
   for pg in range(1,3):# try for higher pages later i.e. 3 to 7
    try:
      write_data_usimin(shr_url+'#page='+str(pg))
    except:
      print('shareets subpage not found',pg)

 driver.quit()

