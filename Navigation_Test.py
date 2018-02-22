from selenium import webdriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Login_EM import CloudClass
import time


if __name__ == '__main__':
	# Create a new instance of IE driver
	driver = webdriver.Chrome()
	driver.implicitly_wait(5)
	
	#Define URL 
	url = "http://emuidemo.azurewebsites.net/index.html"	
	
	#create cloudClass object
	test = CloudClass(driver, url)
	
	# Log into page
	test.Login()
	test.systemStatus_Tab()
	test.utilityResponse_Tab()
	test.systemAccess_Tab()
	test.settings_Tab()
	test.analytics_Tab()