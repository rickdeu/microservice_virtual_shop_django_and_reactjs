import React from 'react'
import ReactStars from "react-rating-stars-component";
import { Link, useLocation } from 'react-router-dom';

// import images
import prodcompare from '../images/prodcompare.svg'
import wish from '../images/wish.svg'
import wishlist from '../images/wishlist.svg'
import watch from '../images/watch.jpg'
import addcart from '../images/add-cart.svg'
import view from '../images/view.svg'


const ProductCardList = (props) => {
    const {  product } = props;

    let location = useLocation();


    return (
        <>
            <div className='col-3'>
                <Link  to='/product/:id' className='product-card position-relative'>
                    <div className='wishlist-icon position-absolute'>
                        <Link >
                            <img src={wish} alt='whishlist' />
                        </Link>
                    </div>
                    <div className='product-image'>
                        <img src={product.image} className='img-fluid' width={269} height={269} alt='product images' />
                        <img src={watch} className='img-fluid' width={269} height={269} alt='product images' />

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
                               <p className='description'>
                               {product.description}
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

            </div>

          
        </>

    )
}
export default ProductCardList