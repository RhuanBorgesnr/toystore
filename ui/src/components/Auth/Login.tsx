import React from 'react';
import styled from 'styled-components';

const LoginContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
`;

const LoginCard = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 400px;
  width: 100%;
`;

const Title = styled.h1`
  color: #333;
  margin-bottom: 1rem;
`;

const Message = styled.p`
  color: #666;
  margin-bottom: 1.5rem;
`;

const SuccessIcon = styled.div`
  font-size: 3rem;
  color: #4CAF50;
  margin-bottom: 1rem;
`;

const Login: React.FC = () => {
  return (
    <LoginContainer>
      <LoginCard>
        <SuccessIcon>✅</SuccessIcon>
        <Title>Autenticado</Title>
        <Message>
          Você está autenticado automaticamente com token JWT fixo.
        </Message>
      </LoginCard>
    </LoginContainer>
  );
};

export default Login; 