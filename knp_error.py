import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Storage_Warehouse",
    layout="centered",)


storage=pd.read_csv('uji_coba.csv', delimiter=';',decimal=',')
storage['position']=storage["Zona"].astype(str)+storage["Aisle"].astype(str)+storage["Depth"].astype(str)+storage["Level"].astype(str)


#st.dataframe(storage)

print(list(storage.columns))
print(storage['Nm_Brg'].drop_duplicates())

#pilih=storage[storage['Nm_Brg']=='Dragon']



storage['color'] = storage['Nm_Brg'].apply(lambda x: 'balance' if x == 'Dragon' else 'Plasma')




#for a in storage['position']:
x_gab=storage[['x1','x2','x3','x4','x5','x6','x7','x8']].values.tolist()
y_gab=storage[['y1','y2','y3','y4','y5','y6','y7','y8']].values.tolist()
z_gab=storage[['z1','z2','z3','z4','z5','z6','z7','z8']].values.tolist()
v_gab=storage[['v1','v2','v3','v4','v5','v6','v7','v8']].values.tolist()
pick_color = storage['color'].tolist()    


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
        
    ))
    i += 1  # Update kondisi iterasi


#fig_test.add_surface(colorscale='algae', colorbar_thickness=25, colorbar_len=1.5)

fig_test.update_traces(text="ada_aza", selector=dict(type='isosurface'))
fig_test.update_traces(hovertext="apa", selector=dict(type='isosurface'))



fig_test.update_layout(autosize=True,width=2000,height=600, margin=dict(t=0, l=0, b=0,),)

fig_test.update_layout(scene = dict(xaxis = dict(title='Blok XYZ',tickangle=0, labelalias= {0:'', 
                                                                                             0.5: 'XYZ.01', 
                                                                                             1:'', 
                                                                                             1.5:'XYZ.02', 
                                                                                             2:'',
                                                                                             2.5:'XYZ.03',
                                                                                             3:''
                                                                                             }),
                    yaxis = dict(title='Depth', showticklabels=False),
                    zaxis = dict(title='Level', showticklabels=False), ))


st.subheader('VISUALISASI PENYIMPANAN DI GUDANG - AAA')
st.plotly_chart(fig_test)

