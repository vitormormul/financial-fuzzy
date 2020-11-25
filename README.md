# Financial Fuzzy

Financial Fuzzy é uma aplicação em lógica fuzzy aplicada ao mercado brasileiro de ações com o objetivo de ajudar um usuário à encontrar uma empresa que esteja com bons valores no mercado.  

Ele serve como uma ferramenta de indicação e sugestões de aplicações monetárias, não sendo responsabilizada pelo real retorno de uma ação em específico.  

O Financial Fuzzy utiliza um banco de dados oficial, porém do fechamento diário da bolsa de valores brasileira, portanto seus dados não são em tempo real, podendo ocasionar divergências.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as devidas dependências do projeto.

```bash
pip install -r requirements.txt
```

## Uso
Para rodar o programa é bastante simples. Basta navegar até a pasta do projeto e utilizar o [Python 3](https://docs.python.org/3/) para rodar o arquivo main.py

```bash
python main.py
```

## Funcionamento
Primeiramente o programa irá chamar o arquivo fundamentus para realizar a captura dos dados de fonte oficial, criando então o arquivo data.csv.  

Com isso feito, o programa irá enviar cada empresa capturada no primeiro passo à lógica fuzzy, gerando respostas para cada uma delas e salvando tudo em um novo arquivo, results.csv.  

Por fim, os gráficos de cada parâmetro utilizado na lógica fuzzy é mostrado, por fins de demonstração.  

Esses passos podem ser acompanhados no terminal, com algumas indicações do que está sendo realizado pelo programa, assim como seu progresso.
