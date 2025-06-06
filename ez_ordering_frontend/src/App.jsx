import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import OrderPage from './pages/OrderPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/customer/login" element={<LoginPage />} />
        <Route path="/customer/order" element={<OrderPage />} />
      </Routes>
    </Router>
  );
}

export default App;
