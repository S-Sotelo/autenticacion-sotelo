// /workspaces/autenticacion-sotelo/src/components/Private.js

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Private = () => {
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPrivateData = async () => {
      const token = sessionStorage.getItem('token');
      if (!token) {
        navigate('/login');
        return;
      }

      const response = await fetch('http://localhost:5000/private', {
        method: 'GET',
        headers: {
          'Authorization': token,
        },
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(data.message);
      } else {
        navigate('/login');
      }
    };

    fetchPrivateData();
  }, [navigate]);

  return <div>{message}</div>;
};

export default Private;
