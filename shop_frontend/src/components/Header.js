import React, { useEffect } from 'react'
import { NavLink, Link } from 'react-router-dom'
import { BsSearch } from 'react-icons/bs'
import { useDispatch, useSelector } from 'react-redux'
import { listCategory } from '../actions/CategoryActions'

const Header = () => {

  const dispatch = useDispatch()
  const categoryList = useSelector(state => state.categoryList)
  const cart = useSelector(state => state.cart)

  const { categories } = categoryList

  const { cartItems } = cart

  useEffect(() => {
    dispatch(listCategory())
  }, [dispatch])



  return (
    <>
      <header className='header-top-strip py-3'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-6'>
              <p className='text-white mb-0'>
                MERCADO VIRTUAL INTELIGENTE
              </p>

            </div>
            <div className='col-6'>
              <p className='text-end text-white mb-0'>
               <b> Contacto: </b> <a className='text-white' href='tel:244926610909'>+244 926-610-909</a> 
               <b> Email: </b> <a className='text-white' href='mailto:edgarlopes@gmail.com'>edgarlopes@gmail.com</a>

              </p>

            </div>

          </div>

        </div>

      </header>

      <header className='header-upper py-3'>
        <div className='row align-items-center'>
          <div className='col-2'>
            <h2>
              <Link className='text-white'>Shop Online</Link>
            </h2>

          </div>
          <div className='col-5'>
            <div className="input-group">
              <input type="text" className="form-control py-2" placeholder="Procurar productos..." aria-label="Procurar productos..." aria-describedby="basic-addon2" />
              <span className="input-group-text py-3" id="basic-addon2">
                <BsSearch className='fs-6' />
              </span>
            </div>
          </div>

          <div className='col-5'>
            <div className='header-upper-links d-flex align-items-center justify-content-between'>
              <div>
                <Link to='/compare-product' className='d-flex align-items-center gap-10 text-white'>
                  <img src='/images/compare.svg' alt='compare' />
                  <p className='mb-0'>Comparar <br />Productos</p>
                </Link>
              </div>
              <div>
                <Link to='/wishlist' className='d-flex align-items-center gap-10 text-white'>
                  <img src='/images/wishlist.svg' alt='favoritos' />
                  <p className='mb-0'>Favoritos</p>
                </Link>
              </div>
              <div>
                <Link to='/login' className='d-flex align-items-center gap-10 text-white'>
                  <img src='/images/user.svg' alt='user' />
                  <p className='mb-0'>Login <br />Minha Conta</p>
                </Link>
              </div>
              <div>
                <Link to='/cart' className='d-flex align-items-center gap-10 text-white'>
                  <img src='/images/cart.svg' alt='cart' />
                  <div className='d-flexe flex-column gap-10'>
                    <span className='badge bg-white text-dark'>
                    {cartItems.reduce((acc, item) => acc + item.qty, 0)}
                    </span>
                    <p className='mb-0'>{cartItems.reduce((acc, item) => acc + item.qty * item.price, 0).toFixed(2)}</p>

                  </div>
                </Link>
              </div>


            </div>

          </div>

        </div>

      </header>

      <header className='header-bottom py-3'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <div className='menu-bottom d-flex align-items-center gap-30'>
                <div>

                  <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle bg-transparent border-0 gap-15  d-flex align-items-center" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                     <img src='/images/menu.svg' alt='menu'/>
                      <span className='me-5 d-inline-block'>Categorias</span>
                    </button>
                    <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">

                      {
                        categories.map((category)=>(
                          <li key={category.id}><Link className="dropdown-item text-white" to="">{category.name}</Link></li>
                        ))
                      }
                     
                    
                    
                    </ul>
                  </div>

                </div>
                <div className='menu-links'>
                  <div className='d-flex align-items-center gap-15'>
                    <NavLink className='text-white' to='/'>Pagina Inicial</NavLink>
                    <NavLink className='text-white' to='/store'>Nossas Lojas</NavLink>
                    <NavLink className='text-white' to='/blogs'>Novidades</NavLink>
                    <NavLink className='text-white' to='/contact'>Contactos</NavLink>

                  </div>
                </div>



              </div>

            </div>


          </div>

        </div>

      </header>

    </>
  );
}

export default Header