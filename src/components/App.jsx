import './app.css';
import Navbar from './Navbar/Navbar';
import ItemListContainer from './ItemListContainer/ItemListContainer';
// import ItemCount from './ItemCount/ItemCount';
import Home from './Home/Home';

const App = () => {
  return (
   <>
      <Navbar/> 
      {/* <ItemCount /> */}
      <ItemListContainer />
      <Home />
   </>
  );
}

export default App;
