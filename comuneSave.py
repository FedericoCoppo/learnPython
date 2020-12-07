from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import xlrd

month_Array = ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"]

# READ FROM EXCEL
excel_file_name = input('Enter excel file name:')

workbook = xlrd.open_workbook(excel_file_name + '.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)
CFList = []
CFData = []
CFHour = []

for i in range(1, sheet.nrows):
    CFList.append(sheet.cell(i,2))
    CFData.append(xlrd.xldate.xldate_as_datetime(sheet.cell(i, 5).value, workbook.datemode))

# hour management
if len(CFList) >= 10:
    peopleForSlot = (len(CFList))/10
    peopleForSlot = int(peopleForSlot)
    if peopleForSlot < 10:
        peopleForSlot = peopleForSlot + 1
else:
    peopleForSlot = 1

for i in range(0, len(CFList)):
    if i < peopleForSlot:
        CFHour.append("08:00")
    elif i < peopleForSlot*2:
        CFHour.append("08:30")
    elif i < peopleForSlot*3:
        CFHour.append("09:00")
    elif i < peopleForSlot*4:
        CFHour.append("09:30")
    elif i < peopleForSlot*5:
        CFHour.append("10:00")
    elif i < peopleForSlot*6:
        CFHour.append("10:30")
    elif i < peopleForSlot*7:
        CFHour.append("11:00")
    elif i < peopleForSlot*8:
        CFHour.append("11:30")
    elif i < peopleForSlot*9:
        CFHour.append("12:00")
    else:
        CFHour.append("12:30")

usr = input('Enter your username: ')
pwd = input('Enter your password: ')
pin = input('Enter your pin: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://extracom.comune.torino.it/solidapp.html')

username_box = driver.find_element_by_name('j_username')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('j_password')
password_box.send_keys(pwd)

pin_box = driver.find_element_by_name('j_pin')
pin_box.send_keys(pin)

login_btn = driver.find_element_by_class_name('loginbutton')
login_btn.submit()

# wait page refresh
time.sleep(1)

for i in range(0, len(CFList)):
    # code research
    year = str(CFData[0].date().year)
    month = str(CFData[0].date().month)
    day = str(CFData[0].date().day)
    schedule = CFHour[i]
    cf = CFList[i].value
    cf_box = driver.find_element_by_name('cf')
    cf_box.send_keys(cf)
    driver.find_element_by_class_name('btn').submit()
    time.sleep(0.6)

    try:
        # appuntamento_btn = driver.find_element_by_id('ngb-nav-3') # IT CHANGE DINAMICALLY
        # appuntamento_btn.click()
        appuntamento_btn = driver.find_elements_by_class_name('nav-item')
        appuntamento_btn.pop(3).click()
    except IndexError:
        print("network delay...")
        time.sleep(4)
        appuntamento_btn = driver.find_elements_by_class_name('nav-item')
        appuntamento_btn.pop(3).click()

    modifica_btn = driver.find_element_by_class_name('btn')
    modifica_btn.click()
    time.sleep(0.5)

    # schedule
    schedule_box = driver.find_elements_by_class_name('form-control')
    h = schedule_box.pop(0)
    schedule_box.clear()
    h.send_keys(schedule)
    #schedule_box = driver.find_element_by_id('val[0]')  # change dinamically
    #schedule_box.clear()
    #schedule_box.send_keys(schedule)

    # home delivery
    search_radio = driver.find_elements_by_class_name("form-check-input")
    search_radio.pop(0)
    search_radio.pop(0).click() # NO HOME DELIVERY
    # search_radio.pop(0) # TO BE REMOVED -> FOR SMS YES
    search_radio.pop(0).click()

    # address
    addressList = driver.find_elements_by_tag_name("option")
    addressList.pop(0).click()

    # date
    date_btn = driver.find_element_by_class_name('input-group-append')
    date_btn.click()
    time.sleep(0.6)

    # year
    from_year = driver.find_elements_by_class_name('custom-select')
    select_from_year = Select(from_year.pop(1))
    select_from_year.select_by_visible_text(year)

    # month
    select_from_month = Select(from_year.pop(0))
    select_from_month.select_by_value(month)

    # keep all day for that year-month calendar
    date_box = driver.find_elements_by_class_name("ngb-dp-day")

    idx = 0
    found = False
    foundedNumber = date_box[0]
    for x in date_box:
        foundedNumber = x
        s_page = x.get_attribute("aria-label")  # keep the string value
        s_compare = day + " " + month_Array[int (month) - 1]
        if s_compare in s_page:
            found = True
            break

    # select the day
    if found == True:
        foundedNumber.click()
        print(CFList[i].value + " saved." )

    else :
        print ("error during day search")
        exit(1)

    # save button
    save_button_bar = driver.find_elements_by_class_name('btn')
    save_button_bar.pop(0).click()  # TO BE ENABLED

    # go back
    back_button_bar = driver.find_element_by_class_name('fa')
    back_button_bar.click()
    time.sleep(0.5)

print( str(len(CFList)) + " elements, " "insertion terminated!")
