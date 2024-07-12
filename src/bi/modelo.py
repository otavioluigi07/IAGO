import google.generativeai as genai
from dotenv import load_dotenv

import re
import textwrap

import os

load_dotenv()

def formatar_texto(texto):
    # Divide o texto em linhas para processar cada uma individualmente
    linhas = texto.split('\n')
    texto_formatado = []

    for linha in linhas:
        # Adiciona recuo nas linhas que começam com número de sugestão
        if linha.startswith('('):
            linha = textwrap.fill(linha, width=70, subsequent_indent='    ')
        texto_formatado.append(linha)

    # Junta todas as linhas novamente em um único texto
    return '\n'.join(texto_formatado)

# import boto3

# # Configurar a sessão com as credenciais
# session = boto3.Session(
#     aws_access_key_id='ASIAQIZ2SGMN5HRB5R7Y',
#     aws_secret_access_key='ZAPJb3ntePCOq0nMv04W/KPiEKqznNj9dvVrGpan',
#     aws_session_token = 'IQoJb3JpZ2luX2VjEK7//////////wEaCXVzLWVhc3QtMSJIMEYCIQC+ghvPPFrCzPQC4N1VfZ0StZm0Dga3l5CHRmOnhNl3HQIhAKvluhOmyI29UYIbm+KWr/FDrdS3g1ssz9Z1xAe5eRMUKqQDCHYQAhoMMDE4OTEzMzA5NDY3Igxc2jPmyM07FnNDuEcqgQM+l4DL/ARCG+Q9Z4lC6kNnDH8Jph29D84o5aJfRQrjDPvaVxlWuY2/P6VHPeuqgcBT40fLhymBx6rhMRUYaF88E2zBny7Sm+6ENNG/WoAMppdoO9mqZnCLddHdkqaatdEexowPdlUSvdLZeOMP2fGh/cdTHmFMwtWmrLYoQpe6fZ7M8CMs6RCk8FccuH2hYZtotVCuLE9c3tqpcP3PWVoS2sQK8WqkpNFAi+Eym9b4P4LeSJOnw5EiZyt/d8UTbJN/dRuAdeXwgfL1eADEAwaWkE6z72HGRCR1bW/evDW5v6Y2EShxG3a3pP8EbLg7vztB96LD3ZmdM/jCff0RDCLDIsLfp/tg35AwusXRMrCdJceDMvb3BtFiLSylarWROLvnWHftiH9kMlM+7sYevO9MLhbLnrmJJEfPv0qsOM2sM5Bh9fs3y948xGA2s86GlsFenSncLxVCTK2MC8jUryL6m+9FaAZV9needX9gfzRG6UwBsYX56NwQ97BRlZ4KZGECMPTTxLQGOqUBh2xgfVVkbrp7DnGwHKe3HUn+aUulGuXY6bXleNfUUyw7RNlLV8J/VmRUUU+kzao43X1dZTi+wlsG5vdHL56lJJ/ao22xf0813yEws3kkGj59jSFs7LJkZB27+TpIHL5jzx/mqEoYOVsy1boJDX9yr0kGEIEi6oqK7AAg05Y8jyz+BozKefinUAjra4/4lJ9vL1k4iD13ac5N9UyE3CVmISmlTWww',
#     region_name='us-east-1'
# )



# Criar o cliente do serviço (substitua 'bedrock' pelo serviço que você está usando)
# client = session.client('bedrock-runtime')

# Configurar o ChatBedrock com as credenciais e o cliente
# model = ChatBedrock(
#     client=client,
#     model_id="mistral.mistral-large-2402-v1:0",
#     model_kwargs={"temperature": 0.9}
# )

# # Configurar o ChatBedrock com as credenciais e o cliente
# model2 = ChatBedrock(
#     client=client,
#     model_id="mistral.mistral-large-2402-v1:0",
#     model_kwargs={"temperature": 0.7}
# )

# Access your API key as an environment variable.
# Obtém a chave de API do ambiente
api_key = os.getenv("API_KEY")

# Configura o genai com a chave de API
genai.configure(api_key=api_key)

# Choose a model that's appropriate for your use case.
model = genai.GenerativeModel('gemini-1.5-flash')

#estrutura_copycanvas
estrutura_copycanvas = """
Estrutura do Copy Canvas
O Copy Canvas é um modelo projetado para criar copy de vendas eficazes, transformando ideias complexas em mensagens claras e impactantes. Ele permite que qualquer pessoa escreva textos persuasivos, independentemente de sua experiência em marketing.

Elementos do Copy Canvas
O Copy Canvas é dividido em 10 elementos, agrupados nas seções principais A, B e C, e suas subseções numeradas de 1 a 3.

(A) Audiência: Quem é o seu cliente ideal? Quais são suas necessidades e desejos?
(A1) Problema / Oportunidade: Qual problema ou desejo seu cliente ideal tem? 
(A2) Solução / Jornada: Como seu produto/serviço resolve esse problema ou atende a esse desejo? Sua solução é única, específica, útil e urgente?
O elemento (A1) mais o (A2) unidos formam o elemento (A3) Lead: Em qual estágio de consciência está seu cliente ideal? (História, Previsões, Segredo, Oferta, Promessa, Solução de Problemas)



(B1) Emoção: Qual emoção está associada ao problema ou desejo? (Vergonha, Frustração, Raiva, Medo, Susto, Esperança, Vaidade, Respeito, Ganância, Ego)
(B2) Nudge (Gatilho mental): O que faria seu cliente ideal agir? (Urgência, escassez, curiosidade, exclusividade, oportunidade, FOMO)
O elemento (B1) mais o (B2) unidos formam o elemento (B3) Big Idea: É a ideia principal que diferencia o produto ou serviço no mercado e captura a atenção do público-alvo, gerando interesse e desejo. 

(C1) Prova: Qual o melhor argumento para defender a sua solução e convencer sua audiência?
(C2) Objeções: Quais barreiras mentais seu cliente pode ter? (Não acredito, Não tenho tempo, Não tenho dinheiro, Não tenho interesse, Isso não é pra mim, Posso fazer outra hora)
O elemento (C1) mais o (C2) unidos formam o elemento (C3) Proposta / Oferta: Apresente a oferta de forma clara e atraente, destacando seu valor.


"""

#conceitos_auxiliares_copycanvas
conceitos_auxiliares_copycanvas = """
Conceitos auxiliares no entendimento dos conceitos do copy canvas:

Awareness, ou Curva de consciência
Eugene Schwartz defende que existem cinco níveis distintos de consciência, são eles:
Inconsciente: aquele cliente que não conhece seu produto e nem o problema que ele resolve;
Consciente do problema: o consumidor que, de alguma maneira, sabe que precisa resolver algum problema, mas não sabe como. Por exemplo: um vendedor que precisa aumentar seu faturamento, mas não sabe como;
Consciente da solução: aqui, o cliente já sabe como resolver o problema. Seguindo o exemplo anterior, é como se o vendedor já tivesse descoberto que ele precisa de um curso que o qualifique para aumentar as vendas, mas ele não sabe qual curso;
Consciente do produto: Quase no fim da jornada, o cliente já sabe que determinado produto resolve seu problema, mas não tem certeza se ele será realmente eficaz;
Mais consciente: por fim, o consumidor já não tem dúvidas. Ele sabe que precisa comprar o curso e já tomou a decisão. Aguarda, apenas, uma oferta.

Soluções e Jornadas
Todas as jornadas devem ter 4 tipos de solução distintas:
(1) Única: Deve ser um argumento que identifique a solução como única, que não pode ser encontrada facilmente em outros lugares
(2) Útil: Deve ser um argumento que prove a utilidade inegável da solução
(3) Ultra-específica: Deve ser um argumento que demonstre um benefício muito específico
(4) Urgente: Deve ser um argumento que demonstre a urgência na aquisição da solução

"""


exemplos_guia = f"""
INICIO DOS EXEMPLOS DE GUIA COPY CANVAS ------------------------
Exemplo 1)
COPY CANVAS: PRD01 [Projeto Renda - Felipe Miranda]

A) AUDIÊNCIA
 
(1) Interessados por Renda Extra.
(2) Conhecem ou se interessam o Guru.
Melhor: já investe, já é assinante, Comprador Recente, segue a Empiricus ou o Felipe Miranda.
Pior: Curioso (Assiste Vídeo sobre investimentos), Nunca Comprou Antes.
 
A1) PROBLEMA/OPORTUNIDADE
 
(1) Dificilmente ganha a renda extra desejada (muito menos, com consistência).
 
(2) Quando ganha, o esforço, o estresse e frustração são desgastantes demais.
 
A2) SOLUÇÃO/JORNADA
 
Única: Plano pra ter 11 novas fontes de renda
 
Útil: Renda Extra com diversas estratégias

Urgente: vagas limitadas
 
A3) LEAD
 
O lead começa com muitos depoimentos de seguidores da Empiricus e do Felipe que estão ganhando rendimentos extras + promessa de buscar 11 novas fontes de renda extra, com a possibilidade de ter rendimentos pingando na conta todos os dias.
 
B1) EMOÇÃO
 
Greed
 
B2) NUDGE
 
11 novas fontes de renda (oportunidade)
 
B3) BIG IDEA
 
Projeto Renda
 
Como você pode ter 11 novas fontes de renda pingando na sua conta periodicamente.
 
C1) PROVA
 
(1) Credibilidade da Empiricus/guru
 
(2) Método: Dezenas de Prints de Depoimentos
 
(3) Método: Dezenas de Prints de Resultados
 
(4) Método: mostra as 11 estratégias de renda
 

 
C2) OBJEÇÕES
 
(1) Não acredito em você: demonstração
 
(2) Não sei investir: treinamento
 
(3) Não tenho dinheiro: comece com pouco
 
(4) Posso fazer outra hora: vagas limitadas
 
 
C3) PROPOSTA/OFERTA
 
Validade: 12 meses
(1) Treinamento: Projeto Renda
 
(2) 1 ano de acesso do Double Income
 
(3) Curso CEA
 
(4) Livro "Do que você precisa para se aposentar"
 
(5) Sorteio mensal de R$ 10.000 por 12 meses
 
(6) Podcasts de dúvidas periódicos
 
(7) Garantia 7 dias para cancelar + Garantia condicional de lucros: terminar o treinamento com pelo menos 1 nova fonte de renda ou R$ 1.000 de volta em créditos na loja.
 
 
Preço: (¹) Prazo: 12x de R$ 292 (²) À Vista: 10% OFF

Exemplo 2)
COPY CANVAS: OGR02


A) AUDIÊNCIA
 
(1) Apaixonados por Day Trade.
(2) Com Algum Relacionamento com o Guru.
Melhor: Trader (Opera na Bolsa), Cliente Antigo, Já Adquiriu N Produtos, Comprador Recente e fãs do Ogro
Pior: Curioso (Assiste Vídeo sobre Trade), Nunca Comprou Antes, Segue oOgro.
 
A1) PROBLEMA/OPORTUNIDADE
 
(1) Deseja mais renda para ter uma vida melhor com sua família
 
(2) Perde ou perdeu dinheiro com day trade
 
A2) SOLUÇÃO/JORNADA
 
(1) Única: Método Ogro Trade System
 
(2) Útil: Renda com Day Trade
 
(3) Ultra-Específica: Média de R$ 2.000 por dia AGORA, em 2024
 
(4) Urgente: construir essa renda agora, em 2024, antes que o ano acabe. E logo encerraremos as vagas.

A3) LEAD
 
O lead começa com o Ogro dizendo que tem um plano prático para buscar ganhos de R$ 2.000 por dia, na média, agora, em 2024.
Depois mostra as provas de como o guru e seus seguidores estão conseguindo ganhos similares ou até maiores que esses.

B1) EMOÇÃO
 
Greed
 
B2) NUDGE
 
Oportunidade + Método + FOMO
 
B3) BIG IDEA
 
OGRO Trading System: Um plano prático pra você buscar ganhos médios de R$ 2.000 por dia em 2024
 
C1) PROVA
 
(1) História do Guru, que ficou multimilionário com day trade
(2) reportagens reforçando sua autoridade e muitas fotos de família
(3) Método: Prints de Depoimentos falando de ganhos, elogiando o guru, seu assistente e a sala de trading
 
C2) OBJEÇÕES
 
(1) Não acredito no valor, que é alto: mostra que não é da noite pro dia, que tem um passo a passo
 
(2) Não tenho tempo: opera só de manhã, às vezes pode resolver tudo em 20 minutos
 
(3) Não tenho dinheiro: capital mínimo relativamente baixo, começando com com R$ 1.000 por minicontrato
 
(4) Posso fazer outra hora: é pra começar a ganhar agora,em 2024
 
(5) Não tenho interesse: [público de Day Trade]

(6) Se é tão bom, por que você mesmo não vive disso?; foi o que elefezpor mais de 10 anos e continua ganhando dinheiro, só que agora de forma mais diversificada, como ele mesmo recomenda.
 
C3) PROPOSTA/OFERTA
 
Validade: 6 Meses
 
(1) Treinamento: Ogro Trading System
 
(2) Série Carteira Empiricus, por questões fiscais
 
(3) 3 meses de sala ao vivo

(4) Curso Básico Introdutório
 
(5) Plantão de Dúvidas Ao Vivo fora do horário com Ogro e Mario
 

 
(6) Certificado de Investidor
 
Preço: (¹) Prazo: 12x de R$197 (²) À Vista: 10% OFF
 
Garantia: (¹) Incondicional: 7 dias (²) Condicional: ***

Exemplo 3)
COPY CANVAS: GRL03 ["Gradiente Linear GPT"]

A) AUDIÊNCIA
(1) Clientes da Empiricus.
(2) Apaixonados por Day Trade.
(3) Entusiastas de IA / Automação com Robô.

A1) PROBLEMA/OPORTUNIDADE
(1) Dificilmente ganha a renda extra diária (muito menos, com consistência).
(2) Quando ganha, o esforço, o estresse e frustração são desgastantes demais.
 
A2) SOLUÇÃO/JORNADA
 
Única: "1º robô de trade do Brasil criado aos moldes de IA"
Útil: Renda Extra com Day Trade
Ultra-Específica: Média de R$ 238,09 por dia 
Urgente: 500 logins com trial de 30 dias 
 
A3) LEAD
O lead começa apresentando rapidamente Valério Klug (criador do robô) – que durante toda fase de captação não apareceu em nenhum momento.
Logo após, a promessa é apresentada ("robô de IA com meta de R$ 238,09 por dia") junto com uma ilustração do operacional (4 cliques).
Em seguida, ancoramos expectativa do tutorial/VSL: o que seria mostrado nos primeiros 15 minutos ("robô em ação") e nos últimos 15 minutos ("vagas limitadas com trial grátis de 30 dias"). 
Fim do lead, início das provas.

B1) EMOÇÃO
 Greed

B2) NUDGE
 Oportunidade + Automatização + FOMO

B3) BIG IDEA
GRADIENTE LINEAR [GPT]
META 2024: Renda média de R$ 238,09 por dia com apenas 4 cliques no GL GPT:
(1) "PLAY"  (2) "STOP" (3) "GAIN" (4) "ROBÔ" 
C1) PROVA
(1) Prints com ganhos de R$ 238
(2) Prints com ganhos de MAIS de R$ 238
(3) Depoimentos de Alunos 
(4) História do Robô e Gradiente Linear 
(5) Demonstração do Robô Operando
 
C2) OBJEÇÕES
 (1) Não acredito em você: demonstração / depoimentos 
 (2) Não tenho tempo: 10 minutos por dia (robô faz o resto)
 (3) Não tenho dinheiro: comece operando com R$ 100
 (4) Posso fazer outra hora: vagas limitadas
 (5) Não tenho interesse: [público de Day Trade]
 
C3) OFERTA
Validade: 3 meses
(1) Treinamento
(2) Sala ao Vivo de 9-12h Dia de Pregão
(3) Plataforma de Day Trade [Trader Evolution]
(4) Robô de Day Trade [Algoritmos Default]
(5) Simulador de Day Trade
(6) Live de Boas-Vindas c/ Valerio Klug [Set-Up]
(7) Comunidade de Day Traders Quant [Telegram] 
(8) Certificado de Trader Quant [GL/Empiricus]
(9) Carteira Empiricus
Preço: (¹) Prazo: 12x de R$169,90 (²) À Vista: 10% OFF
Garantia: 30 dias

Exemplo 4)
COPY CANVAS: INX01

A) AUDIÊNCIA
 
(1) Apaixonados por Day Trade.
(2) Cara que já perdeu dinheiro com day trade e procura algo novo
Melhor: Trader (Opera na Bolsa), Cliente Antigo, Já Adquiriu N Produtos, Comprador Recente.
"Pior": Curioso (Assiste a Vídeos sobre Trade), Nunca Comprou Antes.
 
A1) PROBLEMA/OPORTUNIDADE
 
(1) Deseja mais renda para ter uma vida melhor com sua família
 
(2) Perde ou perdeu dinheiro com day trade

A2) SOLUÇÃO/JORNADA
 
Única: Uma ferramenta nova que simplifica o mercado financeiro – IndicadorX
 
Útil: Renda com Day Trade
 
Ultra-Específica: Média de R$ 3.000 por dia
 
Urgente: vagas limitadas a 750,que logo serão encerradas
 
A3) LEAD
 
O lead começa com o Paulo Wesley dizendo que vai operar o IndicadorX por você, como uma Inteligência Artificial, para que você tenha a chance de chegar mais rápido aos GANHOS MÉDIOS DE ATÉ R$ 3.000 POR DIA.
Depois diz que o próprio prospect também pode operar, se desejar.
Mostra os ganhos de outras pessoas e apresenta a ferramenta, inclusive visualmente, provando que ela é bem simples.

 
 
B1) EMOÇÃO
 
Greed

B2) NUDGE
 
Oportunidade + novidade + FOMO
 
B3) BIG IDEA
 
IndicadorX: a ferramenta quant que simplifica o mercado financeiro em busca de até R$ 3.000 por dia

C1) PROVA
 
(1) Track record da ferramenta
(2) Prints de Depoimentos falando de ganhos, elogiando a ferramenta e a sala de trading
(3) Visual simples da ferramenta, indicando compra ou venda

C2) OBJEÇÕES

(1) Não tenho dinheiro: o capital mínimo é relativamente baixo, começando com com R$ 1.000 por minicontrato

(2) Não acredito no valor, que é alto: mostra que não é da noite pro dia, que tem um passo a passo,mas que o cara já pode começar ganhando
 
(3) Não tenho tempo: eu posso operar por você e replicar o resultado na sua conta. Caso você queira operar por conta própria, opera só de manhã. às vezes pode resolver tudo em 20 ou 30 minutos.

(4) Day Trade não funciona: sim, funciona. Minha ferramenta prova isso. A maioria perde porque opera sozinho, e deixa se levar pelo lado emocional. O IndicadorX tira esse peso, e você pode operar numa sala com mais pessoas.
 
(5) Posso fazer outra hora: apenas 750 vagas pra você começar a jornada agora e ter a chance de ganhar dinheiro mais rápido
 
(5) Não tenho interesse: [público de Day Trade]

(6) Se é tão bom, por que você mesmo não vive disso?; porque eu posso ganhar ainda mais com você operando comigo. E acho importante que o trader diversifique suas fontes de renda. Eu faço isso e quero que você também faça.
 
C3) PROPOSTA/OFERTA
 
Validade: 3 Meses
 
(1) Treinamento: IndicadorX
 
(2) Copy Trade do IndicadorX (3 meses)

(3) 3 meses de sala ao vivo

(4) Curso de Nivelamento (Básico)
 
(5) Plantão de Dúvidas Ao Vivo fora do horário com Paulo Wesley

(6) Certificado “Trader: IndicadorX"
 
Preço: (¹) Prazo: 12x de R$197 (²) À Vista: 10% OFF
 
Garantia: (¹) Incondicional: 7 dias (²) Condicional: ***





FIM DOS EXEMPLOS DE GUIA COPY CANVAS ------------------------

"""

