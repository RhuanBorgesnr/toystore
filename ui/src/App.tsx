import React from 'react';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';
import { useAuth } from './hooks/useAuth';
import { PrivateRoute } from './components/Auth/PrivateRoute';
import { CustomerList } from './components/Customers/CustomerList';
import { Statistics } from './components/Sales/Statistics';

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <BrowserRouter>
      <nav style={{ padding: '1rem', background: '#eee', marginBottom: '2rem' }}>
        <Link to="/customers" style={{ marginRight: '1rem' }}>Clientes</Link>
        <Link to="/statistics">Estatísticas</Link>
      </nav>
      <Routes>
        <Route path="/customers" element={
          <PrivateRoute isAuthenticated={isAuthenticated}>
            <CustomerList />
          </PrivateRoute>
        } />
        <Route path="/statistics" element={
          <PrivateRoute isAuthenticated={isAuthenticated}>
            <Statistics />
          </PrivateRoute>
        } />
        <Route path="*" element={<Navigate to="/customers" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
