import React from 'react'
import { BsGithub, BsInstagram, BsLinkedin, BsYoutube } from 'react-icons/bs'
import { Link } from 'react-router-dom'

const Footer = () => {
  return (
    <>
      <footer className='py-4'>
        <div className='container-xxl'>
          <div className='row align-items-center'>
            <div className='col-5'>
              <div className='footer-top-data d-flex gap-30 align-items-center'>
                <img src='images/newsletter.png' alt='newsletter' />
                <h2 className='mb-0 text-white'>Assine a nossa newsletter</h2>

              </div>

            </div>
            <div className='col-7'>

              <div className="input-group">
                <input type="text" className="form-control py-1" placeholder="Endereço de email..." aria-label="Endereço de email..." aria-describedby="basic-addon2" />
                <span className="input-group-text py-2" id="basic-addon2">
                  Subscrever
                </span>
              </div>

            </div>

          </div>

        </div>
      </footer>
      <footer className='py-4'>

        <div className='container-xxl'>
          <div className='row'>
            <div className='col-4'>
              <h4 className='text-white mb-4'> Contacte-nos</h4>
              <div>

                <address className='text-white fs-6'>
                  Angola, Huila, Lubango, Arimba, <br />
                  Instituto Superior Politecnico da Huila, <br /> estrada principal.
                  <br />
                  Codigo Postal: 000019

                </address>

                <a className='mt-3 d-block mb-2 text-white' href='tel:244926610909'>+244 926-610-909</a>

                <a className='mt-2 d-block mb-1 text-white' href='mailto:edgarlopes@gmail.com'>edgarlopes@gmail.com</a>
                <div className='social_icons d-flex align-center gap-30 mt-text-4'>

                  <a href='#' className='text-white'>
                    <BsLinkedin className='fs-4' />

                  </a>
                  <a href='#' className='text-white'>
                    <BsInstagram className='fs-4' />

                  </a>
                  <a href='#' className='text-white'>
                    <BsGithub className='fs-4' />

                  </a>
                  <a href='#' className='text-white'>
                    <BsYoutube className='fs-4' />

                  </a>

                </div>
              </div>
            </div>
            <div className='col-3'>
              <h4 className='text-white mb-4'> Informação </h4>
              <div className='footer-links d-flex flex-column'>
                <Link to='/privacy-policy' className='text-white py-2 mb-1'>Politicas de Privacidade</Link>
                <Link to='/refund-policy' className='text-white py-2 mb-1'>Politicas de Reembolso</Link>
                <Link to='/shipping-policy' className='text-white py-2 mb-1'>Politicas de Entrega</Link>
                <Link to='/termandconditions' className='text-white py-2 mb-1'>Termos & Condições</Link>
                <Link to='/blogs' className='text-white py-2 mb-1'>Noticias</Link>

              </div>          </div>
            <div className='col-3'>
              <h4 className='text-white mb-4'> Minha conta </h4>
              <div className='footer-links d-flex flex-column'>
                <Link className='text-white py-2 mb-1'>Sobre nós</Link>
                <Link className='text-white py-2 mb-1'>Faq</Link>
                <Link className='text-white py-2 mb-1'>Conteudos</Link>

              </div>          </div>
            <div className='col-2'>
              <h4 className='text-white mb-4'> Links Rapidos </h4>
              <div className='footer-links d-flex flex-column'>
                <Link className='text-white py-2 mb-1'>PC's & Laptops</Link>
                <Link className='text-white py-2 mb-1'>HeadPhones</Link>
                <Link className='text-white py-2 mb-1'>Tablets & Telefones</Link>
                <Link className='text-white py-2 mb-1'>Acessorios</Link>

              </div>
            </div>

          </div>

        </div>



      </footer>
      <footer className='py-4'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <p className='text-center mb-0 text-white'>
                &copy; {new Date().getFullYear()}; Desenvolvido por Edgar Lopes

              </p>


            </div>

          </div>

        </div>
      </footer>

    </>

  )
}

export default Footer