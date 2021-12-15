import * as React from 'react';
import { DiagramEngine, PortWidget } from '@projectstorm/react-diagrams-core';
import { TSCustomNodeModel } from './TSCustomNodeModel';

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
			<div className="custom-node">
				
				{ 
				// ["Sales", "Conversion", "Inventory"].includes( this.props.node.type )
				this.props.node.port_selection == 'in' || this.props.node.port_selection == 'both'
				?	<PortWidget engine={this.props.engine} port={this.props.node.getPort('in')}>
						<div className="circle-port" />
					</PortWidget>
				: <div className="circle-port" style={{ visibility: "hidden" }} />
			}

				{ 
				// ["Purchase", "Conversion", "Inventory"].includes( this.props.node.type ) 
				this.props.node.port_selection == 'out' || this.props.node.port_selection == 'both'
				?
					<PortWidget engine={this.props.engine} port={this.props.node.getPort('out')}>
						<div className="circle-port" />
					</PortWidget>
				: <div className="circle-port" style={{ visibility: "hidden" }} />
				}

				<div className="custom-node-color" style={{ backgroundColor: this.props.node.color }} />
			</div>
		);
	}
}
