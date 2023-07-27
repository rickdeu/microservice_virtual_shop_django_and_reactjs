import React from 'react';
import './App.css';
import Layout from './components/Layout';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import OurStore from './pages/OurStore';
import Blogs from './pages/Blogs';
import CompareProduct from './pages/CompareProduct';
import Wishlist from './pages/Wishlist';
import Login from './pages/Login';
import ForgoutPassword from './pages/ForgoutPassword';
import Signup from './pages/Signup';
import ResetPassword from './pages/ResetPassword';
import SingleBlog from './pages/SingleBlog';
import PrivacyPolicy from './pages/PrivacyPolicy';
import RefundPolicy from './pages/RefundPolicy';
import ShippingPolicy from './pages/ShippingPolicy';
import TermAndConditions from './pages/TermAndConditions';
function App() {
  return(
  <>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>

          <Route index element={<Home />} />
          <Route path='about' element={<About/>}/>  
          <Route path='contact' element={<Contact/>}/>
          <Route path='store' element={<OurStore/>}/>
          <Route path='blogs' element={<Blogs/>}/>
          <Route path='blog/:id' element={<SingleBlog/>}/>
          <Route path='compare-product' element={<CompareProduct/>}/>
          <Route path='wishlist' element={<Wishlist/>}/>
          <Route path='login' element={<Login/>}/>
          <Route path='signup' element={<Signup/>}/>
          <Route path='forgot-password' element={<ForgoutPassword/>}/>
          <Route path='reset-password' element={<ResetPassword/>}/>
          
          <Route path='privacy-policy' element={<PrivacyPolicy/>}/>
          <Route path='refund-policy' element={<RefundPolicy/>}/>
          <Route path='shipping-policy' element={<ShippingPolicy/>}/>
          <Route path='termandconditions' element={<TermAndConditions/>}/>





        </Route>
      </Routes>
    </BrowserRouter>
  </>);
}
export default App;