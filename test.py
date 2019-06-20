import urllib.request as ul
from selenium import webdriver
from PIL import Image
import pytesseract as pt
from bs4 import BeautifulSoup


browser = webdriver.Chrome(
    '/home/aryandosaj/Desktop/Flask_Web_Hook/chromedriver')
browser.get('https://erp.bitmesra.ac.in')
image = browser.find_elements_by_tag_name('img')
list_of_images = []
for i in image:
    list_of_images.append(i.get_attribute('src'))
browser.get(list_of_images[1])
browser.save_screenshot('captha.png')
browser.back()
username = browser.find_element_by_id('txt_username')
username.send_keys('BE/10080/17')
password = browser.find_element_by_id('txt_password')
password.send_keys('Gudda@1999')
captha_txt = (pt.image_to_string(Image.open('captha.png'), lang='eng'))
print(captha_txt)
captha = browser.find_element_by_id('txtcaptcha')
captha.send_keys(captha_txt)
login = browser.find_element_by_id('btnSubmit')
login.click()

browser.get(
    'https://erp.bitmesra.ac.in/Academic/Comprehensive_Stud_Report1.aspx?pageno=76')
page = browser.page_source


soup = BeautifulSoup(page, 'html.parser')
attendance = soup.find("div", {"id": "divAttendance"})
table_head = attendance.find('thead')
table_head = table_head.find_all('th')
attendance_heading = []
for element in table_head:
    attendance_heading.append((element.contents[0]).strip())
attandance_body = attendance.find('tbody')
attandance_body = attandance_body.find_all('tr')
attendance_body_content = []
for entry in attandance_body:
    temp = entry.find_all('td')
    t = []
    for d in temp:
        t.append(d.contents[0].strip())
    attendance_body_content.append(t)

examination = soup.find("div", {"id": "divTestMark"})
examination = examination.find_all('tbody')
examination = examination[0].find_all('tr')
examination_heading = []
examination_body = []


for element in examination[0].find_all('th'):
    examination_heading.append(element.contents[0].strip())
for element in examination[1:]:
    # print(element)
    t = []
    for d in element.find_all('td'):
        t.append(d.contents[0].strip())
    examination_body.append(t)

result = soup.find("div", {"id": "div37419"})
result = result.find('tbody')
result = result.find_all('tr')

result_heading = []
result_body = []

for element in result[0].find_all('th'):
    result_heading.append(element.contents[0].strip())
for element in result[1:]:
    t = []
    for d in element.find_all('td')[:2]:
        t.append(d.contents[0].strip())
    ele = element.find_all('span')
    for d in ele:
        t.append(d.contents[0].strip())
    result_body.append(t)

content = {
    'Attendance':
        {
            'heading': attendance_heading,
            'body': attendance_body_content
        },
    'Examination': {
        
            'heading': examination_heading,
            'body': examination_body
        
        },
    'Result':
        {
            'heading': result_heading,
            'body': result_body
        }
}
