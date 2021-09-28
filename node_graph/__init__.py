import os
import streamlit.components.v1 as components
import json 

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "node_graph",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("node_graph", path=build_dir)

def node_graph(key=None):
    component_value = _component_func(key=key, default=None)
    try:
        return json.loads(component_value)
    except:
        return component_value

if not _RELEASE:
    import streamlit as st
    diagram = node_graph(key="foo")
    # st.write(diagram)
    if diagram['lastNodeSelected']:
        st.write(diagram['lastNodeSelected'])