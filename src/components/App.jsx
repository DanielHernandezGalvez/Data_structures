import './app.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Navbar from './Navbar/Navbar';
// import ItemListContainer from './ItemListContainer/ItemListContainer';
// import ItemCount from './ItemCount/ItemCount';
import Home from './Home/Home';
import ItemDetailContainer from './ItemDetailContainer/ItemDetailContainer';
import Carrito from './Carrito/Carrito';

const App = () => {
  return (
   <>
   <BrowserRouter>
      <Navbar/> 
      <Routes>
      {/* <ItemCount /> */}
      {/* <ItemListContainer /> */}
          <Route path='/' element={<Home />}/>
          <Route path='/itemdetailcontainer/:id' element={<ItemDetailContainer/>} /> 
          <Route path='/carrito' element={ <Carrito/>}/>
      </Routes>
      </BrowserRouter>
   </>
  );
}

export default App;