# Função para criar GUIA
def run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, elemento, elemento_num, formato_saida, instrucao_adicional, exemplos, exemplos_guia, criativo):
  #Prompt Solução (Sem tags)
    prompt = f"""
    Criação de Elementos:  {elemento}

    Atue como um publicitário especializado na criação de campanhas digitais para venda de produtos e serviços na internet.
    Você é um especialista na utilização do framework Copy Canvas, desenvolvido por Roberto Altenhoffen, CMO da Empiricus Research.
    Este é uma explicação sobre a estrutura do framework Copy Canvas, abaixo contido entre ???
    ???{estrutura_copycanvas}???

    Conceitos Auxiliares:
    Abaixo, entre ~~ estão algumas informações de importantes sobre os conceitos principais do Copy Canvas:
    ~~{conceitos_auxiliares_copycanvas}~~

    O usuário está estruturando um projeto e precisa de ajuda para criar a 'Guia do Copycanvas'.
    Neste momento, ele está estruturando o elemento {elemento} (elemento {elemento_num}). 
    Sua missão é auxiliar o usuário a criar uma boa definição de {elemento} (elemento {elemento_num}).

    O usuário fornecerá uma entrada criativa relacionada ao projeto em que está trabalhando. 
    Também será disponibilizado um conjunto de exemplos criativos e as descrições de {elemento} entre ;;;.
    ;;;{exemplos};;;

    Aqui estão alguns exemplos de GUIAS já feitas para você entender melhor. Os exemplos estão entre ????
    ??{exemplos_guia}??

    A seguir estão as instruções de como você deve responder à solicitação do usuário.
    Todas as instruções devem ser seguidas à risca:
    Instrução 1: Utilize a ESTRUTURA COPYCANVAS, os CONCEITOS AUXILIARES e sua base interna de conhecimento como referências criativas e instrucionais.
    Instrução 2: Leia os EXEMPLOS DE {elemento}. Compare o input criativo do exemplo com o input criativo do usuário e utilize os exemplos como referência, adaptando-os ao input criativo do usuário.
    Instrução 3: Crie exemplos de descrições de {elemento} adequados para o input criativo do usuário.
    Instrução 4: Utilize os EXEMPLOS DE {elemento} como referência criativa, de formato e de tamanho, pois são comprovadamente eficientes.
    Instrução 5: Não faça sugestões de novos inputs criativos. Dê apenas as descrições de {elemento} para o input do usuário e não fale sobre outros aspectos do Copycanvas.
    Instrução 6: A resposta deve ter como objetivo estender o conceito do input criativo do usuário. Todas as outras informações devem ser apenas referências criativas e instrucionais.
    Instrução 7: A resposta deve ter o seguinte formato: {formato_saida}

    Instrução adicional: {instrucao_adicional}

    CRIATIVO DE NEGÓCIO DO USUÁRIO:
    {criativo}
    """

    response = model.generate_content(prompt)
    return (formatar_texto(response))


# Exemplos de Audiência
exemplos_audiencia = """
INICIO DOS EXEMPLOS DE AUDIÊNCIAS-------------------------------------------

entrada criativa:o especialista em daytrade Léo Nonato consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Exemplo 1:

Audiência:
(1) Apaixonados por Day Trade.
(2) Com Algum Relacionamento com o Guru.
Melhor: Trader (Opera na Bolsa), Cliente Antigo, Já Adquiriu N Produtos, Comprador Recente.
Pior: Curioso (Assiste Vídeo sobre Trade), Nunca Comprou Antes, Segue Leo Nonato.

Exemplo 2:

(1) Interessados por Renda Extra.
(2) Conhecem ou se interessam o Guru.
Melhor: já investe, já é assinante, Comprador Recente, segue a Empiricus ou o Felipe Miranda.
Pior: Curioso (Assiste Vídeo sobre investimentos), Nunca Comprou Antes.

Exemplo 3:

(1) Clientes da Empiricus.
(2) Apaixonados por Day Trade.
(3) Entusiastas de IA / Automação com Robô.
 
Exemplo 4:

(1) Pessoas que interagiram com o instagram da Empiricus nos últimos 30 dias
(2) Lookalike de pessoas que assinam o Exponencial Coins
(3) Assinantes Empiricus

FIM DOS EXEMPLOS DE AUDIÊNCIAS-------------------------------------------
"""
formato_saida_audiencia = """
Dê 2 sugestões:
(1)
(2)
Dê uma sugestão de:
Melhor: O que seria a melhor audiência possível, entre os 2 exemplos
Pior: Qual seria a pior audiência possível, entre os 2 exemplos
"""
instrucao_adicional = """ """

# Exemplos de Problema e Oportunidade
exemplos_problema = """
INICIO DOS EXEMPLOS DE PROBLEMA/OPORTUNIDADE-------------------------------------------

Exemplo 1:

entrada criativa:o especialista em daytrade Léo Nonato consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Problema/Oportunidade:
(1) Dificilmente ganha a renda extra desejada (muito menos, com consistência).
(2) Quando ganha, o esforço, o estresse e frustração são desgastantes demais.

Exemplo 2:

(1) Deseja mais renda para ter uma vida melhor com sua família
(2) Perde ou perdeu dinheiro com day trade

Exemplo 3:

(1)  Estou frustrado com a minha realidade atual, já passei dos 40 anos e comecei a perceber que preciso tomar risco/um caminho diferente para realizar os meus sonhos - uma tacada certeira nesse mercado muda a vida de qualquer pessoa para sempre
(2) Já vi muita gente ficando rica do meu lado e eu nunca fiz nada - você está diante do melhor momento possível para fazer pouco dinheiro virar muito
(3) Tenho pouco dinheiro e nunca investi em criptomoedas - essa oportunidade realmente é para mim?




FIM DOS EXEMPLOS DE PROBLEMA/OPORTUNIDADE-------------------------------------------
"""
formato_saida_problema = """
Dê 2 sugestões:
(1)
(2)
"""
instrucao_adicional = """ """

# Exemplos de Solução e Jornada
exemplos_solucao = """
INICIO DOS EXEMPLOS DE SOLUÇÃO/JORNADA-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Solução/Jornada:
(1) Única: 1º robô do especialista
(2) Útil: Renda Extra com Day Trade
(3) Ultra-Específica: Média de R$ 538,02 (errando até 80% dos trades)
(4) Urgente: 1.000 logins iniciais

Exemplo 2:

(1) Única: Uma criptomoeda que custa 50 centavos  e tem o potencial de multiplicar o dinheiro por 100x
(2) Útil: qualquer pessoa pode investir pouco dinheiro e conquistar uma fortuna
(3) Ultra-Específica: ela usta 50 centavos e pode multiplicar o dinheiro por 100 vezes em até 19 meses
(4) Urgente: Ela já estava disparando e existiam gatilhos de curto prazo que tornariam essas altas ainda maiores (halving) - Depois do halving já era. 

Exemplo 3:

(1) Única: 5 moedas com o potencial de te deixar milionário
(2) Útil: com R$ 500 em cada você já pode ir em busca do milhão
(3) Ultra-Específica: quem investir R$ 500 nestas 5 moedas pode fazer conquistar R$ 1 milhão
(4) Urgente: Mas você precisa ser rápido, o halving acontece na semana que vem e, historicamente, o que vemos após essa atualização são valorizações exponenciais.

Exemplo 4:

(1) Única: Plano pra ter 11 novas fontes de renda
(2) Útil: Renda Extra com diversas estratégias
(3) Urgente: vagas limitadas

FIM DOS EXEMPLOS DE SOLUÇÃO/JORNADA-------------------------------------------
"""
formato_saida_solucao = """
Dê 2 sugestões contendo as 4 categorias de solução abaixo:
(1) Única:
(2) Útil:
(3) Ultra-Específica:
(4) Urgente:
"""
#instrucao_adicional = """Dê menos peso aos exemplos fornecidos, utilize os conceitos auxiliares e seu conhecimento interno para gerar esta resposta. """
instrucao_adicional = """
- Garanta que as soluções e jornadas estejam totalmente alinhadas com o input criativo do usuário e utilize os exemplos apenas como referência de linguagem
- Cria respostas mais curtas, com no máximo 20 palavras
- Quando possível, cite valores, em especial se eles tiverem sido mencionados no input criativo do usuário. Utilize os exemplos como referência de como utilizar valores
"""

# Exemplos de Leads
exemplos_lead = """
INICIO DOS EXEMPLOS DE LEAD-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

O lead começa com a promessa de buscar ganhos de R$ 583 por dia, em média, mesmo errando 80% das operações.
Depois mostra as provas de como o guru e seus seguidores estão conseguindo ganhos similares ou até maiores que esses.

Exemplo 2:

O lead começa contextualizando o leitor do que está acontecendo no mercado de criptomoedas, o que isso está causando na vida dos seus investidores e que os movimentos podem ficar ainda mais agressivos no curto prazo por conta do halving.
Criptomoedas disparando
Maior quantidade de dinheiro já vista entrando por conta dos ETFs
O maior e possível último ciclo de alta da história das criptomoedas foi iniciado.
Muita gente ficando milionária em pouco tempo.
A criptomoeda do copy estava voando e poderia ir ainda mais longe por conta do halving que acontece nos próximos dias
Pouco risco muito retorno (assimetria positiva)
Termino o lead deixando claro que existem dois caminhos possíveis: seguir a vida da maneira que ele está hoje ou agarrar essa oportunidade arriscando pouco em busca da chance de mudar de vida.

Exemplo 3:

O lead começa com o Marcelo Oliveira dizendo que agora é a sua vez de replicar o segredo dos Grandes Bancos para buscar ganhos de até R$ 1.500 toda manhã e ter a possibilidade de MAIS LUCROS durante o dia com estratégias profissionais, automatizadas pela Quantzed.
Depois diz que tem um plano prático para atingir a meta financeira e que vai dar 4 meses gratuitos de uso da ferramenta.
Mostra os ganhos de outras pessoas e apresenta a ferramenta com as estratégias e mais resultados e prints de ganhos

Exemplo 4:

O lead começa apresentando rapidamente Valério Klug (criador do robô) – que durante toda fase de captação não apareceu em nenhum momento.
Logo após, a promessa é apresentada ("robô de IA com meta de R$ 238,09 por dia") junto com uma ilustração do operacional (4 cliques).
Em seguida, ancoramos expectativa do tutorial/VSL: o que seria mostrado nos primeiros 15 minutos ("robô em ação") e nos últimos 15 minutos ("vagas limitadas com trial grátis de 30 dias"). 
Fim do lead, início das provas.

FIM DOS EXEMPLOS DE LEAD-------------------------------------------
"""
formato_saida_lead = """
Dê 3 sugestões de lead que o usuário poderia se encaixar:
(1)
(2)
(3)
"""
instrucao_adicional = """ """

# Exemplos de Emoção
exemplos_emocao = """
INICIO DOS EXEMPLOS DE EMOÇÕES-------------------------------------------

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Exemplo 1:

Emoção: Ganância

Exemplo 2:

Emoção: Greed

Exemplo 3:

Emoção: Ambição

FIM DOS EXEMPLOS DE EMOÇÕES-------------------------------------------
"""
formato_saida_emocao = """
Dê as 3 emoções que seriam mais aplicáveis e uma breve descrição do porquê
(1)
(2)
(3)
"""
instrucao_adicional = """ """

# Exemplos de Nudge
exemplos_nudge = """
INICIO DOS EXEMPLOS DE NUDGES-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Nudges: Oportunidade única, Automatização de trades, FOMO (Medo de perder a oportunidade)

Exemplo 2:

Oportunidade + novidade + FOMO

Exemplo 3:

11 novas fontes de renda (oportunidade)

FIM DOS EXEMPLOS DE NUDGES-------------------------------------------
"""
formato_saida_nudge = """
Dê 3 nudges que seriam aplicáveis e uma breve descrição do porquê
(1)
(2)
(3)
"""
instrucao_adicional = """ """

# Exemplos de Big Idea
exemplos_bigidea = """
INICIO DOS EXEMPLOS DE BIG IDEA-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.
Dolar Ultimate Machine - O 1º robô automático de Day Trade do Leo Nonato programado para buscar média de R$ 538,02 por dia (mesmo errando 80% das operações).

Exemplo 2:

IndicadorX: a ferramenta quant que simplifica o mercado financeiro em busca de até R$ 3.000 por dia

Exemplo 3:

GRADIENTE LINEAR [GPT]
META 2024: Renda média de R$ 238,09 por dia com apenas 4 cliques no GL GPT:
(1) "PLAY"  (2) "STOP" (3) "GAIN" (4) "ROBÔ" 

Exemplo 4:

Nova criptomoeda de 50 centavos que pode disparar 9.900% em até 19 meses 

Exemplo 5:

Plataforma Quantzed: com uma única estratégia, você tem a chance diária de colocar até R$ 1.500 no bolso em apenas 10 minutos, logo na abertura do mercado)

FIM DOS EXEMPLOS DE BIG IDEA----------------------------------------------
"""
formato_saida_big_ideia = """ Dê 3 sugestões de big idea que o usuário poderia se encaixar:
(1)
(2) 
(3)
"""
instrucao_adicional = """ """

# Exemplos de Prova
exemplos_prova = """
INICIO DOS EXEMPLOS DE PROVAS-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Provas:
(1) Currículum do Guru
(2) Método: Dezenas de Prints de Depoimentos
(3) Método: Dezenas de Prints de Resultados
(4) Track Record do Robô (com Método Programado)
(5) Demonstração do Robô em Ação

Exemplo 2:

(1) Histórico do departamento de análise - pegando forte na última indicação de 50 centavos - AXS - que fez um investimento de R$ 3.500 virarem R$ 1 milhão em apenas 10 meses.
(2) Matérias de jornal falando que esse é o maior ciclo de alta da história das criptomoedas, que existem milhares de pessoas ficando milionárias.
(3) Depoimento de pessoas que já fizeram milhão com nossas indicações
(4) Depoimento de pessoas que já fizeram milhão no mercado de criptomoedas (sem ser indicação nossa)
(5) Histórico de retorno das criptomoedas menores nos últimos dois ciclos de alta.
(6) Histórico de retorno de criptomoedas que são listadas na Coinbase e Binance.
(7) Volume de compra dos ETFs com o juros nos EUA nas máximas.

Exemplo 3:

(1) Credibilidade da Empiricus/guru
(2) Método: Dezenas de Prints de Depoimentos 
(3) Método: Dezenas de Prints de Resultados
(4) Método: mostra as 11 estratégias de renda


Exemplo 4: 

(1) Prints com ganhos de R$ 238
(2) Prints com ganhos de MAIS de R$ 238
(3) Depoimentos de Alunos 
(4) História do Robô e Gradiente Linear 
(5) Demonstração do Robô Operando

FIM DOS EXEMPLOS DE PROVAS-------------------------------------------
"""
formato_saida_prova = """
Dê 2 sugestões de provas, contendo 6 provas cada sugestão, que o usuário poderia tentar obter:
(1)
(2)
"""
instrucao_adicional = """ """

