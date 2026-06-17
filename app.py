
import streamlit as st,pandas as pd,plotly.express as px
st.set_page_config(layout='wide')
st.title('AI-Powered Social Media Engagement Dashboard')
df=pd.read_csv('data/social_media_data.csv')
df['Engagement']=df['Likes']+df['Comments']+df['Shares']+df['Saves']
a,b,c,d=st.columns(4)
a.metric('Impressions',f"{df.Impressions.sum():,}")
b.metric('Reach',f"{df.Reach.sum():,}")
c.metric('Engagement',f"{df.Engagement.sum():,}")
d.metric('Avg AI Score',round(df.AIContentScore.mean(),1))
st.plotly_chart(px.bar(df.groupby('Platform')['Engagement'].sum().reset_index(),x='Platform',y='Engagement'),use_container_width=True)
st.plotly_chart(px.line(df.groupby('PostDate')['Engagement'].sum().reset_index(),x='PostDate',y='Engagement'),use_container_width=True)
