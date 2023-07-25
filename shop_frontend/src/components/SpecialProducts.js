import React from 'react'
import ReactStars from 'react-rating-stars-component'
import { Link } from 'react-router-dom'

const SpecialProducts = () => {
    return (
        <div className='col-6 mb-3'>
            <div className='special-product-card'>
                <div className='d-flex justify-content-between'>
                    <div>
                        <img className='img-fluid' src='images/watch.jpg' alt='watch' />
                    </div>
                    <div className='special-product-content'>
                        <h5 className='brand'>Watches</h5>
                        <h6 className='title'> Exclusivo para Sansung Galaxy Not10+ Mobile Phone Sim...</h6>
                        <ReactStars
                            count={5}
                            size={24}
                            value={3}
                            edit={false}
                            activeColor="#ffd700"
                        />
                        <p className='price'>
                            <span className='red-p'>Akz 1000</span>
                            &nbsp;
                            <strike>Akz 2000</strike>
                        </p>
                        <div className='discount-till d-flex align-items-center gap-10'>
                            <p className='mb-0'><b>5  </b>Dias</p>
                            <div className='d-flex gap-10 align-items-center'>
                                <span className='badge rounded-circle p-2 bg-danger'>4</span>:
                                <span className='badge rounded-circle p-2 bg-danger'>3</span>:
                                <span className='badge rounded-circle p-2 bg-danger'>2</span>
                            </div>



                        </div>
                        <div className='prod-count my-3'>
                            <p>Productos: 5</p>
                            <div className='progress'>
                                <div className='progress-bar'
                                    role='progessbar'
                                    style={{ 'width': '25%' }}
                                    aria-valuemin={0}
                                    aria-valuenow={25}
                                    aria-valuemax={100}>

                                </div>
                            </div>

                        </div>

                        <Link className='buttom'>Adicionar ao carrinho</Link>
                    </div>

                </div>

            </div>
        </div>
    )
}

export default SpecialProducts