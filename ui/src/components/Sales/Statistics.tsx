import React, { useEffect, useState } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import api from '../../services/api';
import styled from 'styled-components';

const HighlightCard = styled.div<{
  color?: string;
}>`
  background: ${({ color }) => color || '#f5f5f5'};
  color: #222;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  font-weight: 500;
`;

const SectionTitle = styled.h3`
  margin-top: 2rem;
  margin-bottom: 1rem;
`;

export const Statistics: React.FC = () => {
  const [dailySales, setDailySales] = useState<{date: string, total: number}[]>([]);
  const [customerStats, setCustomerStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    setLoading(true);
    Promise.all([
      api.get('/sales/statistics/'),
      api.get('/sales/customers/statistics/')
    ])
      .then(([salesRes, custRes]) => {
        setDailySales(salesRes.data.daily_sales);
        setCustomerStats(custRes.data);
      })
      .catch(() => setError('Erro ao carregar estatísticas'))
      .finally(() => setLoading(false));
  }, []);

  const chartOptions = {
    title: { text: 'Total de Vendas por Dia' },
    xAxis: { categories: dailySales.map(s => s.date) },
    yAxis: { title: { text: 'Total (R$)' } },
    series: [{
      name: 'Vendas',
      data: dailySales.map(s => s.total),
      color: '#007bff',
      type: 'line',
    }],
    chart: { height: 350 },
  };

  if (loading) return <div>Carregando estatísticas...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <HighchartsReact highcharts={Highcharts} options={chartOptions} />
      <SectionTitle>Destaques dos Clientes</SectionTitle>
      {customerStats && (
        <div>
          {customerStats.highest_volume && (
            <HighlightCard color="#ffe082">
              <span role="img" aria-label="volume">🏆</span> <b>Maior volume de vendas:</b> {customerStats.highest_volume.customer.full_name} <br/>
              <small>Total vendido: R$ {customerStats.highest_volume.total_sales.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</small>
            </HighlightCard>
          )}
          {customerStats.highest_average && (
            <HighlightCard color="#b2ffb2">
              <span role="img" aria-label="media">💰</span> <b>Maior média por venda:</b> {customerStats.highest_average.customer.full_name} <br/>
              <small>Média: R$ {customerStats.highest_average.average_sale.toLocaleString('pt-BR', {minimumFractionDigits: 2})}</small>
            </HighlightCard>
          )}
          {customerStats.highest_frequency && (
            <HighlightCard color="#b3e5fc">
              <span role="img" aria-label="frequencia">🔁</span> <b>Maior frequência de compras:</b> {customerStats.highest_frequency.customer.full_name} <br/>
              <small>Dias diferentes com compras: {customerStats.highest_frequency.unique_purchase_days}</small>
            </HighlightCard>
          )}
        </div>
      )}
    </div>
  );
}; 