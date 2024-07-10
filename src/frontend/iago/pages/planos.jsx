import Image from 'next/image';
import Navbar from "@components/Navbar";
import Footer from "@components/Footer";
import planos from '../assets/planos.png';

export default function Planos() {
  return (
    <div className="bg-[#3A338E30]">
      <Navbar />
      <div className='pt-20 p-10'>
        <h1 className='text-4xl mt-14'>Planos</h1>
        <h2 className='mt-10 text-2xl'>
          Atualmente seu plano é: <span className="text-[#00F0FF]">GRATUITO</span>
        </h2>
        <p className="mt-10 text-[#FFFFFF60]">
          Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        </p>
        
        <div className="flex justify-center items-center">
          <Image src={planos} alt="Descrição da Imagem" className="mt-20 w-full h-auto" />
        </div>
        
        <div className="flex flex-col items-center mt-10 sm:flex-row sm:justify-center sm:space-x-10">
          <button className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-20 rounded-full transform w-full sm:w-auto hover:shadow-2xl hover:shadow-[#7000FF] mb-10">
            Assinar Ouro
          </button>
          <button className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-20 rounded-full transform w-full sm:w-auto hover:shadow-2xl hover:shadow-[#7000FF] mb-10">
            Assinar Prata
          </button>
          <button className="bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-20 rounded-full transform w-full sm:w-auto hover:shadow-2xl hover:shadow-[#7000FF] mb-10">
            Assinar Bronze
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
}
