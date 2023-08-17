import axios from "axios"
import {
    CATEGORY_LIST_REQUEST,
    CATEGORY_LIST_SUCCESS,
    CATEGORY_LIST_FAIL,

    CATEGORY_DETAILS_REQUEST,
    CATEGORY_DETAILS_SUCCESS,
    CATEGORY_DETAILS_FAIL,

    CATEGORY_DELETE_REQUEST,
    CATEGORY_DELETE_SUCCESS,
    CATEGORY_DELETE_FAIL,

    CATEGORY_CREATE_REQUEST,
    CATEGORY_CREATE_SUCCESS,
    CATEGORY_CREATE_FAIL,

    CATEGORY_UPDATE_REQUEST,
    CATEGORY_UPDATE_SUCCESS,
    CATEGORY_UPDATE_FAIL,

    CATEGORY_CREATE_REVIEW_REQUEST,
    CATEGORY_CREATE_REVIEW_SUCCESS,
    CATEGORY_CREATE_REVIEW_FAIL,


    CATEGORY_TOP_REQUEST,
    CATEGORY_TOP_SUCCESS,
    CATEGORY_TOP_FAIL,

} from '../constants/CategoryConstants'



export const listCategory = () => async (dispatch) => {
    try {
        dispatch({ type: CATEGORY_LIST_REQUEST })

        const response = await axios.get('http://127.0.0.1:8000/api/category-list')

        dispatch({
            type: CATEGORY_LIST_SUCCESS,
            payload: response.data
        })

    } catch (error) {
        dispatch({
            type: CATEGORY_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}