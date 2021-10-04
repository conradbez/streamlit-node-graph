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
    print(build_dir)
    _component_func = components.declare_component("node_graph", path=build_dir)

def node_graph(model = False, key="foo") -> dict:
    try:
        assert type(model) == type(True) or type(model) == type({}) 
    except:
        raise "needs to be a bool or dict passed node_graph as model param"
    
    default_compoennt_value = json.dumps({'model': model, 'lastNodeSelected': None})
    if model:
        model=json.dumps(model)
    component_value = _component_func(model=model, key=key, default=default_compoennt_value)
    
    return json.loads(component_value)

if not _RELEASE:
    import streamlit as st
    diagram = node_graph()
    st.write(diagram)