# Exemplos de Objeções
exemplos_objecoes = """
INICIO DOS EXEMPLOS DE OBJEÇÕES-------------------------------------------

Exemplo 1:

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.

Objeções:
(1) Não acredito em você: demonstração
(2) Não tenho tempo: 30 minutos por dia
(3) Não tenho dinheiro: comece operando com R$ 1OO
(4) Posso fazer outra hora: vagas limitadas
(5) Não tenho interesse: [público de Day Trade]

Exemplo 2:

(1) Não acredito no valor, que é alto: mostra que não é da noite pro dia, que tem um passo a passo
(2) Não tenho tempo: opera só de manhã, às vezes pode resolver tudo em 20 minutos
(3) Não tenho dinheiro: capital mínimo relativamente baixo, começando com com R$ 1.000 por minicontrato
(4) Posso fazer outra hora: é pra começar a ganhar agora,em 2024
(5) Não tenho interesse: [público de Day Trade]
(6) Se é tão bom, por que você mesmo não vive disso?; foi o que elefezpor mais de 10 anos e continua ganhando dinheiro, só que agora de forma mais diversificada, como ele mesmo recomenda.

Exemplo 3:

(1) Quem é você? - chefe do departamento de análise que indicou uma moeda que também custava 50 centavos e fez R$ 3.500 virarem R$ 1 milhão em 10 meses.
(2)  É realmente possível fazer R$ 1.000 virarem R$ 100 mil em até 19 meses? - a moeda já está disparando e esse movimento deve ficar ainda mais forte daqui pra frente
(3)  Essa criptomoeda é uma memecoin? Ela é uma moeda que possui fundamento
(4) Será que agora é o melhor momento possível para investir nessa criptomoeda? Estamos diante do melhor momento possível - juros altos, com o halving na cara do gol para acontecer
(5) Posso fazer outra hora: gatilho (halving) prestes a acontecer

Exemplo 4:

(1) Não tenho dinheiro: o capital mínimo é relativamente baixo, começando com com R$ 1.000 por minicontrato
(2) Não acredito no valor, que é alto: mostra que não é da noite pro dia, que tem um passo a passo,mas que o cara já pode começar ganhando
(3) Não tenho tempo: eu posso operar por você e replicar o resultado na sua conta. Caso você queira operar por conta própria, opera só de manhã. às vezes pode resolver tudo em 20 ou 30 minutos.
(4) Day Trade não funciona: sim, funciona. Minha ferramenta prova isso. A maioria perde porque opera sozinho, e deixa se levar pelo lado emocional. O IndicadorX tira esse peso, e você pode operar numa sala com mais pessoas.
(5) Posso fazer outra hora: apenas 750 vagas pra você começar a jornada agora e ter a chance de ganhar dinheiro mais rápido
(6) Não tenho interesse: [público de Day Trade]
(7) Se é tão bom, por que você mesmo não vive disso?; porque eu posso ganhar ainda mais com você operando comigo. E acho importante que o trader diversifique suas fontes de renda. Eu faço isso e quero que você também faça.




FIM DOS EXEMPLOS DE OBJEÇÕES-------------------------------------------
"""

formato_saida_objecoes = """
Dê 5 sugestões de objeções e seus contra-argumentos. Seja conciso nos contra argumentos, não mais do que 10 palavras
(1)
(2)
(3)
(4)
(5)
"""
instrucao_adicional = """ """

# Exemplos de Oferta
exemplos_oferta = """
INICIO DOS EXEMPLOS DE PROPOSTA/OFERTA-------------------------------------------

entrada criativa do exemplo:especialista em daytrade consegue entregar o resultado x... agora ele criou um robô que executa suas operações de forma automatizada.
Ofertas:
(1) Treinamento: Dolar Ultimate
(2) Robô de Day Trade: Dolar Ultimate
(3) Calculadora Proprietária da Neo Traders
(4) Plantão de Dúvidas Ao Vivo (Pregão: 8h50 – 13h00)

Exemplo 2:

Validade: 12 Meses de acesso ao treinamento
(1) Treinamento: Formação Trader Quantzed
(2) Plataforma Quantzed (acesso por 4 meses)
(3) 8 Lives Quinzenais
(4) Comunidade Quantzed, com calls diários e atualização do mercado
Preço: (¹) Prazo: 12x de R$159 (²) À Vista: 10% OFF
Garantia: (¹) Incondicional: 7 dias (²) Condicional: ***


Exemplo 3:

Validade: 12 meses
(1) Treinamento: Projeto Renda
(2) 1 ano de acesso do Double Income
(3) Curso CEA
(4) Livro "Do que você precisa para se aposentar"
(5) Sorteio mensal de R$ 10.000 por 12 meses
(6) Podcasts de dúvidas periódicos
(7) Garantia 7 dias para cancelar + Garantia condicional de lucros: terminar o treinamento com pelo menos 1 nova fonte de renda ou R$ 1.000 de volta em créditos na loja. 
Preço: (¹) Prazo: 12x de R$ 292 (²) À Vista: 10% OFF


FIM DOS EXEMPLOS DE PROPOSTA/OFERTA-------------------------------------------
"""
formato_saida_oferta = """
Dê 2 sugestões de Proposta/Oferta tangíveis e realistas para o usuário
(1)
(2)
"""
instrucao_adicional = """ """

exemplo_copy = f"""

Estrutura Copy:
O Copy é uma mensagem gerada a partir do framework Copy Canvas, baseado em informações categorizadas para garantir clareza e impacto. A mensagem pode ser adaptada para diversas plataformas e formatos, atendendo às necessidades de cada campanha.

Contexto:
A Empiricus usa marketing digital para apresentar produtos e captar leads para lançamentos. Quando um usuário acessa um anúncio online e fornece seus dados, ele passa a receber copys de anúncio por meio de plataformas de comunicação. Esses copys são elaborados para manter o interesse do usuário e incentivá-lo a conhecer mais sobre os produtos.

Tipos de Copy:
No contexto de lançamentos de produtos da Empiricus, os copys são estruturados em três tipos principais:

(1)Welcome: Primeira mensagem enviada no período de pré-lançamento após o acesso ao anúncio. O objetivo é apresentar 
o produto da campanha e captar usuários para a comunidade do WhatsApp.
(1.1.)CPL/WARMUP: Conteúdo de pré-lançamento enviado aos leads captados para mantê-los engajados antes da abertura das vendas.

(2)PROMO: Mensagens de tentativas de vendas diárias do produto, divididas em três subtipos:
(2.1.)PROMO ABERTURA DE CARRINHO/VSL: Primeira mensagem no lançamento do produto, com o objetivo de captar leads para disseminação de propaganda e potenciais compradores.
(2.2.)PROMO: Mensagens enviadas diariamente aos leads para aquecer o interesse no produto.
(2.3.)PROMO ÚLTIMA: Mensagens finais para incentivar a compra antes do término da campanha.

(3) COUNTDOWN: Esse tipo de COPY é usada no último de aula
(4) CARRINHO ABANDONADO: Esse tipo de COPY é usada para quando o usuário ABANDONAR O CARRINHO DE COMPRA
"""

import re

def extrair_conteudo(string):
    # Expressão regular para encontrar o conteúdo entre content=' e '
    padrao = re.compile(r"content='(.*?)'", re.DOTALL)
    # Buscar todas as correspondências na string
    correspondencias = padrao.findall(string)
    
    # Retornar a lista de correspondências encontradas
    return correspondencias

def run_2(tipo_copy, instrucao_adicional, exemplos, exemplo_copy, novo_prompt, plataforma, politica):
    # Prompt Solução (Sem tags)
    prompt = f"""
    Criação de Tipo de Copy: {tipo_copy}

    Copy Canvas e informações do criativo/produto entre ^^^.
    ^^^{novo_prompt}^^^

    Atue como um publicitário especializado na criação de campanhas digitais para venda de produtos e serviços na internet. Você é um especialista na criação de copies utilizando o framework Copy Canvas, desenvolvido por Roberto Altenhoffen, CMO da Empiricus Research.

    Este é um resumo sobre a estrutura de uma Copy:
    ???{exemplo_copy}???

    O usuário está estruturando um projeto e precisa de ajuda para criar o Copy. Sua missão é auxiliar o usuário a criar uma boa mensagem/anúncio para {tipo_copy}.

    Também será disponibilizado um conjunto de exemplos e inputs criativos e as descrições do {tipo_copy} entre ;;;.
    ;;;{exemplos};;;

    Instruções:
    1. Utilize a ESTRUTURA COPY e sua base interna de conhecimento como referências criativas e instrucionais.
    2. Leia os EXEMPLOS DE {tipo_copy}. Compare o input criativo do exemplo com o input criativo do usuário e utilize os exemplos como referência, adaptando-os ao input criativo do usuário.
    3. Crie exemplos de descrições de {tipo_copy} adequados para o input criativo que o usuário deu.
    4. Utilize os EXEMPLOS DE {tipo_copy} como referência criativa, de formato e de tamanho, pois são comprovadamente eficientes.
    5. Não faça sugestões de novos inputs criativos. Dê apenas as descrições de {tipo_copy} para o input do usuário e não fale sobre outros aspectos do Copy ou Copy Canvas.
    6. A resposta deve estender o conceito do input criativo do usuário. Todas as outras informações devem ser apenas referências criativas e instrucionais.

    Você está construindo uma COPY para essa plataforma: {plataforma}

    Instruções adicionais: {instrucao_adicional}

    Políticas de bom uso que você deve seguir ao criar a COPY: {politica}
    - Não crie COPIES que vão contra as políticas de bom uso
    - Não crie COPIES se o Copy Canvas e informações do criativo/produto forem contra as políticas de bom uso.

    PERGUNTA DO USUÁRIO:
    Gere um uma copy seguindo esse copy canvas: {novo_prompt}
    """
    response = model.generate_content(prompt)
    return (formatar_texto(response))

#Plataformas de uso:

plataforma_email = 'Email'

plataforma_whatsapp = 'WhatsApp - Comunidade/grupo'

plataforma_instagram = 'Instagram'

plataforma_telegram = 'Telegram'

politicas_google = f"""
Conteúdo proibido
Produtos falsificados
O Google Ads proíbe a venda ou promoção de produtos falsificados. Esses produtos contêm um logotipo ou uma marca registrada idêntica ou que possui diferenças mínimas em relação à marca verdadeira. Eles imitam as características da marca no produto em uma tentativa de se passar por produtos originais do proprietário da marca. Esta política se aplica ao conteúdo do seu anúncio e do seu site ou aplicativo. 

Produtos ou serviços perigosos
Queremos proteger as pessoas on-line e off-line. Sendo assim, não permitimos a promoção de alguns produtos ou serviços que causam danos, prejuízos ou ferimentos.
Exemplos de conteúdo perigoso: drogas recreativas (químicas ou à base de plantas); substâncias psicoativas; equipamentos para facilitar o uso de entorpecentes; armas, munições, materiais explosivos e fogos de artifício; instruções para a confecção de bombas ou outros produtos nocivos; derivados do tabaco.

Permissão de comportamento desonesto
Valorizamos a honestidade e a justiça. Por isso, não permitimos a promoção de produtos ou serviços que viabilizam comportamentos desonestos.
Exemplos de produtos ou serviços que permitem comportamento desonesto: software ou instruções para invasões; serviços destinados a aumentar artificialmente o tráfego do anúncio ou do site; documentos falsificados; serviços de falsificação acadêmica.

Conteúdo inadequado
Valorizamos a diversidade e o respeito e não queremos ofender os usuários. Por isso, não permitimos anúncios ou destinos que mostram conteúdo chocante ou promovem ódio, intolerância, discriminação ou violência.

Exemplos de conteúdo inadequado ou ofensivo: bullying ou intimidação de um indivíduo ou grupo, discriminação racial, produtos pertencentes a grupos de ódio, imagens de cenas de crimes ou de acidentes, crueldade com animais, assassinato, automutilação, extorsão ou chantagem, venda ou comércio de espécies ameaçadas de extinção, anúncios com linguagem obscena.

Práticas proibidas
Abuso da rede de publicidade
Queremos que os anúncios em toda a Rede do Google sejam úteis, variados, relevantes e seguros para os usuários. Não permitimos que os anunciantes exibam anúncios, conteúdos ou destinos que tentem enganar ou burlar nossos processos de revisão.
Exemplos de abuso da rede de publicidade: promoção de conteúdo com malware; uso de técnicas de cloaking ou outras técnicas para ocultar o direcionamento real dos usuários; "arbitragem" ou impulsionar destinos com a finalidade exclusiva ou principal de veicular anúncios; promoção de destinos de "bridge" ou "gateway" com o objetivo único de direcionar os usuários a outro lugar; publicidade com a intenção única ou principal de ganhar apoio público do usuário nas redes sociais; manipulação de configurações na tentativa de burlar nossos sistemas de análise de compliance com a política.

Coleta e uso de dados
Queremos que os usuários confiem que as respectivas informações pessoais serão respeitadas e tratadas com os devidos cuidados. Sendo assim, nossos parceiros de publicidade não devem usar essas informações de modo inadequado nem fazer a coleta para fins pouco claros ou sem as medidas apropriadas de segurança ou divulgação.

Há políticas adicionais sobre o uso da publicidade personalizada, que inclui remarketing e públicos-alvo personalizados. Se você usa recursos de segmentação de publicidade personalizada, leia as políticas sobre coleta e uso de dados de anúncios personalizados.

Exemplos de informações sobre o usuário que devem ser tratadas com cuidado: nome completo; e-mail; endereço de correspondência; número de telefone; carteira de identidade, pensão, previdência social, ID fiscal, matrícula de convênio médico ou número da carteira de habilitação; data de nascimento ou nome de solteira da mãe, além de uma das informações mencionadas acima; situação financeira; filiação política; orientação sexual; raça ou etnia; religião.

Exemplos de coleta e uso irresponsável de dados: coleta de informações de cartão de crédito em um servidor não seguro, promoções que afirmam conhecer a orientação sexual ou situação financeira de um usuário, violações das nossas políticas que se aplicam à publicidade com base em interesses e ao remarketing.

Deturpação
Queremos que os usuários confiem nos anúncios da nossa plataforma. Sendo assim, fazemos todo o possível para que eles sejam claros e verdadeiros, além de oferecerem as informações necessárias para que as pessoas tomem decisões fundamentadas. Não permitimos anúncios ou destinos que excluam informações relevantes dos produtos para tentar confundir os usuários ou que exibam conteúdo enganoso sobre produtos, serviços ou empresas.

Exemplos de deturpação: omissão ou encobrimento de detalhes de faturamento (por exemplo: como, quanto e quando os usuários serão cobrados); omissão ou encobrimento de encargos associados aos serviços financeiros, como taxas de juros, tarifas e multas; não apresentação de números fiscais ou de licença, dados de contato ou endereço físico quando relevante; ofertas que não estão efetivamente disponíveis; afirmações enganosas ou irreais em relação a perda de peso ou ganho financeiro; coleta de doações sob falsos pretextos; "phishing" ou alegar falsamente ser uma empresa respeitável para fazer os usuários darem informações pessoais ou financeiras valiosas.


Conteúdos e recursos restritos
As políticas a seguir abrangem conteúdos que podem ser sensíveis em termos jurídicos ou culturais. A publicidade on-line pode ser uma maneira eficiente de alcançar clientes. No entanto, em áreas sensíveis, também trabalhamos duro para evitar que esses anúncios apareçam em um contexto em que podem ser inadequados.

Por essa razão, permitimos a promoção do conteúdo abaixo, mas de forma limitada. Essas promoções podem não aparecer para todos os usuários em todos os locais. Além disso, podemos pedir que os anunciantes atendam a outros requisitos para que seus anúncios sejam qualificados. Nem todos os produtos, recursos ou redes de publicidade aceitam esse conteúdo restrito. Mais detalhes podem ser encontrados na Central de políticas.

Tratamento padrão de anúncios
Nosso compromisso é oferecer uma experiência de publicidade segura e confiável para todos os usuários. Por isso, limitamos a veiculação de determinadas categorias de anúncios para usuários que não fizeram login ou que, de acordo com nossos sistemas, têm menos de 18 anos.

Conteúdo sexual
Os anúncios precisam respeitar as preferências do usuário e obedecer aos regulamentos legais. Restringimos certos tipos de conteúdo sexual nos anúncios e destinos. Eles só serão exibidos em um número limitado de situações, com base nas consultas de pesquisa, na idade do usuário e na legislação vigente de onde o anúncio está sendo veiculado. Os anúncios não podem segmentar menores de idade.
Saiba mais sobre o que acontece quando nossas políticas são violadas.
Exemplos de conteúdo sexual restrito: órgãos genitais e seios femininos expostos, encontros para sexo casual, brinquedos sexuais, clubes de striptease, chats ao vivo com conotação sexual e modelos em poses sensuais.

Respeitamos as leis de bebidas alcoólicas vigentes e os padrões do setor. Portanto, não permitimos determinados tipos de publicidade relacionados a qualquer tipo de bebidas alcoólicas. Alguns tipos de anúncio relacionados a bebidas alcoólicas são permitidos desde que atendam às políticas abaixo, não segmentem menores de idade e segmentem apenas os países que têm permissão explícita para exibi-los.

Exemplos de bebidas alcoólicas restritas: cerveja, vinho, saquê, destilados, champanhe, vinho fortificado, cerveja sem álcool, vinho sem álcool, bebidas destiladas sem álcool.

Direitos autorais
Ilustração representando a política do Google de proteger os detentores de direitos autorais.

Respeitamos as leis de direitos autorais vigentes e protegemos os detentores desses direitos. Portanto, não permitimos anúncios que não têm autorização para usar conteúdo protegido por direitos autorais. Se você tiver permissão legal para utilizar esse tipo de conteúdo, inscreva-se para receber uma certificação (ou então no DV360) e começar a anunciar. Se você encontrar conteúdo não autorizado, envie uma denúncia relacionada a direitos autorais.

Jogos de azar
Ilustração representando a política do Google de limitar determinados anúncios que envolvem publicidade relacionada a jogos de azar.
Apoiamos a publicidade responsável de jogos de azar e respeitamos a legislação de jogos de azar vigente e os padrões do setor. Portanto, não permitimos determinados tipos de publicidade relacionada a jogos de azar. Anúncios relacionados a jogos de azar só serão permitidos se obedecerem às políticas abaixo e se o anunciante tiver recebido a certificação adequada do Google Ads. Os anúncios de jogos de azar precisam segmentar países aprovados, ter uma página de destino que exiba informações sobre a prática de jogos de azar com responsabilidade e nunca segmentar menores de idade. Verifique os regulamentos vigentes das regiões que você deseja segmentar.

Exemplos de conteúdo restrito relacionado a jogos de azar: cassinos físicos; locais onde os usuários podem apostar em pôquer, bingo, roleta ou eventos desportivos; loterias nacionais ou privadas; sites agregadores de probabilidades de esportes; sites que oferecem códigos de bônus ou ofertas promocionais para sites de cassino; materiais educativos on-line para jogos de cassino; sites que oferecem jogos de pôquer "por diversão"; sites de jogatinas com aposta de dinheiro que não pertencem a um cassino.

Saúde e medicamentos
Ilustração representando a política do Google de limitar determinados anúncios que envolvem conteúdo relacionado à saúde.

Nós nos esforçamos para seguir os regulamentos de publicidade sobre saúde e medicamentos. Portanto, esperamos que os anúncios e destinos obedeçam às leis e aos padrões do setor relevantes. Não é possível anunciar alguns conteúdos relacionados a saúde, e outros tipos de conteúdo só podem ser anunciados se o anunciante for certificado pelo Google e segmentar apenas países aprovados. Consulte os regulamentos das regiões que você quer segmentar.

Conteúdo político
Ilustração representando a política do Google de limitar determinados anúncios com conteúdo político.
Esperamos que todos os anúncios e destinos políticos obedeçam às leis eleitorais e de campanha vigentes das regiões segmentadas pelos anúncios. Essa política inclui os "períodos de silêncio" eleitorais exigidos por lei.

Exemplos de conteúdo político: divulgação de partidos ou candidatos políticos, defesa de questões políticas.

Serviços financeiros
Ilustração representando a política do Google de limitar a veiculação de determinados anúncios que promovem serviços financeiros.
Queremos que os usuários tenham informações adequadas para tomar decisões financeiras fundamentadas. O objetivo das nossas políticas é oferecer aos usuários informações para que eles considerem os custos associados aos produtos e serviços financeiros, além de proteger as pessoas contra práticas nocivas ou enganosas. Para os fins desta política, são considerados produtos e serviços financeiros aqueles que estão relacionados ao gerenciamento ou investimento de dinheiro e criptomoedas, incluindo consultorias personalizadas.

Ao promover produtos e serviços financeiros, você precisa obedecer às regulamentações estaduais e locais de todos os locais segmentados pelos seus anúncios (por exemplo, incluir as divulgações específicas exigidas pela legislação vigente). Os anunciantes devem pesquisar por conta própria sobre os regulamentos vigentes dos locais segmentados pelos anúncios.

Marcas registradas
Ilustração representando a política do Google de limitar determinados anúncios que incluem marcas registradas.
Existem vários fatores que determinam quando as marcas registradas podem ser usadas em anúncios do Google Ads. Junto aos fatores descritos na nossa Central de políticas, estas políticas se aplicam somente quando o proprietário de uma marca registrada envia uma reclamação válida ao Google.
Requisitos legais
Ilustração representando a política do Google sobre conformidade com todas as leis e regulamentações aplicáveis. 

Você é responsável por garantir compliance com todas as leis e regulamentações aplicáveis, além das políticas de publicidade do Google, de todos os locais onde seus anúncios são veiculados.

Outros negócios restritos
Ilustração representando a política do Google sobre restringir a publicidade de determinados tipos de empresa no Google Ads.
Restringimos a publicidade de determinados tipos de empresa para evitar que os usuários sejam explorados, mesmo que algumas pareçam estar em conformidade com as outras políticas. Com base nas nossas revisões contínuas, nos comentários de usuários, reguladores e órgãos de proteção ao consumidor, ocasionalmente identificamos produtos ou serviços que tendem a cometer abusos. Se percebermos que determinados tipos de empresa representam risco desarrazoado à segurança ou à experiência do usuário, limitaremos ou interromperemos a exibição de anúncios relacionados.
Restrição de recursos e formatos de anúncio
Ilustração representando os requisitos e o processo de certificação do Google para formatos de anúncio avançados.
Existem vários fatores que determinam o acesso a recursos e formatos de anúncio avançados no Google Ads. Determinados recursos e formatos de anúncio só ficam disponíveis para todos os anunciantes depois que eles atendem aos nossos requisitos específicos ou concluem o processo de certificação.

Requisitos do conteúdo para crianças
Ilustração representando a política do Google sobre restrição de anúncios em conteúdo para crianças. 
Os anunciantes não podem exibir publicidade personalizada em vídeos definidos como conteúdo para crianças. Veja aqui as categorias restritas para publicidade nesse tipo de conteúdo.

Proteções de veiculação de anúncios para crianças e adolescentes
É importante que a experiência de publicidade em todos os produtos do Google seja útil, informativa e, acima de tudo, segura para os usuários. Isso também inclui crianças e adolescentes. Nossas políticas de anúncios para crianças e adolescentes usam salvaguardas para ajudar a proteger usuários com menos de 18 anos, incluindo a desativação da personalização de anúncios e restrições de categorias sensíveis de anúncios.

Veiculação de anúncios limitada
Esta ilustração representa a política de veiculação de anúncios limitada do Google Ads.
Para proteger a integridade do nosso ecossistema do Google Ads, limitamos as impressões de anúncios com alto potencial de resultar em abuso ou em uma experiência insatisfatória para os usuários. Nesses casos, apenas anunciantes qualificados poderão mostrar publicidade sem limites de impressões. Saiba em que casos a veiculação de anúncios limitada é válida e quem são os anunciantes qualificados.

Requisitos editoriais e técnicos
Queremos exibir anúncios que envolvam os usuários e não sejam desagradáveis ou de difícil interação. Sendo assim, desenvolvemos requisitos editoriais para ajudar a manter seus anúncios atraentes para os usuários. Também especificamos requisitos técnicos para ajudar os usuários e anunciantes a aproveitar ao máximo a variedade de formatos de anúncios que oferecemos.

Requisitos editoriais
Para oferecer uma experiência de qualidade aos usuários, o Google exige que todos os anúncios, recursos e destinos sigam altos padrões profissionais e editoriais. Só permitimos anúncios claros, com aparência profissional e que apresentam conteúdo relevante, útil e de fácil interação.
Exemplos de promoções que não atendem a esses requisitos editoriais e profissionais:

Anúncios muito genéricos que contêm frases vagas, como "Compre produtos aqui"
Artifícios no uso de palavras, números, letras, símbolos ou pontuação, como GRÁTIS, g-r-á-t-i-s e G ₹ A T I S!
Requisitos de destino
Nosso objetivo é que os consumidores tenham uma boa experiência quando clicam em um anúncio. Portanto, os destinos de anúncio precisam agregar valor exclusivo aos usuários, além de serem funcionais, úteis e fáceis de navegar.
Exemplos de promoções que não atendem aos requisitos de destino:

Um URL de visualização que não reflete com precisão o URL da página de destino, como "google.com.br" levando para a página do "gmail.com.br"
Sites ou aplicativos que estão em construção, domínios reservados ou que simplesmente não estão funcionando
Sites que não são visíveis nos navegadores mais utilizados
Sites que desativaram o botão "Voltar" do navegador
Requisitos técnicos
Para nos ajudar a manter a clareza e a funcionalidade dos anúncios, os anunciantes precisam atender aos nossos requisitos técnicos.

Requisitos de formato do anúncio
Para ajudar você a proporcionar uma experiência de qualidade ao usuário e exibir anúncios atraentes e profissionais, permitimos apenas promoções que obedeçam aos requisitos específicos de cada anúncio. Revise os requisitos específicos de formato de todos os formatos de anúncio que você usa.

Observação: não é permitido usar anúncios não indicados para menores em anúncios gráficos, em vídeo e em outros formatos que não sejam de texto. Saiba mais sobre nossa política de conteúdo adulto.

Exemplos de requisitos de formato do anúncio: limites de caracteres para o título ou o corpo do anúncio; requisitos de tamanho de imagem; limites de tamanho de arquivo; limites de duração do vídeo; proporções etc.
"""

