export interface RawCustomer {
  id?: number;
  info: {
    nomeCompleto: string;
    detalhes: {
      email: string;
      nascimento: string;
    };
  };
  duplicado?: {
    nomeCompleto: string;
  };
  estatisticas: {
    vendas: Array<{
      data: string;
      valor: number;
    }>;
  };
}

export interface NormalizedCustomer {
  id?: number;
  fullName: string;
  email: string;
  birthDate: string;
  sales: Array<{
    date: string;
    value: number;
  }>;
}

export const normalizeCustomerData = (rawData: RawCustomer): NormalizedCustomer => {
  return {
    id: rawData.id,
    fullName: rawData.info.nomeCompleto,
    email: rawData.info.detalhes.email,
    birthDate: rawData.info.detalhes.nascimento,
    sales: rawData.estatisticas.vendas.map(sale => ({
      date: sale.data,
      value: sale.valor
    }))
  };
}; 