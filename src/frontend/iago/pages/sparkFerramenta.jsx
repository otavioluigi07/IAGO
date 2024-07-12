import Navbar from "@components/Navbar"
import Footer from "@components/Footer"
import Usarspark from "@components/usarSpark"
import Sparkformulario from "@components/sparkFormulario"
import { SP } from "next/dist/shared/lib/utils"

export default function Perfil() {
  return (
    <div className="bg-[#3A338E40]">
      <Navbar />
      <div className='pt-20 p-10'>
        <h1 className="mt-14 text-4xl">
        Conheça nosso criador de <span className="text-purple-600">copywriter</span>:
        </h1>
        <h1 className="text-[#7000FF] text-8xl mt-4">Spark</h1>
      </div>
      <Usarspark />
      <Sparkformulario />








    <Footer />

    </div>
  )
}
