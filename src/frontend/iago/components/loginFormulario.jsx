import { useState } from 'react';
import { useRouter } from 'next/router';
import Image from "next/image";
import Link from 'next/link';
import logo from "../assets/logo.svg";

const Loginformulario = () => {
  const [senha, setSenha] = useState('');
  const [email, setEmail] = useState('');
  const router = useRouter();


  const handleSubmit = (e) => {
    e.preventDefault();
    // Adicione a lógica de envio do formulário aqui
  };

  const login = async (e) => {
    e.preventDefault();

    if (password !== passwordC) {
      alert("As senhas não coincidem!");
      return;
    }

    const userData = {
      name: nome,
      email: email,
      password: password,
      occupation: profissao,
      cell: celular,
      age: idade,
      gender: genero,
      subscription_id: 1,
      role: "user"
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/user/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });

      if (response.ok) {
        alert("Cadastro feito com sucesso!");

      } else {
        alert("Email ou senha inválidos.");
      }
    } catch (error) {
      alert("Erro ao efetuar o login: " + error);
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
        <form onSubmit={handleSubmit} className="space-y-6 text-white">
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
              type="submit"
              onClick={handleCadastroClick}
              className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
            >
              Cadastrar
            </button>
            <button
              type="submit"
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
