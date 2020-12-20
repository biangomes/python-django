# Documentação simples do sistema de perguntas e respostas

## Sobre o sistema.
Trata-se de um sistema de perguntas e respostas utilizando dicionários.
A quantidade de perguntas e respostas é arbitrária, o objetivo é aumentar
o nível de abstração do leitor sobre dicionários aninhados. Foi elaborado
com base no curso do professor Luiz Otávio Miranda, desenvolvido, alterado e 
documentado por Beatriz Nascimento.

Abaixo é feita uma descrição do código.

---

## Descrição do código
**Linha 2 até linha 5:** foi criado um dicionário "*master*", em que
tinha como **valor** as perguntas feitas ao usuário. Portanto, caso
queira adicionar perguntas, precisa inseri-las na estrutura do dicionário
"*master*". As **chaves** desse dicionário também eram dicionários, em que
as chaves foram separadas em:

- **pergunta**: a pergunta propriamente dita;

- **respostas**: as respostas foram passadas na forma de dicionários, uma
vez que trata-se de respostas **objetivas**. Neste dicionário em questão,
as chaves são as alternativas e os valores são o enunciado dessas 
alternativas.

- **resposta_certa**: esta chave tem como valor a alternativa correta.
Ela é útil para fazer a validação posteriormente.

**Linhas 7 até 8:** variáveis responsáveis por contabilizar a 
**quantidade** de respostas certas, erradas. A variável matemática
```taxa_de_acerto``` calcula a **porcentagem** de acertos da questão.

**Linhas 12 até 14:** para iterar sobre o dicionário, é utilizado o `for`
onde `chave_pergunta` e `valor_pergunta` acessam as chaves e os valores 
do dicionário `perguntas`, respectivamente.

**Linhas 16 até 17:** mostra ao usuário as alternativas, agora acessando
especificamente a chave `respostas`.

**Linha 19:** solicita ao usuário a alternativa escolhida por ele e 
armazena na variável `resposta_usuario`.

**Linhas 22 até 25:** faz a validação da resposta inserida pelo usuário
que foi armazenada na variável `resposta_usuario`. A verificação desta 
variável é feita diretamente com a chave `resposta_correta`. Se a
resposta estiver correta, a variável `respostas_certas` é incrementada
em um; senão, a variável `respostas_erradas` é incrementada em um. A
lógica destes contadores é para que a variável `taxa_de_acerto` realize
os cálculos de aproveitamento.

**Linha 28:** faz o cálculo da taxa de aproveitamento do usuário em porcentagem.

**Linha 29 e 30:** a linha 29 apenas faz uma quebra de linha e a linha 30
mostra ao usuário as estatísticas.