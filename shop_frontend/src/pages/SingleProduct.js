import React, { useState } from 'react'
import ReactStars from 'react-rating-stars-component'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'
import ProductCard from '../components/ProductCard'
import ReactImageZoom from 'react-image-zoom';
import Color from '../components/Colors'
import { Link } from 'react-router-dom'
import { HiOutlineHeart, HiOutlineSwitchVertical, HiOutlineViewList } from 'react-icons/hi'
import { AiOutlineHeart } from 'react-icons/ai'

import { TbGitCompare } from 'react-icons/tb'

const SingleProduct = () => {
    const img = 'https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg'
    const props = {
        width: 400,
        height: 600,
        zoomWidth: 500,
        img: 'https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg'
    };
    const [
        orderedProduct,
        setOrderedProduct] = useState(true)

    const copyToclipboard = (text) => {
        console.log('text', text)
        var textField = document.createElement('textarea');
        textField.innerText = text;
        document.body.appendChild(textField);
        textField.select();
        document.execCommand('copy')
        textField.remove()

    }




    return (
        <>
            <Meta title='Product Name' />
            <BreadCrumb title='Product Name' />
            <div className='main-product-wrapper py-5 home-wrapper-2'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-6'>
                            <div className='main-product-image'>
                                <div>
                                    <ReactImageZoom {...props} />
                                </div>

                            </div>
                            <div className='other-product-images d-flex flex-wrap gap-15'>
                                <div> <img className='https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg' alt='watch' /> </div>
                                <div> <img className='https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg' alt='watch' /> </div>
                                <div> <img className='https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg' alt='watch' /> </div>
                                <div> <img className='https://images.pexels.com/photos/1342609/pexels-photo-1342609.jpeg' alt='watch' /> </div>



                            </div>
                        </div>
                        <div className='col-6'>

                            <div className='main-product-details'>
                                <div className='border-bottom'>
                                    <h3 className='title'>
                                        Kids headphones bult 10 Pack Multi Colored for Students
                                    </h3>
                                </div>
                                <div className='py-3'>
                                    <p className='price'>
                                        Akz 100
                                    </p>
                                    <div className='d-flex align-items-center gap-10' >
                                        <ReactStars
                                            count={5}
                                            size={24}
                                            value={3}
                                            edit={false}
                                            activeColor="#ffd700"
                                        />
                                        <p className='mb-0 t-review'>
                                            (2 reviews)
                                        </p>
                                    </div>
                                    <a className='review-btn' href='#review'>Write a Review</a>
                                </div>

                                <div className='border-bottom py-3'>
                                    <div className='d-flex gap-10 align-items-center my-2'>
                                        <h3 className='product-heading'>Type: </h3> <p className='product-data'>
                                            Watch
                                        </p>
                                    </div>
                                    <div className='d-flex gap-10 align-items-center my-2'>
                                        <h3 className='product-heading'>Brand: </h3> <p className='product-data'>
                                            Havells
                                        </p>
                                    </div>
                                    <div className='d-flex gap-10 align-items-center my-2'>
                                        <h3 className='product-heading'>Category: </h3> <p className='product-data'>
                                            Watch
                                        </p>
                                    </div>
                                    <div className='d-flex gap-10 align-items-center my-2'>
                                        <h3 className='product-heading'>Tags: </h3> <p className='product-data'>
                                            watch
                                        </p>
                                    </div>
                                    <div className='d-flex gap-10 align-items-center my-2'>
                                        <h3 className='product-heading'>Avaliablity: </h3> <p className='product-data'>
                                            In Stock
                                        </p>
                                    </div>


                                    <div className='d-flex gap-10 flex-column mt-2 mb-3'>
                                        <h3 className='product-heading'>Size: </h3>
                                        <div className='d-flex flex-wrap gap-15'>

                                            <span className='badge border border-1 bg-white text-dark border-secondary'>S</span>
                                            <span className='badge border border-1 bg-white text-dark border-secondary'>M</span>
                                            <span className='badge border border-1 bg-white text-dark border-secondary'>XL</span>
                                            <span className='badge border border-1 bg-white text-dark border-secondary'>XXl</span>

                                        </div>


                                    </div>

                                    <div className='d-flex gap-10 align-items-center  mt-2 mb-3'>
                                        <h3 className='product-heading'>Color: </h3>


                                        <Color />


                                    </div>
                                    <div className='d-flex align-items-center gap-15 flex-row  mt-2 mb-3'>
                                        <h3 className='product-heading'>Quantity: </h3>
                                        <div className=''>
                                            <input className='form-control' type='number' min={1} max={10} name='' style={{ 'width': '70px' }} id='' />

                                        </div>

                                        <div className='d-flex align-items-center gap-30 ms-5'>
                                            <button className='buttom border-0' type='submit'>ADD TO CART</button>
                                            <button className='buttom signup'>Buy It Now</button>

                                        </div>


                                    </div>

                                    <div className='d-flex align-items-center gap-15'>
                                        <div>
                                            <a href=''>
                                                <TbGitCompare className='fs-5 me-2' /> Add to Compare
                                            </a>
                                        </div>
                                        <div>
                                            <a href=''>
                                                <AiOutlineHeart className='fs-5 me-2' />Add to Wishilsit
                                            </a>                                        </div>

                                    </div>


                                    <div className='d-flex gap-10 flex-column  my-3'>
                                        <h3 className='product-heading'>Shipping & Returns: </h3> <p className='product-data'>
                                            Free Shipping and returns Avaliable on all orders!<br /> We ship
                                            all US domestic orders within <b>5.10 business days</b>
                                        </p>
                                    </div>

                                    <div className='d-flex gap-10 align-items-center my-3'>
                                        <h3 className='product-heading'>Product Link</h3>
         
                                        <a href='javascript:void(0)' onClick={() => { copyToclipboard(img) }}>
                                            Copy Product Link
                                        </a>
                                    </div>

                                </div>



                            </div>

                        </div>
                    </div>
                </div>

            </div>

            <div className='description-wrapper py-5 home-wrapper-2'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-12'>
                            <h4>Description</h4>

                            <div className='bg-white p-3'>
                                <p >
                                    Relogios com cobertura de ouro, adequado para crianças e adultos, Relogios com cobertura de ouro, adequado para crianças e adultos
                                    Relogios com cobertura de ouro, adequado para crianças e adultos, Relogios com cobertura de ouro, adequado para crianças e adultos

                                </p>
                            </div>


                        </div>
                    </div>
                </div>
            </div>

            <section className='reviews-wrapper  home-wrapper-2'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-12'>
                            <h3 id='review'>Reviews</h3>

                            <div className='review-inner-wrapper'>
                                <div className='review-head d-flex justify-content-between align-items-end'>
                                    <div>
                                        <h4 className='mb-2'>Customer Reviews</h4>
                                        <div className='d-flex align-items-center gap-10'>
                                            <ReactStars
                                                count={5}
                                                size={24}
                                                value={3}
                                                edit={false}
                                                activeColor="#ffd700"
                                            />
                                            <p className='mb-0'>
                                                Based on 2 reviews
                                            </p>
                                        </div>
                                    </div>

                                    {
                                        orderedProduct && (
                                            <div>
                                                <a className='text-dark text-decoration-underline' href=''>Write a review</a>
                                            </div>
                                        )
                                    }


                                </div>

                                <div className='review-form py-4'>
                                    <h4>Write a review</h4>
                                    <form action='' className='d-flex flex-column gap-15'>
                                        <div>
                                            <ReactStars
                                                count={5}
                                                size={24}
                                                value={3}
                                                edit={true}
                                                activeColor="#ffd700"
                                            />
                                        </div>


                                        <div>
                                            <textarea name='' id='' type='text' cols={30} rows={4} className='w-100 form-control' placeholder='write your comment here' />
                                        </div>

                                        <div className='d-flex justify-content-end'>

                                            <button className='buttom border-0'>Submit Review</button>

                                        </div>
                                    </form>
                                </div>
                                <div className='reviews mt-4'>
                                    <div className='review'>
                                        <div className='d-flex gap-10 align-items-center'>
                                            <h6 className='mb-0'>@andrehangalo</h6>
                                            <ReactStars
                                                count={5}
                                                size={24}
                                                value={3}
                                                edit={false}
                                                activeColor="#ffd700"
                                            />


                                        </div>

                                        <p className='mt-3 '>
                                            Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                                            Lorem Ipsum is simply dummy text of the printing and typesetting industry.

                                        </p>

                                    </div>
                                </div>

                            </div>

                        </div>
                    </div>
                </div>
            </section>

            <section className='popular-wrapper py-5 home-wrapper-2'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-12'>
                            <h3 className='section-heading'>
                                Productos mais populares
                            </h3>
                        </div>
                    </div>
                    <div className='row'>


                        <ProductCard />

                    </div>
                </div>


            </section>
        </>

    )
}

export default SingleProduct