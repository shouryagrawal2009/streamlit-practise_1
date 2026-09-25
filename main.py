import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Kinematics Visualiser")

u=st.sidebar.slider("Initial velocity (m/s)",0,50, 20)
a=st.sidebar.slider("Acceleartion (m/s2)",0, 20, 10)

t= np.linspace(0, 20, 50)
X= u*t +0.5*a*t**2

fig2= go.Figure(go.Scatter(x=t, y=X, mode='lines', name='Position'))
fig2.update_layout(title="Position vs Time", xaxis_title="Time (s)", yaxis_title="Position (m)")
st.plotly_chart(fig2, use_container_width=True)

col1, col2=st.columns(2)
with col1:
  st.plotly_chart(fig, use_container_width=True)
with col2:
  st.plotly_chart(fig2, use_container_width=True)
