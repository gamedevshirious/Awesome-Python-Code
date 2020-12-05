from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.firefox.options import Options

import smtplib
from datetime import datetime as date
today_day = date.today().strftime("%A")


def download_subscription_list():
	with open(r'E:\Dropbox\Toastmasters\test-mailing-list.txt') as f:
		list = f.readlines()
	
	ret_data = {}	
	for entry in list:
		record = entry.split(';')
		ret_data[record[1]] = {}		
		ret_data[record[1]]["name"] = record[0]
		
		rday_list = record[2].split(',')
		day_list = []
		for day in rday_list:
			day_list.append(day.strip())
		
		ret_data[record[1]]["days"] = day_list
	print(ret_data)
	return ret_data



profile = webdriver.FirefoxProfile()
profile.set_preference("network.http.pipelining", True)
profile.set_preference("network.http.proxy.pipelining", True)
profile.set_preference("network.http.pipelining.maxrequests", 8)
profile.set_preference("content.notify.interval", 500000)
profile.set_preference("content.notify.ontimer", True)
profile.set_preference("content.switch.threshold", 250000)
profile.set_preference("browser.cache.memory.capacity", 65536) # Increase the cache capacity.
profile.set_preference("browser.startup.homepage", "about:blank")
profile.set_preference("reader.parse-on-load.enabled", False) # Disable reader, we won't need that.
profile.set_preference("browser.pocket.enabled", False) # Duck pocket too!
profile.set_preference("loop.enabled", False)
profile.set_preference("browser.chrome.toolbar_style", 1) # Text on Toolbar instead of icons
profile.set_preference("browser.display.show_image_placeholders", False) # Don't show thumbnails on not loaded images.
profile.set_preference("browser.display.use_document_colors", False) # Don't show document colors.
profile.set_preference("browser.display.use_document_fonts", 0) # Don't load document fonts.
profile.set_preference("browser.display.use_system_colors", True) # Use system colors.
profile.set_preference("browser.formfill.enable", False) # Autofill on forms disabled.
profile.set_preference("browser.helperApps.deleteTempFileOnExit", True) # Delete temprorary files.
profile.set_preference("browser.shell.checkDefaultBrowser", False)
profile.set_preference("browser.startup.homepage", "about:blank")
profile.set_preference("browser.startup.page", 0) # blank
profile.set_preference("browser.tabs.forceHide", True) # Disable tabs, We won't need that.
profile.set_preference("browser.urlbar.autoFill", False) # Disable autofill on URL bar.
profile.set_preference("browser.urlbar.autocomplete.enabled", False) # Disable autocomplete on URL bar.
profile.set_preference("browser.urlbar.showPopup", False) # Disable list of URLs when typing on URL bar.
profile.set_preference("browser.urlbar.showSearch", False) # Disable search bar.
profile.set_preference("extensions.checkCompatibility", False) # Addon update disabled
profile.set_preference("extensions.checkUpdateSecurity", False)
profile.set_preference("extensions.update.autoUpdateEnabled", False)
profile.set_preference("extensions.update.enabled", False)
profile.set_preference("general.startup.browser", False)
profile.set_preference("plugin.default_plugin_disabled", False)
profile.set_preference("permissions.default.image", 2) 

options = Options()
options.headless = True
driver = webdriver.Firefox(profile, options=options)

url = "https://easy-speak.org/meetonline.php"
'''
chrome_options = Options()
#chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-data-dir=selenium")
		 
driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe', options=chrome_options)
'''

