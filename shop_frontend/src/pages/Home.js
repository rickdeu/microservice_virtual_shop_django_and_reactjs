import React, { useState } from 'react'
import Marquee from "react-fast-marquee";
import { Link } from 'react-router-dom';
import BlogCard from '../components/BlogCard';
import ProductCard from '../components/ProductCard';
import SpecialProducts from '../components/SpecialProducts';
import axios from 'axios';

const Home = () => {

  const [categories, setCategories] = useState([])

  useState(() => {
    axios.get('http://127.0.0.1:8000/category-list/')
      .then(response => {
        setCategories(response.data)
      })
      .catch(error => {
        console.error('Error fetching categories')
      })

  }, []);
  return (
    <>
      <section className='home-wrapper-1 py-5'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-6'>
              <div className='main-banner position-relative'>
                <img className='img-fluid rounded' src='images/main-banner-1.jpg' alt='main-banner-1' />
                <div className='main-banner-content position-absolute'>
                  <h4>promoção de</h4>
                  <h5>iPad s13+ Pro.</h5>
                  <p>De Akz 90.000,00 até Akz 500.000,00</p>
                  <Link className='buttom'>COMPRE JÁ</Link>
                </div>


              </div>
            </div>

            <div className='col-6'>



              <div className='d-flex flex-wrap gap-10 justify-content-between align-items-center'>

                <div className='small-banner position-relative'>
                  <img className='img-fluid rounded' src='images/catbanner-01.jpg' alt='catbanner-01' />
                  <div className='small-banner-content position-absolute'>
                    <h4>COMPUTADORES</h4>
                    <h5>MackBook Pro</h5>
                    <p>De 900.000  à 2k AO</p>
                  </div>
                </div>

                <div className='small-banner position-relative'>
                  <img className='img-fluid rounded' src='images/catbanner-02.jpg' alt='catbanner-02' />
                  <div className='small-banner-content position-absolute'>
                    <h4>Novos Productos</h4>
                    <h5>Apple Watches</h5>
                    <p> A prtir de 20.000, 00 Kz</p>
                  </div>
                </div>

                <div className='small-banner position-relative'>
                  <img className='img-fluid rounded' src='images/catbanner-03.jpg' alt='catbanner-03' />
                  <div className='small-banner-content position-absolute'>
                    <h4>10% de Desconto</h4>
                    <h5>Smartwatch 7</h5>
                    <p>7 dias de Garantia</p>
                  </div>
                </div>

                <div className='small-banner position-relative'>
                  <img className='img-fluid rounded' src='images/catbanner-04.jpg' alt='catbanner-04' />
                  <div className='small-banner-content position-absolute'>
                    <h4>Mais vendidos</h4>
                    <h5>AirPods Max</h5>
                    <p>Alta Qualidade de Som</p>
                  </div>
                </div>



              </div>

            </div>

          </div>
        </div>

      </section>
      <section className='home-wrapper-2 py-5'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <div className='services d-flex slign align-items-center justify-content-between'>
                <div className='d-flex align-items-center gap-15'>
                  <img src='images/service.png' alt='services' />
                  <div>
                    <h6> Entrega gratuita</h6>
                    <p className='mb-0'>Compras a partir de 10.000 Akz</p>
                  </div>
                </div>
                <div className='d-flex align-items-center gap-15'>
                  <img src='images/service-02.png' alt='services' />
                  <div>
                    <h6> Ofertas diarias</h6>
                    <p className='mb-0'> Ganhe 25% de desconto </p>
                  </div>
                </div>
                <div className='d-flex align-items-center gap-15'>
                  <img src='images/service-03.png' alt='services' />
                  <div>
                    <h6> Suporte 24/7 </h6>
                    <p className='mb-0'>Atendimento persolizado</p>
                  </div>
                </div>
                <div className='d-flex align-items-center gap-15'>
                  <img src='images/service-04.png' alt='services' />
                  <div>
                    <h6> Preços acessiveis </h6>
                    <p className='mb-0'> Preços Justos</p>
                  </div>
                </div>
                <div className='d-flex align-items-center gap-15'>
                  <img src='images/service-05.png' alt='services' />
                  <div>
                    <h6> Pagamentos seguro </h6>
                    <p className='mb-0'> Pagamento 100% Protegido</p>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
      </section>
      <section className='home-wrapper-2 py-5'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <div className='categories d-flex justify-content-between flex-wrap align-items-center'>

                {categories.map(category => (
                  <div key={category.id} className='d-flex gap align-items-center'>
                    <div>
                      <h6>{category.name}</h6>
                      <p>10 Items</p>
                    </div>
                    <img className='img-fluid' width={110} height={110} src={category.image} alt='camera' />
                  </div>

                ))}


              </div>
            </div>

          </div>
        </div>

      </section>
      <section className='featured-wrapper py-5 home-wrapper-2'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <h3 className='section-heading'>
                Products em Destaques
              </h3>
            </div>
            <ProductCard />
            <ProductCard />
            <ProductCard />
            <ProductCard />


          </div>
        </div>


      </section>
      <section className='famous-wrapper py-5 home-wraper-2'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-3'>
              <div className='famous-card position-relative'>
                <img src='images/catbanner-01.jpg' className='img-fluid' alt='famous' />
                <div className='famous-content position-absolute'>
                  <h5 className='text-dark'>MackBook</h5>
                  <h6 className='text-dark'>Super Potente</h6>
                  <p className='text-dark'>Preços a partir de 500.000 Akz</p>

                </div>
              </div>
            </div>

            <div className='col-3'>
              <div className='famous-card position-relative'>
                <img src='images/catbanner-02.jpg' className='img-fluid' alt='famous' />
                <div className='famous-content position-absolute'>
                  <h5 className='text-dark'>Watch</h5>
                  <h6 className='text-dark'>Versão 2022</h6>
                  <p className='text-dark'>Preços a partir de 500.000 Akz</p>

                </div>
              </div>
            </div>

            <div className='col-3'>
              <div className='famous-card position-relative'>
                <img src='images/catbanner-03.jpg' className='img-fluid' alt='famous' />
                <div className='famous-content position-absolute'>
                  <h5 className='text-dark'>iPad</h5>
                  <h6 className='text-dark'>Verão melhorada</h6>
                  <p className='text-dark'>Preços a partir de 500.000 Akz</p>

                </div>
              </div>
            </div>

            <div className='col-3'>
              <div className='famous-card position-relative'>
                <img src='images/catbanner-04.jpg' className='img-fluid' alt='famous' />
                <div className='famous-content position-absolute'>
                  <h5 className='text-dark'>Auriculas</h5>
                  <h6 className='text-dark'>Suporte Bluethoot</h6>
                  <p className='text-dark'>Preços a partir de 500.000 Akz</p>

                </div>
              </div>
            </div>
          </div>
        </div>

      </section>
      <section className='special-wrapper py-3 home-wrapper-2'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <h3 className='section-heading'>Especial para ti</h3>
            </div>
          </div>
          <div className='row'>
            <SpecialProducts />
            <SpecialProducts />
            <SpecialProducts />
            <SpecialProducts />

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
            <ProductCard />
            <ProductCard />
            <ProductCard />
          </div>
        </div>


      </section>
      <section className='marque-wrapper py-5'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <div className='marquee-inner-wrapper card-wrapper'>
                <Marquee className='d-flex'>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-01.png' alt='brand-01' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-02.png' alt='brand-02' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-03.png' alt='brand-03' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-04.png' alt='brand-04' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-05.png' alt='brand-05' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-06.png' alt='brand-06' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-07.png' alt='brand-07' />
                  </div>
                  <div className='mx-4 w-25'>
                    <img src='images/brand-08.png' alt='brand-08' />
                  </div>
                </Marquee>
              </div>

            </div>
          </div>
        </div>

      </section>
      <section className='blog-wrapper py-5 home-wrapper-2'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>
              <h3 className='section-heading'>
                Noticias no nosso blog
              </h3>
            </div>




          </div>
          <div className='row'>
            <div className='col-3'>
              <BlogCard />
            </div>
            <div className='col-3'>
              <BlogCard />
            </div>
            <div className='col-3'>
              <BlogCard />
            </div>
            <div className='col-3'>
              <BlogCard />
            </div>
          </div>
        </div>


      </section>
    </>

  );
}

export default Home