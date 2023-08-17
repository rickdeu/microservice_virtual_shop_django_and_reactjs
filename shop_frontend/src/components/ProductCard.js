import React, { useState } from 'react'
import ReactStars from "react-rating-stars-component";
import { Link, useLocation } from 'react-router-dom';

// import images
import prodcompare from '../images/prodcompare.svg'
import wish from '../images/wish.svg'
import wishlist from '../images/wishlist.svg'
import watch from '../images/watch.jpg'
import addcart from '../images/add-cart.svg'
import view from '../images/view.svg'
import { useDispatch } from 'react-redux';
import { addToCart } from '../actions/CartActions';


const ProductCard = (props) => {
    const { grid, product } = props;
    const dispatch = useDispatch()

    const [qty, setQty] = useState(1)

    let location = useLocation();

    const addToCartHandler = (id, qty) => {
        dispatch(addToCart(id, qty))
    }


    return (
        <>
            <div className={` ${location.pathname === '/store' ? `gr-${grid}` : 'col-3'} `} >
                <Link to={`/product/${product.pk}`} className='product-card position-relative'>
                    <div className='wishlist-icon position-absolute'>
                        <Link >
                            <img src={wish} alt='whishlist' />
                        </Link>
                    </div>
                    <div className='product-image'>
                        <img src={product.image} className='img-fluid' width={269} height={269} alt={product.name} />
                        <img src={product.image} className='img-fluid' width={269} height={269} alt={product.name} />








                    </div>
                    <div className='product-details'>
                        <h6 className='brand'>{product.name}</h6>
                        <h5 className='product-title'>
                            {product.category}
                        </h5>
                        <ReactStars
                            count={5}
                            size={24}
                            value={3}
                            edit={false}
                            activeColor="#ffd700"
                        />
                        <p className={`description ${grid === 12 ? "d-block" : "d-none"}`} >
                            {product.description}
                        </p>
                        <p className='price'> {product.price}</p>
                    </div>

                    <div className='action-bar position-absolute'>

                        <div className='d-flex flex-column gap-15'>
                            <Link>
                                <img src={prodcompare} alt='compare' />
                            </Link>
                            <Link>
                                <img src={view} alt='view' />
                            </Link>

                            <Link onClick={() => addToCartHandler(product.pk, qty) }>
                                <img src={addcart} alt='add-cart' />
                            </Link>

                        </div>

                    </div>
                </Link>

            </div>


            {/* <div className={` ${location.pathname === '/store' ? `gr-${grid}` : 'col-3'} `}
            >
                <Link className='product-card position-relative'>
                    <div className='wishlist-icon position-absolute'>
                        <Link>
                            <img src={wish} alt='whishlist' />
                        </Link>
                    </div>
                    <div className='product-image'>
                        <img src={watch} className='img-fluid' alt='product images' />
                        <img src='images/tab1.jpg' className='img-fluid' alt='product images' />

                    </div>
                    <div className='product-details'>
                        <h6 className='brand'>Relogio</h6>
                        <h5 className='product-title'>Relogios com cobertura de ouro, adequado para crianças e adultos</h5>
                        <ReactStars
                            count={5}
                            size={24}
                            value={3}
                            edit={false}
                            activeColor="#ffd700"
                        />
                               <p className={`description ${grid === 12 ? "d-block":"d-none"}`} >
                        Relogios com cobertura de ouro, adequado para crianças e adultos Relogios com cobertura de ouro, adequado para crianças e adultos
                        Relogios com cobertura de ouro, adequado para crianças e adultos Relogios com cobertura de ouro, adequado para crianças e adultos
                        </p>
                        <p className='price'> 100.00 Akz</p>
                    </div>

                    <div className='action-bar position-absolute'>

                        <div className='d-flex flex-column gap-15'>
                            <Link>
                                <img src={prodcompare} alt='compare' />
                            </Link>
                            <Link>
                                <img src={view} alt='view' />
                            </Link>

                            <Link>
                                <img src={addcart} alt='add-cart' />
                            </Link>

                        </div>

                    </div>
                </Link>

            </div> */}
        </>

    )
}
export default ProductCard