politicas_meta = f"""
Os anunciantes devem seguir nossos Padrões de Publicidade, que foram criados para ajudar a proteger as pessoas de experiências ruins e apoiar conexões significativas entre pessoas e empresas nas nossas tecnologias. Por exemplo, não queremos anúncios que usem linguagem ofensiva, mostrem nudez excessiva ou incluam desinformação.

Nossas políticas se aplicam à publicidade paga por meio da nossa plataforma de anúncios, incluindo o Facebook, o Messenger, o Instagram e o Audience Network da Meta. Para obter uma lista completa das nossas políticas de publicidade, acesse os Padrões de Publicidade.

Na Central de Ajuda da Meta para Empresas, fornecemos mais informações sobre nossas políticas de publicidade. Veja abaixo uma lista de artigos:

Atributos pessoais: política de publicidade da Meta que proíbe anúncios que contêm atributos pessoais, incluindo informações sobre como evitar suposições sobre os atributos pessoais de alguém nos seus anúncios.
Conteúdo sensacionalista: nossa política de publicidade que proíbe conteúdo sensacionalista, incluindo informações sobre como evitar conteúdo chocante, sensacionalista, polêmico ou excessivamente violento nos seus anúncios.
COVID-19: nossas políticas de publicidade relacionadas à COVID-19, incluindo quais tipos de produtos e conteúdos estão temporariamente restritos ou proibidos.
Produtos e serviços de criptomoeda: nossa política de publicidade para produtos e serviços de criptomoeda, incluindo informações sobre qualificação para veicular anúncios sobre criptomoeda.
Namoro: nossa política de publicidade para anúncios sobre serviços de encontros.
Tratamento de dependência de drogas e álcool: nossa política de publicidade para tratamento de dependência de drogas e álcool, incluindo informações sobre como se inscrever para veicular esses tipos de anúncios.
Jogos online e jogos de azar: nossa política de publicidade para jogos de azar e jogos online, incluindo informações sobre como se inscrever para veicular esses tipos de anúncios.
Saúde pessoal e aparência: nossa política de publicidade que proíbe anúncios que geram deturpação da autoimagem ou prometem resultados inesperados ou irreais.
Álcool: nossa política de publicidade sobre a promoção de álcool.
Temas sociais, eleições ou política: nossa política de publicidade para anúncios sobre temas sociais, eleições ou política.
Outras políticas que podem ser aplicadas ao seu anúncio
Quando os anunciantes usam produtos diferentes da nossa família de apps e serviços, políticas adicionais também podem ser relevantes, incluindo:

Facebook: os anúncios veiculados no Facebook devem seguir os Padrões da Comunidade do Facebook, que se aplicam a todos os conteúdos nessa plataforma.
Instagram: os anúncios veiculados no Instagram devem seguir as Diretrizes da Comunidade do Instagram, que se aplicam a todos os conteúdos nessa plataforma.
Comércio: os anunciantes podem veicular certos tipos de anúncios, como anúncios com etiquetas de produto ou classificados do Marketplace turbinados, ou usar catálogos para carregar produtos para uso em plataformas de comércio, que estão sujeitas às nossas Políticas Comerciais.
Páginas e eventos: os anunciantes podem promover Páginas ou eventos, que estão sujeitos às Políticas de Páginas, grupos e eventos relevantes.
Messenger: os anunciantes que enviam mensagens patrocinadas pelo Messenger ou que iniciam conversas automatizadas a partir de anúncios de clique para o Messenger devem seguir nossas Políticas do Desenvolvedor.
Conteúdo de marca: os anúncios podem incluir conteúdo de marca, que está sujeito às Políticas de Conteúdo de Marca.
"""

# Exemplos de E-MAIL WELCOME
exemplos_emailWelcome = f"""
INICIO DOS EXEMPLOS DE E-MAIL WELCOME-------------------------------------------
 
Exemplo 1:
 
SEMANA QUANTZED: OPERANDO COMO INSTITUCIONAIS Com Marcelo Oliveira e Pedro Menin
 
Olá, tudo bem?
 
Aqui é Marcelo Oliveira, analista CFA e fundador da plataforma Quantzed, um sistema com ferramentas e estratégias para o cidadão comum investir como um profissional.
 
Mesmo que você atue em outra área…
 
Mesmo começando do zero…
 
A Quantzed foi desenvolvida pra facilitar seu processo de investimento.
 
Pra fazer você operar como os grandes tubarões do mercado, com estratégias simples e consagradas, finalmente acessíveis para quem deseja buscar mais renda.
 
No mês… na semana… no dia!
 
Que tal a possibilidade de lucrar R$ 1.500 toda manhã, logo na abertura do pregão?
 
Isso tornaria sua vida mais tranquila?
 
Eu acredito que SIM, que você também pode ter ganhos como esse e até mais ao longo do dia – com estratégias automatizadas pela Quantzed.
 
Eu e meu sócio, Pedro Menin, queremos te mostrar como elas funcionam.
 
Queremos te ajudar a colocá-las em prática pra que você também tenha a chance de gerar mais renda, dia após dia.
 
Para isso, estamos organizando a Semana Quantzed.
 
Trata-se de um evento on-line e gratuito, com vagas limitadas.
 
Tá preparado?
 
No encontro, Pedro e eu vamos te mostrar as nossas três principais estratégias para buscar dinheiro de verdade.
 
Como ganham os tubarões, não as sardinhas.
 
Eu já trabalhei para os Grandes Bancos, operando de 5 a 6 bilhões de reais e sei bem como esse tipo de estratégia pode ser lucrativa.
 
Tanto que passei a operar por conta própria e essa foi minha principal fonte de renda por mais de 2 anos.
 
Já ensinamos muita gente a fazer igual por meio da Plataforma Quantzed e agora a gente acabou de firmar uma parceria inédita com a Empiricus Research pra que você tenha a mesma oportunidade.
 
Será que você também é capaz de buscar R$ 1.500 toda manhã?
 
Acredito que sim e queremos te ajudar nesse objetivo.
 
Então anote na agenda: o primeiro encontro, on-line e gratuito, é no dia 22/03, quarta-feira.
 
Pode acreditar em mim, você nunca viu uma ferramenta tão completa e com tantas possibilidades simples de ganhar dinheiro.
 
Mas vamos com calma, uma estratégia por vez.
 
A primeira, já no nosso encontro do dia 22/03. Vou liberar um vídeo nesse dia mostrando exatamente como ela funciona.
 
Aproveite e já se cadastre no nosso grupo de whatsapp para receber mais informações antecipadamente.
 
É só clicar neste ou em qualquer outro link deste e-mail.
 
A gente se vê lá!
 
Abraço,
 
Marcelo Oliveira.


 
Exemplo 2:
 
Olá, tudo bem?
 
Aqui quem fala é o Felipe Miranda, fundador e CEO da Empiricus e sócio do BTG Pactual.
 
Fico feliz que você tenha demonstrado interesse em participar de um dos projetos mais importantes da minha carreira, o Projeto Renda.
 
Para confirmar sua pré-matrícula, basta clicar no botão abaixo e entrar na comunidade de alunos no WhatsApp.
 
CONFIRME AQUI SUA PRÉ-MATRÍCULA (BOTÃO)
 
Por lá eu e a minha equipe vamos te enviar vídeos e áudios com conteúdos importantes antes da abertura da turma 0, que vai acontecer no dia 13 de novembro.
 
Por enquanto, você já pode assistir ao primeiro vídeo que foi liberado clicando aqui.
 
Você vai descobrir como construir uma "impressora de dinheiro" que pode ser responsável por gerar uma renda diária na sua conta.
 
Dentro das próximas semanas, ao meu lado, você vai construir sua primeira fonte de renda passiva e se transformar em um investidor completo, certificado por mim e pela Empiricus.
 
E não importa se você já sabe investir ou se ainda está começando.
 
Vamos te guiar do zero por todas as oportunidades de fazer renda que eu utilizo para mim, para minha família e para a minha empresa.
 
Estou falando desde dividendos, até milhas, fundos imobiliários, fundos de investimento, renda fixa, ações, previdência, investimentos internacionais, criptomoedas, small caps e opções…
 
Começando do básico até as mais avançadas estratégias utilizadas por grandes gestores da Faria Lima.
 
Mas agora que você entendeu o que é o Projeto Renda, você precisa entender o que ele NÃO É.
 
Não somos mais um cursinho do seu Youtuber favorito, com conteúdos rasos criados para tirar seu dinheiro.
 
Como diz George Soros, somos verdadeiros "animais do mercado financeiro', criados e forjados dentro desse ambiente.
 
Não estamos aqui para falar de mentalidade. Deixamos esse trabalho para o seu psicólogo.
 
Não espere ver horas intermináveis de conteúdos sobre mentalidade da riqueza.
 
Preferimos focar no que realmente importa: como fazer você sair do zero e se tornar um investidor completo com uma nova fonte de renda sob o seu CPF, fazendo dinheiro "pingar" diariamente na sua conta bancária.
 
Eu passei os últimos meses trabalhando forte em cima desse projeto, sem fazer alarde com a mídia e com as redes sociais.
 
Isso deixou de ser apenas um trabalho e se tornou uma missão pessoal para mim.
 
Se você chegou até aqui saiba que você faz parte de um seleto grupo de pessoas que vão ter a chance de se formar na Turma 0 do Projeto Renda.
 
E eu não vou sossegar até ver cada um de vocês com sua própria fonte de renda passiva.
 
Você tem a minha palavra.
 
Basta clicar no link abaixo e confirmar sua pré-matrícula.
 
CONFIRME SUA PRÉ-MATRÍCULA AQUI [PROJETO RENDA] (BOTAO)
Aguarde maiores informações em breve.
 
Abraços,
 
Marcelo Oliveira.
 
 
FIM DOS EXEMPLOS DE E-MAIL WELCOME-------------------------------------------
"""
exemplos = exemplos_emailWelcome    
tipo_copy = "E-MAIL WELCOME",
plataforma = plataforma_email
politica = politicas_google
instrucao_adicional = """ """

