from node_graph import node_graph
import streamlit as st

d = node_graph({},key="foo")

st.write(d)