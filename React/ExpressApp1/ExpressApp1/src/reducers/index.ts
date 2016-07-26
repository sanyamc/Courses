import { combineReducers } from 'redux';
import layout from './layout';
import summary from './summary';


const rootReducer = combineReducers({
	layout,
	summary

});

export default rootReducer;
