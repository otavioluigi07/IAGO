import React from "react";

export default function Navbar() {
    return (
        <div>
            <nav className="bg-gray-800 p-6">
                <div className="container mx-auto flex justify-between items-center">
                    <div className="flex items-center">
                        <img src="caminho_para_sua_logo.png" alt="Logo" className="h-10 mr-4" />
                        <span className="text-white text-lg font-semibold">Sua Empresa</span>
                    </div>
        
                    <div className="flex items-center">
                        <a href="#" className="text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">Menu</a>
                        <a href="#" className="text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">Serviços</a>
                        <a href="#" className="text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">Contato</a>
                        <a href="#" className="text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">Sobre</a>
                        <a href="#" className="text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium">Planos</a>
                        <a href="#" className="bg-blue-500 text-white px-4 py-2 rounded-md text-sm font-medium">Cadastrar</a>
                    </div>
                </div>
            </nav>
        </div>
    );
}
