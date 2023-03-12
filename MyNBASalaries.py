from multiprocessing.sharedctypes import Value
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
title = driver.title
driver.implicitly_wait(0.5)


df = pd.DataFrame(columns=['Player','Salary','Year']) # creates master dataframe 

for yr in range(1990,2022):
    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements(by=By.CLASS_NAME, value='name')
    salaries = driver.find_elements(by=By.CLASS_NAME, value='hh-salaries-sorted')
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
    
    data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
    temp_df['Year'] = yr # adds season beginning year to each dataframe
    df = df.append(temp_df) # appends to master dataframe
    
driver.close()
driver.quit()

df.to_csv('salaries.csv', index=False)