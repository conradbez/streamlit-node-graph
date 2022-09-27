class Diagram:
    def __init__(self, diagram, ) -> None:
        self.diagram = diagram
        self.model = self.diagram['model']
        self.selected = self.get_selected_node()

    def get_all_nodes_node_inputs(self):
        nodes, links = self.process_diagram_output()
        for node in nodes:
            node['sources'] = []
            for link in links:
                if link['target'] == node['id']:
                    node['sources'].append(link['source'])
        return nodes

    def get_selected_node(self) -> str|None:
        if self.model == False: # no nodes on model
            return None
        diagram_nodes = self.get_all_nodes_node_inputs()
        try:
            return list(filter(lambda n: n['selected'], diagram_nodes))[0]
        except:
            return None

    def process_diagram_output(self):
        # Extract nodes
        diagram_nodes = self.model['layers'][1]['models']
        node_attr_to_keep = ['id', 'type', 'name', 'selected']

        diagram_nodes = [  { k : v for k, v in diagram_node.items() if k in node_attr_to_keep }
            for diagram_node_key, diagram_node in diagram_nodes.items()
        ]

        # Extract links
        diagram_links =self.model['layers'][0]['models']
        link_attr_to_keep = ['source', 'target']
        diagram_links = [  { k : v for k, v in diagram_link.items() if k in link_attr_to_keep }
            for diagram_link_key, diagram_link in diagram_links.items()
        ]
        return diagram_nodes, diagram_links