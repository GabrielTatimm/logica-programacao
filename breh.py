alunos = []

for i in range(3):
    nome = input("Nome: ")
    idade = input("Idade: ")
    nota = input("Nota: ")
    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print("--------------------------")

for aluno in alunos:
    print(f"nome: {aluno["nome"]} ,idade: {aluno["idade"]},nota: {aluno["nota"]}")
