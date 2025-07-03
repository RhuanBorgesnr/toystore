import React, { useState } from 'react';
import styled from 'styled-components';

interface CustomerFormData {
  username: string;
  full_name: string;
  email: string;
  birth_date: string;
  password: string;
}

interface CustomerFormProps {
  onSubmit: (data: CustomerFormData) => Promise<void>;
  onCancel: () => void;
}

const FormContainer = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: 2rem auto;
`;

const Title = styled.h2`
  margin-bottom: 1.5rem;
  color: #333;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const Input = styled.input`
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
`;

const Button = styled.button`
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  flex: 1;

  &.primary {
    background-color: #007bff;
    color: white;

    &:hover {
      background-color: #0056b3;
    }
  }

  &.secondary {
    background-color: #6c757d;
    color: white;

    &:hover {
      background-color: #545b62;
    }
  }

  &:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
`;

export const CustomerForm: React.FC<CustomerFormProps> = ({ onSubmit, onCancel }) => {
  const [formData, setFormData] = useState<CustomerFormData>({
    username: '',
    full_name: '',
    email: '',
    birth_date: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit(formData);
    } catch (error) {
      console.error('Erro ao criar cliente:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <FormContainer>
      <Title>Adicionar Cliente</Title>
      <Form onSubmit={handleSubmit}>
        <Input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <Input
          type="text"
          name="full_name"
          placeholder="Nome completo"
          value={formData.full_name}
          onChange={handleChange}
          required
        />
        <Input
          type="email"
          name="email"
          placeholder="E-mail"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <Input
          type="date"
          name="birth_date"
          value={formData.birth_date}
          onChange={handleChange}
          required
        />
        <Input
          type="password"
          name="password"
          placeholder="Senha"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <ButtonGroup>
          <Button type="button" className="secondary" onClick={onCancel}>
            Cancelar
          </Button>
          <Button type="submit" className="primary" disabled={loading}>
            {loading ? 'Salvando...' : 'Salvar'}
          </Button>
        </ButtonGroup>
      </Form>
    </FormContainer>
  );
}; 