# https://codechalleng.es/oauth/complete/github/&response_type=code&state=dcYOJU1M0IK33oiiO6ekdg3OogeuCKPU

# https://codechalleng.es/oauth/login/github/?next=

import argparse
import os
from IPython.display import HTML

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_parser():
    """TODO
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", help="Authentication method: userid/github" )
    parser.add_argument("-u", "--userid", help="User id" )
    parser.add_argument("-p", "--password", help="password" )
    parser.add_argument("-a", "--action", help="action - get, test, run, submit")
    return parser    

def get_url(auth):
    url = ""
    base_url = "https://codechalleng.es"
    userid_login_url = f"{base_url}/login/"
    github_login_url = f"{base_url}/oauth/login/github/?next="
    if auth == 'userid':
        return userid_login_url
    elif auth == 'github':
        return github_login_url
    else:
        return None


def login( url, userid, password):


    WAIT_SECONDS = 2
    CODE_TEMPLATE = ""
    TEST_NAME = ""
    CODE_TEST = ""


    # Set options to be headless, ..
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Open it, go to a website, and get results
    #driver = webdriver.Chrome('chromedriver', options=options)
    driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', options=options)

    driver.get(LOGIN_URL)
    
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD + Keys.RETURN)

driver.find_element_by_name('login').send_keys('pavanraomr@gmail.com')
driver.find_element_by_name('password').send_keys('calCPR!23' + Keys.RETURN)

def get_bite(driver, bite_no):
    pass

def test_bite(driver, bite_no):
    pass

def run_bite(driver, bite_no):
    pass

def submit_bite(driver, bite_no):
    pass

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    driver = login(get_url(args.auth), args.userid, args.password)


    