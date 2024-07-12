import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { parseCookies, setCookie } from 'nookies';
import { destroyCookie } from 'nookies';


const Formularioperfil = () => {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [profissao, setProfissao] = useState('');
  const [celular, setCelular] = useState('');
  const [idade, setIdade] = useState('');
  const [genero, setGenero] = useState('');
  const [userID, setUserID] = useState(''); // Estado para armazenar o userID

  const router = useRouter();

  useEffect(() => {
    const cookies = parseCookies();
    const userEmail = cookies['email'];
    const userNome = cookies['name'];
    const userProfissao = cookies['occupation'];
    const userCelular = cookies['cell'];
    const userIdade = cookies['age'];
    const userGenero = cookies['gender'];
    const id = cookies['userID'];

    setNome(userNome);
    setEmail(userEmail);
    setProfissao(userProfissao);
    setCelular(userCelular);
    setIdade(userIdade);
    setGenero(userGenero);
    setUserID(id); // Armazena o userID no estado
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userData = {
      nome: nome,
      email: email,
      profissao: profissao,
      celular: celular,
      idade: idade,
      genero: genero
    };

    try {
      const response = await fetch(`http://127.0.0.1:5000/user/${userID}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });

      if (response.ok) {
        alert('Dados atualizados com sucesso!');

        // Atualizar cookies após a atualização bem-sucedida
        setCookie(null, 'userEmail', email, {
          maxAge: 30 * 24 * 60 * 60,
          sameSite: 'strict',
        });
        setCookie(null, 'occupation', profissao, {
          maxAge: 30 * 24 * 60 * 60,
        });
        setCookie(null, 'cell', celular, {
          maxAge: 30 * 24 * 60 * 60,
        });
        setCookie(null, 'age', idade, {
          maxAge: 30 * 24 * 60 * 60,
        });
        setCookie(null, 'gender', genero, {
          maxAge: 30 * 24 * 60 * 60,
        });
        setCookie(null, 'name', nome, {
          maxAge: 30 * 24 * 60 * 60,
        });

        router.push('/perfil');
      } else {
        alert('Erro ao atualizar os dados. Por favor, tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao realizar a requisição:', error);
      alert('Erro na comunicação com o servidor. Por favor, tente novamente.');
    }
  };

  const handleLogout = () => {
    // Limpar todos os cookies relevantes
    destroyCookie(null, 'name');
    destroyCookie(null, 'email');
    destroyCookie(null, 'occupation');
    destroyCookie(null, 'cell');
    destroyCookie(null, 'age');
    destroyCookie(null, 'gender');
    destroyCookie(null, 'userID');
    destroyCookie(null, 'authenticated');

    // Redirecionar para a página inicial
    router.push('/');
  };

  return (
    <div className="mt-10">
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
              type="text"
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

        <div className="flex justify-end">
          <button
            type="submit"
            className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
          >
            Atualizar
          </button>
          <button
          onClick={handleLogout}
          className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]"
          >
          Sair
        </button>
        </div>
      </form>
    </div>
  );
};

export default Formularioperfil;
