import React, { useEffect, useState } from 'react';
import api from '../api/axios';

interface Produto {
  id: number;
  nome: string;
  descricao: string;
}

const ProdutosList: React.FC = () => {
  const [produtos, setProdutos] = useState<Produto[]>([]);

  useEffect(() => {
    api.get('/produtos')
      .then((response) => setProdutos(response.data))
      .catch((error) => console.error('Erro ao carregar produtos:', error));
  }, []);

  return (
    <div>
      <h3>Produtos</h3>
      <ul>
        {produtos.map((produto) => (
          <li key={produto.id}>
            {produto.nome} - {produto.descricao}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProdutosList;
