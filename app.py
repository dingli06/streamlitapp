import  streamlit as st
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False

side=st.sidebar
side.title("Welcome Here")
side.image("t.jpg")
classes=["智能科学与技术19-1","智能科学与技术19-2","大数据科学与技术19-1","大数据科学与技术19-2"]
sheets=["sheet1","sheet2","sheet3","sheet4"]
choose=st.selectbox("选择班级",classes)
if choose:
    xls=pd.read_excel("score.xls",sheet_name=sheets[classes.index(choose)])
    st.table(xls.sort_values(by="折合成绩",ascending=False))
fig,(ax1,ax2)=plt.subplots(1,2)
y,x,p=ax1.hist(xls["折合成绩"],bins=5,edgecolor='k',color="#7B68EE")
x_=[(x[i]+x[i+1])/2 for i in range(len(x)-1)]
ax1.set_xticks(x)
for i,j in zip(x_,y):
    ax1.text(i-0.2,j+0.1,str(int(j)))
plt.style.use("default")
ax1.plot(x_,y,color="#6495ED",linestyle="--")
stas=xls["折合成绩"]
x1=len(stas[stas<60])
x2=len(stas[(stas>=60)&(stas<70)])
x3=len(stas[(stas>=70)&(stas<80)])
x4=len(stas[(stas>=80)&(stas<90)])
x5=len(stas[(stas>90)&(stas<100)])
all_x=[x1,x2,x3,x4,x5]
ax2.pie(
    x=all_x,
    labels=["under 60","60-70","70-80","80-90","90-100"],
autopct="%5.2f%%",
explode=(0,0.1,0.05,0.05,0.1)

)
fig.dpi=150
plt.subplots_adjust(left=0,right=1,top=1,bottom=0,hspace=0.1)
plt.tight_layout()
st.write(fig)
