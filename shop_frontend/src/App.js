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
          <Route path='compare-product' element={<CompareProduct/>}/>
          <Route path='wishlist' element={<Wishlist/>}/>
          <Route path='login' element={<Login/>}/>
          <Route path='signup' element={<Signup/>}/>
          <Route path='forgot-password' element={<ForgoutPassword/>}/>
          <Route path='reset-password' element={<ResetPassword/>}/>



        </Route>
      </Routes>
    </BrowserRouter>
  </>);
}
export default App;