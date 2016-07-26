import * as actionTypes from "../constants/actionTypes";

export default function layout(state={appInitializing:true, sidebarOpen:false},action){
	switch(action.type){
		case actionTypes.SET_APPINITIALIZING:
            return Object.assign({}, state, {
                appInitializing: state.appInitializing
            });
		case actionTypes.TOGGLE_SIDEBAR:
		return Object.assign({},state,{
			sidebarOpen: !state.sidebarOpen
			});
	}	
	return state;
}