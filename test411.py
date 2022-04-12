# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:34:13 2022

@author: g_s_s
"""


# =============================================================================
# from selenium import webdriver
# import time
# import requests
# 
# driver=webdriver.Chrome("C:\\Users\\g_s_s\\Desktop\\chromedriver.exe")
# url="https://share.streamlit.io/hsianglioujiao/map_test/main/test411.py"
# url_post="https://share.streamlit.io/api/v1/telemetry/datadog?ddforward=https://browser-http-intake.logs.datadoghq.com/v1/input/pub80bea74eec96ecfc73fa52f86798cadf?ddsource=browser&ddtags=sdk_version%3A3.11.0%2Cenv%3Aprod%2Cservice%3Aweb"
# driver.get(url)
# time.sleep(15)
# print("已等候網頁打開!")
# button=driver.find_element_by_class_name("css-po3v1j")
# print(button)
# #button.click()
# #files = {'uploadFile':open("D:\\data\\.Py202X\\66map4.csv","rb")}
# #r = requests.post(url_post,files=files)
# #print(r.text)
# =============================================================================


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
import pandas as pd


st.header("車機即時位置與車速")
st.write("自動接收訊號")
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


# =============================================================================
# uploaded_file=st.file_uploader("人工輸入檔案(略)",type=".csv")
# st.header("")
# 
# if uploaded_file:
#     df=pd.read_csv(uploaded_file)
#     map_data=df[["<latitude>", "<longitude>"]]        
#     map_data.columns=['lat','lon']
#     st.map(map_data)
# =============================================================================
