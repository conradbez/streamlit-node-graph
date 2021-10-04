from node_graph import node_graph
import streamlit as st

d = node_graph(False,key="foo")

st.write(d['model'])

if st.checkbox('show second:'):
    d2 = node_graph(d['model'],key="bar")