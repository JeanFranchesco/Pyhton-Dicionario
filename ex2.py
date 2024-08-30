lista=[
    {'aluno':'','idade':'','nota':''},
    {'aluno':'','idade':'','nota':''},
    {'aluno':'','idade':'','nota':''}
]

media=0
loop=True
count=0
for x in range(0,3):
  name=input("Digite o nome do aluno ")
  lista[x]['aluno']=name
  age=input("Digite a idade  do aluno ")
  lista[x]['idade']=age
  
  total_notas = 0
  num_notas = 0

  while num_notas < 3:
        try:
            note = int(input(f"Digite a Nota {num_notas + 1} do aluno (0 a 10): "))
            if 0 <= note <= 10:
                total_notas += note
                num_notas += 1
            else:
                print("A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        if(count==3):
          loop=False
  total_notas=total_notas/3
  saveNote=str(total_notas)
  lista[x]['nota']=saveNote
  exit=input("Deseja sair ? s/n")
  match(exit.lower()):
    case "s":
      break
    case _:
      y=0
choice=int(input("1 - "+lista[0]['aluno']+"\n2 - "+lista[1]['aluno']+"\n3 - "+lista[2]['aluno']))
if(choice==1):
  choice1=0
elif(choice==2):
  choice1=1
else:
  choice=2
print("Nome  Do Aluno: "+lista[choice1]['aluno'])
print("Idade Do Aluno: "+lista[choice1]['idade'])
print("Nota  Do Aluno: "+lista[choice1]['nota'])
