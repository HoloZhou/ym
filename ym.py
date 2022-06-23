# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:08:34 2022

@author: Zhou N
"""


import numpy as np 
import pandas as pd



from tensorflow.keras.models import load_model

ann = load_model('heart.h5')



import streamlit as st
from PIL import Image
image1 = Image.open('image.png')
image2 = Image.open('image2.png')


col1, col2=st.columns([2,3])

with st.sidebar:
    st.title('影像辅助诊断系统')   
    st.image(image)
    st.subheader('基本信息')
    st.text_input('姓名')
    age=st.number_input('年龄')
    gender=st.selectbox('性别',options=('男','女'))
    if gender=='男':
        sex=1
    else:
        sex=0
    
    
with col1:
    st.subheader('影像资料上传区')
    st.image(image2)

with col2:
    st.subheader('预测结果')
    outcome=dis(output)
    st.write('预测结果为',outcome)  
    st.subheader('未来5年心脑血管病趋势预测')  
    vessels=np.random.rand(5,2) 
    line_data = pd.DataFrame(
    vessels,
    columns=['心脏病风险', '卒中风险'])
   
    st.line_chart(line_data,use_container_width=True,height=240)   

    st.subheader('癌前病变风险评估') 
    x = ('黏膜白斑','腺瘤性肠息肉','慢性萎缩性胃炎','乳腺囊性增生','肝硬化')
    y = np.random.rand(5,1) 
    chart_data= pd.DataFrame(
        y,index=x,columns=['风险程度'])
    st.bar_chart(chart_data,use_container_width=True,height=240)




    
