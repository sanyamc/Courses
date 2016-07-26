import * as actionTypes from "../constants/actionTypes";

export default function summary(state={data:null},action){
    //console.log("action is "+JSON.stringify(action)+" state is: "+JSON.stringify(state));
	switch(action.type){
		case actionTypes.SET_APPINITIALIZING:
            return Object.assign({}, state, {
                appInitializing: state.appInitializing
            });
		case actionTypes.GET_ENGAGEMENTDATA:
		return Object.assign({},state,{
			data:action.payload
			});
	}	
	return state;
}