import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from stock_response import *

# Function for getting user from
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_2EoyP"]')
    new_chat.click()
    # Enter the name of chat
    new_user = chrome_browser.find_element_by_xpath('//div[@class="J3VFH"]')
    new_user.send_keys(user_name)

    time.sleep(1)

    try:
        # Select for the title having user name
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        chrome_browser.close()
        print(e)
        sys.exit()


if __name__ == '__main__':
    input_string_stocks = input("Enter stock symbols separated by space :")
    #Following is the stock list whose price is to be obtained
    
    
    input_string_contacts = input("Enter the contact names separated by space :")
    #following is the contact list where the bot's response is to be sent
    user_name_list = input_string_contacts.split(" ")
    
    input_string = input("Enter stock symbols separated by space :")
    #Following is the stock list whose price is to be obtained
    stocks = input_string.split(" ")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:/Users/HP/AppData/Local/Google/Chrome/User Data/Default')
    options.add_argument('--profile-directory=Default')

    # Register the drive
    chrome_browser = webdriver.Chrome(executable_path='E:\hackJOURNEY\Projects\WhatsappBot\chromedriver',
                                      options=options)  # Change the path as per your local dir.
    chrome_browser.get('https://web.whatsapp.com/')

    # Sleep to scan the QR Code
    time.sleep(15)

    for user_name in user_name_list:
        try:
            # Select for the title having user name
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)
    
        # Typing message into message box
        message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
        message_box.send_keys(res(stocks))
        time.sleep(1)
        # Click on send button
        message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
        message_box.click()