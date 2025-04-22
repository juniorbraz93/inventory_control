import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/axios';
import ProdutosList from '../components/ProdutosList';
import FornecedoresList from '../components/FornecedoresList';

const DashboardPage: React.FC = () => {
  const navigate = useNavigate();
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/');
      return;
    }

    // Verifica se o usuário é admin
    api.get('/auth/me')  // Supondo que você tenha uma rota de "me" para obter dados do usuário
      .then((response) => {
        setIsAdmin(response.data.is_admin);
      })
      .catch(() => {
        localStorage.removeItem('access_token');
        navigate('/');
      });
  }, [navigate]);

  return (
    <div>
      <h2>Dashboard</h2>
      {isAdmin ? <h3>Admin</h3> : <h3>Funcionário</h3>}
      <ProdutosList />
      <FornecedoresList />
    </div>
  );
};

export default DashboardPage;