# Exemplos de E-MAIL WELCOME
exemplos_emailWarmup = f"""
FIM DOS EXEMPLOS DE E-MAIL WARMUP-------------------------------------------

Exemplo 1:

Olá, tudo bem?

Aqui é Marcelo Oliveira, analista CFA e fundador da Plataforma Quantzed, um sistema com ferramentas e estratégias para o cidadão comum investir como um profissional.

Não sei se você já sabe, mas fizemos uma parceria inédita com a Empiricus Research.

E liberamos dois conteúdos que acredito ser do seu interesse:

Primeiro… 

A operação que os Grandes Bancos fazem e que agora você pode replicar em busca de R$ 1.500 ou mais toda manhã.

Você pode conferir neste link.

Trata-se de uma operação muito simples, que você pode abrir e fechar em cerca de 10 minutos, mesmo se ainda for iniciante no mercado financeiro.

E depois tem o resto do dia pra seguir sua vida: se dedicar ao seu trabalho, ao seu negócio, fazer academia, cuidar dos filhos…

E o segundo conteúdo é tão relevante quanto o primeiro…

Duas Estratégias Profissionais (e uma terceira extra) pra você buscar mais dinheiro ao longo dia, além dos R$ 1.500 da manhã.

Está disponível neste link.

Já tem muita gente ganhando dinheiro com essas estratégias, e esta é sua chance de buscar ganhos similares.

Como meus alunos já estão fazendo…

(IMAGENS)
Fonte: Mensagens dos alunos

Aproveite o fim de semana para ver os vídeos.

Porque, na segunda-feira, temos uma surpresa logo de manhã para quem estiver disposto a colocar em prática essas estratégias, que só a Quantzed tem.

Combinado?

Te vejo nos vídeos!

(VÍDEO)

QUERO BUSCAR ATÉ R$ 1.500 OU MAIS TODA MANHÃ (BOTÃO)

Abraço,

Marcelo Oliveira


 
Exemplo 2:

Opa, tudo bem?

Como prometido, aqui está o primeiro vídeo do Projeto Renda. 

Basta clicar no vídeo abaixo e assistir antes que ele saia do ar.

(VÍDEO)

Nele eu mostrei como eu vou pegar na sua mão e te ajudar a construir 11 novas fontes de renda passiva no seu nome já nas próximas semanas.

Trouxe também alguns casos de pessoas que vivem de renda apenas seguindo essa estratégia simples.

(IMAGENS)

Pessoas comuns que sequer sabiam como investir e hoje possuem fontes de renda pingando periodicamente na conta delas, proporcionando mais liberdade e poder de escolha. 

Se você quiser e ouvir o que tenho para dizer, esse pode ser o seu caso também, começando já nas próximas semanas com os primeiros rendimentos caindo na sua conta.

E eu não estou falando de algo que você vai fazer agora para começar a colher os frutos daqui 10 ou 20 anos.

Eu estou falando de algo imediato que você vai fazer agora e já vai começar a se beneficiar com os pagamentos. 

R$ 1.000, R$ 2.000, R$ 5.000, R$ 10.000 e, em alguns casos, até R$ 20.0000 de renda extra na sua conta todos os meses.

Você topa? 

Então clique e assista ao vídeo o mais rápido possível.

ASSISTIR PRIMEIRO VÍDEO [PROJETO RENDA] (BOTÃO)

Hoje no final do dia vou tirar um tempo para ler todos os comentários.

Espero ver sua mensagem lá. 

Abraços, 

Felipe Miranda

CEO da Empiricus


FIM DOS EXEMPLOS DE E-MAIL WARMUP-------------------------------------------
"""
exemplos = exemplos_emailWelcome	
tipo_copy = "E-MAIL CPL/WARMUP",
politica = politicas_google

formato_saida = """
Escreva um e-mail convidativo com conteúdos no período de pré-lançamento do produto, enviado aos leads captados para mantê-los engajados antes da abertura das vendas.
 """
plataforma = plataforma_email
instrucao_adicional = """ 
"""

# Exemplos de E-MAIL WELCOME
exemplos_emailPromoInicial = f"""
INICIO DOS EXEMPLOS DE E-MAIL PROMO ABERTURA DE CARRINHO -------------------------------------------
 
Exemplo 1: 

Eu tenho um plano prático para você buscar até R$ 1.500 toda manhã e ter a possibilidade real de mais lucros durante o dia. [Garanta hoje mesmo a sua vaga]
 
Fala, pessoal!
 
Acabei de liberar o último episódio da Semana Quantzed.
 
É só clicar neste link e conferir… (LINK)
 
(VÍDEO)
 
No vídeo, você vai conferir um plano prático para replicar as estratégias profissionais que os Grandes Bancos usam.
 
Em busca de R$ 1.500 toda manhã com a possibilidade real de ganhos ainda maiores ao longo do dia.
 
Mesmo que você seja iniciante…
 
Porque a gente vai operar com ferramentas simples e intuitivas, como você pode conferir no vídeo final.
 
Titulo Imagem
(IMAGEM)
Fonte:
 
Titulo Imagem
(IMAGEM)
Fonte:
 
Titulo Imagem
(IMAGEM)
Fonte:
 
Afinal, a matemática está toda do seu lado.
 
Então, não perca mais tempo porque as vagas são limitadas.
 
Preparei uma condição especial para você testar a ferramenta com 4 meses gratuitos de uso da Plataforma Quantzed.
 
Lembrando que você tem 7 dias sem compromisso para conhecer todas as nossas estratégias, simples e intuitivas, para você começar o quanto antes a buscar mais renda.
 
Preparado?
 
Te espero no vídeo. (LINK)
 
QUERO BUSCAR ATÉ R$ 1.500 OU MAIS TODA MANHÃ (BOTÃO)
 
Abraço,
 
Marcelo Oliveira
 

 
Exemplo 2:
 
Chegou a hora!
 
Como prometido, aqui está o link da transmissão com o alerta de compra da criptomoeda de 50 centavos de dólar que pode multiplicar o seu dinheiro por 100 vezes em até 20 meses.
 
Só com essa indicação você tem a chance de fazer cada:
 
• R$ 1.000 virarem R$ 100 mil
 
• R$ 5.000 virarem R$ 500 mil
 
• R$ 10 mil virarem R$ 1 milhão
 
Eu te provo como cheguei nesse número na transmissão:
 
ACESSAR AGORA: CRIPTOMOEDA DE 50 CENTAVOS DE DÓLAR QUE PODE MULTIPLICAR O DINHEIRO POR 100X (BOTÃO)
 
Além disso, na conversa com o Roberto Altenhofen eu vou te mostrar:
 
• Por que você deveria investir nessa criptomoeda ainda hoje;
 
• Os motivos que me fazem ter convicção de que estamos só no início de um novo ciclo de alta desse mercado;
 
• Os fatores que me fazem acreditar que a minha indicação pode ser a principal beneficiada desse movimento.
 
Além de liberar acesso ao nome, eu também vou te entregar os tutoriais de compra para essa criptomoeda.
 
Dessa forma, você vai poder investir nesse ativo, caso queira, com a mesma facilidade que você compra uma roupa na internet.
 
O momento é agora. Clica aí e vem com a gente:
 
(VÍDEO)
 
Você pode se lembrar de hoje como o dia em que você começou a mudar de vida.
 
Da minha parte eu vou fazer de tudo para que isso aconteça.
 
Te vejo lá,
 
Valter Rebelo
 
Head de Ativos Digitais na Empiricus
 
FIM DOS EXEMPLOS DE E-MAIL PROMO ABERTURA DE CARRINHO -------------------------------------------
"""
exemplos = exemplos_emailPromoInicial  
tipo_copy = "PROMO ABERTURA DE CARRINHO",
plataforma = plataforma_email
politica = politicas_google

instrucao_adicional = """ """



# Exemplos de E-MAIL WELCOME
exemplos_emailPromo = f"""
INICIO DOS EXEMPLOS DE E-MAIL PROMO -------------------------------------------
 
Exemplo 1:

Eu estou tentando te avisar…
 
Quem investir "nesta criptomoeda de centavos de dólar"(LINK) ainda em março vai sim ter uma ótima chance de multiplicar o dinheiro investido por até 100x…
 
Ontem à noite eu te enviei o alerta de compra dessa moeda. Você pode ver gratuitamente aqui:
 
(VÍDEO)
 
Desde então, dá uma olhada no que aconteceu:
 
(IMAGEM)
Fonte: Criptob
 
Enquanto outras criptomoedas estavam caindo, a nossa nova estrela está despontando.
 
Foram 34,8% em apenas 24 horas.
 
Essa não é uma alta isolada… eu acredito que ainda tem muito potencial nesse ativo para os próximos meses.
 
Quem aproveitar, pode mudar de vida.
 
Não dá pra ficar vendo isso acontecer sem fazer nada.
 
Então reforço…
 
Veja a "transmissão"(LINK), saiba qual criptomoeda é essa e decida depois se quer investir ou não.
 
R$ 1.000 aqui tem grandes chances de se tornarem R$ 100 mil em muito menos tempo do que você imagina.
 
Você pode pagar pra ver de novo, ou pode clicar no botão abaixo para saber o nome da criptomoeda que pode ser a grande responsável por mudar a sua vida.
 
QUERO CONHECER A CRIPTOMOEDA AGORA (BOTÃO)
 
Abraço,
 
Valter Rebelo
 
Head de Ativos Digitais na Empiricus
 

 
Exemplo 2:
 
A Prova definitiva de como é possível ter ganhos médios de R$ 2.000 por dia com trade AGORA, em 2024 [Veja aqui] (LINK)
 
Fala, galera! Tudo bem?
 
Muitas pessoas me questionaram quando lancei esta proposta dos R$ 2.000 por dia, em parceria com a Empiricus Research.
 
"O Ogro se vendeu…"
 
"Ele tá fazendo promessa na internet…"
 
"Que vergonha…”
 
Confesso que no início fiquei meio p@#% com as críticas, mas agora estou entendendo melhor a reação de alguns.
 
Eles nunca ganharam dinheiro de verdade com investimentos, mesmo aqueles que tentaram.
 
Claro… eles usaram técnicas furadas que "aprenderam" com fake traders, aí o resultado não poderia mesmo ser positivo.
 
Aqui "neste vídeo"(LINK) tem a prova definitiva de que a meta que estabelecemos é perfeitamente factível, mesmo para os iniciantes.
 
E, sim, num prazo inferior a 6 meses, pra que você possa ter mais uma fonte de renda, que faça a diferença já em 2024.
 
(VÍDEO)
 
Eu não estou aqui pra brincar com os sonhos de ninguém.
 
Tenho 22 anos de mercado financeiro.
 
Day trade é a primeira fonte de renda da minha família, e graças a Deus pudemos educar três filhos sem nunca deixar faltar nada em casa.
 
Hoje ganho no mercado financeiro uma renda média diária muito maior que a meta estabelecida aqui, e sabe o que é o melhor disso tudo?
 
Você também pode trilhar o mesmo caminho, com a minha ajuda.
 
Sem bater cabeça como eu já bati.
 
Começando do jeito certo, com os pés no chão.
 
Muitos alunos meus já estão tendo essa mesma oportunidade.
 
(VÍDEO)
 
Disclaimer: Ganhos passados não são garantia de ganhos futuros. Investimentos têm riscos.
 
O Bruno revelou pra gente que tá batendo 500 pontos para mais, quase todos os dias.
 
Sabe quanto isso representa em dinheiro?
 
A conta é simples:
 
Operando pequeno, com apenas 1 minicontrato, você estaria recebendo em média R$ 100 por dia.
 
Com 2 minicontratos, seriam R$ 200.
 
R$ 500 por dia com 5 minicontratos.
 
Com apenas 20 contratos, o que também não é uma mão pesada, você já teria a chance de ganhar seus 2.000 reais por dia, na média, e bater a meta estabelecida no projeto.
 
Seriam cerca de 10 mil reais por semana… 40 mil reais por mês!
 
Repito: não há nada de absurdo nesses ganhos.
 
O mercado financeiro é, na minha opinião, o ambiente mais democrático pra quem deseja ganhar dinheiro – e o mais próspero também.
 
Seja como fonte adicional de renda ou mesmo como renda principal.
 
Eu quero que você sinta isso na prática, o quanto antes.
 
"Veja o vídeo"(LINK), tá em tempo ainda.
 
Faço questão de estar ao seu lado nessa jornada por mais renda.
 
QUERO BUSCAR GANHOS MÉDIOS DE R$ 2.000 POR DIA (BOTÃO)
 
André Machado
 
O Ogro de Wall Street
 
FIM DOS EXEMPLOS DE E-MAIL PROMO -------------------------------------------
"""
exemplos = exemplos_emailPromo  
tipo_copy = "PROMO",
politica = politicas_google

plataforma = plataforma_email
instrucao_adicional = """ """


# Exemplos de E-MAIL WELCOME
exemplos_emailPromoUltima = f"""
FIM DOS EXEMPLOS DE E-MAIL PROMO ÚLTIMA-------------------------------------------

Exemplo 1:
Antes de mais nada, obrigado.

Obrigado por ter ao menos se interessado pelo meu maior projeto nos últimos meses: 5 moedas para investir R$ 500 em cada e buscar R$ 1 milhão.

Eu sei que é uma ideia chamativa…  

Desculpa por isso.

O meu objetivo aqui é fazer com que o máximo de pessoas conheça o mercado de criptomoedas.

Esse mercado mudou a minha vida e principalmente mudou a vida de quem segue o nosso trabalho:

(IMAGEM)

Eu realmente acredito que somente nesse mercado é possível atingir um resultado como esse partindo de pouco dinheiro.

Por isso, eu insisto: veja a minha lista de 5 moedas para investir R$ 500 em cada e buscar R$ 1 milhão.

Parece absurdo em um primeiro momento, mas é possível nesse mercado… ainda mais agora, com todos os gatilhos que estamos vivendo.

Halving… ETFs… taxa de juros.

A chance é realmente única.

Este é meu último e-mail para você.

Se quiser liberar acesso à lista, aqui está a sua última chance:

LIBERAR ACESSO: 5 CRIPTOMOEDAS PARA BUSCAR R$ 1 MILHÃO (BOTÃO)

No mais é isso. 

Obrigado! Espero ter aberto os seus olhos para esse mercado que é repleto de oportunidades.

Um abraço,

Valter Rebelo

Head de Ativos Digitais na Empiricus


 
Exemplo 2:

Últimas horas para destravar sua vaga extra em busca de R$ 2.000 por dia [Ogro Trading System]

Fala, galera!

Obrigado, de coração, a todos que estão confiando no meu trabalho e aceitaram o desafio de fazer parte da nova turma do OGRO Trading System.

Você já sabe a nossa meta: R$ 2.000 por dia, na média, AGORA em 2024.

Mesmo sendo iniciante, já que vamos te dar todo o passo a passo para construir essa receita.

E começando com um capital pequeno, para aumentá-lo aos poucos, à medida que adquire mais confiança na estratégia.

Sua vaga extra ainda está reservada, mas você tem só até a meia-noite para decidir.

Pode clicar neste link para conhecer o projeto.

Faço questão de reforçar meu compromisso em te ajudar a cumprir a meta financeira dos ganhos médios de R$ 2.000 por dia.

Essa é uma estratégia que envolve riscos, mas muitos alunos meus já estão nesse caminho.

(IMAGEM)

GANHOS DE R$ 1.800,00

(IMAGEM)

700 PONTOS = R$ 70… R$ 140…
R$ 280… R$ 700… R$ 1.400…  R$ 2.100… 

Ganhos passados não são garantia de ganhos futuros. Investimentos têm riscos.

E você pode ser o próximo, com uma nova possibilidade de renda ainda em 2024, como você provavelmente nunca teve antes com seus investimentos.

Todos os benefícios que preparamos estão mantidos para as vagas extras.

✔ Treinamento completo OGRO Trading System, com 5 Módulos;

✔ Série Carteira Empiricus, com 3 meses de acesso.

Mais os Bônus especiais:

✔ BÔNUS 1: 3 Meses de Sala de Trade AO VIVO (R$ 2.250)

✔ BÔNUS 2: Curso Básico Introdutório (R$ 2.000)

✔ BÔNUS 3: Lives com Ogro de Wall St. e SuperMario Pisani

✔ BÔNUS 4: Certificado de Trader

Com 7 dias gratuitos pra você conhecer o projeto e assistir às primeiras aulas do treinamento.

Pensa comigo…

Quanto vale pra você a chance de construir uma renda média adicional de R$ 2.000 por dia?

Estou falando de um potencial médio de R$ 10.000 por semana…

Cerca de R$ 40.000 por mês, na média!

É a sua liberdade em ter uma vida financeira muito mais tranquila com a sua família.

Eu quero ter a chance de fazer por você o mesmo que já fiz por milhares de alunos.

Em respeito à sua história e a tudo que você já passou.

É o seu projeto de vida que está em jogo.

É o seu patrimônio…

São os sonhos da sua família.

Ninguém tem o direito de brincar com isso.

Estamos juntos nessa jornada por mais renda, você não vai se arrepender.

A possibilidade de gerar 2.000 reais por dia, na média – e muito mais – é real.

Eu quero te dar todas as ferramentas necessárias para você buscar essa renda muito rápido.

Você tem poucas horas para dar esse passo importante na sua vida financeira.

(IMAGEM)

Estas são as últimas vagas extras.

Espero de coração que uma delas seja sua.

QUERO BUSCAR GANHOS MÉDIOS DE R$ 2.000 POR DIA (BOTÃO)

Abraço,

André Machado

O Ogro de Wall Street


FIM DOS EXEMPLOS DE E-MAIL PROMO ÚLTIMA-------------------------------------------
"""
exemplos = exemplos_emailPromoUltima	
tipo_copy = "PROMO ÚLTIMA",
politica = politicas_google
formato_saida = """
Escreva um e-mail com a mensagem final à audiência para incentivar a compra do produto antes do término da campanha.
 """
plataforma = plataforma_email
instrucao_adicional = """ """



# Exemplos de WHATS WELCOME
exemplos_zapWelcome = f"""
INICIO DOS EXEMPLOS DE WHATSAPP WELCOME -------------------------------------------
 
Bem-vindo à comunidade oficial da *Semana Quantzed*!
 
Anota na agenda: nosso encontro será on-line e gratuito, com vagas limitadas e início marcado para o dia 22 de março.
 
Vamos te mostrar as nossas três principais estratégias pra te ajudar a buscar dinheiro de verdade. Como ganham os tubarões, não as sardinhas.
 
Será que você também é capaz de fazer R$1.500 por dia?
 
Acredito que sim e queremos te ajudar nesse objetivo.
 
Permaneça no grupo para receber todas as notificações sobre as aulas, incluindo a data, horário e link de acesso, combinado?
 
_*ATENÇÃO*: Fique atento a fraudes! Confie somente nos administradores do grupo. Não vamos solicitar dados no privado, como conta bancária e transferência de valores (PIX)._
 
 

 
Exemplo 2:
 
PARTE 1:
 
Seja bem-vindo(a). Parabéns por tomar essa decisão.
 
Você está cada vez mais perto da oportunidade de transformar cada R$ 1.000 investidos seus em R$ 100 mil investindo em um ativo de apenas 50 centavos.
 
É importante que você fique no grupo, aqui você vai receber todas as atualizações sobre o ativo.
 
No dia 18, às 19:00 em ponto eu vou te enviar um link por aqui.
 
Peço que não compartilhe com ninguém, porque vai ser lá que eu vou mostrar todas as informações desse ativo para você.
 
 
PARTE 2:
 
Mas antes eu precisava te conhecer melhor. Eu quero saber um pouco da sua história.
 
Do motivo que está te fazendo investir nesse ativo. Eu quero te conhecer de verdade, pode se abrir comigo.
 
Eu criei um formulário pra gente poder conversar, para ver ele basta clicar aqui:
(FORMULÁRIO)
 
Eu serei o seu guia nessa jornada e farei de tudo para que você consiga alcançar o nosso objetivo aqui.
 
_ATENÇÃO: Fique atento a fraudes! Confie somente nos administradores da comunidade. Não vamos solicitar dados no privado, como conta bancária e transferência de valores (PIX)._
 
 
FIM DOS EXEMPLOS DE WHATSAPP WELCOME -------------------------------------------
"""
exemplos = exemplos_zapWelcome  
tipo_copy = "WELCOME",
plataforma = plataforma_whatsapp
politica = politicas_meta
instrucao_adicional = """ """


