import React from 'react'
import { Link } from 'react-router-dom'

const BlogCard = () => {
    return (
            <div className='blog-card'>
                <div className='card-image'>
                    <img className='img-fluid w-100' src='images/blog-1.jpg' alt='card-image' />
                </div>
                <div className='blog-content'>
                    <p className='date'>20 de Julho de 2023</p>
                    <h5 className='title'>Rejuvenesça com nossos aparelhos</h5>
                    <p className=' desc'>Lorem Ipsum is simply dummy text of 
                    the printing and typesetting industry.</p>
                    <Link className='buttom' to=''>Ler mais</Link>

                </div>



            </div>
    )
}

export default BlogCard