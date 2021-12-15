import * as React from 'react';
import { TSCustomNodeModel } from './TSCustomNodeModel';
import { TSCustomNodeWidget } from './TSCustomNodeWidget';
import { AbstractReactFactory } from '@projectstorm/react-canvas-core';
import { DiagramEngine } from '@projectstorm/react-diagrams-core';

interface TSCustomNodeFactoryTypes extends AbstractReactFactory<TSCustomNodeModel, DiagramEngine> {
 }

export class TSCustomNodeFactory extends AbstractReactFactory<TSCustomNodeModel, DiagramEngine> implements TSCustomNodeFactoryTypes {
	constructor(props:any) {
		super(props.type);
	}
	

	generateModel() {
		return new TSCustomNodeModel();
	}

	generateReactWidget(event :any): JSX.Element {
		return <TSCustomNodeWidget engine={this.engine as DiagramEngine} node={event.model} />;
	}
}


