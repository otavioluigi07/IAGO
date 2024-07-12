import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';
import { useState, useEffect } from 'react';
import { parseCookies } from 'nookies';
import { useRouter } from 'next/router';

const Ferramentas = () => {
    const [authenticated, setAuthenticated] = useState(false); // Estado para armazenar o status de autenticação
    const [error, setError] = useState(''); // Estado para armazenar a mensagem de erro
    const router = useRouter(); // Hook do Next.js para navegação

    useEffect(() => {
        const cookies = parseCookies();
        const isAuthenticated = Boolean(cookies['authenticated']); // Converte para booleano
        setAuthenticated(isAuthenticated);
        console.log(isAuthenticated);
    }, []);

    useEffect(() => {
        if (error) {
            const timer = setTimeout(() => {
                setError('');
            }, 3000); // Limpa a mensagem de erro após 3 segundos

            return () => clearTimeout(timer); // Limpa o timer se o componente for desmontado ou o estado error mudar
        }
    }, [error]);


    // Funções de clique para cada botão
    const handleButtonClick1 = () => {
        if (authenticated) {
            router.push('/perfil');
        } else {
            setError('Você precisa estar cadastrado na plataforma para usar esse serviço.');
        }
    };

    const handleButtonClick2 = () => {
        if (authenticated) {
            router.push('/sparkFerramenta');
        } else {
            setError('Você precisa estar cadastrado na plataforma para usar esse serviço.');
        }
    };

    const handleButtonClick3 = () => {
        if (authenticated) {
            router.push('/perfil');
        } else {
            setError('Você precisa estar cadastrado na plataforma para usar esse serviço.');
        }
    };

    return (
        <div className='p-10'>
            <h1 className="text-4xl">
                Serviços <span className="text-purple-600">IAGO</span>!
            </h1>

            {error && (
                <div className="bg-red-500 text-white p-4 rounded mb-4">
                    {error}
                </div>
            )}

            <div className="flex flex-wrap mt-10">
                <div className="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30] shadow-[#7000FF] shadow-md p-4 py-14 sm:mr-8 mb-8 mr-0 text-center rounded-3xl">
                    <h2 className='text-2xl'>Chatbot especializado</h2>
                    <p className='sm:px-14 mt-4 text-[#FFFFFF43]'>
                        Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    </p>
                    <button onClick={handleButtonClick1} className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">
                        Iniciar
                    </button>
                </div>

                <div className="flex-1 bg-gradient-to-r from-[#FFFFFF43] to-[#6AF6FF71] shadow-[#6AF6FF50] shadow-lg p-4 py-14 text-center rounded-3xl mb-8">
                    <h2 className='text-2xl'>Escritor de Copywriter</h2>
                    <p className='sm:px-14 mt-4 text-[#FFFFFF]'>
                        Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    </p>
                    <button onClick={handleButtonClick2} className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#00F0FF50] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#00F0FF]">
                        Iniciar
                    </button>
                    <p className='mt-8 text-[#00F0FF] text-2xl'>
                        POPULAR
                    </p>
                </div>

                <div className="flex-1 bg-gradient-to-r from-[#28009921] to-[#DB00FF30] shadow-[#7000FF] shadow-md p-4 py-14 sm:ml-8 mb-8 text-center rounded-3xl">
                    <h2 className='text-2xl'>Chatbot especializado</h2>
                    <p className='sm:px-14 mt-4 text-[#FFFFFF43]'>
                        Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    </p>
                    <button onClick={handleButtonClick3} className="mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-12 sm:px-20 rounded-full transform sm:w-auto sm:h-auto shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">
                        Iniciar
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Ferramentas;
