# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://b11test4a.mentoringmindsonline.com/mysdb_m3_test4/_design/mys/mmloginw.html")
    wd.find_element_by_id("loginUserID").click()
    wd.find_element_by_id("loginUserID").clear()
    wd.find_element_by_id("loginUserID").send_keys("113177")
    wd.find_element_by_id("userPasswd").click()
    wd.find_element_by_id("userPasswd").clear()
    wd.find_element_by_id("userPasswd").send_keys("Ctfl*5258")
    wd.find_element_by_id("sign-in").click()
    wd.find_element_by_id("reportsBigBtnBtn").click()
    wd.find_element_by_id("selectReportTypeW").click()
    wd.find_element_by_id("dijit_MenuItem_30_text").click()
    wd.find_element_by_id("dijit_MenuItem_39_text").click()
    wd.find_element_by_id("dijit_MenuItem_92_text").click()
    wd.find_element_by_id("generateReportBtn").click()
    wd.find_element_by_css_selector("#dojox_mobile_ToolBarButton_34 > span.mblToolBarButtonBody.mblColorDefault > table.mblToolBarButtonText > tbody > tr > td.mblToolBarButtonLabel").click()
    wd.find_element_by_css_selector("#dojox_mobile_ToolBarButton_4 > span.mblToolBarButtonBody.mblColorDefault > table.mblToolBarButtonText > tbody > tr > td.mblToolBarButtonLabel").click()
    wd.find_element_by_css_selector("td.mblToolBarButtonLabel").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
