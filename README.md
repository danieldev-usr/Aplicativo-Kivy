# Aplicativo Kivy com Gerenciamento de Telas

## Descrição

Este aplicativo é um exemplo de como usar o Kivy para criar uma aplicação com múltiplas telas e gerenciamento de conteúdo dinâmico. O aplicativo possui uma tela inicial com um botão que leva a uma segunda tela, onde opções adicionais estão disponíveis. Dependendo da escolha do usuário, o aplicativo exibe informações de um arquivo JSON em uma nova tela.


---

## Licença e Uso

O código deste projeto é fornecido para uso livre e educacional. Você está livre para modificar, distribuir e utilizar o código de acordo com suas necessidades, desde que o uso esteja restrito a fins não comerciais e educacionais. Não há garantias de qualquer tipo, e o autor não se responsabiliza por quaisquer problemas resultantes do uso do código.
Se você utilizar ou modificar este código para criar novos projetos, seria apreciado se você mantivesse a atribuição adequada ao projeto original.
Isso garante clareza sobre o uso do código e os limites de responsabilidade.

## Funcionalidades

- Tela inicial com imagem de fundo, título e botão para navegar para a segunda tela.
- Segunda tela com um conjunto de botões que levam a diferentes telas baseadas em texto.
- Telas adicionais que mostram texto dinâmico carregado de um arquivo JSON.
- Navegação entre telas usando o `ScreenManager` do Kivy.

## Tecnologias

- **Kivy:** Biblioteca para desenvolvimento de interfaces gráficas.
- **Python:** Linguagem de programação usada para o desenvolvimento.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/danieldev-usr/Aplicativo-Kivy
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Aplicativo-Kivy
   ```

3. Instale as dependências:
   ```bash
   pip install kivy
   ```

4. Coloque a imagem `img.jpg` e o arquivo `textos.json` no diretório do projeto. (ou pode fazer uma modificação da imagem)

## Uso

1. Execute o aplicativo:
   ```bash
   python app.py
   ```

2. Navegue pelas telas usando os botões disponíveis:
   - **Tela Inicial:** Clique no botão para ir para a tela com opções adicionais.
   - **Tela de Opções:** Escolha uma das opções para carregar uma tela com texto baseado na escolha.
   - **Telinhas Adicionais:** Exibem o texto carregado do arquivo JSON.
.

---
## Instruções para Usuários Android

1. **Instale o Pydroid:** Baixe e instale o Pydroid 3, um ambiente de desenvolvimento Python para Android, da Google Play Store.

2. **Instale o Kivy:** Abra o Pydroid, vá para a seção de pacotes (Pip) e instale o Kivy. Procure por "kivy" e faça a instalação.

3. **Prepare os Arquivos:**
   - Abra o Gerenciador de Arquivos no seu dispositivo Android.
   - Crie uma nova pasta onde você deseja armazenar os arquivos do projeto.

4. **Copie os Arquivos:**
   - Copie os arquivos do projeto (por exemplo, `app.py`, `img.jpg`, e `textos.json`) para a pasta que você criou.

5. **Execute o Aplicativo:**
   - No Pydroid, navegue até a pasta onde você copiou os arquivos.
   - Abra o arquivo `app.py` e execute-o.
   - Certifique-se de que todos os arquivos necessários (como `img.jpg` e `textos.json`) estejam na mesma pasta para que o aplicativo funcione corretamente.


Você pode ajustar os detalhes como o nome do repositório, caminho da imagem e do arquivo JSON, e qualquer outra informação específica do projeto!
