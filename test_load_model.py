from node_graph import node_graph
import streamlit as st
import json

MODEL = False
MODEL = """ 
{
  "id": "ff3b346c-432f-481a-a079-626b3cda1dce",
  "offsetX": 14.704666666666759,
  "offsetY": 22.06392044913387,
  "zoom": 94.6333333333333,
  "gridSize": 0,
  "layers": [
    {
      "id": "4891e68c-1511-4588-b5a3-e28a1fed7490",
      "type": "diagram-links",
      "isSvg": true,
      "transformed": true,
      "models": {
        "8511b203-a4a3-4fc1-955a-9f7b1f635f25": {
          "id": "8511b203-a4a3-4fc1-955a-9f7b1f635f25",
          "type": "default",
          "selected": false,
          "source": null,
          "sourcePort": null,
          "target": null,
          "targetPort": null,
          "points": [
            {
              "id": "99c967e4-2b3c-4151-8755-aed1e4116518",
              "type": "point",
              "x": 112,
              "y": 108
            },
            {
              "id": "7d10b609-7ce6-442c-a44f-20425ebd94aa",
              "type": "point",
              "x": 0,
              "y": 0
            }
          ],
          "labels": [],
          "width": 3,
          "color": "gray",
          "curvyness": 50,
          "selectedColor": "rgb(0,192,255)"
        },
        "f4321479-6b7b-4385-a6b5-b2ab7c170c2a": {
          "id": "f4321479-6b7b-4385-a6b5-b2ab7c170c2a",
          "type": "default",
          "selected": false,
          "source": null,
          "sourcePort": null,
          "target": null,
          "targetPort": null,
          "points": [
            {
              "id": "82c53624-c45e-4b72-ac3f-655fe4b6a38f",
              "type": "point",
              "x": 112,
              "y": 108
            },
            {
              "id": "d161bdb7-9ba1-4769-b73f-47cddc0fec2e",
              "type": "point",
              "x": 218,
              "y": 176
            }
          ],
          "labels": [],
          "width": 3,
          "color": "gray",
          "curvyness": 50,
          "selectedColor": "rgb(0,192,255)"
        },
        "b43dd138-76fe-465c-bbcc-2c05ae40d38d": {
          "id": "b43dd138-76fe-465c-bbcc-2c05ae40d38d",
          "type": "default",
          "selected": false,
          "source": "d4fb6919-8fe4-4203-9b58-132fd249b939",
          "sourcePort": "73a040ba-4b3d-468e-84a2-1963ef6c1a00",
          "target": "02c6d6e4-4f6f-4203-9e60-76be4adababf",
          "targetPort": "1bfeaeb8-12d7-4eda-8583-490179bb0b51",
          "points": [
            {
              "id": "59a8bb31-d5ad-4deb-aed1-5dc7bcb1d8f1",
              "type": "point",
              "x": 120,
              "y": 277
            },
            {
              "id": "23a16da7-aa28-463a-936c-c5b0c56590ac",
              "type": "point",
              "x": 284,
              "y": 225
            }
          ],
          "labels": [],
          "width": 3,
          "color": "gray",
          "curvyness": 50,
          "selectedColor": "rgb(0,192,255)"
        },
        "d2078eb0-63b7-43e8-9fbd-46107db9e5e6": {
          "id": "d2078eb0-63b7-43e8-9fbd-46107db9e5e6",
          "type": "default",
          "selected": false,
          "source": "d4fb6919-8fe4-4203-9b58-132fd249b939",
          "sourcePort": "73a040ba-4b3d-468e-84a2-1963ef6c1a00",
          "target": "acea4cce-a879-42be-8779-0edc19dab8f5",
          "targetPort": "98968243-a76d-4de6-9c92-edefa6d6736d",
          "points": [
            {
              "id": "80745294-dc11-41b8-8d26-f2497e1e1ec6",
              "type": "point",
              "x": 120,
              "y": 277
            },
            {
              "id": "ae055683-25f1-45ff-9396-98b3e5d25ed5",
              "type": "point",
              "x": 277,
              "y": 388
            }
          ],
          "labels": [],
          "width": 3,
          "color": "gray",
          "curvyness": 50,
          "selectedColor": "rgb(0,192,255)"
        },
        "3119c8d3-fe7d-4e05-bc70-ccca65a2bac2": {
          "id": "3119c8d3-fe7d-4e05-bc70-ccca65a2bac2",
          "type": "default",
          "selected": true,
          "source": "2f772e22-c28f-41ed-9a37-732557a08f16",
          "sourcePort": "275d68e2-948b-4005-b4ff-b88fc2a2bb60",
          "target": "d4fb6919-8fe4-4203-9b58-132fd249b939",
          "targetPort": "73a040ba-4b3d-468e-84a2-1963ef6c1a00",
          "points": [
            {
              "id": "4f50dd80-a63f-4e17-a214-a6248181cc76",
              "type": "point",
              "x": 54.687488691619436,
              "y": 123.00000073276959
            },
            {
              "id": "38c32d29-82da-497c-8160-0e034aab003f",
              "type": "point",
              "x": 120,
              "y": 277
            }
          ],
          "labels": [],
          "width": 3,
          "color": "gray",
          "curvyness": 50,
          "selectedColor": "rgb(0,192,255)"
        }
      }
    },
    {
      "id": "87288e6f-2af4-4725-884a-3591c4e465e9",
      "type": "diagram-nodes",
      "isSvg": false,
      "transformed": true,
      "models": {
        "d4fb6919-8fe4-4203-9b58-132fd249b939": {
          "id": "d4fb6919-8fe4-4203-9b58-132fd249b939",
          "type": "Purchase",
          "selected": false,
          "x": 80,
          "y": 267,
          "ports": [
            {
              "id": "73a040ba-4b3d-468e-84a2-1963ef6c1a00",
              "type": "default",
              "x": 112,
              "y": 269,
              "name": "out",
              "alignment": "right",
              "parentNode": "d4fb6919-8fe4-4203-9b58-132fd249b939",
              "links": [
                "b43dd138-76fe-465c-bbcc-2c05ae40d38d",
                "d2078eb0-63b7-43e8-9fbd-46107db9e5e6",
                "3119c8d3-fe7d-4e05-bc70-ccca65a2bac2"
              ],
              "in": false,
              "label": "out"
            }
          ],
          "color": "rgb(192,0,255)",
          "portsInOrder": [],
          "portsOutOrder": []
        },
        "02c6d6e4-4f6f-4203-9e60-76be4adababf": {
          "id": "02c6d6e4-4f6f-4203-9e60-76be4adababf",
          "type": "Inventory",
          "selected": false,
          "x": 274,
          "y": 215,
          "ports": [
            {
              "id": "1bfeaeb8-12d7-4eda-8583-490179bb0b51",
              "type": "default",
              "x": 276,
              "y": 217,
              "name": "in",
              "alignment": "left",
              "parentNode": "02c6d6e4-4f6f-4203-9e60-76be4adababf",
              "links": [
                "b43dd138-76fe-465c-bbcc-2c05ae40d38d"
              ],
              "in": true,
              "label": "in"
            },
            {
              "id": "0dfae41d-cf73-4f6b-8362-2930259640fe",
              "type": "default",
              "x": 306,
              "y": 217,
              "name": "out",
              "alignment": "right",
              "parentNode": "02c6d6e4-4f6f-4203-9e60-76be4adababf",
              "links": [],
              "in": false,
              "label": "out"
            }
          ],
          "color": "rgb(192,255, 0)",
          "portsInOrder": [],
          "portsOutOrder": []
        },
        "acea4cce-a879-42be-8779-0edc19dab8f5": {
          "id": "acea4cce-a879-42be-8779-0edc19dab8f5",
          "type": "Sales",
          "selected": false,
          "x": 267,
          "y": 378,
          "ports": [
            {
              "id": "98968243-a76d-4de6-9c92-edefa6d6736d",
              "type": "default",
              "x": 269,
              "y": 380,
              "name": "in",
              "alignment": "left",
              "parentNode": "acea4cce-a879-42be-8779-0edc19dab8f5",
              "links": [
                "d2078eb0-63b7-43e8-9fbd-46107db9e5e6"
              ],
              "in": true,
              "label": "in"
            }
          ],
          "color": "rgb(255,192,0)",
          "portsInOrder": [],
          "portsOutOrder": []
        },
        "3e65c939-0ffc-4093-9a53-3f7d6a2c776b": {
          "id": "3e65c939-0ffc-4093-9a53-3f7d6a2c776b",
          "type": "Sales",
          "selected": false,
          "x": 137,
          "y": 500,
          "ports": [
            {
              "id": "91124305-63a2-44f8-8b0d-e22c79dc7d69",
              "type": "default",
              "x": 139,
              "y": 502,
              "name": "in",
              "alignment": "left",
              "parentNode": "3e65c939-0ffc-4093-9a53-3f7d6a2c776b",
              "links": [],
              "in": true,
              "label": "in"
            }
          ],
          "color": "rgb(255,192,0)",
          "portsInOrder": [],
          "portsOutOrder": []
        },
        "2f772e22-c28f-41ed-9a37-732557a08f16": {
          "id": "2f772e22-c28f-41ed-9a37-732557a08f16",
          "type": "Conversion",
          "selected": true,
          "x": 44.6939063050369,
          "y": 113.00043629890753,
          "ports": [
            {
              "id": "275d68e2-948b-4005-b4ff-b88fc2a2bb60",
              "type": "default",
              "x": 46.687492088433345,
              "y": 115.0000041295835,
              "name": "in",
              "alignment": "left",
              "parentNode": "2f772e22-c28f-41ed-9a37-732557a08f16",
              "links": [
                "3119c8d3-fe7d-4e05-bc70-ccca65a2bac2"
              ],
              "in": true,
              "label": "in"
            },
            {
              "id": "5c42f4e4-f8cb-4510-8fe6-c0af736b76dd",
              "type": "default",
              "x": 76.68750756758536,
              "y": 115.0000041295835,
              "name": "out",
              "alignment": "right",
              "parentNode": "2f772e22-c28f-41ed-9a37-732557a08f16",
              "links": [],
              "in": false,
              "label": "out"
            }
          ],
          "name": "Untitled",
          "color": "rgb(0,192,255)",
          "portsInOrder": [
            "275d68e2-948b-4005-b4ff-b88fc2a2bb60"
          ],
          "portsOutOrder": [
            "5c42f4e4-f8cb-4510-8fe6-c0af736b76dd"
          ]
        },
        "601f9cd0-1154-4fad-b4be-05ecc56c86c1": {
          "id": "601f9cd0-1154-4fad-b4be-05ecc56c86c1",
          "type": "Sales",
          "x": 61.601268052130955,
          "y": 433.1835993845011,
          "ports": [
            {
              "id": "adafa78a-76f2-40fd-bae9-aa19c95de30d",
              "type": "default",
              "x": null,
              "y": null,
              "name": "in",
              "alignment": "left",
              "parentNode": "601f9cd0-1154-4fad-b4be-05ecc56c86c1",
              "links": [],
              "in": true,
              "label": "in"
            }
          ],
          "name": "Untitled",
          "color": "rgb(255,192,0)",
          "portsInOrder": [
            "adafa78a-76f2-40fd-bae9-aa19c95de30d"
          ],
          "portsOutOrder": []
        }
      }
    }
  ]
}
"""

d = node_graph(MODEL,key="foo")

st.write(d['model'])


