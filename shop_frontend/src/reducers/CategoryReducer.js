import {
    CATEGORY_LIST_REQUEST,
    CATEGORY_LIST_SUCCESS,
    CATEGORY_LIST_FAIL,

/*     CATEGORY_DETAILS_REQUEST,
    CATEGORY_DETAILS_SUCCESS,
    CATEGORY_DETAILS_FAIL,

    CATEGORY_DELETE_REQUEST,
    CATEGORY_DELETE_SUCCESS,
    CATEGORY_DELETE_FAIL,

    CATEGORY_CREATE_REQUEST,
    CATEGORY_CREATE_SUCCESS,
    CATEGORY_CREATE_FAIL,
    CATEGORY_CREATE_RESET,

    CATEGORY_UPDATE_REQUEST,
    CATEGORY_UPDATE_SUCCESS,
    CATEGORY_UPDATE_FAIL,
    CATEGORY_UPDATE_RESET,

    CATEGORY_CREATE_REVIEW_REQUEST,
    CATEGORY_CREATE_REVIEW_SUCCESS,
    CATEGORY_CREATE_REVIEW_FAIL,
    CATEGORY_CREATE_REVIEW_RESET,

    CATEGORY_TOP_REQUEST,
    CATEGORY_TOP_SUCCESS,
    CATEGORY_TOP_FAIL, */
} from '../constants/CategoryConstants'


export const CategoryListReducer = (state = { categories: [] }, action) => {
    switch (action.type) {
        case CATEGORY_LIST_REQUEST:
            return { loading: true, categories: [] }

        case CATEGORY_LIST_SUCCESS:
            return {
                loading: false,
                categories: action.payload,
            }

        case CATEGORY_LIST_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}
export default CategoryListReducer;
