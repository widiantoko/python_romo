import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Storage_Warehouse",
    layout="centered",)


storage=pd.read_csv('uji_coba.csv', delimiter=';',decimal=',', dtype={'Aisle':str}) 
storage['posisi']=storage["Zona"].apply(str)+"."+storage["Aisle"].apply(str)
storage['color'] = storage['Nm_Brg'].apply(lambda x: 'balance' if x == 'Dragon' else 'Plasma')


#for a in storage['position']:
x_gab=storage[['x1','x2','x3','x4','x5','x6','x7','x8']].values.tolist()
y_gab=storage[['y1','y2','y3','y4','y5','y6','y7','y8']].values.tolist()
z_gab=storage[['z1','z2','z3','z4','z5','z6','z7','z8']].values.tolist()
v_gab=storage[['No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch','No_Batch']].values.tolist()
hvr_txt=storage[['Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg','Nm_Brg' ]].values.tolist()
pick_color = storage['color'].tolist()
lokasi = storage[['posisi','posisi','posisi','posisi','posisi','posisi','posisi','posisi']].values.tolist()

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
        font_family="Arial"),)




fig_test.update_layout(autosize=True,width=2000,height=600, margin=dict(t=0, l=0, b=0,),)
fig_test.update_layout(scene = dict(xaxis = dict(title='Blok AB',tickangle=0, labelalias= {0:'', 
                                                                                             0.5: 'AB.01', 
                                                                                             1:'', 
                                                                                             1.5:'AB.02', 
                                                                                             2:'',
                                                                                             2.5:'AB.03',
                                                                                             3:''
                                                                                             }),
                    yaxis = dict(title='Depth', showticklabels=False),
                    zaxis = dict(title='Level', showticklabels=False), ))


st.subheader('VISUALISASI PENYIMPANAN DI GUDANG - AAA')
st.plotly_chart(fig_test)




storage_new=pd.read_csv('uji_coba_baru.csv', delimiter=';',decimal=',', dtype={'aisle':str}) 




storage_new['color'] = storage_new['nm_brg'].apply(lambda x: 'balance' if x == 'Dragon' else 'Plasma')


#for a in storage['position']:
x_gab_new=storage_new[['x1','x2','x3','x4','x5','x6','x7','x8']].values.tolist()
y_gab_new=storage_new[['y1','y2','y3','y4','y5','y6','y7','y8']].values.tolist()
z_gab_new=storage_new[['z1','z2','z3','z4','z5','z6','z7','z8']].values.tolist()
v_gab_new=storage_new[['no_batch','no_batch','no_batch','no_batch','no_batch','no_batch','no_batch','no_batch']].values.tolist()
hvr_txt_new=storage_new[['nm_brg','nm_brg','nm_brg','nm_brg','nm_brg','nm_brg','nm_brg','nm_brg' ]].values.tolist()
pick_color_new = storage_new['color'].tolist()
lokasi_new = storage_new[['posisi','posisi','posisi','posisi','posisi','posisi','posisi','posisi']].values.tolist()

#st.text(storage['posisi'])

fig_test_new = go.Figure()
i = 0
while i < len(x_gab):
    fig_test_new.add_trace(go.Isosurface(
        x=x_gab_new[i],
        y=y_gab_new[i],
        z=z_gab_new[i],
        value=v_gab_new[i],
        showscale=False,
        opacity=1,
        colorscale=pick_color_new[i],
        text=lokasi_new[i],
        hovertext=hvr_txt_new[i],
        hovertemplate=
            "<b>Lokasi:</b> %{text}"
            "<br><b>Produk:</b> %{hovertext}" 
            "<br><b>Batch:</b> %{value:d3-format} <extra></extra>"


        
       ))
    i += 1  # Update kondisi iterasi

 
fig_test_new.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Arial"),)




fig_test_new.update_layout(autosize=True, width=1000,height=1000, margin=dict(t=0, r=0, l=0, b=0,),)

fig_test_new.update_layout(scene = dict(xaxis = dict(title='Blok AA',tickangle=0, showticklabels=False),
                    yaxis = dict(title='Depth', showticklabels=False),
                    zaxis = dict(title='Level', showticklabels=False), ))




st.plotly_chart(fig_test_new)
