from fastapi import APIRouter       # importando roteador

order_router = APIRouter(prefix= "/order")    # definindo prefixo padrao da rota
                                              # Ex:    https://dominio/ORDER/caminho definido a partir daqui