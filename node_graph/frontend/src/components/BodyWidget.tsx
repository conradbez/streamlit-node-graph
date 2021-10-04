import * as React from 'react';
import { TrayWidget } from './TrayWidget';
import { TrayItemWidget } from './TrayItemWidget';
import createEngine, { DefaultPortFactory, DiagramModel, DefaultLinkFactory } from '@projectstorm/react-diagrams';
import { CanvasWidget } from '@projectstorm/react-canvas-core';
import { DemoCanvasWidget } from '../DemoCanvasWidget';
import { TSCustomNodeFactory } from './custom-node-ts/TSCustomNodeFactory';
import { TSCustomNodeModel } from './custom-node-ts/TSCustomNodeModel';
import * as _ from 'lodash';
import {
	Streamlit,
	StreamlitComponentBase,
	withStreamlitConnection,
  } from "streamlit-component-lib"

import styled from '@emotion/styled';

const FullscreenCanvas = styled(DemoCanvasWidget)`
  height: 100%;
  width: 100%;
`;
const Container = styled.div`
  height: 800px;
  width: 100vw;
`;

export interface BodyWidgetProps {
}

interface BodyWidgetState {
	diagramEngine: any;
	lastNodeSelected: string | null
  }


namespace S {
	export const Body = styled.div`
		flex-grow: 1;
		display: flex;
		flex-direction: column;
		min-height: 100%;
	`;

	export const Content = styled.div`
		height: 100px;
		display: flex;
		flex-grow: 1;
	`;

	export const Layer = styled.div`
		position: relative;
		flex-grow: 1;
	`;
}

class BodyWidget extends StreamlitComponentBase<BodyWidgetState> {

	public constructor(props : any) {
		super(props)
		this.state = {
			diagramEngine: createEngine(),
			lastNodeSelected: null
			}
		this.state.diagramEngine.getNodeFactories().registerFactory(new TSCustomNodeFactory({'type': 'Purchase'}) as any);
		this.state.diagramEngine.getNodeFactories().registerFactory(new TSCustomNodeFactory({'type': 'Inventory'}) as any);
		this.state.diagramEngine.getNodeFactories().registerFactory(new TSCustomNodeFactory({'type': 'Sales'}) as any);
		this.state.diagramEngine.getNodeFactories().registerFactory(new TSCustomNodeFactory({'type': 'Conversion'}) as any);
		this.state.diagramEngine.getPortFactories().registerFactory(new DefaultPortFactory() as any);
		// this.state.diagramEngine.getPortFactories().registerFactory(new DefaultLinkFactory() as any);
		
		var model =  new DiagramModel()
		if (props.args['model']){
			model.deserializeModel(JSON.parse(props.args['model']), this.state.diagramEngine);
		}

		model.registerListener({
			nodesUpdated: this.sendToStreamlit.bind(this), 
			linksUpdated: this.sendToStreamlit.bind(this),
		})

		_.forEach(model.getNodes(), (node) => {
			node.registerListener({
				selectionChanged: this.selectionChangedListner.bind(this)
			})
			});
		

		this.state.diagramEngine.setModel(model)

	}

	componentDidMount(){
		Streamlit.setFrameHeight()
	}
	
	selectionChangedListner(event : any) : void {
		this.setState({ 
			lastNodeSelected: event.entity.options.id 
			}, this.sendToStreamlit)
	}
		
	sendToStreamlit() : void {
		var model = this.state.diagramEngine.getModel()
		var send_to_streamlit = JSON.stringify(
			{"model" : model.serialize(), 'lastNodeSelected':this.state.lastNodeSelected}
			);
		Streamlit.setComponentValue(send_to_streamlit);
	}

	render() {
		return (
			<S.Body>
				<S.Content>
					<TrayWidget>
						<TrayItemWidget model={{ type: 'Purchase' }} name="Purchase" color="rgb(192,0,255)" />
						<TrayItemWidget model={{ type: 'Inventory' }} name="Inventory" color="rgb(192,255,0)" />
						<TrayItemWidget model={{ type: 'Conversion' }} name="Conversion" color="rgb(0,192,255)" />
						<TrayItemWidget model={{ type: 'Sales' }} name="Sales" color="rgb(255,192,0)" />
					</TrayWidget>
					<S.Layer
						onDrop={(event) => {
							var data = JSON.parse(event.dataTransfer.getData('storm-diagram-node'));
							// var nodesCount = _.keys(this.state.diagramEngine.getModel().getNodes()).length;
							var node: TSCustomNodeModel;
							
							if (data.type === 'Purchase') {
								node = new TSCustomNodeModel({ color: 'rgb(192,0,255)' , type: data.type });
							}if (data.type === 'Inventory') {
								node = new TSCustomNodeModel({ color: 'rgb(192,255, 0)' , type: data.type  });
							}if (data.type === 'Conversion') {
								node = new TSCustomNodeModel({ color: 'rgb(0,192,255)' , type: data.type  });
							}if (data.type === 'Sales') {
								node = new TSCustomNodeModel({ color: 'rgb(255,192,0)' , type: data.type  });
							}
							var point = this.state.diagramEngine.getRelativeMousePoint(event);
							node.setPosition(point);
							node.registerListener({
								selectionChanged: this.selectionChangedListner.bind(this)
							})
							this.state.diagramEngine.getModel().addNode(node);
							this.forceUpdate();
						}}
						onDragOver={(event) => {
							event.preventDefault();
						}}>
						<Container>
						<FullscreenCanvas>
							<CanvasWidget engine={this.state.diagramEngine} />
						</FullscreenCanvas>
						</Container>
					</S.Layer>
				</S.Content>
			</S.Body>
		);
	}
}

export default withStreamlitConnection(BodyWidget);
