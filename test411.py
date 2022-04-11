# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:34:13 2022

@author: g_s_s
"""
# =============================================================================
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# 
# 
# driver=webdriver.Chrome("C:\\Users\\g_s_s\\Desktop\\chromedriver.exe")
# 
# #driver.get("https://share.streamlit.io/hsianglioujiao/teststreamlit/main")
# #driver.get("https://www.google.com.tw")
# driver.get("https://pythonscraping.com/pages/files/form.html")
# """
# 關於版本更新的警告
# DeprecationWarning:
#     executable_path has been deprecated, please pass in a Service object
# """
# time.sleep(15)
# 
# # 定位搜尋框
# #element=driver.find_element_by_class_name("gLFyf.gsfi")
# element=driver.find_element_by_class_name("step-down.css-t2mhok.e1jwn65y2")
# # 傳入字串
# #element.send_keys("3500")
# 
# #element.send_keys(Keys.RETURN)
# 
# #button=driver.find_element_by_class_name("gNO89b")
# #button=driver.find_element_by_class_name("step-up.css-t2mhok.e1jwn65y2")
# #button.click()
# 
# 
# #driver.close()
# =============================================================================

import streamlit as st

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
