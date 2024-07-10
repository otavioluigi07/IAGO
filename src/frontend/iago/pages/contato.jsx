import Navbar from "@components/Navbar"
import Footer from "@components/Footer"
import Formulario from "@components/formulario"

export default function Contato() {
  return (
    <div className="bg-[#3A338E40]">
        <Navbar />
        <div className='pt-20 p-10'>

            <h1 className="mt-14 text-4xl">
                Entre em <span className="text-purple-600">contato </span>com nossa equipe!
            </h1>
            <Formulario />

            

        </div>






      <Footer />

    </div>
  )
}
