from fastapi import APIRouter       # importando roteador

auth_router = APIRouter(prefix= "/auth")    # definindo prefixo padrao da rota
                                            # Ex:    https://dominio/AUTH/caminho definido a partir daqui


#   PARA CRIAÇÃO DE ROTAS
    # Estrutura da rota:
        # @ = decorator (usado para definir que é uma rota) | auth_router = variável que atribuimos o APIRouter | .get = metodo aser utilizado (get, post, put,etc ..) | ("/") = caminho do endpoint  

@auth_router.get("/")
async def autenticar():
        
        """
        Essa é a rota padrão de autenticação do nosso sistema

        """
        return {"mensagem":"Você acessou a rota padrão de autenticação", "autenticado": False}