from selenium import webdriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime


class CloudClass:
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url
		print(self.TimeStamp() + " Web Browser Started\n") 

	

	def TimeStamp(self):
		ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		return ts

	def Loading_Element(self):
		# We have to wait for the 'loading' element to disappear
		# : need to make sure we don't prematurely check if element 
		# : isn't being blocked and disappeared before it had a chance to appear
		time.sleep(3) #give some time for spinner to show up. 
		loading_done = False
		while (loading_done == False): 
			try: 
				# if time out execeptio was raised - check the loading element again if it has disappeared.  
				loading_done = WebDriverWait(self.driver, 3).until_not(EC.visibility_of_element_located((By.XPATH, "//h1[@class='visible loading-text']")))
			except TimeoutException:
				print("Page not finished loading yet...wait another 3 seconds")
				time.sleep(3)

		return print(self.TimeStamp() + " Page finished loading")



	def Login(self):
		print(self.TimeStamp() + " Logging into Cloud App")
		# go to the home page
		self.driver.maximize_window()
		self.driver.get(self.url)
		assert "Douglas Energy Management System" in self.driver.title

		CompanyCode_Element = self.driver.find_element_by_xpath(".//*[@name='companyCode']")
		CompanyCode_Element.send_keys("######")

		userName_Element = self.driver.find_element_by_xpath(".//*[@name='userName']")
		userName_Element.send_keys("######")


		password_Element = self.driver.find_element_by_xpath(".//*[@name='password']")
		password_Element.send_keys("######")
		password_Element.submit()

		img_responsive = None
		while (img_responsive == None):
			try:
				img_responsive = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='assets/energy.png']")))
				time.sleep(2)

			except TimeoutException:
				 print("Page not finished loading yet...wait another 3 seconds")

			 
		print(self.TimeStamp() + " Login Successful")
		self.Loading_Element()




	# Go to systemStatus Tab	
	def systemStatus_Tab(self):	
		print('Changing to System Status Tab')
		systemStatus_Element = self.driver.find_element_by_xpath(".//*[@id='ngb-tab-1']")
		systemStatus_Element.click()
		# run the Loading_Element() method to wait until loading disappear
		self.Loading_Element()	
		print('System Status Page Ready\n')


	def utilityResponse_Tab(self):	
		print("Changing to Utility Response Tab")
		UtilityResponse_Element = self.driver.find_element_by_xpath(".//*[@id='ngb-tab-2']")
		UtilityResponse_Element.click()
		# run the Loading_Element() method to wait until loading disappear
		self.Loading_Element()	
		print('Utility Response Page Ready\n')

	def systemAccess_Tab(self):	
		print("Changing to System Access Tab")
		SystemAccess_Element = self.driver.find_element_by_xpath(".//*[@id='ngb-tab-3']")
		SystemAccess_Element.click()
		# run the Loading_Element() method to wait until loading disappear
		self.Loading_Element()	

		print('System Access Page Ready\n')

	def settings_Tab(self):
		print("Changing to Settings Tab")
		# Find the Tab
		Settings_Element = self.driver.find_element_by_xpath(".//*[@id='ngb-tab-4']")
		Settings_Element.click()
		# run the Loading_Element() method to wait until loading disappear
		self.Loading_Element()	

		print('Settings Page Ready\n')

	def analytics_Tab(self):
		print("Changing to Analytics Tab")	
		# Find the Tab		
		Analytics_Element = self.driver.find_element_by_xpath(".//*[@id='ngb-tab-0']")
		Analytics_Element.click()
		# run the Loading_Element() method to wait until loading disappear
		self.Loading_Element()	

		print('Analytics Page Ready\n')	




if __name__ == '__main__':
	# Define the url for the Cloud App
	url = "http://emuidemo.azurewebsites.net/index.html"
	
	# Create a new instance of IE driver
	driver = webdriver.Chrome()

	# Define implicit wait time in seconds
	driver.implicitly_wait(5)

	test = CloudClass(driver, url)
	test.Login()
	test.systemStatus_Tab()
	test.utilityResponse_Tab()
	test.systemAccess_Tab()
	test.settings_Tab()
	test.analytics_Tab()
	

