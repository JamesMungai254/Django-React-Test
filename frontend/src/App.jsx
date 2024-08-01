import React from 'react';
import { BrowserRouter,Routes,Route,Navigate } from 'react-router-dom';
import Login from './pages/login'
import Home from './pages/home'
import Register from './pages/register'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute';

function Logout(){
  localStorage.clear()
  return <Navigate to='/login'/>
}

function RegisterAndLogout(){
  localStorage.clear()
  return <Register />
}




function App() {
  

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path = '/'
          element ={
            <ProtectedRoute>
              <Home/>
            </ProtectedRoute>
          }
        />
        <Route path ='/Login' element={<Login/>}/>
        <Route path ='/Logout' element={<Logout/>}/>
        <Route path ='/Register' element={<RegisterAndLogout/>}/>
        <Route path ='*' element={<NotFound/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
