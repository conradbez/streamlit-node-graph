from node_graph import node_graph
import streamlit as st
import json

MODEL = False
MODEL = """ 
{
  "id": "b4175c1f-81de-4b60-8dec-699925330c33",
  "offsetX": 0,
  "offsetY": 0,
  "zoom": 100,
  "gridSize": 0,
  "layers": [
    {
      "id": "ee417f6a-5114-4497-998e-557a34c00d58",
      "type": "diagram-links",
      "isSvg": true,
      "transformed": true,
      "models": {}
    },
    {
      "id": "5941ab7b-e947-498f-a08b-a328f46ce4f7",
      "type": "diagram-nodes",
      "isSvg": false,
      "transformed": true,
      "models": {
        "bf4278c8-4a5c-40d2-85fe-1e71a3ab455c": {
          "id": "bf4278c8-4a5c-40d2-85fe-1e71a3ab455c",
          "type": "Purchase",
          "x": 100,
          "y": 83,
          "ports": [
            {
              "id": "49282e36-74a5-40f3-9d86-fbec44c26967",
              "type": "default",
              "x": 132,
              "y": 85,
              "name": "out",
              "alignment": "right",
              "parentNode": "bf4278c8-4a5c-40d2-85fe-1e71a3ab455c",
              "links": [],
              "in": false,
              "label": "out"
            }
          ],
          "name": "Untitled",
          "color": "rgb(255,0, 192)",
          "portsInOrder": [],
          "portsOutOrder": [
            "49282e36-74a5-40f3-9d86-fbec44c26967"
          ],
          "port_selection": "out"
        },
        "f99a000e-2f97-4d8a-8cf3-777624434eb2": {
          "id": "f99a000e-2f97-4d8a-8cf3-777624434eb2",
          "type": "Inventory",
          "x": 349,
          "y": 219,
          "ports": [
            {
              "id": "1be39df7-c892-4ff8-a32f-5b6f6b1c5849",
              "type": "default",
              "x": 351,
              "y": 221,
              "name": "in",
              "alignment": "left",
              "parentNode": "f99a000e-2f97-4d8a-8cf3-777624434eb2",
              "links": [],
              "in": true,
              "label": "in"
            },
            {
              "id": "b2c534a4-a7c1-45d8-8863-8522436d4b76",
              "type": "default",
              "x": 381,
              "y": 221,
              "name": "out",
              "alignment": "right",
              "parentNode": "f99a000e-2f97-4d8a-8cf3-777624434eb2",
              "links": [],
              "in": false,
              "label": "out"
            }
          ],
          "name": "Untitled",
          "color": "rgb(255, 192, 0)",
          "portsInOrder": [
            "1be39df7-c892-4ff8-a32f-5b6f6b1c5849"
          ],
          "portsOutOrder": [
            "b2c534a4-a7c1-45d8-8863-8522436d4b76"
          ],
          "port_selection": "both"
        },
        "798132bd-bcb9-429c-bddd-b3f21cfdef66": {
          "id": "798132bd-bcb9-429c-bddd-b3f21cfdef66",
          "type": "Conversion",
          "x": 88,
          "y": 142,
          "ports": [
            {
              "id": "cb7e145f-1fd8-4533-b155-6a0d277d051a",
              "type": "default",
              "x": 90,
              "y": 144,
              "name": "in",
              "alignment": "left",
              "parentNode": "798132bd-bcb9-429c-bddd-b3f21cfdef66",
              "links": [],
              "in": true,
              "label": "in"
            },
            {
              "id": "ba36fee8-84dd-494d-9ca6-172f9ce1925e",
              "type": "default",
              "x": 120,
              "y": 144,
              "name": "out",
              "alignment": "right",
              "parentNode": "798132bd-bcb9-429c-bddd-b3f21cfdef66",
              "links": [],
              "in": false,
              "label": "out"
            }
          ],
          "name": "Untitled",
          "color": "rgb(0, 192, 255)",
          "portsInOrder": [
            "cb7e145f-1fd8-4533-b155-6a0d277d051a"
          ],
          "portsOutOrder": [
            "ba36fee8-84dd-494d-9ca6-172f9ce1925e"
          ],
          "port_selection": "both"
        },
        "ad1050e0-d301-4361-9446-7fc37e888d24": {
          "id": "ad1050e0-d301-4361-9446-7fc37e888d24",
          "type": "Sales",
          "x": 291,
          "y": 150,
          "ports": [
            {
              "id": "8e161a38-8c5b-4fe3-adca-305e4b3b84e6",
              "type": "default",
              "x": null,
              "y": null,
              "name": "in",
              "alignment": "left",
              "parentNode": "ad1050e0-d301-4361-9446-7fc37e888d24",
              "links": [],
              "in": true,
              "label": "in"
            }
          ],
          "name": "Untitled",
          "color": "rgb(0,255, 192)",
          "portsInOrder": [
            "8e161a38-8c5b-4fe3-adca-305e4b3b84e6"
          ],
          "portsOutOrder": [],
          "port_selection": "in"
        }
      }
    }
  ]
}
"""
MODEL = json.loads(MODEL)

item_types = [
    {"title":'Purchase',"color":"rgb(255,0, 192)", "port_selection" : 'out'},
    {"title":'Inventory',"color":"rgb(255, 192, 0)", "port_selection" : 'both'},
    {"title":'Conversion',"color":"rgb(0, 192, 255)", "port_selection" : 'both'},
    {"title":'Sales',"color":"rgb(0,255, 192)", "port_selection" : 'in'},
    ]

d = node_graph(
  MODEL, 
  item_types = item_types,
  key="foo",
  )

st.write(d['model'])


