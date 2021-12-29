## Start dev 
`cd node_graph/frontend && npm install && npm run start`

and in another shell

`streamlit run node_graph/__init__.py `

## Build
`cd node_graph/frontend && npm build`
`cd../..`
`python setup.py sdist bdist_wheel`

## Upload
1. Change version in `setup.py`
2. `twine upload dist/*`