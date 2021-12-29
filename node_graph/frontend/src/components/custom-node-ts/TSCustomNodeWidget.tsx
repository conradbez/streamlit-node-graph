import * as React from 'react';
import { DiagramEngine, PortWidget } from '@projectstorm/react-diagrams-core';
import { TSCustomNodeModel } from './TSCustomNodeModel';
import { EditText, EditTextarea } from 'react-edit-text';
import 'react-edit-text/dist/index.css';

export interface TSCustomNodeWidgetProps {
	node: TSCustomNodeModel;
	engine: DiagramEngine;
}

export interface TSCustomNodeWidgetState {}

export class TSCustomNodeWidget extends React.Component<TSCustomNodeWidgetProps, TSCustomNodeWidgetState> {
	constructor(props: TSCustomNodeWidgetProps) {
		super(props);
		this.state = {};
	}

	render() {
		return (
			<div 
			style={{
				display: "flex",
				flexDirection: "column",
				justifyContent: "center",
				alignItems: "center",
				color: 'white'
			  }}
			  >
			<div className="custom-node">
				
				{ 
				this.props.node.port_selection == 'in' || this.props.node.port_selection == 'both'
				?	<PortWidget engine={this.props.engine} port={this.props.node.getPort('in')}>
						<div className="circle-port" />
					</PortWidget>
				: <div className="circle-port" style={{ visibility: "hidden" }} />
			}

				{ 
				this.props.node.port_selection == 'out' || this.props.node.port_selection == 'both'
				?
					<PortWidget engine={this.props.engine} port={this.props.node.getPort('out')}>
						<div className="circle-port" />
					</PortWidget>
				: <div className="circle-port" style={{ visibility: "hidden" }} />
				}

				<div className="custom-node-color" style={{ backgroundColor: this.props.node.color }} />
				
			</div>
			<div >
				<EditText 
				placeholder = {this.props.node.name}
				// defaultValue = {this.props.node.name}
				onSave= { (e)=>{ 
					this.props.node.name = e['value'];
					console.log(this.props.engine.getModel());
					this.props.engine.getModel().fireEvent({ node: this.props.node, nameChanged: true }, 'nodesUpdated');
				}  } 
				/>
			</div>
			</div>
		);
	}
}
