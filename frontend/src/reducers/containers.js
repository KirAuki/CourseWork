import {GET_CONTAINERS_LIST,DELETE_CONTAINER,TOGGLE_CONTAINER, CREATE_CONTAINER,GET_SCHEDULES} from "../actions/types";

const initialState = {
    containers: [],
    schedules: []
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
            case GET_SCHEDULES:
            return {
                ...state,
                schedules: action.payload
            };
            case CREATE_CONTAINER:
            return {
                ...state,
                containers: [...state.containers, action.payload]
            };
        default:
            return state;
    }

};