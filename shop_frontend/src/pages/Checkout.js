import React from 'react'
import { BiArrowBack } from 'react-icons/bi'
import { Link } from 'react-router-dom'
import watch from '../images/watch.jpg'


const Checkout = () => {
    return (
        <>
            <div className='checkout-wrapper py-5 home-wrapper-2'>
                <div className='container-xxl'>
                    <div className='row'>
                        <div className='col-7'>
                            <div className='checkout-left-data'>
                                <h3 className='website-name'>Dev Corner</h3>
                                <nav style={{ '--bs-breadcrumb-divider': '>' }}
                                    aria-label='breadcrumb'
                                >
                                    <ol className='breadcrumb'>
                                        <li className='breadcrumb-item'>
                                            <Link className='text-dark total-price' href='/cart'>Cart </Link>
                                        </li>
                                        &nbsp;  /
                                        <li className='breadcrumb-item active' aria-current='page'>
                                            Information
                                        </li>
                                        &nbsp;  /
                                        <li className='breadcrumb-item active total-price'>
                                        &nbsp;  Shipping
                                        </li>
                                        &nbsp;  /
                                        <li className='breadcrumb-item active total-price' aria-current='page'>
                                            Payment
                                        </li>
                                    </ol>

                                </nav>

                                <h4 className='title'>
                                    Contact Information
                                </h4>
                                <p className='user-details'>
                                    Navedeep dahiya ( edgarlopes@gmail.com)
                                </p>
                                <h4 className='mb-3'>
                                    Shipping Address
                                </h4>
                                <form action='' className='d-flex gap-15 flex-wrap justify-content-between'>

                                    <div className='w-100'>
                                        <select className='form-control form-select' id=''>
                                            <option value='' selected disabled>Select Country</option>
                                            <option value='Angola'>Angola</option>
                                            <option value='Nigeria'>Nigeria</option>
                                            <option value='Namibia'>Namibia</option>
                                            <option value='Togo'>Togo</option>

                                        </select>
                                    </div>
                                    <div className='flex-grow-1'>
                                        <input type='text' placeholder='First Name' className='form-control' />
                                    </div>
                                    <div className='flex-grow-1'>
                                        <input type='text' placeholder='Last Name' className='form-control' />
                                    </div>
                                    <div className='w-100'>
                                        <input type='text' placeholder='Address' className='form-control' />
                                    </div>
                                    <div className='w-100'>
                                        <input type='text' placeholder='Apartment' className='form-control' />
                                    </div>
                                    <div>
                                        <input type='text' placeholder='City' className='form-control' />

                                    </div>
                                    <div className='flex-grow-1'>
                                        <select className='form-control form-select' id=''>
                                            <option value='' disabled selected>Select State</option>
                                            <option value='Luanda'>Luanda</option>
                                            <option value='Lubango'>Lubango</option>
                                            <option value='Namibe'>Togo</option>

                                        </select>
                                    </div>
                                    <div className='flex-grow-1'>
                                        <input type='text' placeholder='Zipcode' className='form-control' />

                                    </div>

                                    <div className='w-100'>
                                        <div className='d-flex justify-content-between align-items-center'>
                                            <Link to='/cart' className='text-dark'>
                                                <BiArrowBack className='mb-2' />  Return to Cart
                                            </Link>

                                            <Link to='#' className='buttom'>
                                                Continue to Shipping
                                            </Link>

                                        </div>

                                    </div>

                                </form>
                            </div>
                        </div>
                        <div className='col-5'>

                            <div className='border-bottom py-4'>
                                <div className='d-flex gap-10 mb-2 align-items-center'>
                                    <div className='w-75 d-flex gap-10'>
                                        <div className='w-25 position-relative'>
                                            <span style={{ 'top': '-10px', 'right': '2px' }} className='badge bg-secondary text-white rounded-circle p-2 position-absolute'>1</span>
                                            <img className='img-fluid' src={watch} alt=' produc t' />
                                        </div>
                                        <div>
                                            <h5 className='title'>Product1</h5>
                                            <p className='description'>
                                                Product with super quality / enjoy
                                            </p>
                                        </div>

                                    </div>
                                    <div className='flex-grow-1'>
                                        <h5 className='total'>Akz 1.000</h5>

                                    </div>
                                </div>

                            </div>
                            <div className='border-bottom py-4'>
                                <div className='d-flex justify-content-between align-items-center'>
                                    <p className='subtotal'>Subtotal</p>
                                    <p className='total-price'>Akz 5.000.00</p>
                                </div>
                                <div className='d-flex justify-content-between align-items-center'>
                                    <p className='mb-0 shipping'>Shipping</p>
                                    <p className='mb-0 total-price' >Akz 5.000.00</p>
                                </div>
                            </div>
                            <div className='d-flex justify-content-between align-items-center border-bottom py-4'>
                                <h4 className='total'>Total</h4>
                                <h5 className='total-price'>Akz 5.000.00</h5>
                            </div>


                        </div>

                    </div>
                </div>
            </div>
        </>

    )
}

export default Checkout