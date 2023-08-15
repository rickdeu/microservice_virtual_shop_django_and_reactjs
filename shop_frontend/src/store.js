import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk'

import productListReducer, { productDetailsReducer } from './reducers/productReducers';
import { composeWithDevTools } from 'redux-devtools-extension'
import CategoryListReducer from './reducers/CategoryReducer';
import { cartReducer } from './reducers/CartReducer';

const reducer = combineReducers({
    productList: productListReducer,
    productDetails: productDetailsReducer,
    categoryList: CategoryListReducer,

    cart: cartReducer,


})
const cartItemsFromStorage = localStorage.getItem('cartItems') ?
    JSON.parse(localStorage.getItem('cartItems')) : []

const initialState = {
    cart: {
        cartItems: cartItemsFromStorage,
    }
}


const middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))


export default store;