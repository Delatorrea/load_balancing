# Load Balancing


### Instruções

Resolva o problema proposto no documento em anexo e disponibilize o código via github, nos envie o link do seu repositório quando finalizar a tarefa. Caso não possua afinidade com Python o teste pode ser desenvolvido em outra linguagem, mas damos preferência para resoluções em Python 3, caso a resolução seja em outra linguagem descreva no README a forma de executar o seu projeto.

### Problema 

Balanceamento de carga é muito importante em ambientes Cloud. Estamos sempre tentando minimizar os custos para que possamos manter o número de servidores o menor possível. Em contrapartida a capacidade e performance aumenta quando adicionamos mais servidores. Em nosso ambiente de simulação, em cada tick  (unidade básica de tempo da simulação), os usuários conectam aos servidores disponíveis e executam uma tarefa. Cada tarefa leva um número de ticks para ser ﬁnalizada (o número de ticks de uma tarefa é representado por ttask ), e após isso o usuário se desconecta automaticamente.

Os servidores são máquinas virtuais que se auto criam para acomodar novos usuários. Cada servidor custa R$ 1,00 por tick e suporta no máximo umax usuários simultaneamente. Você deve ﬁnalizar servidores que não estão sendo mais usados. O desaﬁo é fazer um programa em Python que recebe usuários e os aloca nos servidores tentando manter o menor custo possível.

### Input 

Um arquivo onde: a primeira linha possui o valor de ttask ;
a segunda linha possui o valor de umax ;
as demais linhas contém o número de novos usuários para cada tick.
Output 

Um arquivo onde cada linha contém uma lista de servidores disponíveis no ﬁnal de cada tick , representado pelo número de usuários em cada servidor separados por vírgula e, ao ﬁnal, o custo total por utilização dos servidores

### Limites 

1 ≤ ttask ≤ 10

1 ≤ umax ≤ 10

### Exemplo 

input.txt

![input](https://user-images.githubusercontent.com/38289677/134824204-ddc1ffef-0f2e-4984-8c42-0d05ab208d46.png)


output.txt

![output](https://user-images.githubusercontent.com/38289677/134824224-cf7b773a-f155-49c3-891f-3eb211910fbf.png)

### Detalhamento do exemplo 

ttask = 4 (valor da primeira linha do input.txt)

umax = 2 (valor da segundo linha do input.txt)

![detalhe](https://user-images.githubusercontent.com/38289677/134824245-0c51e974-55dc-43ba-8238-5e0425e5d3bf.png)


### Critérios de avaliação 


- Funcionamento
- Testes de unidade
- Cobertura de testes
- Complexidade de código
- Padronização de código (PEP-8, PEP-257)