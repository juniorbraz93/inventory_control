import React, { useEffect, useState } from 'react';
import api from '../api/axios';

interface Fornecedor {
  id: number;
  nome: string;
  email: string;
}

const FornecedoresList: React.FC = () => {
  const [fornecedores, setFornecedores] = useState<Fornecedor[]>([]);

  useEffect(() => {
    api.get('/fornecedores')
      .then((response) => setFornecedores(response.data))
      .catch((error) => console.error('Erro ao carregar fornecedores:', error));
  }, []);

  return (
    <div>
      <h3>Fornecedores</h3>
      <ul>
        {fornecedores.map((fornecedor) => (
          <li key={fornecedor.id}>
            {fornecedor.nome} - {fornecedor.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FornecedoresList;
