import { NodeModel, DefaultPortModel, DefaultNodeModel } from '@projectstorm/react-diagrams';
import { BaseModelOptions } from '@projectstorm/react-canvas-core';

export interface TSCustomNodeModelOptions extends BaseModelOptions {
	color?: string;
	port_selection?: string;
	name?: string;
	icon?: string;
}

export class TSCustomNodeModel extends DefaultNodeModel {
	color: string;
	type: string
	port_selection: string;
	name: string;
	icon?: string;

	constructor(options: TSCustomNodeModelOptions = {}) {
		super({
			...options,
		});
		this.color = options.color || 'red';
		this.type = options.type
		this.port_selection = options.port_selection
		this.name = options.name || options.type
		this.icon = options.icon || 'circle'
		this.setupInOutPorts()
	}

	setupInOutPorts(){
		if (this.port_selection == 'in' || this.port_selection == 'both')
			{
				this.addPort(
					new DefaultPortModel({
						in: true,
						name: 'in'
					})
				);
			}
			if (this.port_selection == 'out' || this.port_selection == 'both')
		// if (["Purchase", "Conversion", "Inventory"].includes( this.type ))
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
			port_selection: this.port_selection,
			name: this.name,
		};
	}

	deserialize(event : any): void {
		super.deserialize(event);
		this.color = event.data.color;
		this.options.type = event.data.type;
		this.type = event.data.type;
		this.port_selection = event.data.port_selection;
		this.name = event.data.name;		
	}
}
