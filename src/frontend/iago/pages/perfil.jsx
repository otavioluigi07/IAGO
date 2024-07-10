import Navbar from "@components/Navbar"
import Footer from "@components/Footer"
import Formularioperfil from "@components/formularioPerfil"

export default function Perfil() {
  return (
    <div className="bg-[#3A338E40]">
        <Navbar />
        <div className='pt-20 p-10'>

            <h1 className="mt-14 text-4xl">
                Bem vindo,<span className="text-purple-600"> Luigi Otávio</span>!
            </h1>
            <Formularioperfil />

            

        </div>






      <Footer />

    </div>
  )
}
