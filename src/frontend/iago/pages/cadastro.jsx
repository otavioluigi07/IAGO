import Navbar from "@components/Navbar"
import Footer from "@components/Footer"
import Cadastroform from "@components/cadastroform"

export default function Cadastro() {
  return (
    <div className="bg-[#3A338E50]">
      <Navbar />
      <div className="p-10">
        <h1 className="mt-24 text-4xl">
          Faça já seu  <span className="text-purple-600">cadastro </span> na  <span className="text-purple-600">IAGO</span>!
        </h1>
      </div>
      <Cadastroform />
      <Footer />

    </div>
  )
}
