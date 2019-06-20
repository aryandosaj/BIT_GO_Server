import urllib.request as ul
from selenium import webdriver
from PIL import Image
import pytesseract as pt
import parser
browser = webdriver.Chrome(
    '/home/aryandosaj/Desktop/Flask_Web_Hook/chromedriver')
def get_detail(roll,pas):
    browser.get('https://erp.bitmesra.ac.in')
    image = browser.find_elements_by_tag_name('img')
    list_of_images = []
    for i in image:
        list_of_images.append(i.get_attribute('src'))
    browser.get(list_of_images[1])
    browser.save_screenshot('captha.png')
    browser.back()
    username = browser.find_element_by_id('txt_username')
    username.send_keys(roll)
    password = browser.find_element_by_id('txt_password')
    password.send_keys(pas)
    captha_txt = (pt.image_to_string(Image.open('captha.png'),lang='eng'))
    print(captha_txt)
    captha = browser.find_element_by_id('txtcaptcha')
    captha.send_keys(captha_txt)
    login = browser.find_element_by_id('btnSubmit')
    login.click()
    browser.get('https://erp.bitmesra.ac.in/Academic/Comprehensive_Stud_Report1.aspx?pageno=76')
    student_detail = browser.page_source
    return parser.parse(student_detail)
    




    

