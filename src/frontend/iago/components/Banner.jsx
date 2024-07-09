// components/Banner.jsx
import Image from 'next/image';
import banner from '../assets/banner.png';
import mulher from '../assets/mulher.svg';


const Banner = () => {
  return (
    <div className="banner-container px-10">
      <Image
        src={banner}
        alt="Banner"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="banner-image"
      />
      <style jsx>{`
        .banner-container {
          position: relative;
          width: 100%;
          height: 605px; /* Defina a altura desejada para o banner */
          overflow: hidden;
        }

        .banner-image {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }

        .highlight-text {
          color: #7000FF; /* Cor magenta para destacar */
        }
      `}</style>
      <div className='mt-52'>
        <h1 className='text-5xl font-zen-dots'>
          Soluções com <span className="text-purple-500">inteligência</span><br />
          além da <span className="text-purple-500">artificial</span>
        </h1>
        <p className='mt-10 pr-10'>
        Lorem Ipsum is simply dummy text of the printing and types printing and <br></br>typesetting industry.Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        </p>
        <div className="mt-10">
            <button className="bg-white hover:shadow-2xl hover:shadow-white text-black font-bold py-2 px-4 sm:px-14 rounded-full transform sm:w-auto sm:h-auto shadow-white shadow-md">
                Contato
            </button>
            <button className="ml-4 mt-10 bg-gradient-to-r from-[#7000FF] to-[#998100] text-white font-bold py-2 px-4 sm:px-14 rounded-full transform sm:w-auto sm:h-auto shadow-[#7000FF] shadow-md hover:shadow-2xl hover:shadow-[#7000FF]">
                Serviços
            </button>
        </div>

        <div className="absolute bottom-0 right-0">
          <Image
            src={mulher}
            alt="Mulher"
            width={430} // Defina a largura da imagem conforme necessário
            height={600} // Defina a altura da imagem conforme necessário
          />
        </div>


      </div>



    </div>
  );
};

export default Banner;
