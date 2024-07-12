import { useState } from 'react';
import { useRouter } from 'next/router';
import Image from "next/image";
import logo from "../assets/logo.svg";
import { setCookie } from 'nookies';

const Loginformulario = () => {
  const [senha, setSenha] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState(''); // Estado para armazenar mensagens de erro
  const router = useRouter();

  const login = async (e) => {
    e.preventDefault();

    const userData = {
      email: email,
      password: senha
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/user/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });

      if (response.ok) {
        const { data, authenticated, id, name, email, occupation, cell, age, gender, subscription_id, role, password } = await response.json();
        if (authenticated) {
          console.log(id);
          alert('Login bem-sucedido');

          // Definir cookies
          setCookie(null, 'userEmail', email, {
            maxAge: 30 * 24 * 60 * 60,
            sameSite: 'strict',
          });
          setCookie(null, 'userID', id, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'authenticated', true, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'email', email, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'occupation', occupation, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'cell', cell, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'age', age, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'gender', gender, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'subscription_id', subscription_id, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'role', role, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'password', password, {
            maxAge: 30 * 24 * 60 * 60,
          });
          setCookie(null, 'name', name, {
            maxAge: 30 * 24 * 60 * 60,
          });

          router.push('/perfil');
        } else {
          console.log(senha)
          console.log(password)
          setError('Email ou senha incorretos'); // Define erro aqui se a autenticação falhar
        }
      } else if (response.status === 401) {
        const data = await response.json();
        setError(data.error); // Define o erro recebido do servidor
      } else {
        setError('Ocorreu um erro inesperado. Por favor, tente novamente.');
      }
    } catch (error) {
      setError('Erro na comunicação com o servidor. Por favor, tente novamente.');
    }
  };

  const handleCadastroClick = () => {
    router.push('/cadastro');
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="p-10">
        <div className="flex justify-center mb-8">
          <Image src={logo} alt="Logo" width={200} height={180} />
        </div>
        <form className="space-y-6 text-white">
          {error && <div className="text-red-500">{error}</div>} {/* Mostra mensagem de erro, se houver */}
          <div className="flex flex-col space-y-4">
            <div className="w-full">
              <label htmlFor="email" className="block font-medium text-white mb-4 text-xl">Email</label>
              <input
                type="text"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="bg-[#7000FF50] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
                required
              />
            </div>
            <div className="w-full">
              <label htmlFor="senha" className="block font-medium text-white mb-4 text-xl">Senha</label>
              <input
                type="password"
                id="senha"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
                className="bg-[#7000FF50] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
                required
              />
            </div>
          </div>
          <div className="flex justify-center space-x-4">
            <button
              type="button"
              onClick={handleCadastroClick}
              className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
            >
              Cadastrar
            </button>
            <button
              type="button"
              onClick={login}
              className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
            >
              Entrar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Loginformulario;
