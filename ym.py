# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:08:34 2022

@author: Zhou N
"""


import numpy as np 
import pandas as pd


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
    st.subheader('诊断决策信息')
    outcome=dis(output)
    st.write('预测结果为',outcome)  
    st.subheader('卒中风险')  
    vessels=np.random.rand(5,2) 
    line_data = pd.DataFrame(
    vessels,
    columns=['腔隙性梗死', '后循环梗死'])
   
    st.line_chart(line_data,use_container_width=True,height=240)   

    st.subheader('脑内静脉窦血栓的特征权重') 
    x = ('男性患者','50岁以上','吸烟史','血栓病史','卒中家族史')
    y = np.random.rand(5,1) 
    chart_data= pd.DataFrame(
        y,index=x,columns=['权重系数'])
    st.bar_chart(chart_data,use_container_width=True,height=240)




    
