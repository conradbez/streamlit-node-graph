

# Usage

## Installation

`pip install streamlit-node-graph`

## Create a graph element

```

# define items the user can use
item_types = [
        {"title":'Test 1',"color":"rgb(255,0, 192)", "port_selection" : 'out'},
        {"title":'Test 2',"color":"rgb(255, 0, 192)", "port_selection" : 'in'},
        {"title":'Test 3',"color":"rgb(0,255, 192)", "port_selection" : 'both'},
    ]

diagram = node_graph.node_graph(model=model, item_types=item_types, key='test' )
st.write(diagram['selected']) # access currently selected node id
st.write(diagram['model']) # access the underlysing model
```

## Features

 - specify a node icon with the icon property e.g. ` {"title":'Purchase',"color":"rgb(255,0, 192)", "port_selection" : 'out', "icon" : 'shopping-cart'}` (icons in the font-awesome collection can be used)
 - use diagram utils

# Contribute

## Start dev 
`cd node_graph/frontend && npm install && npm run start`

uncomment `# _RELEASE = True` in `node_graph/__init__.py` and in another shell
`streamlit run node_graph/__init__.py `

## Build
`cd node_graph/frontend && npm build`
`cd../..`
`rm -rf dist/*`
`python setup.py sdist bdist_wheel`

## Upload
1. Change version in `setup.py`
2. `twine upload dist/*`