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

def analisar_endpoint(codigos_endpoints):
    qtd_sucesso = 0
    for codigo in codigos_endpoints:
        if eh_sucesso(codigo):
            qtd_sucesso += 1
    qtd_total = len(codigos_endpoints)
    qtd_erros = - qtd_total - qtd_sucesso
    porcentagem_sucesso = (qtd_sucesso / qtd_total) * 100
