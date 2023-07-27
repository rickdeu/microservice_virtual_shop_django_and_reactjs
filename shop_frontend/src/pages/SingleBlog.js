import React from 'react'
import { Link } from 'react-router-dom'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'
import { BsSearch, HiOutlineArrowLeft } from 'react-icons/hi'

const SingleBlog = () => {
    return (

        <>
            <Meta title='Dynamic Blog Name' />
            <BreadCrumb title='Dynamic Blog Name' />
            <div className='blog-wrapper home-wrapper-2 py-2'>
                <div className='container-xxl'>
                    <div className='row'>
                      
                        <div className='col-12'>
                            <div className='single-blog-card'>
                                <Link className='d-flex align-items-center gap-10' to='/blogs'> <HiOutlineArrowLeft className='fs-4'/>  Go back to Blogs</Link>
                                <h3 className='title'>
                                    A Beatiful Sunday Morning Remaissance
                                </h3>
                                <img src='images/blog-1.jpg' alt='blog' className='img-fluid w-100 my-4'/>
                                <p>
                                Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                                Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                                Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                                </p>

                            </div>

                        </div>

                    </div>
                </div>

            </div>

        </>

    )
}

export default SingleBlog