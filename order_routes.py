from fastapi import APIRouter       # importando roteador

order_router = APIRouter(prefix= "/order", tags=["pedidos"])    # definindo prefixo padrao da rota
                                              # Ex:    https://dominio/ORDER/caminho definido a partir daqui

#   PARA CRIAÇÃO DE ROTAS
    # Estrutura da rota:
        # @ = decorator (usado para definir que é uma rota) | order_router = variável que atribuimos o APIRouter | .get = metodo aser utilizado (get, post, put,etc ..) | ("/") = caminho do endpoint  

@order_router.get("/")
async def pedidos():
        
        """
        Essa é a rota padrão de pedidos do nosso sistema

        """
        return {"mensagem":"Você acessou a rota de pedidos"}