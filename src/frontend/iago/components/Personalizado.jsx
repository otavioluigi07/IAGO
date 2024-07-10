import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import logo from '../assets/logo.svg';

const Personalizados = () => {
  return (
    <div className='py-10 text-center justify-center items-center'>
      <h1 className='text-4xl'>
        Planos <span className="text-[#7000FF]">personalizados?</span><br />
        Entre em contato com nossa equipe!
      </h1>
      <div className='mt-10 flex flex-col items-center space-y-4 sm:flex-row sm:justify-center sm:space-x-4 sm:space-y-0'>
        <button className="bg-[#7000FF] text-white font-bold py-2 px-20 rounded-full transform w-full sm:w-auto hover:shadow-2xl hover:shadow-[#7000FF]">
          Email
        </button>
        <button className="bg-[#138500] text-white font-bold py-2 px-20 rounded-full transform w-full sm:w-auto hover:shadow-2xl hover:shadow-[#9eff8b]">
          WhatsApp
        </button>
        
      </div>
    </div>
  );
};

export default Personalizados;
