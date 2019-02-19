from sklearn.naive_bayes import MultinomialNB

# [é gordo? tem perna curta? faz auau?]
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
teste = [misterioso1, misterioso2, misterioso3]
marcacoes_teste = [-1, 1, -1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

resultado = modelo.predict(teste)
diferencas = resultado - marcacoes_teste
acertos = []
for d in diferencas:
    if d == 0:
        acertos.append(0)

total_de_acertos = len(acertos)
# print(total_de_acertos)
total_de_testes = len(teste)
# print(total_de_testes)
taxa_de_acerto = (total_de_acertos / total_de_testes) * 100
print(taxa_de_acerto)