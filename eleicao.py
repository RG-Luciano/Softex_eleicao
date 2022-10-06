import enum
x = 0 
y = 0
z = 0
b = 0
maisvotado = 0
stop = False
class Candidatos(enum.Enum):
        candidato_x = 889
        candidato_y = 847
        candidato_z = 515
        branco = 0
while stop == False: 
    try:
        print("Digite seu voto: ")
        voto = int (input())
        if(voto==889):
            x = x + 1
        elif(voto == 847):
            y = y + 1
        elif(voto == 515):
         z = z + 1
        else:
            b = b + 1
    except:
        print("Dados errados")
        print("Digite um numero")
    resposta = input(("Deseja voltar de novo? 'S' ou 'N' "))
    if(resposta == 'N' or resposta == 'n' or resposta == 'Nao' or resposta== 'nao'):
        stop = True    
if(x > y) and (x > z):
    maisvotado = x
    vencedor = Candidatos.candidato_x
elif (y > x) and (y > z):
    maisvotado = y
    vencedor = Candidatos.candidato_y
elif (z > x) and (z > y):
    maisvotado = y
    vencedor = Candidatos.candidato_z

candidatox = Candidatos.candidato_x
candidatoy = Candidatos.candidato_y
candidatoz = Candidatos.candidato_z
brancos = Candidatos.branco

print("Vencedor é: ", vencedor.name)
print(candidatox, " recebeu ", x, "votos")
print(candidatoy, "  recebeu ", y, " votos")
print(candidatoz, "  recebeu ", z, " votos")
print(brancos, "  teve ", b, " votos")
