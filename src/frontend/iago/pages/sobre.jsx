import Image from 'next/image';
import Navbar from '@components/Navbar';
import Footer from '@components/Footer';
import logo from '../assets/logo.svg';
import sobre from '../assets/sobre.png';
import computador from '../assets/computador.svg';

export default function Sobre() {
  return (
    <div className="bg-[#3A338E40]">
      <Navbar />
      <div className="pt-20">
        <div className="p-10 text-center sm:text-left">
          <h1 className="text-4xl mt-14">
            Sobre <span className="text-purple-600">nós</span>
          </h1>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:mb-20 items-center">
          <div className="col-span-1 sm:text-center">
            <Image src={logo} alt="Descrição da Imagem" className="mx-auto w-3/4 sm:w-full h-auto" />
          </div>
          <div className="col-span-1 sm:col-span-2 px-10 sm:text-left text-center mb-10 sm:mb-0">
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div className="col-span-1 sm:col-span-2 flex items-center px-10 sm:text-left text-center">
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            </p>
          </div>
          <div className="col-span-1 sm:col-span-1 flex items-center justify-center px-10 text-center">
            <h1 className="text-4xl">Valores</h1>
          </div>
        </div>

        <div className="relative flex flex-col sm:mt-20 mt-20 px-4 sm:pl-10 banner-container items-center sm:items-start sm:justify-start justify-center">
          <Image
            src={sobre}
            alt="Banner"
            layout="fill"
            objectFit="cover"
            quality={100}
            className="banner-image sm:w-1/2 w-full"
          />
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-6 relative z-10 text-center sm:text-left">
            <div className="col-span-2 flex flex-col">
              <h1 className="text-4xl mb-4">Missão</h1>
              <p className=''>
                Temos como principal objetivo trazer soluções tecnológicas para outras empresas em um processo de desenvolvimento mútuo entre cliente e empresa, com a finalidade de desenvolver a melhor solução possível visando um objetivo em comum: o impacto social.
              </p>
            </div>
          </div>
          <div className="absolute bottom-0 right-0 -mt-20">
            <Image src={computador} alt="Descrição da Imagem" className="hidden sm:block w-full h-auto"/>
          </div>
        </div>

        <div className="mt-24 p-10 text-center sm:text-left ">
          <div>
            <h1 className="text-4xl mb-4">Visão</h1>
            <p>
              Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and types printing and typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            </p>
          </div>
        </div>

        <Footer />
      </div>

      <style jsx>{`
        .banner-container {
          position: relative;
          width: 100%;
          height: 250px; /* Defina a altura desejada para o banner */
        }
        .banner-image {
          position: absolute;
          top: 0;
          left: 0;
          width: 50%;
          height: 50%;
        }
        @media (max-width: 640px) {
          .banner-container {
            height: 300px; /* Defina a nova altura desejada para dispositivos móveis */
          }
          .banner-image {
            height: auto;
            width: 100%;
          }
        }
      `}</style>
    </div>
  );
}
