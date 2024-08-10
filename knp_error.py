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
    eye=dict(x=0, y=3, z=3))

fig_test.update_layout(scene_camera=camera)

#fig_test.update_traces(surface_count=1, selector=dict(type='isosurface'))
fig_test.update_layout(autosize=True,width=2500,height=600, margin=dict(t=0, l=0, b=0, r=0),)
fig_test.update_layout(scene = dict(xaxis = dict(title='Blok AA', showticklabels=False),
                    yaxis = dict(title='Depth', showticklabels=False),
                    zaxis = dict(title='Level', showticklabels=False), ))

fig_test.update_layout(scene_aspectmode='data')
st.subheader('VISUALISASI PENYIMPANAN BLOK AA')
#st.plotly_chart(fig_test)




new2=pd.read_csv('new2.csv', delimiter=';',decimal=',', dtype={'batchvendor':str}) 
result_new = new2.loc[new2.index.repeat(new2.qtybag)]
#result_new['total_loc'] = (result_new['loc_new'] != result_new['loc_new'].shift(1)).cumsum()
#result_new['count'] = result_new.groupby('loc_new')['loc_new'].transform('count')
result_new["seq"] = result_new.groupby("loc_new").cumcount() + 1


kode_seq = {1:'BW_1', 2:'AT_1', 3:'BW_2', 4:'AT_2', 5:'BW_3', 6:'AT_3', 7:'BW_4', 8:'AT4',
         9:'BW_1', 10:'AT_1', 11:'BW_2', 12:'AT_2', 13:'BW_3', 14:'AT_3', 15:'BW_4', 16:'AT4'}

result_new['posisi']=[kode_seq[x] for x in result_new['seq']]

result_new['x1']= result_new['bayint']-1
result_new['x2']= result_new['bayint']-1
result_new['x3']= result_new['bayint']-1
result_new['x4']= result_new['bayint']-1
result_new['x5']= result_new['bayint']-0.05
result_new['x6']= result_new['bayint']-0.05
result_new['x7']= result_new['bayint']-0.05
result_new['x8']= result_new['bayint']-0.05

#result_new['y1']= result_new['seq']


#BW_1A = ['y1':0.95, 'y2':0.00, 'y3':0.95,	'y4':0.00,	'y5':0.95,	'y6':0.00,	'y7':0.95,	'y8':0.00]
BW_1A = ['0.95,0.00,0.95,0.00,0.95,0.00,0.95,0.00']
AT_1 = [0.95,	0.00,	0.95,	0.00,	0.95,	0.00,	0.95,	0.00]
BW_2 = ['1.95,1.00,1.95,1.00,1.95,1.00,1.95,1.00']
AT_3 = {1.95,	1.00,	1.95,	1.00,	1.95,	1.00,	1.95,	1.00}
BW_4 = {2.95,	2.00,	2.95,	2.00,	2.95,	2.00,	2.95,	2.00}
AT_4 = {2.95,	2.00,	2.95,	2.00,	2.95,	2.00,	2.95,	2.00}
BW_5 = {3.95,	3.00,	3.95,	3.00,	3.95,	3.00,	3.95,	3.00}
AT_5 = {3.95,	3.00,	3.95,	3.00,	3.95,	3.00,	3.95,	3.00}
BW_6 = {4.95,	4.00,	4.95,	4.00,	4.95,	4.00,	4.95,	4.00}
AT_6 = {4.95,	4.00,	4.95,	4.00,	4.95,	4.00,	4.95,	4.00}
BW_7 = {5.95,	5.00,	5.95,	5.00,	5.95,	5.00,	5.95,	5.00}
AT_7 = {5.95,	5.00,	5.95,	5.00,	5.95,	5.00,	5.95,	5.00}
BW_8 = {6.95,	6.00,	6.95,	6.00,	6.95,	6.00,	6.95,	6.00}
AT_8 = {6.95,	6.00,	6.95,	6.00,	6.95,	6.00,	6.95,	6.00}


#result_new['y1'],['y2'],['y3'],['y4'],['y5'],['y6'],['y7'],['y8'] = result_new['posisi'].apply(lambda x:  BW_1A if x=='BW_1' else None)
#result_new[['y1','y2','y3','y4','y5','y6','y7','y8']] = result_new['posisi'].apply(lambda x:  BW_1A if x=='BW_1' else None)
result_new['gab'] = result_new['posisi'].apply(lambda x:  BW_1A if x=='BW_1' else BW_2)
result_new[['y1','y2','y3','y4','y5','y6','y7','y8']] = result_new['gab'].str.split(',', n=1, expand=True)



#df[['A', 'B']] = df['AB'].str.split(' ', n=1, expand=True)
#df[['First Name', 'Last Name']] = df['Name'].str.split(' ', expand=True)


result_new['test'] = result_new['seq'].apply(lambda x: 'genap' if x %2 ==  0 else 'ganjil')



st.dataframe(result_new.head(30))
st.text(result_new.dtypes)


