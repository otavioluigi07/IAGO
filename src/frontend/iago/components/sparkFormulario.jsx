import { useState } from 'react';

const Sparkformulario = () => {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [profissao, setProfissao] = useState('');
  const [celular, setCelular] = useState('');
  const [descricao, setDescricao] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Adicione a lógica de envio do formulário aqui
  };

  return (
    <div className="mt-10 p-10">
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

        <div>
          <label htmlFor="descricao" className="block font-medium text-white mb-4 text-xl">Descrição</label>
          <textarea
            id="descricao"
            value={descricao}
            onChange={(e) => setDescricao(e.target.value)}
            className="bg-[#7000FF21] mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm py-4"
            rows="4"
            required
          />
        </div>

        <div className="flex justify-end">
          <button
            type="submit"
            className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
          >
            Enviar
          </button>
        </div>
      </form>
    </div>
  );
};

export default Sparkformulario;
