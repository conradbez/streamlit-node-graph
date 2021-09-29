from node_graph import node_graph
import streamlit as st
import json

MODEL = False
MODEL = """ 
{
  "id": "03a8393c-4900-440c-901b-a32f4a7ad4e3",
  "offsetX": 0,
  "offsetY": 0,
  "zoom": 100,
  "gridSize": 0,
  "layers": [
    {
      "id": "4a89eac4-326d-4719-807e-acb1e9da1032",
      "type": "diagram-nodes",
      "isSvg": false,
      "transformed": true,
      "models": {
        "9c1c1cf9-b93d-46e8-9130-57fb9588616e": {
          "id": "9c1c1cf9-b93d-46e8-9130-57fb9588616e",
          "type": "Inventory",
          "selected": true,
          "x": 221,
          "y": 113,
          "ports": [],
          "color": "rgb(192,0,255)"
        }
      }
    }
  ]
}
"""

d = node_graph(MODEL,key="foo")

st.write(d['model'])


