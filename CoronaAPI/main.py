from selenium import webdriver

class CoronaAPI:
	countryWiseData ={}
	driver = None
	def createDriver(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument("--test-type")
		options.add_argument("user-data-dir=cache") 
		#options.add_argument("--start-maximized")
		options.add_argument("--headless")
		options.binary_location = "/usr/bin/chromium-browser"
		self.driver = webdriver.Chrome(chrome_options=options)
	
	def gotoLink(self):
		self.driver.get("https://www.worldometers.info/coronavirus/")

	
	def updateData(self):
		self.createDriver()
		self.gotoLink()
		
		for i in range(1, 196):
			country = self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr["+str(i)+"]/td[1]").text
			patients = self.driver.find_element_by_xpath("//*[@id='main_table_countries_today']/tbody[1]/tr["+str(i)+"]/td[2]").text
		
			self.countryWiseData[country] = patients
		
	def printData(self):
		self.updateData()
		
		print(self.countryWiseData)
		
	def getPatientCount(self, country):
		self.updateData()
		
		try:
			return self.countryWiseData[country]
		except:
			print("Please modify your search")
			return

api = CoronaAPI()
print(api.printData()[:10])


