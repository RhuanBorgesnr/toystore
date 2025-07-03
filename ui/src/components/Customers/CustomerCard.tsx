import React from 'react';
import styled from 'styled-components';
import { NormalizedCustomer } from '../../utils/dataNormalizer';
import { findMissingLetter } from '../../utils/alphabetHelper';

interface CustomerCardProps {
  customer: NormalizedCustomer;
  onEdit?: (customer: NormalizedCustomer) => void;
  onDelete?: (customer: NormalizedCustomer) => void;
}

const Card = styled.div`
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
`;

const CustomerInfo = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
`;

const CustomerDetails = styled.div`
  flex: 1;
`;

const CustomerName = styled.h3`
  margin: 0 0 0.5rem 0;
  color: #333;
`;

const CustomerEmail = styled.p`
  margin: 0 0 0.25rem 0;
  color: #666;
`;

const CustomerBirthDate = styled.p`
  margin: 0;
  color: #666;
  font-size: 0.9rem;
`;

const MissingLetterBadge = styled.div`
  background: #007bff;
  color: white;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
  margin-left: 1rem;
`;

const SalesInfo = styled.div`
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
`;

const SalesCount = styled.p`
  margin: 0;
  color: #666;
  font-size: 0.9rem;
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
`;

const Button = styled.button`
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;

  &.edit {
    background-color: #28a745;
    color: white;

    &:hover {
      background-color: #218838;
    }
  }

  &.delete {
    background-color: #dc3545;
    color: white;

    &:hover {
      background-color: #c82333;
    }
  }
`;

export const CustomerCard: React.FC<CustomerCardProps> = ({ 
  customer, 
  onEdit, 
  onDelete 
}) => {
  const missingLetter = findMissingLetter(customer.fullName);
  const salesCount = customer.sales.length;

  return (
    <Card>
      <CustomerInfo>
        <CustomerDetails>
          <CustomerName>{customer.fullName}</CustomerName>
          <CustomerEmail>{customer.email}</CustomerEmail>
          <CustomerBirthDate>
            Nascimento: {new Date(customer.birthDate).toLocaleDateString('pt-BR')}
          </CustomerBirthDate>
        </CustomerDetails>
        <MissingLetterBadge title="Primeira letra não presente no nome">
          {missingLetter}
        </MissingLetterBadge>
      </CustomerInfo>
      
      <SalesInfo>
        <SalesCount>
          Total de vendas: {salesCount}
        </SalesCount>
      </SalesInfo>

      {(onEdit || onDelete) && (
        <ButtonGroup>
          {onEdit && (
            <Button className="edit" onClick={() => onEdit(customer)}>
              Editar
            </Button>
          )}
          {onDelete && (
            <Button className="delete" onClick={() => onDelete(customer)}>
              Excluir
            </Button>
          )}
        </ButtonGroup>
      )}
    </Card>
  );
}; 