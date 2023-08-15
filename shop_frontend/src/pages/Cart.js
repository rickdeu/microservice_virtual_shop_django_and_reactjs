import React from 'react'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'
import watch from '../images/watch.jpg'
import { AiFillDelete } from 'react-icons/ai'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import Message from '../components/Message'
import { removeFromCart } from '../actions/CartActions'
import { Button } from 'react-bootstrap'

const Cart = () => {

    const dispatch = useDispatch()

    const cart = useSelector(state => state.cart)
    const { cartItems } = cart
    const removeFromCartHandler = (id) => {
        dispatch(removeFromCart(id))
    }

    return (

        <>
            <Meta title={'Cart'} />
            <BreadCrumb title='Cart' />
            <section className='cart-wrapper home-wrapper-2 py-5'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-12'>
                            <div className='cart-header py-3 d-flex justify-content-between align-items-center'>
                                <h4 className='cart-col-1'>PRODUCT</h4>
                                <h4 className='cart-col-2'>PRICE</h4>
                                <h4 className='cart-col-3'>QUANTITY</h4>
                                <h4 className='cart-col-4'>TOTAL</h4>
                            </div>

                            {
                                cartItems.length === 0 ?
                                    <Message variant='infor'>your cart is empty</Message>
                                    :

                                    cartItems.map(product => (
                                        <div className='cart-data mb-2 py-3 d-flex justify-content-between align-items-center'>
                                            <div className='cart-col-1 gap-15 d-flex align-items-center'>
                                                <div className='w-25'>
                                                    <img className='img-fluid' src={product.image} width={110} height={110} alt={product.name} />
                                                </div>
                                                <div className='w-75'>
                                                    <p>{product.name}</p>
                                                    <p>Size: </p>
                                                    <p>Color: </p>

                                                </div>

                                            </div>
                                            <div className='cart-col-2'>
                                                <h5>{product.price}</h5>
                                            </div>
                                            <div className='cart-col-3 d-flex align-items-center gap-15'>
                                                <input className='form-control' value={product.qty} type='number' min={1} max={10} name='' style={{ 'width': '70px' }} id='' />
                                                <div>

                                                </div>
                                                {/*          
                                                <AiFillDelete onClick={() => removeFromCartHandler(product.pk)} className='text-danger' /> */}
                                                <Button
                                                    type='button'
                                                    variant='light'
                                                    onClick={() => removeFromCartHandler(product.pk)}
                                                >
                                                    <AiFillDelete className='text-danger' />
                                                </Button>
                                            </div>
                                            <div className='cart-col-4'>
                                                <h5>{product.price * product.qty}</h5>
                                            </div>


                                        </div>
                                    ))



                            }





                            <div className='col-12 py-2 mt-4'>
                                <div className='d-flex justify-content-between align-items-baseline'>
                                    <Link to='/store' className='buttom' >Continue To Shopping</Link>
                                    <div className='d-flex flex-column align-items-end'>
                                        <h4>Sub Total:  ({cartItems.reduce((acc, item) => acc + item.qty, 0)}) items</h4>
                                        Akz {cartItems.reduce((acc, item) => acc + item.qty * item.price, 0).toFixed(2)}
                                        <p>Taxes and shipping calculated at checkout</p>
                                        <Link aria-disabled={cartItems.length === 2} to='/checkout' className='buttom'>Checkout</Link>
                                    </div>

                                </div>

                            </div>


                        </div>
                    </div>
                </div>

            </section>

        </>

    )
}

export default Cart