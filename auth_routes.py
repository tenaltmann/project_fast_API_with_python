from fastapi import APIRouter       # importando roteador

auth_router = APIRouter(prefix= "/auth")    # definindo prefixo padrao da rota
                                            # Ex:    https://dominio/AUTH/caminho definido a partir daqui