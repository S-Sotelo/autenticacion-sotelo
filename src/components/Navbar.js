// /workspaces/autenticacion-sotelo/src/components/Navbar.js

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    sessionStorage.removeItem('token');
    navigate('/login');
  };

  const isAuthenticated = !!sessionStorage.getItem('token');

  return (
    <nav>
      <ul>
        <li><Link to="/signup">Signup</Link></li>
        <li><Link to="/login">Login</Link></li>
        {isAuthenticated && <li><Link to="/private">Private</Link></li>}
        {isAuthenticated && <li><button onClick={handleLogout}>Logout</button></li>}
      </ul>
    </nav>
  );
};

export default Navbar;
