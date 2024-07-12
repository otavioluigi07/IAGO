# app.py
from flask import Flask, request, jsonify, render_template
from modelo import rodar, gerar_copy  # Importa as funções do seu arquivo Python

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/executar-funcao', methods=['GET'])
def executar_funcao():
    parametro = request.args.get('parametro')  # Obtém o parâmetro da URL
    guia = rodar(parametro)  # Chama sua função Python com o parâmetro
    return jsonify({'retorno': guia})

@app.route('/gerar-copy', methods=['POST'])
def gerar_copy_route():
    data = request.json  # Obtém os parâmetros enviados via POST como JSON

    novo_prompt = data.get('novo_prompt')
    tipo_comunicacao = data.get('tipo_comunicacao')
    print('novo_prompt:', novo_prompt)
    print('tipo_comunicacao:', tipo_comunicacao)
    
    # Chama sua função Python com os parâmetros
    copy = gerar_copy(novo_prompt, tipo_comunicacao)
    return jsonify({'retorno': copy})

if __name__ == '__main__':
    app.run(debug=True)