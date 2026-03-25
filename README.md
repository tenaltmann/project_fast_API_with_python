PROJETO MONTANDO UMA API DO ZERO

BIBLIOTECAS UTILIZADAS
    fastapi 
    uvicorn 
    sqlalchemy 
    passlib{bcrypt} 
    python-jose{cryptograph} 
    python-dotenv 
    python-multipart


# Rest APIs
    # GET => Leitura/coleta
    # POST => enviar/criar
    # PUT / PATCH => edição
    # DELETE => deletar

Formas de criar rotas
    3 Opções:
        1 - Criar tudo no aplicativo (main.py) - não recomendado, usado apenas quando há pouquissimas rotas
        2 - Criar um único arquivo de rotas (routes.py) 
        3 - Dividir em sessoes - exemplo: rota para autenticações e pedidos (order_routes.py e auth_routes.py) - UTILIZAREMOS ESSA

        Tentar sempre utilizar um padão no nome dos arquivos de rotas:
            order_routes.py
            auth_routes.py
            ...._routes.py

        SEMPRE
            atentar na ordem de importação das rotas
            importar após o "app = Fast API()"
            isso evita o problema de "referência cicular", ondfe o arquivo main precisa de outros arquivos para funcionar e outros arquivos precisam do main para funcionar

COMANDOS NO TERMINAL de instalação
    Instalação de bibliotecas:
        pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptograph] python-dotenv python-multipart


COMANDOS NO TERMINAL  usados mais de uma vez (rotineiramente)

    Para rodar o código, iniciar o servidor:
        Executar no terminal:   uvicorn main:app --reload
