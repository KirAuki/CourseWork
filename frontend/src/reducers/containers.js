import {GET_CONTAINERS_LIST,DELETE_CONTAINER,TOGGLE_CONTAINER} from "../actions/types";

const initialState = {
    containers: []
};

export default function (state = initialState, action) {
    switch (action.type){
        case GET_CONTAINERS_LIST:
            return {
                ...state,
                containers: action.payload
            };
        case DELETE_CONTAINER:
            return {
                ...state,
                containers: state.containers.filter(container => container.id != action.payload )
            };
            case TOGGLE_CONTAINER:
            return {
                ...state,
                containers: [...state.containers]
            };
        default:
            return state;
    }

};