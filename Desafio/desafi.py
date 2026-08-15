endpoints = ["/login", "/produtos", "/pedidos"]
status = [
        [200, 200, 401, 200, 500],
        [200, 200, 200, 200, 200],
        [201, 500, 502, 201, 500]
]

# Função que verifica se um codigo http de uma
# requisição é sucesso ou n
# 200 = true
# 401 = false
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# Função que verifica se tem 2 erros seguidos em uma
# lista de requisições (codigos) de UM endpoint

def erros_seguidos(codigos):
    for i in range(len(codigos)-1):
        codigo_atual = codigos[i]
        prox_codigo = codigos[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

print(erros_seguidos(status[2]))
