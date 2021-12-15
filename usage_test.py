from node_graph import node_graph
import streamlit as st

item_types = [
    {"title":'Purchase',"color":"rgb(255,0, 192)", "port_selection" : 'out'},
    {"title":'Inventory',"color":"rgb(255, 192, 0)", "port_selection" : 'both'},
    {"title":'Conversion',"color":"rgb(0, 192, 255)", "port_selection" : 'both'},
    {"title":'Sales',"color":"rgb(0,255, 192)", "port_selection" : 'in'},
    ]

d = node_graph(False, item_types=item_types, key="foo")

st.write(d['model'])

if st.checkbox('show second:'):
    d2 = node_graph(d['model'], item_types=item_types ,key="bar")