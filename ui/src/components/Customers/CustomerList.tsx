import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import api from '../../services/api';
import { CustomerCard } from './CustomerCard';
import { CustomerForm } from './CustomerForm';
import { NormalizedCustomer, normalizeCustomerData, RawCustomer } from '../../utils/dataNormalizer';

const Container = styled.div`
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
`;

const Title = styled.h1`
  color: #333;
  margin: 0;
`;

const AddButton = styled.button`
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;

  &:hover {
    background-color: #0056b3;
  }
`;

const FilterContainer = styled.div`
  margin-bottom: 2rem;
  display: flex;
  gap: 1rem;
`;

const FilterInput = styled.input`
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  flex: 1;
`;

const CustomersGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 1rem;
`;

const LoadingMessage = styled.div`
  text-align: center;
  padding: 2rem;
  color: #666;
`;

const ErrorMessage = styled.div`
  background-color: #f8d7da;
  color: #721c24;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
`;

export const CustomerList: React.FC = () => {
  const [customers, setCustomers] = useState<NormalizedCustomer[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [nameFilter, setNameFilter] = useState('');
  const [emailFilter, setEmailFilter] = useState('');

  const fetchCustomers = async () => {
    try {
      setLoading(true);
      const response = await api.get('/customers/');
      const rawCustomers: RawCustomer[] = response.data.data.clientes;
      const normalizedCustomers = rawCustomers.map(normalizeCustomerData);
      setCustomers(normalizedCustomers);
    } catch (err) {
      setError('Erro ao carregar clientes');
      console.error('Erro ao carregar clientes:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCustomers();
  }, []);

  const handleCreateCustomer = async (data: any) => {
    try {
      await api.post('/customers/', data);
      setShowForm(false);
      fetchCustomers();
    } catch (err) {
      console.error('Erro ao criar cliente:', err);
    }
  };

  const handleDeleteCustomer = async (customer: NormalizedCustomer) => {
    console.log(customer)
    if (window.confirm('Tem certeza que deseja excluir este cliente?')) {
      try {
        await api.delete(`/customers/${customer.id}/`);
        fetchCustomers();
      } catch (err) {
        console.error('Erro ao excluir cliente:', err);
      }
    }
  };

  const filteredCustomers = customers.filter(customer => {
    const matchesName = customer.fullName.toLowerCase().includes(nameFilter.toLowerCase());
    const matchesEmail = customer.email.toLowerCase().includes(emailFilter.toLowerCase());
    return matchesName && matchesEmail;
  });

  if (loading) {
    return <LoadingMessage>Carregando clientes...</LoadingMessage>;
  }

  return (
    <Container>
      <Header>
        <Title>Clientes</Title>
        <AddButton onClick={() => setShowForm(true)}>
          Adicionar Cliente
        </AddButton>
      </Header>

      {error && <ErrorMessage>{error}</ErrorMessage>}

      <FilterContainer>
        <FilterInput
          type="text"
          placeholder="Filtrar por nome..."
          value={nameFilter}
          onChange={(e) => setNameFilter(e.target.value)}
        />
        <FilterInput
          type="text"
          placeholder="Filtrar por email..."
          value={emailFilter}
          onChange={(e) => setEmailFilter(e.target.value)}
        />
      </FilterContainer>

      {showForm && (
        <CustomerForm
          onSubmit={handleCreateCustomer}
          onCancel={() => setShowForm(false)}
        />
      )}

      <CustomersGrid>
        {filteredCustomers.map((customer, index) => (
          <CustomerCard
            key={index}
            customer={customer}
            onDelete={handleDeleteCustomer}
          />
        ))}
      </CustomersGrid>

      {filteredCustomers.length === 0 && !loading && (
        <LoadingMessage>Nenhum cliente encontrado.</LoadingMessage>
      )}
    </Container>
  );
}; 