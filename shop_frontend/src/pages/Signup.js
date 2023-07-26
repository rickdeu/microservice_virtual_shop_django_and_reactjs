import React from 'react'
import { Link } from 'react-router-dom'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'

const Signup = () => {
    return (

        <>
            <Meta title='SignUp' />
            <BreadCrumb title='SignUp' />
            <div className='login-wrapper py-5 home-wrapper-2'>
              <div className='container-xxl'>
              <div className='row'>
                    <div className='col-12'>
                        <div className='auth-card'>
                            <h3 className='text-center mb-3'>Create Account</h3>
                            <form action='' className='d-flex flex-column gap-15'>
                            <div>
                                    <input type='text' name='name' className='form-control' placeholder='Name' />
                                </div>
                                <div>
                                    <input type='tel' name='mobile' className='form-control' placeholder='Mobile number' />
                                </div>
                                <div>
                                    <input type='email' name='email' className='form-control' placeholder='Email' />
                                </div>
                                <div>
                                    <input type='password' name='password' className='form-control' placeholder='Password' />
                                </div>
                                <div className='mt-1'>
                                    <div className='mt-3 d-flex justify-content-center gap-15 align-items-center'>
                                        <button className='buttom border-0' type='submit'>Create</button>

                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

              </div>
            </div>

        </>

    )
}

export default Signup