# Exemplos de WHATS WELCOME
exemplos_zapLembrete = f"""
INICIO DOS EXEMPLOS DE WHATSAPP LEMBRETE -------------------------------------------
 
Exemplo 1:

*CONTAGEM REGRESSIVA! FALTAM 5 DIAS*

Está chegando a hora de aprender 3 estratégias consagradas para você operar como os tubarões do mercado.

Na série de aulas da Semana Quantzed, você vai conhecer  a operação diária que os grandes bancos fazem e que agora você pode replicar para buscar até R$ 1.500 (ou mais) toda manhã, logo na abertura do mercado.

Serão três encontros em que vamos compartilhar com você estratégias vencedoras…
Estratégias que os Grandes Bancos usam para ganhar muito dinheiro no mercado e que você terá a chance de usá-las também.

Marca na agenda: é dia 22 de março. Te vejo lá!


 
Exemplo 2:
 
*DAQUI A 3 DIAS TUDO PODE COMEÇAR A MUDAR PRA VOCÊ*

Logo na primeira aula da Semana Quantzed, eu vou começar direto pela estratégia que eu considero a mais importante de todas:

Aquela que te dá a possibilidade diária de colocar no bolso até R$ 1.500 logo de manhã, na abertura do pregão.

Você abre e fecha a operação muitas vezes em menos de 10 minutos, por volta das 10 horas da manhã.

E depois tem o resto do dia pra seguir sua vida.

Seja qual for a sua agenda, você terá controle do seu tempo.

E ainda pode ficar mais tranquilo financeiramente, a partir do momento que você começar a aplicar essa estratégia com consistência e com riscos controlados.

Tá preparado?



Exemplo 3:

*TUDO PRONTO PRA AMANHÃ! PREPARADOS?*

Vamos te revelar um segredo que os bancos guardam a sete chaves.

É um tipo de operação que costuma trazer muito dinheiro para eles, de forma relativamente simples.

O melhor de tudo é que o risco é controlado e a estatística fica a nosso favor.

Eu sei bem o que tô falando porque já estive do lado de lá.

Eu operava quantias bilionárias na tesouraria de um Grande Banco: algo entre 5 e 6 bilhões de reais.

Foi operando pra valer, por conta própria e ganhando dinheiro que eu pude desenvolver a estratégia que vou apresentar nos próximos dias.

Fica de olho aqui no grupo. Falta pouco para o nosso primeiro encontro!



Exemplo 4:

Faltam apenas 5 dias para você receber acesso ao nome do ativo digital que custa centavos de dólar e pode ter a chance de fazer o seu dinheiro multiplicar por até 200 vezes.

O mercado está jogando a nosso favor… o Bitcoin já passou a marca de US$ 70 mil.

Agora chegou a vez dos ativos menores decolarem.

Não dá pra ver tudo isso acontecendo sem fazer nada.

Por isso, no dia 18/03, às 19h eu vou te enviar o link por aqui liberando acesso ao nome dessa oportunidade. Te espero lá.



Exemplo 5:

Já preparou a sua conta bancária para poder receber até R$ 100 mil? 

Se não preparou ainda dá tempo.

Daqui a 2 dias, eu vou te enviar o alerta de compra do ativo digital que tem potencial de multiplicar o seu dinheiro por até 100 vezes em apenas alguns meses.

Seus mil reais têm a chance de virarem cem mil em pouco tempo.

Então marca aí na agenda: dia 18, depois de amanhã, às 19 horas

Te espero lá!



Exemplo 6:

(IMAGEM)
Fala, pessoal! Aqui é o Paulo Wesley 👋

No dia 24/06, em parceria inédita com a Empiricus Research, vamos apresentar ao grande público uma ferramenta inovadora de day trade, algo que você nunca viu igual…

Pra você buscar diariamente ganhos médios de R$ 3.000 com apenas duas operações.

Mas eu resolvi me antecipar ao grande encontro e gravei pra você dois conteúdos especiais sobre o IndicadorX.

O pessoal da Empiricus tá fazendo a edição e vai liberar o vídeo na *terça-feira à tarde, por volta das 15h*. 

Fique atento. Esse primeiro vídeo é fundamental para você avaliar se o IndicadorX é para você.

No vídeo eu estou apresentando a nova ferramenta e também mostro por que é tão simples operar com ela. Vale a pena conferir.

⏰ Por isso, fique atento na terça, às 15h. Até lá!



Exemplo 7:

(IMAGEM)

É hoje, pessoal!

Hoje *às 15h, vou liberar o primeiro conteúdo que eu preparei sobre o IndicadorX*, a ferramenta inovadora de day trade que simplifica o mercado financeiro, em busca de ganhos médios de até R$ 3.000 por dia.

Já tem muita gente ganhando dinheiro com o IndicadorX…

💰 *Ganhos de R$ 100… R$ 500… R$ 1.000… R$ 2.000… R$ 3.000*

Você vai ter a chance de ganhar também. 

Não perca o vídeo, é daqui a pouco 🙌🏻

 
FIM DOS EXEMPLOS DE WHATSAPP LEMBRETE -------------------------------------------
"""
exemplos = exemplos_zapLembrete  
tipo_copy = "CPL/WARMUP",
politica = politicas_meta

plataforma = plataforma_whatsapp
 
instrucao_adicional = """ """

# Exemplos de WHATS WELCOME
exemplos_zapVSL = f"""
INICIO DOS EXEMPLOS DE WHATSAPP VSL -------------------------------------------

Exemplo 1:

O seu lote do primeiro ativo digital da lista que pode fazer R$ 500 em cada se tornar R$ 1 milhão está te esperando…

🔓 *Acabamos de liberar o acesso a lista!*

Muita gente já está com a lista na mão e esperando para receber o lote da primeira.

Se você ver o vídeo ainda hoje e *seguir o passo a passo vai conseguir:*
 

 
Exemplo 2:
 
Bom dia, galera!!! *Hoje vocês vão conhecer a Ogra*, minha amada esposa Graziela.

👨🏻‍💻 Ela também tem um desabafo a fazer, que vai te dar uma boa dimensão de como é a vida de um trader – tanto das coisas boas quanto das ruins.

*Aproveitei o vídeo para já esclarecer muitas dúvidas que surgiram*.

Tenho recebido muitas mensagens de gente interessada e *resolvi antecipar a resposta* à principais perguntas que me fizeram

🕒 O Comunicado Extraordinário da Ogra *sai daqui a pouco,às 15 horas*.

Quem ainda não viu o primeiro vídeo que eu liberei, ainda dá tempo:

Corre lá, depois me diga o que achou, combinado?

Abraço!


 
Exemplo 3:
 
*MAIS DE 40 MIL PESSOAS PRÉ-MATRICULADAS*

Já somos mais de 40 mil pessoas pré-matriculadas e, ao mesmo tempo que isso é bom, também é ruim, já que, como expliquei no vídeo, esta será uma turma PEQUENA. 

Se você ainda não viu o 1º vídeo do Projeto Renda, nele, eu mostrei como eu vou pegar na sua mão e te ajudar a construir 11 novas fontes de renda passiva no seu nome já nas próximas semanas.

*Toque no link para se preparar:*

Nos vemos na segunda.




Exemplo 4: 

*É a SUA VEZ de replicar esse segredo…* 👇🏼

No último vídeo da Semana Quantzed, você vai conferir um plano prático para replicar as estratégias profissionais que os grandes bancos usam.

Em busca de R$ 1.500 toda manhã com a possibilidade real de ganhos ainda maiores ao longo do dia.

Mesmo que você seja iniciante, porque a gente vai operar com ferramentas simples e intuitivas, assim como já fizeram alguns dos nossos alunos *(PRINT ACIMA)*

Com muitas possibilidades reais de ganhos e a matemática está toda do seu lado.

Também preparei uma condição especial para você testar a ferramenta com *4 meses gratuitos de uso da Plataforma Quantzed.*

Não perca mais tempo, toque no link e descubra como ter a chance de começar a buscar lucros ainda hoje:


FIM DOS EXEMPLOS DE WHATSAPP VSL -------------------------------------------
"""
exemplos = exemplos_zapVSL  
tipo_copy = "VSL",
plataforma = plataforma_whatsapp
politica = politicas_meta


instrucao_adicional = """ """

# Exemplos de WHATS WELCOME
exemplos_zap_posVSL = f"""
INICIO DOS EXEMPLOS DE WHATSAPP PÓS-VSL -------------------------------------------

Exemplo 1:

Fala, galera! 👋

Ontem o dia foi cheio por aqui, recebendo os novos alunos da minha nova turma do OGRO Trading System, em parceria com a Empiricus Research.

*Nossa meta: Ganhos médios de R$ 2.000 por dia, AGORA em 2024*:  

Reservei alguns presentes especiais para os alunos, por isso é importante que você veja esta mensagem ainda hoje.

💰 Faço questão de reforçar que construí todo o meu patrimônio com day trade. *Essa é a principal fonte de renda da minha família*.

Sou profissional de verdade, bem diferente dos picaretas que existem por aí e nunca ganharam dinheiro de verdade.

Eu ganhei…bastante. *E quero te ajudar a ganhar também*.

Te vejo no vídeo!


 
Exemplo 2:

*[+1 Prova]: R$ 42 mil em 40 horas*

Foi a grana extra que o Rafael ganhou entre 26/12/2023 e 5/01/2024.

💰 *R$ 42.331 em 5 dias úteis – cerca de 40 horas comerciais*..

Na verdade, "0 horas comerciais" (simplesmente porque o robô fez todo o trabalho)! 

Você também vai ganhar quase 40 salários mínimos em 5 dias com o GL GPT?

Dificilmente.

Mas uma renda média de R$ 238,09 por dia com 4 cliques é mais do que razoável.

*Veja o Gradiente Linear [powered by Generative Pre-Trained Transformer] em ação…

… e caso goste, libere seu 1º login hoje e teste o novo robô do Brasil antes de expirarem as senhas do trial de 30 dias! 


 
Exemplo 3:

*[+1 PROVA]: R$ 25 MIL ATÉ 12H00*

GL GPT 2024 : DEMONSTRAÇÃO AQUI >>>

R$ 25.700 antes da hora do almoço…

… foi a grana que o Raúl fez no dia 26/01/2024.

🙌🏻 *Tudo graças à automação de 4 cliques do GL*.

Você acredita que pode fazer 100x menos do que o Raúl em 24 horas?

Se R$ 238,09/dia parece uma meta razoável, então veja o robô em ação e libere seu 1º login: 

GL GPT 2024: *DEMONSTRAÇÃO AQUI >>>*  


 
Exemplo 4:

16% em 24 horas: compre esse ativo digital ainda hoje *(veja no link)*:  

Eu estou tentando te avisar… a moeda de centavos de dólar já está disparando.

Nas últimas 24 horas ela já entregou mais 16% de valorização.

A chance aqui é real e quem investir nela agora pode sim multiplicar o dinheiro por até 100 vezes em 20 meses.

*Eu explico tudo no neste vídeo* 👉  



FIM DOS EXEMPLOS DE WHATSAPP PÓS-VSL -------------------------------------------
"""
exemplos = exemplos_zap_posVSL  
tipo_copy = "PROMO ÚLTIMA/PÓS-VSL",
plataforma = plataforma_whatsapp
politica = politicas_meta


instrucao_adicional = """  """



# Exemplos de WHATS WELCOME
exemplos_zap_aula = f"""
INICIO DOS EXEMPLOS DE WHATSAPP AULA -------------------------------------------

Exemplo 1:

*SUA NOVA VIDA FINANCEIRA COMEÇA EM MENOS DE 2 DIAS!*

Eu quero que você tenha a oportunidade de testar a plataforma e começar, o quanto antes, a *buscar seus R$ 1.500 por dia ou até mais, logo na abertura do pregão.*

Você viu aqui algumas ferramentas profissionais que usamos para buscar mais renda.

Quer operar com elas sem compromisso algum num primeiro momento?

Fique atento aqui no grupo, que *segunda-feira, às 8h*, passo aqui pra deixar o link de acesso.

Infelizmente as vagas são limitadas porque esse projeto exige uma atenção especial da minha parte. Combinado?

Enquanto isso, aproveite para ver ou rever as aulas:

*Aula 1* 👉 https://emprc.us/76lZOx
*Aula 2* 👉 https://emprc.us/zYWPAA


 
Exemplo 2:

*Não deixe de ver essa aula!*

Seja na abertura do pregão ou ao longo do dia, você tem a possibilidade de lucrar de cara até 1.500 reais ou mais com o projeto Quantzed, com ferramentas que geram alertas com alta probabilidade de acerto.

Assista à aula 2 em que revelo tintim por tintim mais duas estratégias profissionais pra você buscar mais dinheiro diariamente nos pregões.

TOQUE NO LINK:

https://emprc.us/zYWPAA


 
Exemplo 3:

*AULA MAIS IMPORTANTE ATÉ AGORA!*

Mais cedo liberamos a segunda e penúltima aula da Semana Quantzed!

Nela, eu revelei mais duas estratégias profissionais *(e uma terceira extra)* pra você buscar mais dinheiro ao longo do dia.

Você também vai ver como ter a chance de operar como um profissional do mercado usando ferramentas simples que a gente desenvolveu, que automatizam boa parte da análise.

É só tocar no link pra conferir enquanto ela ainda está disponível: 

https://emprc.us/mYnvdx


 
Exemplo 4:

*AULA 2 COMEÇOU!*

Depois de te mostrar a minha principal estratégia pra ganhar dinheiro, chegou a hora de entender quanto você pode ganhar e como isso depende exclusivamente de alguns pontos que vou te apresentar agora.

Está chegando a hora de ter a chance de alcançar a sua independência financeira

Para destravar o seu acesso à aula, é só tocar no link:

https://emprc.us/PSB2cz

FIM DOS EXEMPLOS DE WHATSAPP AULA -------------------------------------------
"""
exemplos = exemplos_zap_aula  
tipo_copy = "",
plataforma = plataforma_whatsapp
politica = politicas_meta

instrucao_adicional_aula = """ 
A AULA é uma mensagem de alerta que informa a audiência sobre novas aulas na comunidade de WhatsApp de uma campanha, têm o objetivo de alertar a audiência a respeito do post de aulas novas, como é possivel ver nos exemplos  
"""



# Exemplos de WHATS cpl
exemplos_zap_cpl = f"""
INICIO DOS EXEMPLOS DE WHATSAPP CPL -------------------------------------------
 
Exemplo 1:

(VÍDEO)
(VÍDEO)

_IndicadorX: *A ferramenta que simplifica o mercado financeiro em busca de ganhos médios de até R$ 3.000 por dia com apenas DUAS operações*_

📍 Entre os dias *18 e 20 de junho*, vou te mostrar no detalhe como funciona essa ferramenta Quant inovadora.

Você tem todas as condições de buscar ganhos médios como os das pessoas que já estão usando a ferramenta: R$ 100 por dia… R$ 300… R$ 500… R$ 1.000… até R$ 3.000! Fique atento às mensagens!

Permaneça na comunidade para receber todos os detalhes dos nossos encontros, inclusive os horários e os links de acesso.

_ATENÇÃO: Fique atento a fraudes. Confie somente nos administradores do grupo. Não vamos solicitar dados no privado, como conta bancária e transferência de valores (PIX)._



 
Exemplo 2:

Fala, galera! André Machado falando…

*Daqui a pouco vamos liberar o Comunicado Extraordinário que eu gravei aqui na Ogro Cave*.

🕒 O horário programado *é 15h*, por isso peço que fique atento às mensagens.

_*Ganhos médios de R$ 2.000 por dia ainda em 2024, essa é a nossa meta*._

Será que você consegue gerar uma renda adicional dessa magnitude com a minha ajuda?

Assim que o pessoal do audiovisual da Empiricus finalizar a edição do vídeo, eu te aviso.

Até lá!



Exemplo 3:

Bom dia, galera!!! *Hoje vocês vão conhecer a Ogra*, minha amada esposa Graziela.

👨🏻‍💻 Ela também tem um desabafo a fazer, que vai te dar uma boa dimensão de como é a vida de um trader – tanto das coisas boas quanto das ruins.

*Aproveitei o vídeo para já esclarecer muitas dúvidas que surgiram*.

Tenho recebido muitas mensagens de gente interessada e *resolvi antecipar a resposta* à principais perguntas que me fizeram

🕒 O Comunicado Extraordinário da Ogra *sai daqui a pouco,às 15 horas*.

Quem ainda não viu o primeiro vídeo que eu liberei, ainda dá tempo: https://emprc.us/n2VVYK 

Corre lá, depois me diga o que achou, combinado?

Abraço!



Exemplo 4:

*ESTÁ CHEGANDO A HORA! É HOJE, ÀS 19H!*

Passando para lembrar vocês que hoje, às 19 horas, vai ao ar a primeira aula da *Semana Quantzed*. 

Eu vou direto ao ponto, começando direto pela estratégia que eu considero a mais importante de todas:

Aquela que te dá a possibilidade diária de colocar no bolso até R$ 1.500 logo de manhã, na abertura do pregão.

Você abre e fecha a operação muitas vezes em menos de 10 minutos, por volta das 10 horas da manhã.

Tá preparado? Já ativa o alarme porque eu tenho certeza que ninguém quer chegar atrasado.

Até daqui a pouco!




Exemplo 5:

(IMAGEM)

Fala, pessoal! Aqui é o Paulo Wesley 👋🏻

*Acabei de liberar mais um vídeo* antes do nosso encontro final no dia 24 de junho: https://emprc.us/3XxkBg 

Vai ficar pouco tempo no ar, então recomendo que veja rápido.

*No vídeo, eu respondo as principais dúvidas* que me mandaram sobre como é possível ter ganhos médios de até 3.000 reais por dia com o IndicadorX, realizando apenas duas operações diárias. *Olha o exemplo do Marcus… ele fez 950 pontos no dia* 📈

Com 1 minicontrato, ele receberia 190 reais com apenas uma operação. Ou R$ 3.040 com 16 minicontratos.

E você, quanto pode fazer? Qual é o mínimo de capital que você precisa ter para operar?

↘️ As respostas para essas e outras perguntas estão no segundo vídeo sobre o IndicadorX! https://emprc.us/3XxkBg  Até lá! 

 
FIM DOS EXEMPLOS DE WHATSAPP CPL -------------------------------------------
"""
exemplos = exemplos_zap_cpl  
tipo_copy = "CPL",
plataforma = plataforma_whatsapp
politica = politicas_meta

