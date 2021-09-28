import { NodeModel, DefaultPortModel } from '@projectstorm/react-diagrams';
import { BaseModelOptions } from '@projectstorm/react-canvas-core';

export interface TSCustomNodeModelOptions extends BaseModelOptions {
	color?: string;
}

export class TSCustomNodeModel extends NodeModel {
	color: string;
	type: string

	constructor(options: TSCustomNodeModelOptions = {}) {
		super({
			...options,
		});
		this.color = options.color || 'red';
		this.type = options.type
		// setup an in and out port
		console.log('here')
		console.log(this.options.type)
		if (["Sales", "Conversion", "Inventory"].includes( this.options.type ))
			{
				this.addPort(
					new DefaultPortModel({
						in: true,
						name: 'in'
					})
				);
			}
		if (["Purchase", "Conversion", "Inventory"].includes( this.options.type ))
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
		this.type = event.type;
	}
}
