import React from 'react'
import BreadCrumb from '../components/BreadCrumb'
import Meta from '../components/Meta'
import { AiOutlineHome, AiOutlineInfo, AiOutlineInfoCircle, AiOutlineMail, AiOutlinePhone } from 'react-icons/ai'

const Contact = () => {
  return (
    <>
      <Meta title='Contact Us' />
      <BreadCrumb title='Contact Us' />

      <div className='contact-wrapper py-5 home-wrapper-2'>
        <div className='container-xxl'>
          <div className='row'>
            <div className='col-12'>

              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d123375.2883636634!2d13.446097352286406!3d-14.910452623229652!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1bbcb44c426d406f%3A0x4fd392bb15a4071b!2sInstituto%20Superior%20Polit%C3%A9cnico%20De%20Huila!5e0!3m2!1spt-PT!2sao!4v1690321551356!5m2!1spt-PT!2sao" 
              width="600" 
              height="450" 
              className='border-0 w-100'
              allowFullScreen="" 
              loading="lazy" 
              referrerPolicy="no-referrer-when-downgrade">

              </iframe>

            </div>
            <div className='col-12 mt-5'>
              <div className='contact-inner-wrapper d-flex justify-content-between'>
                <div>
                  <h3 className='contact-title mb-4'> Contact </h3>
                  <form action='' className='d-flex flex-column gap-15'>
                    <div>
                      <input type='text' className='form-control' placeholder='Name' />
                    </div> <div>
                      <input type='email' className='form-control' placeholder='Email' />
                    </div> <div>
                      <input type='tel' className='form-control' placeholder='Mobile number' />
                    </div>
                    <div>
                      <textarea name='' id='' type='text' cols={30} rows={4} className='w-100 form-control' placeholder='write your comment here' />
                    </div>

                    <div>

                      <button className='buttom border-0'>Submit</button>

                    </div>
                  </form>
                </div>
                <div>
                  <h3 className='contact-title mb-4'> Get In Touch With Us </h3>
                  <div>
                    <ul className='ps-0'>
                      <li className='mb-3 d-flex gap-15 align-items-center'>

                        <AiOutlineHome className='fs-5' />
                        <address className='mb-0'>Angola, Huila, Lubango, Arimba, Instituto Superior Politecnico da Huila, estrada principal.</address>

                      </li>
                      <li className='mb-3 d-flex gap-15 align-items-center'>
                        <AiOutlinePhone className='fs-5' />
                        <a href='tel:244926610909'>+244 926-610-909</a>

                      </li>
                      <li className='mb-3 d-flex gap-15 align-items-center'>
                        <AiOutlineMail className='fs-5' />
                        <a href='mailto:edgarlopes@gmail.com'>edgarlopes@gmail.com</a>
                      </li>
                      <li className='mb-3 d-flex gap-15 align-items-center'>
                        <AiOutlineInfoCircle className='fs-5' />
                        <p className='mb-0'>Aberto de segunda-feira a Domingo</p>
                      </li>
                    </ul>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </>

  )
}

export default Contact