print("Solicite seu nome para que poemos continuar")

analista = input("Nome e Sobrenome: ")


#O sistema solicita o nome do analista e a hora de início da sessão (0 a 23).
# Essas informações valem para toda a sessão e o turno é determinado uma única vez.

while True:
    try:
        hora = int(input("Hora de início da sessão (0 a 23): "))
        if 0 <= hora <= 23:
            break
        else:
            print("Este horario nao e valido, por favor digitar outra hora.")
    except:
        print("Apenas numeros.")

if 6 <= hora < 12:
    turno = "Manhã"
elif 12 <= hora < 18:
    turno = "Tarde"
elif 18 <= hora <= 23:
    turno = "Noite"
else:
    turno = "Madrugada"


# Análise de múltiplos e-mails:
# O sistema deve permitir que o analista analise quantos e-mails quiser,
# um após o outro, sem reiniciar o programa. Ao final de cada análise,
# pergunta se deseja continuar

lista_emails = [
    "Gabriela@gmail.com",
    "Giovana.Fiap@fiap.com.br",
    "Rafinha@gmail.com"
]

print("\nLista de e-mails:")
for item in lista_emails:
    print(item)

emails = []

numero = 1
continuar = "S"

while continuar == "S" and numero <= len(lista_emails):

        print(f"\nE-mail #{numero} - {lista_emails[numero - 1]}")

        remetente = input("Remetente conhecido? (S/N): ").upper()
        links = input("Possui links suspeitos? (S/N): ").upper()
        dados = input("Solicita dados pessoais? (S/N): ").upper()
        urgente = input("Possui linguagem urgente? (S/N): ").upper()

        while True:
            try:
                anexos = int(input("Quantidade de anexos: "))
                if anexos >= 0:
                    break
                else:
                    print("Digite um valor válido.")
            except:
                print("Digite apenas números.")

#Calcular a pontuação e a classificação com as mesmas regras do CP1.
        pontos = 0

        if remetente == "N":
            pontos += 2

        if links == "S":
            pontos += 2

        if dados == "S":
            pontos += 3

        if urgente == "S":
            pontos += 2

        if anexos >= 3:
            pontos += 2
        elif anexos > 0:
            pontos += 1

        if pontos <= 2:
            classificacao = "Seguro"
        elif pontos <= 5:
            classificacao = "Suspeito"
        elif pontos <= 8:
            classificacao = "Perigoso"
        else:
            classificacao = "Crítico"


#Exibir o relatório individual no mesmo formato do CP1.
        print("\n--- Resultado ---")
        print("Pontuação:", pontos)
        print("Classificação:", classificacao)

        email = {
            "numero": numero,
            "pontuacao": pontos,
            "classificacao": classificacao
        }

        emails.append(email)
        # registrar o resultado desse e - mail
        continuar = input("\nDeseja analisar outro e-mail? (S/N): ").upper()

        numero += 1

#===========================================
# ETAPA 3
# Resumo da sessão
#===========================================

print("\n================================")
print("RESUMO DA SESSÃO — CyberShield")
print("================================")

print("Analista:", analista)
print("Turno:", turno)
print("Total de e-mails:", len(emails))

print("\n--- Detalhamento ---")

pontuacoes = []

seguro = 0
suspeito = 0
perigoso = 0
critico = 0

for email in emails:

    print(
        f"\nE-mail #{email['numero']} - {lista_emails[email['numero'] - 1]} | "
        f"Pontuação: {email['pontuacao']} | "
        f"Classificação: {email['classificacao']}"
    )

    pontuacoes.append(email["pontuacao"])

    if email["classificacao"] == "Seguro":
        seguro += 1

    elif email["classificacao"] == "Suspeito":
        suspeito += 1

    elif email["classificacao"] == "Perigoso":
        perigoso += 1

    else:
        critico += 1

maior = max(pontuacoes)
menor = min(pontuacoes)
media = sum(pontuacoes) / len(pontuacoes)

print("\n--- Estatísticas ---")
print("Maior pontuação:", maior)
print("Menor pontuação:", menor)
print("Média:", round(media, 1))

print("\n--- Classificações ---")
print("Seguro:", seguro)
print("Suspeito:", suspeito)
print("Perigoso:", perigoso)
print("Crítico:", critico)

print("================================")
