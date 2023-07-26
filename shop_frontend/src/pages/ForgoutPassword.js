import React from 'react'
import { Link } from 'react-router-dom'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'

const ForgoutPassword = () => {
    return (
        <>
            <Meta title='Forgot Password' />
            <BreadCrumb title='Forgot Password' />
            <div className='login-wrapper py-5 home-wrapper-2'>
                <div className='row'>
                    <div className='col-12'>
                        <div className='auth-card'>
                            <h3 className='text-center mb-3'>Reset Your Password</h3>
                            <p className='text-center mt-2 mb-3'>
                                We will send you an email to reset your password

                            </p>
                            <form action='' className='d-flex flex-column gap-15'>
                                <div>
                                    <input type='email' name='email' className='form-control' placeholder='Email' />
                                </div>
                              
                                <div className='mt-1'>
                                    <div className='mt-3 d-flex justify-content-center flex-column gap-15 align-items-center'>
                                        <button className='buttom border-0' type='submit'>Submit</button>
                                        <Link to='/login'>Cancel</Link>

                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

            </div>
     
     
        </>)
}

export default ForgoutPassword