def select_tz(_driver, tz):
	ele = get_data_element(_driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[1]/td/select[2]")
	sel = Select(ele)
	sel.select_by_visible_text(tz)
	
	go = get_data_element(_driver, "/html/body/table[2]/tbody/tr/td[3]/table[2]/tbody/tr[1]/td/input")
	go.click()

def login(d):
	username = "TMShreyash"
	password = "9118b1fa"
	
	uele = get_data_element(d, "/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/span/input[2]")
	uele.send_keys(username)
	
	pele = get_data_element(d, "/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/span/input[3]")
	pele.send_keys(password)
	
	lele = get_data_element(d, "/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/input")
	lele.click()
	
	time.sleep(3)
	
def get_all_meetings():
	driver.get(url)
	print("Browser opened")
	time.sleep(5)
	
	select_tz(driver, "GMT + 5.5 Hours")
	
	
	
	data = []
	table = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/table[1]")
	for rows in table.find_elements_by_css_selector('tr')[2:]:
		row = rows.find_elements_by_tag_name('td')
		if ("restricted" in row[3].text.lower()) or (row[2].text != "English"):
			continue
		
		club = {}
		club["Time"] = row[0].text
		club["Club Name"] = row[1].text
		club["Language"] = row[2].text
		print(row[1].text)		
		club_link = row[1].find_element_by_tag_name('a').get_attribute("href")
		club["Club Link"] = club_link
		meeting_details = get_meeting_link(club_link)
		for key in meeting_details.keys():
			club[key] = meeting_details[key]
			
		data.append(club)		
	return data

def get_data_element(_driver, xpath):
	ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
	wait = WebDriverWait(_driver, 10, ignored_exceptions=ignored_exceptions)
	
	element = wait.until(
		EC.presence_of_element_located((By.XPATH, xpath)
	))
	return element

def get_meeting_link(_url):
	d = webdriver.Firefox(profile, options=options)
	meeting_info = {}
	d.get(_url)
	
	login(d)
	
	d.get(_url)
	time.sleep(3)
	
	meeting_info["Meeting Theme"] = get_data_element(d, "/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr[2]/td/table[2]/tbody/tr[1]/td[1]/span/b[1]").text																					
	try:
		meeting_info["Meeting Link"] = get_data_element(d, "/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr[2]/td/table[2]/tbody/tr[1]/td[1]/span/b[2]/b/a").get_attribute("href")
	except:
		pass
	'''
	##
	ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
	wait = WebDriverWait(d, 10, ignored_exceptions=ignored_exceptions)
	
	element = wait.until(
		EC.presence_of_element_located((By.CLASS_NAME, "genmed")
	))
	
	print("genmed: " + element.text)
	
	##
	
	profile_a_element = element.find_elements_by_tag_name('a')
	meeting_info["contact_name"] = profile_a_element.text
	user_id = profile_a_element.get_attribute("href").split("=")[-1]
	meeting_info["contact_email"] = "https://easy-speak.org/profile.php?mode=email&u="+str(user_id)+"&h=1"
	'''

	d.close()
	
	return meeting_info


def send_email(subject, body, to):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login("sad31198@gmail.com", "anilsujata")
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail("sad31198@gmail.com", to, message)
    server.quit()

def send_mail_to_users(users, msg):
	for usermail in users.keys():
		if today_day in users[usermail]["days"]:
			print("Name: " + users[usermail]["name"] + "\nEmail: " + usermail ) # + "Days: " + users[usermail]["days"])	
			msg = "Hi " + users[usermail]["name"] + ", " + msg
			send_email("#Test#", msg, usermail)

def prepare_message(meetings):
	msg = "\nList of Easy Speak meetings: \n"
	print("listed")
	msg += "\n" + "-"*15 + "\n" 
	for club in meetings:
		for key in club.keys():
			msg += key + ": " + club[key].strip() + "\n"
		msg += "\n" + "-"*15 + "\n" 
	
	msg += """
	
Regards,
----
You can find all these meetings on:
https://easy-speak.org/meetonline.php

Developer Contact:
Devkar Shreyash
+91 9623668478
----
	
	"""
	
	return msg

def main():
	meetings = get_all_meetings()
	message = prepare_message(meetings)
	
	print(message)
	
	users = download_subscription_list()
	
	send_mail_to_users(users, message)

main()
print("program terminated")
	
'''
msg += "IST " + club["meeting_time"].strip()
msg += "\nClub name: " + club["club_name"]
msg += "\nDetails: " + club["meeting_details"]
msg += "\nLanguage: "+ club["language"] + "\n\n"

Time: 14th November 20   00:30
Club Name: Albuquerque Hispano Chamber
Language: English
Meeting Theme: If I would have know what I know now...
Meeting Link: http://us04web.zoom.us/j/201004

Time:   00:35
Club Name: Club Med Toastmasters
Language: EnglishMeeting 
Theme: VeteransMeeting Link: http://zoom.us/j/Zoom389597650

Time:   01:30
Club Name: Redmond Toasters
Language: English
Meeting Theme: Attitude and Possibilities
Meeting Link: http://zoom.us/j/964594564?pwd=cGxtTWJMZW0veXlmUFVyVWVzcHd2UT09

Time:   01:35
Club Name: Downtown Lunchbunch
Language: English
Meeting Theme: World Kindness Day
Meeting Link: http://us02web.zoom.us/j/81427789297

Time:   01:45
Club Name: Torrance Chamber of Commerce
Language: English
Meeting Theme: Q&A with Clara on Hypnosis
Meeting Link: http://zoom.us/j/81698436165

Time:   02:00
Club Name: Yammertime
Language: English
Meeting Theme: Open Office Hours
Meeting Link: http://zoom.us/j/84724909463

Time:   02:30
Club Name: Create WOW!
Language: English
Meeting Theme: TBA
Meeting Link: http://zoom.us/j/7094012267

Time:   03:30
Club Name: Clover Club
Language: English
Meeting Theme: TBA
Meeting Link: http://us02web.zoom.us/j/81752909750?pwd=WkRCdU5TVWdOMHdPek9IS0

Time:   05:00
Club Name: Luminex
Language: English
Meeting Theme: Excellence
Club Link: https://easy-speak.org/view_meeting.php?t=416040

Time:   05:00
Club Name: Luminex
Language: English
Meeting Theme: Excellence
Club Link: https://easy-speak.org/view_meeting.php?t=416041

Time:   05:00
Club Name: Luminex
Language: English
Meeting Theme: Excellence
Club Link: https://easy-speak.org/view_meeting.php?t=416039


print(msg)
'''