instrucao_adicional = """ """



# Exemplos de WHATS WELCOME
exemplos_zap_pos_cpl = f"""
INICIO DOS EXEMPLOS DE WHATSAPP PÓS CPL -------------------------------------------
 
Exemplo 1:

(IMAGEM)

Fala, pessoal! 👋

*Já viram o segundo vídeo* que eu preparei sobre o IndicadorX? 
https://emprc.us/YY9Y9M  

É curtinho, vale a pena dar uma olhada no fim de semana.

🚀 Porque, *na segunda-feira, vamos liberar o IndicadorX* aos interessados que desejam buscar mais renda – até R$ 3.000 por dia – com a nova ferramenta Quant que simplifica o mercado financeiro em três informações:

Sinais… Velocidade… Fluxo… e nada mais!

↘️ O vídeo está aqui *esclarecendo as principais dúvidas* do IndicadorX, corre lá: https://emprc.us/YY9Y9M 

Se puder, deixe o seu comentário. Abraço!


 
Exemplo 2:

(IMAGEM)

*Tá chegando o grande dia…*

O que você acha de *buscar até R$ 3.000 por dia*, na média, com uma nova ferramenta quant que simplifica o mercado financeiro, para que até quem está começando no day trade consiga operar?

Isso mudaria a vida financeira da sua família? Pois essa possibilidade existe. *No dia 24/06, segunda-feira, você vai ver*.

🔥 Enquanto o dia não chega, não se esqueça de ver os conteúdos que eu preparei:

*[VÍDEO 1] O IndicadorX é para você?*:
⇒ https://emprc.us/RJYIuF 

*[VÍDEO 2] A resposta do IndicadorX às suas principais dúvidas*: 
⇒ https://emprc.us/N1KWzH  

O IndicadorX pode te dar uma nova fonte de renda em 2024, e eu quero te ajudar nesse objetivo.

Já tem muita gente tendo a chance de ganhar dinheiro com a ferramenta…

_*GANHOS TOTAIS DO DIA:  R$ 310,00… R$ 1.550,00… R$ 3.100,00*_

Você pode ser o próximo 👋




Exemplo 3:

(IMAGEM)

Sua vida financeira não ficaria muito melhor com uma chance de renda adicional como esta?

✔️ *1 minicontrato: R$ 260,00*
✔️ *5 minicontratos: R$ 1.300,00*
✔️ *12 minicontratos: R$ 3.120,00*

Tenho certeza de que sim, por isso desenvolvi o IndicadorX. E quero te ajudar a buscar ganhos médios como esses, agora, em 2024.

🕖 *Amanhã, às 19h, vou te mostrar direitinho como funciona*.

Recomendo apenas que você veja este conteúdo antes. Preparei alguns conteúdos importantes para que você venha empolgado na segunda-feira

➡️ *[VÍDEO 1] O IndicadorX é para você?*: https://emprc.us/0KLe4X 

➡️ *[VÍDEO 2] A resposta do IndicadorX às suas principais dúvidas*: https://emprc.us/Bh65eR  

Tô te esperando.
 
FIM DOS EXEMPLOS DE WHATSAPP PÓS CPL -------------------------------------------
"""
exemplos = exemplos_zap_pos_cpl 
tipo_copy = "CPL",
plataforma = plataforma_whatsapp
politica = politicas_meta

instrucao_adicional_zap_pos_cpl = """Não se prenda ao nome IndicadorX. Isso que forneci são apenas exemplos de COPY PÓS CPL de um projeto chamado IndicadorX."""



# Exemplos de WHATS WELCOME
exemplos_zap_countdown = f"""
INICIO DOS EXEMPLOS DE WHATSAPP COUNTDOWN -------------------------------------------
 
Exemplo 1:

(IMAGEM)

Oi, pessoal! 👋

*Hoje é o último dia para você entrar na Primeira Turma Oficial do IndicadorX, em busca de ganhos médios de R$ 3.000 por dia*.

Você ainda pode ver como isso vai funcionar através deste link: https://emprc.us/TtPzf2 

Depois, o plano é me dedicar exclusivamente a todos que aceitaram participar comigo desta nova jornada por mais renda.

😱 *Será que você também é capaz de buscar em média até R$ 3.000 por dia?*

Eu acredito que SIM e vou te dar todas as condições para te ajudar a cumprir essa meta ainda em 2024. 

*Tô te esperando* ➡️ https://emprc.us/TtPzf2 

_Disclaimer: Ganho passado não é garantia de ganho futuro. Investimentos têm riscos._


 
Exemplo 2:

(IMAGEM)

🚨 *ÚLTIMO DIA!* https://emprc.us/oagwAi 

Fala, pessoal. Sabe por que eu gosto de operar?

Porque isso me dá mais liberdade, já que o mercado financeiro me permite alavancar potenciais ganhos e diluir riscos.

📈 Fazer 930 pontos no índice, por exemplo, significa um lucro na operação de R$ 186,00 por minicontrato.

Bastaria operar com *apenas 17 minicontratos para bater a nossa meta de até 3.000 reais nesse dia*.

E, como você vai ver, isso é perfeitamente possível – e pode acontecer muito mais rápido do que você imagina, ainda em 2024.

🔥 O IndicadorX é essencial nesse processo.

Estamos próximos de formar a nossa Primeira Turma Oficial do IndicadorX – o que pode acontecer já nas próximas horas.

↘️ *Esta é sua última oportunidade de buscar mais renda no mês*: https://emprc.us/oagwAi 

_Ganhos passados não são garantia de ganhos futuros. Investimentos têm riscos e podem causar perdas ao investidor._




Exemplo 3:

*Será que você também é capaz de ganhar em média R$ 3.000 por dia com o IndicadorX?*

⏱️ Hoje é o seu *ÚLTIMO DIA* para descobrir: https://emprc.us/C08mYQ 

Eu faço questão de estar ao seu lado para te ajudar a cumprir esse objetivo ainda em 2024.

Seja acompanhando ao seu lado os alertas do IndicadorX …

Seja operando por você, sem que você precise tomar nenhuma decisão de entrada ou saída da operação.

Pode inclusive testar as duas maneiras de operar e avaliar qual funciona melhor pra você. 

Tá preparado? Eu tô te esperando… 👊🏻

É só hoje *até a meia-noite* ou até esgotarem as últimas vagas.

Clica aqui no link e venha conferir como *fazer parte da Primeira Turma Oficial do IndicadorX*: 

Só tá faltando você: https://emprc.us/C08mYQ 



Exemplo 4:

Fala, pessoal! 

Quero agradecer a todos que estão confiando no IndicadorX e aceitaram o desafio de fazer parte da nossa Primeira Turma Oficial: https://emprc.us/JLiswk 

💥 *Você já sabe o nosso objetivo: até R$ 3.000 por dia, com as operações do Indicador*

Mesmo começando com um capital pequeno – a ideia é crescer esse capital pouco a pouco…

E mesmo sendo iniciante. _*Eu vou te mostrar o passo a passo do início, com tudo que você precisa para se desenvolver como trader.*_

Posso inclusive *OPERAR POR VOCÊ*, sem cobrar nada adicional por isso

Se você ainda não garantiu a sua vaga, tem até a meia-noite para decidir.

➡️ *Pode clicar neste link* para conhecer o projeto: https://emprc.us/JLiswk 
 
FIM DOS EXEMPLOS DE WHATSAPP COUNTDOWN -------------------------------------------
"""
exemplos = exemplos_zap_countdown 
tipo_copy = "COUNTDOWN",
plataforma = plataforma_whatsapp
politica = politicas_meta

instrucao_adicional_zap_countdown = """Não se prenda ao nome IndicadorX. Isso que forneci são apenas exemplos de COPY de um projeto chamado IndicadorX."""



# Exemplos de WHATS WELCOME
exemplos_zap_carrinho = f"""
INICIO DOS EXEMPLOS DE WHATSAPP CARRINHO ABANDONADO -------------------------------------------
 
Exemplo 1:

Olá! Este é um recado da Equipe Empiricus.
 
Ontem foram encerradas as vagas para a Primeira Turma Oficial do *IndicadorX*, a ferramenta inovadora para buscar ganhos médios de até R$ 3.000 por dia.

Mesmo começando com pouco capital…

🔥 E mesmo sendo iniciante, *com todo o passo a passo que o analista CNPI-T Paulo Wesley vai dar pra você*.

Só que uma coisa nos deixou preocupados…

Fomos avisados de que você se interessou pela ideia de construir uma nova fonte de renda, mas que por algum motivo não finalizou seu cadastro.

🙌🏻 *Então gostaríamos de lhe dar uma última oportunidade*. 

*Você tem 7 dias de acesso sem compromisso para testar o IndicadorX* e conferir se a nova ferramenta atende suas expectativas.

Queremos muito que você também tenha a chance de ganhar dinheiro com essas operações, realizadas com a estatística toda do seu lado.

Por isso, *sua vaga ainda está reservada, mas com validade apenas até HOJE*.

Você só precisa finalizar seu cadastro para ter direito a todas as aulas que o Paulo preparou e a todos os benefícios do nosso pacote, como os 3 meses gratuitos do Robô de Operações e da Sala de Trade ao Vivo.

⏱️ *Aproveite que é só hoje!*

Paulo Wesley e todos os alunos do Treinamento IndicadorX estão te esperando. *Só falta finalizar sua inscrição*: https://emprc.us/jqaEUG   

Abraço!



Exemplo 2:

*VAMOS CANCELAR O SEU ACESSO*

Vimos que se interessou pelo ativo digital de centavos que pode multiplicar o seu dinheiro por 100x.

Pedimos que se manifeste caso ainda tenha interesse.

Já tiramos todos os links do ar, mas para você conseguimos abrir uma exceção.

Você tem apenas algumas horas para confirmar o seu interesse.

Caso contrário, passaremos sua vaga para outro interessado.

*CONFIRME SEU INTERESSE AQUI:* https://emprc.us/MeqIEk 



Exemplo 3:

*Seu nome foi citado.*

Ontem tiramos a lista de 5 moedas para buscar R$ 1 milhão do ar, mas seu nome foi citado na lista de interessados em conhecer essas criptomoedas.

Por isso, conseguimos segurar o link para você até a meia-noite de hoje.

Se você ainda tiver interesse de ver a lista que pode fazer com que R$ 500 investidos em cada moeda se torne R$ 1 milhão, clique no link: https://emprc.us/PGP7Ze 



Exemplo 4:

*VAMOS CANCELAR O SEU ACESSO*

Vimos que se interessou pelo ativo digital de centavos que pode multiplicar o seu dinheiro por 100x.

Pedimos que se manifeste caso ainda tenha interesse.

Já tiramos todos os links do ar, mas para você conseguimos abrir uma exceção.

Você tem apenas algumas horas para confirmar o seu interesse.

Caso contrário, passaremos sua vaga para outro interessado.

*CONFIRME SEU INTERESSE AQUI:* https://emprc.us/MeqIEk 
 
FIM DOS EXEMPLOS DE WHATSAPP CARRINHO ABANDONADO -------------------------------------------
"""
exemplos = exemplos_zap_carrinho
tipo_copy = "CARRINHO ABANDONADO",
plataforma = plataforma_whatsapp
politica = politicas_meta

instrucao_adicional_carrinho = """Não faça agradecimentos ou qualquer coisa relacionada ao final da mensagem. Apenas alerte o usuário."""




#Exemplo genérico COPY INSTAGRAM

# Exemplos de Copy Instagram
exemplos_instagram = f"""
INICIO DOS EXEMPLOS DE INSTAGRAM PROP  -------------------------------------------

Exemplo 1)
OPORTUNIDADE! Empresa vai revelar o nome de 5 moedas para investir R$ 500 em cada e buscar R$ 1 milhão.



Exemplo 2)
E você, compra ou vende Cosan?

🎙️ Matheus Spiess, João Piccioni e Larissa Quaresma no Empiricus Podca$t. Assista/ouça todas as quintas no YouTube/Spotify da Empiricus.

#investimentos #cosan #csan3 #ações #acoes #ondeinvestir #comoinvestir #investidor #economia #b3



Exemplo 3)
Fuja da inflação brasileira. Acesse o link da bio.

#inflação #inflacao #inflaçãonobrasil #dinheiro #real #reais #economia #investimentos #moeda #economiabrasileira



Exemplo 4)
Comente DÓLAR para receber mais informações sobre a oportunidade.

#dolar #rendaemdolar #dólar #dinheiro #finanças #vidafinanceira #rendaextra #renda #estadosunidos #eua



Exemplo 5)

Ouvi um influencer dizer por aí que, para você ser uma pessoa rica, precisa ter pelo menos 6 fontes de renda.
Pois bem, vou revelar 11:

  Dividendos;
  Milhas;
  Fundos Imobiliários;
  Fundos de investimento;
  Renda Fixa;
  Ações;
  Previdência;
  Small Caps;
  Investimentos internacionais;
  Criptomoedas;
  Opções.

Quer descobrir como "plugar" essas 11 fontes de renda passiva na sua conta bancária?

Comente "Renda" e olhe o seu direct.
 
FIM DOS EXEMPLOS DE INSTAGRAM PROP -------------------------------------------
"""
exemplos = exemplos_instagram
tipo_copy = "PROP",
plataforma = plataforma_instagram
politica = politicas_meta
instrucao_adicional = """ """


#Exemplo genérico COPY INSTAGRAM

# Exemplos de Copy Instagram
exemplos_instagramReels = f"""
INICIO DOS EXEMPLOS DE INSTAGRAM REELS PROP  -------------------------------------------

Exemplo 1)
Os 5 Bilionários do Mundo das Criptomoedas

Changpeng Zhao

Apesar dos desafios legais enfrentados, o CEO e fundador da Binance, Changpeng Zhao, continua a liderar como a pessoa mais rica no mundo cripto.

Até o ano passado, CZ possuía um patrimônio líquido total de US$ 37,2 bilhões — registrando um crescimento anual de US$ 24,6 bilhões.

Brian Armstrong

Em segundo lugar, está o Brian Armstrong, cofundador da Coinbase, uma das maiores corretoras de criptomoedas dos EUA, detendo 19% da companhia. Seu patrimônio líquido estimado é de 11,5 bilhões de dólares.

Chris Larsen

Em terceiro, o Cofundador e presidente do protocolo de pagamentos em criptomoedas Ripple, Chris Larsen possui um patrimônio líquido de 6 bilhões de dólares.

      4 e 5. Cameron e Tyler Winklevoss

Além deles, os gêmeos são os fundadores da corretora de criptomoedas Gemini, e cada um deles possui um patrimônio líquido estimado de 4,3 bilhões de dólares.

Quer ter a chance de ser um milionário do mundo cripto?

Comente "EU QUERO" para poder conhecer as 5 MOEDAS PARA BUSCAR R$ 1 MILHÃO!

 
FIM DOS EXEMPLOS DE INSTAGRAM REELS PROP -------------------------------------------
"""
exemplos = exemplos_instagram
tipo_copy = "PROP",
plataforma = plataforma_instagram
politica = politicas_meta
instrucao_adicional = """ """



#Exemplo genérico COPY INSTAGRAM
# Exemplos de Copy Instagram
exemplos_instagramCarrossel = f"""
INICIO DOS EXEMPLOS DE INSTAGRAM CARROSSEL PROP  -------------------------------------------

Exemplo 1)
Comente “EU QUERO” para poder acessar a lista com as 5 moedas!

#crypto #bitcoin #btc #criptomoedas #bullmarket #investimentos #ethereum #halving

Exemplo 2)
Esqueça a máxima do Bitcoin: criptomoeda de US$ 0,50 pode disparar para até US$ 50 em 20 meses; projeta especialista


Veja como você pode transformar sua realidade financeira…

—-----------------------------


O Bitcoin começou 2024 com tudo. 


Em pouco mais de três meses, o ativo digital mais conhecido do planeta conseguiu superar sua máxima histórica, e chegar aos US$ 72 mil. 


—-----------------------------


No ano, a criptomoeda sobe mais de 50% e, segundo especialistas, ainda tem espaço para até dobrar o dinheiro investido nesse ciclo.
No entanto, a valorização do Bitcoin fica muito para trás se comparada à de outros ativos digitais menores do que ele.


—-----------------------------


Para você que não sabe, o Bitcoin é apenas o principal ativo digital dentre os mais de 10 mil existentes. 
Ele funciona como uma espécie de ‘maestro’ desse mercado, puxando para baixo a cotação das outras moedas quando ele cai e para cima quando ele sobe.


—-----------------------------
A diferença é que esses movimentos acontecem nas moedas menores em uma intensidade muito maior do que no Bitcoin.
Por exemplo: existe uma criptomoeda pequena, desconhecida e barata que hoje custa cerca de 50 centavos.
—-----------------------------
Enquanto o Bitcoin valorizou 50% no ano, essa moeda já multiplicou o dinheiro investido por mais de 4 vezes.
É uma diferença brutal que pode ficar ainda maior daqui para frente. 


—-----------------------------
Segundo o head do departamento de criptomoedas, Valter Rebelo, essa moeda ainda tem espaço para saltar até 100 vezes nos próximos meses.
“Quem investir nessa moeda ainda em março vai poder buscar até R$ 100 mil com apenas R$ 1 mil investidos”, disse o especialista.


—-----------------------------


Mas não precisa ficar desesperado se você ainda não investe na moeda. 


Afinal, ela ainda vale apenas 50 centavos, e apresenta potencial para multiplicar seu investimento por até 100 vezes em 20 meses. 


—-----------------------------


Além disso, você terá a oportunidade de receber gratuitamente um alerta de compra desta moeda no dia 18, às 19 horas. 


Para receber este alerta, basta comentar "EU QUERO" para se cadastrar gratuitamente. 
https://emprc.us/oPlRBX

Exemplo 3)


 
FIM DOS EXEMPLOS DE INSTAGRAM CARROSSEL PROP -------------------------------------------
"""
exemplos = exemplos_instagram
tipo_copy = "PROP",
plataforma = plataforma_instagram
politica = politicas_meta
instrucao_adicional = """ """

