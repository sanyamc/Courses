import * as actionTypes from "../constants/actionTypes";


export function toggleSidebar(){
	return {
		type:actionTypes.TOGGLE_SIDEBAR     // no payload is needed
	};
}

export function setAppInitializationState(){
	return {
		type:actionTypes.TOGGLE_SIDEBAR,
		payload:true
	};
}
