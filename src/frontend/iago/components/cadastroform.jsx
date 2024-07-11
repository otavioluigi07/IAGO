import { useState } from 'react';

const Cadastroform = () => {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [profissao, setProfissao] = useState('');
  const [celular, setCelular] = useState('');
  const [idade, setIdade] = useState('');
  const [genero, setGenero] = useState('');
  const [password, setPassword] = useState('');
  const [passwordC, setPasswordC] = useState('');

  const handleSubmit = async (e) => {
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
        alert("Cadastro realizado com sucesso!");
        setCelular('')
        setEmail('')
        setGenero('')
        setIdade('')
        setIdade('')
        setNome('')
        setPassword('')
        setPasswordC('')
        setProfissao('')
      } else {
        alert("Erro ao realizar cadastro.");
      }
    } catch (error) {
      alert("Erro ao enviar dados: " + error);
    }
  };

  return (
    <div className="px-10">
      <form onSubmit={handleSubmit} className="space-y-6 text-white">
        <div className="flex flex-col sm:flex-row sm:space-x-4">
          <div className="w-full sm:w-1/2">
            <label htmlFor="nome" className="block font-medium text-white mb-4 text-xl">Nome</label>
            <input
              type="text"
              id="nome"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
          <div className="w-full sm:w-1/2 mt-4 sm:mt-0">
            <label htmlFor="email" className="block font-medium text-white mb-4 text-xl">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
        </div>

        <div className="flex flex-col sm:flex-row sm:space-x-4">
          <div className="w-full sm:w-1/2">
            <label htmlFor="profissao" className="block font-medium text-white mb-4 text-xl">Profissão</label>
            <input
              type="text"
              id="profissao"
              value={profissao}
              onChange={(e) => setProfissao(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
          <div className="w-full sm:w-1/2 mt-4 sm:mt-0">
            <label htmlFor="celular" className="block font-medium text-white mb-4 text-xl">Celular</label>
            <input
              type="tel"
              id="celular"
              value={celular}
              onChange={(e) => setCelular(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
        </div>

        <div className="flex flex-col sm:flex-row sm:space-x-4">
          <div className="w-full sm:w-1/2">
            <label htmlFor="idade" className="block font-medium text-white mb-4 text-xl">Idade</label>
            <input
              type="number"
              id="idade"
              value={idade}
              onChange={(e) => setIdade(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
          <div className="w-full sm:w-1/2 mt-4 sm:mt-0">
            <label htmlFor="genero" className="block font-medium text-white mb-4 text-xl">Gênero</label>
            <input
              type="text"
              id="genero"
              value={genero}
              onChange={(e) => setGenero(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
        </div>

        <div className="flex flex-col sm:flex-row sm:space-x-4">
          <div className="w-full sm:w-1/2 mt-4 sm:mt-0">
            <label htmlFor="password" className="block font-medium text-white mb-4 text-xl">Senha</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
          <div className="w-full sm:w-1/2 mt-4 sm:mt-0">
            <label htmlFor="passwordC" className="block font-medium text-white mb-4 text-xl">Confirmar senha</label>
            <input
              type="password"
              id="passwordC"
              value={passwordC}
              onChange={(e) => setPasswordC(e.target.value)}
              className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
              required
            />
          </div>
        </div>

        <div className="flex justify-center">
          <button
            type="submit"
            className="mt-4 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
          >
            Cadastrar
          </button>
        </div>
      </form>
    </div>
  );
};

export default Cadastroform;
