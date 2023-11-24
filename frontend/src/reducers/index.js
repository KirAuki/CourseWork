import { combineReducers } from "redux";
import containers from './containers';
import schedules from './containers'

export default combineReducers({
    containers,
    schedules
});