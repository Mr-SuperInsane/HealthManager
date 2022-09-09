import streamlit
import pandas as pd
import math

#sidebar
streamlit.sidebar.title('判定基準(成人)')
streamlit.sidebar.write('BMIの計算式は世界共通ですが、肥満の判定基準は国により異なります。')
streamlit.sidebar.write('【日本肥満学会の判定基準】')
japan_standard = pd.DataFrame({
    'BMI値':['18.5未満','18.5-25未満','25-30未満','30-35未満','35-40未満','40以上'],
    '判定':['低体重','普通体重','肥満(1度)','肥満(2度)','肥満(3度)','肥満(4度)']
})
streamlit.sidebar.table(japan_standard)
streamlit.sidebar.write('【世界保健機関(WHO)の判定基準】')
world_standard = pd.DataFrame({
    'BMI値':['16未満','16-17未満','17-18.5未満','18.5-25未満','25-30未満','30-35未満','35-40未満','40以上'],
    '判定':['痩せすぎ','痩せ','痩せぎみ','普通体重','前肥満','肥満(1度)','肥満(2度)','肥満(3度)']
})
streamlit.sidebar.table(world_standard)

#body
streamlit.title('HealthManager')
streamlit.write('RevoTech')
streamlit.header('計算')
streamlit.write('身長と体重から適正体重とBMI(肥満度)を計算します。(数値をタップして直接入力できます)')
height = streamlit.number_input('身長(cm)',0,200,160)
weight = streamlit.number_input('体重(kg)',0,100,50)
heightm = height/100 #身長をcm>>mに変換
height2 = heightm*heightm #身長の２乗を計算
bmi2 = weight/height2 #BMIを計算
bmi = round(bmi2,1) #少数第１位までを表示
appropriate_weight = math.floor(height2*22) #適正体重を計算
than = math.floor(weight-appropriate_weight) #適正体重と体重の差を計算
if streamlit.button('計算'):
    streamlit.write('適正体重：',appropriate_weight,'kg')
    streamlit.write('適正体重と比較：',than,'kg')
    streamlit.write('BMI：',bmi)
    if bmi<18.5:
        streamlit.write('あなたは<span style="color:red">低体重</span>です',unsafe_allow_html=True)
    elif 18.5 <= bmi <25.0:
        streamlit.write('あなたは<span style="color:red">普通体重</span>です',unsafe_allow_html=True)
    elif 25 <= bmi < 30:
        streamlit.write('あなたは<span style="color:red">肥満(1度)</span>です',unsafe_allow_html=True)
    elif 30 <= bmi < 35:
        streamlit.write('あなたは<span style="color:red">肥満(2度)</span>です',unsafe_allow_html=True)
    elif 35 <= bmi < 40:
        streamlit.write('あなたは<span style="color:red">肥満(3度)</span>です',unsafe_allow_html=True)
    elif bmi <= 40:
        streamlit.write('あなたは<span style="color:red">肥満(4度)</span>です',unsafe_allow_html=True)
streamlit.title('')
streamlit.title('')
streamlit.header('BMIとは')
streamlit.write('BMI(Body Mass Index)はボディマス指数と呼ばれ、体重と身長から算出される肥満度を表す体格指数です。子供には別の指数が存在しますが、成人ではBMIが国際的な指標として用いられています。健康を維持するためには日ごろからBMIを把握することが重要です。')
streamlit.header('計算式')
streamlit.latex('BMI = 体重(kg) ÷ (身長m)^2')
streamlit.latex('適正体重 = (身長m)^2 × 22')
streamlit.header('適正体重')
streamlit.write('日本肥満学会では、BMIが22を適正体重(標準体重)とし統計的に最も病気になりにくい体重とされています。25以上を肥満、18.5未満を低体重と分類しています。')
streamlit.header('病気のリスク')
streamlit.write('肥満は糖尿病・高血圧・脂質異常などの生活習慣病にかかるリスクが高くなります。痩せは栄養不良・慢性進行性疾患などが生じることがあります。妊婦の場合は肥満(BMIが25以上)になると妊娠高血圧症候群・妊娠糖尿病・巨大時の発症率・帝王切開率が高くなり、痩せ(BMIが18.5未満)になると切迫早産・早産・低出生体重児を出産するとリスクが高くなります。')
streamlit.header('メタボの関係性')
streamlit.write('BMIと内臓脂肪は必ずしも相関しないため、メタボの診断基準には盛り込まれていませんが、メタボ予備軍を拾い上げるために特定健診・特定保健指導の基準には採用されています。')
streamlit.write('Developed by RT-Naokun @2020')
