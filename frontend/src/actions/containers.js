import axios from 'axios';
import {GET_CONTAINERS_LIST,DELETE_CONTAINER,TOGGLE_CONTAINER} from "../actions/types"

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
