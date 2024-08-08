import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Storage_Warehouse",
    layout="wide",)




#storage=pd.read_csv('test_xwh.csv', delimiter=';',decimal=',', dtype={'Aisle':str}) 
storage=pd.read_csv('text_xwh_new.csv', delimiter=';',decimal=',') 


storage['color'] = storage['Nm_Brg'].apply(lambda x: 'Sunsetdark' if x == '0052 - WANKAI' else 'tealgrn')


#for a in storage['position']:
x_gab=storage[['x1','x2','x3','x4','x5','x6','x7','x8']].values.tolist()
y_gab=storage[['y1','y2','y3','y4','y5','y6','y7','y8']].values.tolist()
z_gab=storage[['z1','z2','z3','z4','z5','z6','z7','z8']].values.tolist()
v_gab=storage[['No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch']].values.tolist()
hvr_txt=storage[['Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg' ]].values.tolist()
pick_color = storage['color'].tolist()
#lokasi = storage[['posisi','posisi','posisi','posisi','posisi','posisi','posisi','posisi']].values.tolist()
lokasi = storage[['Posisi','Posisi','Posisi','Posisi','Posisi','Posisi','Posisi','Posisi']].values.tolist()


#st.text(storage['posisi'])

fig_test = go.Figure()
i = 0
while i < len(x_gab):
    fig_test.add_trace(go.Isosurface(
        x=x_gab[i],
        y=y_gab[i],
        z=z_gab[i],
        value=v_gab[i],
        showscale=False,
        opacity=1,
        colorscale=pick_color[i],
        text=lokasi[i],
        hovertext=hvr_txt[i],
        hovertemplate=
            "<b>Lokasi:</b> %{text}"
            "<br><b>Produk:</b> %{hovertext}" 
            "<br><b>Batch:</b> %{value:d3-format} <extra></extra>"

        
       ))
    i += 1  # Update kondisi iterasi

 
fig_test.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Arial"),
        
    
        
        )

camera = dict(
    up=dict(x=0, y=0, z=1),
   center=dict(x=0, y=0, z=0),
    eye=dict(x=0, y=3.5, z=2))

fig_test.update_layout(scene_camera=camera)

#fig_test.update_traces(surface_count=1, selector=dict(type='isosurface'))
fig_test.update_layout(autosize=True,width=2500,height=600, margin=dict(t=0, l=0, b=0, r=0),)
fig_test.update_layout(scene = dict(xaxis = dict(title='Blok AA', showticklabels=False),
                    yaxis = dict(title='Depth', showticklabels=False),
                    zaxis = dict(title='Level', showticklabels=False), ))

fig_test.update_layout(scene_aspectmode='data')
st.subheader('VISUALISASI PENYIMPANAN BLOK AA')
st.plotly_chart(fig_test)