# Exemplos de Copy Telegram
exemplos_telegram = f"""
INICIO DOS EXEMPLOS DE TELEGRAM PROP  -------------------------------------------

Exemplo 1)
💰1 milhão de reais na sua conta investindo R$ 500 em cada uma dentro de uma lista de 5 moedas…

Essa é a meta com a nossa nova lista de ativos alternativos.

Da última vez que a gente montou uma lista com esse potencial, R$ 3.500 investidos em apenas uma moeda viraram até R$ 1 milhão.

Agora, esse mercado está ainda mais quente e os retornos estão sendo ainda maiores…🚀

Quem investir R$ 500 em cada uma dessas 5 moedas vai ter a chance real de conquistar R$ 1 milhão nos próximos meses.👏🏻

Quer ter a chance de acessar as moedas dessa lista?

🚨Basta clicar no link abaixo e se cadastrar:

https://emprc.us/ekcJsp

É de graça.

"Retornos passados não são garantia de lucros futuros. Investimentos envolvem riscos e podem causar perdas ao investidor."

Exemplo 2)
Tá impressionado com a valorização do Bitcoin?
Pois é, a maior moeda digital do mercado finalmente atingiu a máxima histórica! 🚀

Só no último mês, o Bitcoin já valorizou mais de 55%.

No entanto, essa valorização é minúscula se comparada à nossa maior aposta neste mercado, que custa menos de 1 dólar.

Veja só:
Esse ativo está pronto para fazer R$1.000 virarem até R$100 mil.

Quer conhecer essa moeda que custa centavos e tem potencial para multiplicar o seu dinheiro por até 100 vezes nos próximos meses? 

Basta clicar aqui: https://emprc.us/3L4WCh



"Retornos passados não são garantia de lucros futuros. Investimentos envolvem riscos e podem causar perdas ao investidor."

Exemplo 3)
💸Os Apps que você tem instalado no seu celular, multiplicam o seu dinheiro em até 3,85x? 💸

Aposto que não.

Entenda: Se você tiver R$1.000, ele se transforma em R$3.850
Se você tiver R$ 5.000 ele se transforma em R$19.250.

Mas, temos uma novidade: Queremos te mostrar uma ferramenta que se parece com um App, e que tem muito potencial.

Foram 285% de retorno nos últimos seis meses. Você pode buscar ter os mesmos resultados com uma ferramenta automática, que ‘copia e cola’ os trades de Eduardo Garufi, que soma mais de 10 anos no mercado, transformando alunos em milionários.

É só instalar a ferramenta e, com alguns cliques, você já pode ter o resultado de um trader profissional.

E qual o diferencial? 

A grande beleza da estratégia de Garufi é que você não precisa que as criptomoedas subam para ter a chance de ganhar dinheiro. Assim, você pode fazer operações que dão lucro na valorização e na desvalorização dos ativos.

INSCREVA-SE NO GRUPO DE INTERESSADOS GRATUITAMENTE 

Exemplo 4)
Como está aproveitando o feriado?

E se você aproveitasse para ter a chance de buscar R$ 1 milhão em apenas 19 meses com ativos digitais?

Nós estamos montando um grupo de pessoas que vão ter a chance de acessar uma lista com 5 moedas alternativas com potencial de crescimento exponencial a partir de 2024.

Moedas como essas já fizeram, no passado, quantias como 4 mil reais se transformarem em até 1 milhão de reais.

Tudo que você precisa fazer agora é clicar no link abaixo e deixar o seu e-mail:

https://emprc.us/VEIwn8

Não perca essa chance!

"Retornos passados não são garantia de lucros futuros. Investimentos envolvem riscos e podem causar perdas ao investidor."
 
FIM DOS EXEMPLOS DE TELEGRAM PROP -------------------------------------------
"""
exemplos = exemplos_telegram
tipo_copy = "PROP",
plataforma = plataforma_telegram
politica = politicas_meta
instrucao_adicional = """ """

def validador(copy):
    # Prompt Solução (Sem tags) 
    prompt = f"""
    Você é um redator especialista. Sua tarefa é ajudar a mim, um colega escritor, a avaliar o poder de persuasão do meu texto usando uma fórmula chamada 'Os Quatro U's': Urgência, Utilidade, Exclusividade e Ultraespecificidade.

    Passos a Seguir:
    Solicitar Cópia: Peça para eu fornecer a cópia para avaliação.
    Aguarde Resposta: Aguarde minha resposta com a cópia.

    Avalie com Base nos Quatro U's:
    Urgência (0-25): Avalie como a cópia cria um senso de urgência, estimulando uma ação imediata ou transmitindo urgência ao público.
    Utilidade (0-25): Avalie a utilidade da cópia. Verifique se ela fornece informações valiosas, aborda pontos problemáticos ou oferece benefícios claros ao público-alvo.
    Exclusividade (0-25): Determine a exclusividade da cópia. Avalie o quão distinta e original é a mensagem ou proposta em comparação com o conteúdo existente ou concorrentes. Verifique se ela se destaca e chama a atenção.
    Ultraespecificidade (0-25): Analise a ultraespecificidade da cópia. Verifique o quão bem definidas e detalhadas são as informações, considerando se elas fornecem evidências, contexto ou instruções específicas para apoiar afirmações ou proposições.
    Pontuação:

    Forneça pontuações para Urgência, Utilidade, Exclusividade e Ultraespecificidade.
    Calcule a pontuação total somando as pontuações individuais.
    Traduza a pontuação total em uma nota alfabética (A a F) com base em uma escala de 0 a 100.

    Sugestões para Melhoria:

    Ofereça sugestões específicas sobre como melhorar as pontuações em cada uma das quatro áreas.
    Faça quaisquer perguntas que você acredita que possam ajudar a tornar as sugestões mais valiosas.
    Se você tiver acesso a plug-ins, ative pesquisas por palavras-chave, manchetes recentes ou outras informações relevantes para avaliar melhor a Exclusividade e a Utilidade da cópia em comparação ao conteúdo existente.
    
    PERGUNTA DO USUÁRIO:
    COPY que você deve analsiar: {copy}. 
    """
    response = model.generate_content(prompt)
    return (formatar_texto(response))


#Lógica genérica:
# Enquanto nota for menor que algo, continue criando novas COPIES
def resultado(nota_copy):
    # Prompt Solução (Sem tags) 
    prompt = f"""
    Você é um especialista em identificar notas de COPIES. Leia essa avaliação de Copy baseada em John Forde entre os sinais <>:

    <{nota_copy}>

    Siga estas instruções à risca:

    - Retorne a letra (nota) que foi atribuída à minha COPY.
    - Não dê notas como: A-, B+. Apenas respostas sem sinais, como: A, B.
    - Não me diga mais nada, apenas retorne a letra da nota.
    
    Exemplo de retorno: a, b, c, d, e, f

    PERGUNTA DO USUÁRIO:
    Qual a letra(NOTA) da minha COPY?
    """

    response = model.generate_content(prompt)
    return (formatar_texto(response))


def recriacao(tipo_copy, exemplos, exemplo_copy, novo_prompt, plataforma, politica, copy, nota_copy):
    # Prompt Solução (Sem tags)
    prompt = f"""
    Criação de Tipo de Copy: {tipo_copy}

    Atue como um publicitário especializado na criação de campanhas digitais para venda de produtos e serviços na internet. Você é um especialista na criação de copies utilizando o framework Copy Canvas, desenvolvido por Roberto Altenhoffen, CMO da Empiricus Research.

    Este é um resumo sobre a estrutura de uma Copy:
    ???{exemplo_copy}???

    O usuário está estruturando um projeto e precisa de ajuda para criar o Copy. Sua missão é auxiliar o usuário a criar uma boa mensagem/anúncio para {tipo_copy}.

    Também será disponibilizado um conjunto de exemplos e inputs criativos e as descrições do {tipo_copy} entre ;;;.
    ;;;{exemplos};;;

    Instruções:
    1. Utilize a ESTRUTURA COPY e sua base interna de conhecimento como referências criativas e instrucionais.
    2. Leia os EXEMPLOS DE {tipo_copy}. Compare o input criativo do exemplo com o input criativo do usuário e utilize os exemplos como referência, adaptando-os ao input criativo do usuário.
    3. Utilize os EXEMPLOS DE {tipo_copy} como referência criativa, de formato e de tamanho, pois são comprovadamente eficientes.
    4. Não faça sugestões de novos inputs criativos. Dê apenas as descrições de {tipo_copy} para o input do usuário e não fale sobre outros aspectos do Copy ou Copy Canvas.
    5. A resposta deve estender o conceito do input criativo do usuário. Todas as outras informações devem ser apenas referências criativas e instrucionais.

    Você está construindo uma COPY para essa plataforma: {plataforma}
    Instruções adicionais: Essa COPY está sendo refeita. O usuário já fez, mas não recebeu uma nota muito boa. Essa é a COPY que ele fez entre <>
    <{copy}>

    Refaça com as sugestões que foram propostas entre ????
    ??{nota_copy}??

    TENTE MANTER O MESMO TAMANHO E A MESMA ESTRUTURA DA COPY entre <>. Foque em modificar apenas o que foi sugerido entre ????
    Políticas de bom uso que você deve seguir ao criar a COPY: {politica}
    - Não crie COPIES que vão contra as políticas de bom uso
    - Não crie COPIES se o Copy Canvas e informações do criativo/produto forem contra as políticas de bom uso.
    SEMPRE ESCREVA EM PORTUGUÊS
    RETORNE APENAS A COPY, NÃO RETORNE O QUE VOCE MUDOU, O QUE FOI IMAGINOU OU QUAIS SUGESTÕES VOCE SEGUIU. RETORNE APENAS A COPY DE USO.    
    
    PERGUNTADO USUÁRIO:
    Gere um uma copy seguindo esse copy canvas: {novo_prompt}"""
    response = model.generate_content(prompt)
    return (formatar_texto(response))


def rodar(criativo):
    print("rodou")
    audiencia = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'AUDIÊNCIAS', 'A', formato_saida_audiencia, instrucao_adicional, exemplos_audiencia, exemplos_guia, criativo))
    problema = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'PROBLEMA/Oportunidade', 'A1', formato_saida_problema, instrucao_adicional, exemplos_problema, exemplos_guia, criativo))
    solucao = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'SOLUÇÕES/JORNADAS', 'A2', formato_saida_solucao, instrucao_adicional, exemplos_solucao, exemplos_guia,criativo))
    lead = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'LEAD', 'A3', formato_saida_lead, instrucao_adicional, exemplos_lead, exemplos_guia,criativo))
    emocao = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'EMOÇÃO', 'B1', formato_saida_emocao, instrucao_adicional, exemplos_emocao, exemplos_guia,criativo))
    nudge = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'NUDGE', 'B2', formato_saida_nudge, instrucao_adicional, exemplos_nudge, exemplos_guia,criativo))
    bigIdeia = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'BIG IDEIA', 'B3', formato_saida_big_ideia, instrucao_adicional, exemplos_bigidea, exemplos_guia,criativo))
    prova =(run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'PROVAS', 'C1', formato_saida_prova, instrucao_adicional, exemplos_prova, exemplos_guia,criativo))
    objecoes =(run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'OBJEÇÕES', 'C2', formato_saida_objecoes, instrucao_adicional, exemplos_objecoes, exemplos_guia,criativo))
    oferta = (run(estrutura_copycanvas, conceitos_auxiliares_copycanvas, 'PROPOSTA/OFERTA', 'C3', formato_saida_oferta, instrucao_adicional, exemplos_oferta, exemplos_guia,criativo))
    novo_prompt = f"""
            Audiência:
            {audiencia}

            Problema:
            {problema}

            Solução:
            {solucao}

            Emoção:
            {emocao}

            Nudge:
            {nudge}

            Objeções:
            {objecoes}

            Oferta:
            {oferta}

            Big Idea:
            {bigIdeia}

            Lead:
            {lead}

            Prova:
            {prova}

            """
    novo_prompt = (formatar_texto(novo_prompt))
    return novo_prompt
    

def gerar_copy(novo_prompt, tipo_comunicacao):
    print("gerando copy")

    #Case Tipo Copy
    match tipo_comunicacao:
        case 'Email welcome':
            exemplos = exemplos_emailWelcome
            tipo_copy = 'Welcome'
            plataforma = plataforma_email
            politica = politicas_google
            instrucao_adicional = ''

        case 'Email warmup':
            exemplos = exemplos_emailWarmup
            tipo_copy = 'WARMUP'
            tipo_copy = 'PROMO ABERTURA DE CARRINHO/VSL'
            plataforma = plataforma_email
            politica = politicas_google
            instrucao_adicional = ''

        case 'Email promo':
            exemplos = exemplos_emailPromo
            tipo_copy = 'PROMO'
            plataforma = plataforma_email
            politica = politicas_google
            instrucao_adicional = ''

        case 'Email promo inicial':
            exemplos = exemplos_emailPromoInicial
            tipo_copy = 'PROMO ABERTURA DE CARRINHO/VSL'
            plataforma = plataforma_email
            politica = politicas_google
            instrucao_adicional = ''

        case 'Email promo ultima':
            exemplos = exemplos_emailPromoUltima
            tipo_copy = 'PROMO ÚLTIMA'
            plataforma = plataforma_email
            politica = politicas_google
            instrucao_adicional = ''

        case 'zap aula':
            exemplos = exemplos_zap_aula
            instrucao_adicional = instrucao_adicional_aula
            tipo_copy = 'PROMO'
            plataforma = plataforma_whatsapp
            politica = politicas_meta

        case 'zap carrinho':
            exemplos = exemplos_zap_carrinho
            instrucao_adicional = instrucao_adicional_carrinho
            tipo_copy = 'CARRINHO ABANDONADO'
            plataforma = plataforma_whatsapp
            politica = politicas_meta

        case 'zap countdown':
            exemplos = exemplos_zap_countdown
            instrucao_adicional = instrucao_adicional_zap_countdown
            tipo_copy = 'COUNTDOWN'
            plataforma = plataforma_whatsapp
            politica = politicas_meta

        case 'zap cpl':
            exemplos = exemplos_zap_cpl
            tipo_copy = 'CPL'
            plataforma = plataforma_whatsapp
            politica = politicas_meta
            instrucao_adicional = ''

        case 'zap pos cpl':
            exemplos = exemplos_zap_pos_cpl
            instrucao_adicional = instrucao_adicional_zap_pos_cpl
            plataforma = plataforma_whatsapp
            politica = politicas_meta
            tipo_copy = 'PROMO'

        case 'zap lembrete':
            exemplos = exemplos_zapLembrete
            tipo_copy = 'PROMO'
            plataforma = plataforma_whatsapp
            politica = politicas_meta
            instrucao_adicional = ''

        case 'zap vsl':
            exemplos = exemplos_zapVSL
            tipo_copy = 'PROMO ABERTURA DE CARRINHO/VSL'
            plataforma = plataforma_whatsapp
            politica = politicas_meta
            instrucao_adicional = ''

        case 'zap pos vsl':
            exemplos = exemplos_zap_posVSL
            plataforma = plataforma_whatsapp
            politica = politicas_meta
            tipo_copy = 'PROMO'
            instrucao_adicional = ''

        case 'instagram':
            exemplos = exemplos_instagram
            tipo_copy = 'PROMO'
            plataforma = plataforma_instagram
            politica = politicas_meta
            instrucao_adicional = ''

        case 'instagram carrosel':
            exemplos = exemplos_instagramCarrossel
            tipo_copy = 'PROMO'
            plataforma = plataforma_instagram
            politica = politicas_meta
            instrucao_adicional = ''

        case 'instagram reels':
            exemplos = exemplos_instagramReels
            tipo_copy = 'PROMO'
            plataforma = plataforma_instagram
            politica = politicas_meta
            instrucao_adicional = ''

        case 'telegram':
            exemplos = exemplos_telegram
            tipo_copy = 'PROMO'
            plataforma = plataforma_telegram
            instrucao_adicional = ''
            politica = politicas_google

    copy = run_2(tipo_copy, instrucao_adicional, exemplos, exemplo_copy, novo_prompt, plataforma, politica)
    nota_copy = validador(copy)
    resultado_letra = resultado(nota_copy)
    resultado_letra = re.sub(r'[^a-z]', '', resultado_letra.strip().lower())
    resultado_letra = resultado_letra.strip().lower()
    print("primeiro resultado letra:", resultado_letra)

    while resultado_letra != 'a' and resultado_letra != 'b' and resultado_letra != 'c':
        copy = recriacao(tipo_copy, exemplos, exemplo_copy, novo_prompt, plataforma, politica, copy, nota_copy)
        nota_copy = validador(copy)
        resultado_letra = resultado(nota_copy)
        resultado_letra = re.sub(r'[^a-z]', '', resultado_letra.strip().lower())
        resultado_letra = resultado_letra.strip().lower()
        print(copy)
        print('Novo resultado', resultado_letra)

    return copy


