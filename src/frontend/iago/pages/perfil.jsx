import Navbar from "@components/Navbar"
import Footer from "@components/Footer"
import Formularioperfil from "@components/formularioPerfil"
import { parseCookies, setCookie } from 'nookies';
import { useState, useEffect } from 'react';


export default function Perfil() {
  const [nome, setNome] = useState('');

  useEffect(() => {
    const cookies = parseCookies();
    const userNome = cookies['name'];
    setNome(userNome);
  }, []);
  return (
    <div className="bg-[#3A338E40]">
        <Navbar />
        <div className='pt-20 p-10'>

            <h1 className="mt-14 text-4xl">
                Bem vindo,<span className="text-purple-600"> {nome}</span>!
            </h1>
            <Formularioperfil />

            

        </div>






      <Footer />

    </div>
  )
}
