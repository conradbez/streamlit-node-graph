import { NodeModel, DefaultPortModel, DefaultNodeModel } from '@projectstorm/react-diagrams';
import { BaseModelOptions } from '@projectstorm/react-canvas-core';

export interface TSCustomNodeModelOptions extends BaseModelOptions {
	color?: string;
}

export class TSCustomNodeModel extends DefaultNodeModel {
	color: string;
	type: string


	constructor(options: TSCustomNodeModelOptions = {}) {
		super({
			...options,
		});
		this.color = options.color || 'red';
		this.type = options.type
		this.setupInOutPorts()
		// setup an in and out port
	}

	setupInOutPorts(){
		if (["Sales", "Conversion", "Inventory"].includes( this.type ))
			{
				this.addPort(
					new DefaultPortModel({
						in: true,
						name: 'in'
					})
				);
			}
		if (["Purchase", "Conversion", "Inventory"].includes( this.type ))
			{
				this.addPort(
					new DefaultPortModel({
						in: false,
						name: 'out'
					})
				);
			}
	}

	serialize() {
		return {
			...super.serialize(),
			color: this.color,
			type: this.type,
		};
	}

	deserialize(event : any): void {
		super.deserialize(event);
		this.color = event.data.color;
		this.options.type = event.data.type;
		this.type = event.data.type;
		
	}
}
