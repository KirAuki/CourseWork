import axios from 'axios';
import {GET_CONTAINERS_LIST,DELETE_CONTAINER,TOGGLE_CONTAINER, CREATE_CONTAINER , GET_SCHEDULES} from "../actions/types"

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';



export const getContainers = () => disaptch => {
    axios.get('api/containers/')
        .then(result => {
            disaptch({
                type: GET_CONTAINERS_LIST,
                payload: result.data
            });
        }).catch(error => console.log(error));
};


export const delContainer = (id) => dispatch => {
    axios.delete(`api/containers/${id}/`)
        .then(result => {
            dispatch({
                type: DELETE_CONTAINER,
                payload: id
            });
        }).catch(error => console.log(error));
};


export const toggleContainer = (container) => dispatch => {
    container.done = !container.done;
    axios.put(`api/containers/${container.id}/`, container)
        .then(result => {
            dispatch({
                type: TOGGLE_CONTAINER,
                payload: result.data
            });
        }).catch(error => console.log(error));
};

export const createContainer = (container) => dispatch => {
    axios.post('api/containers/', container)
        .then(result => {
            dispatch({
                type: CREATE_CONTAINER,
                payload: result.data
            });
        }).catch(error => console.log(error));
};

export const getSchedules = () => (dispatch) => {
    axios.get("api/schedules/")
        .then((result) => {
            dispatch({
                type: GET_SCHEDULES,
                payload: result.data
            });
      }).catch((error) => console.log(error));
};