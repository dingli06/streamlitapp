import  streamlit as st
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
side=st.sidebar
side.title("Welcome Here")
classes=["智能科学与技术19-1","智能科学与技术19-2","大数据科学与技术19-1","大数据科学与技术19-2"]
sheets=["sheet1","sheet2","sheet3","sheet4"]
choose=st.selectbox("选择班级",classes)
if choose:
    xls=pd.read_excel("score.xls",sheet_name=sheets[classes.index(choose)])
    st.table(xls.sort_values(by="折合成绩",ascending=False))
fig,ax=plt.subplots()
y,x,p=ax.hist(xls["折合成绩"],bins=5,edgecolor='k')
x_=[(x[i]+x[i+1])/2 for i in range(len(x)-1)]
ax.set_xticks(x)
for i,j in zip(x_,y):
    ax.text(i-0.2,j+0.1,str(int(j)))
ax.plot(x_,y)
plt.style.use("dark_background")
st.write(fig)
