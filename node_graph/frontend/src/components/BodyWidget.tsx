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

		// Regiter factories
		var item_types = this.props.args['item_types'];
		console.log(item_types);
		for (const item of item_types) {
			var item_name = item['title']
			this.state.diagramEngine.getNodeFactories().registerFactory(new TSCustomNodeFactory({'type': item_name}) as any);
		  }
		  


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
		var tray_items = this.props.args['item_types']
		 const tray_item_widgets_to_render = tray_items.map((item:any) => (
				<TrayItemWidget model={{ type: item['title'] }} name={item['title']} color={item['color']}/>
			  ))

		return (
			<S.Body>
				<S.Content>
					<TrayWidget>
						{tray_item_widgets_to_render}
					</TrayWidget>
					<S.Layer
						onDrop={(event) => {
							var data = JSON.parse(event.dataTransfer.getData('storm-diagram-node'));							
							var nodeColor = tray_items.filter((i:any) => i['title']==data['type'])[0]['color']
							var nodePortSelections = tray_items.filter((i:any) => i['title']==data['type'])[0]['port_selection']
							var node: TSCustomNodeModel = new TSCustomNodeModel({ color: nodeColor , type: data.type, port_selection: nodePortSelections});
				
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