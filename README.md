<a name="_5tjvaieie9gi"></a>Relatório do Trabalho prático

<a name="_5gydzy5nz44c"></a>Sistemas Distribuídos

<a name="_93h6yzz2w7jj"></a>***Venda de Carros - Smart Contract***

<img src="images/LOGOTIPO_ESTG.jpeg">

<a name="_svhnxa147qrk"></a><a name="_8i9bt9xbdiy8"></a>Aluno: Bruno Martins, 1704756, 

<a name="_y1cuk2bpwb78"></a>       BMSM15, brunomiguelmartins1522@gmail.com



<a name="_76iruwrnpnu"></a>***Índice***

[**1. Descrição do Trabalho	3**](#_5ytd58hv9tul)

[**2. Implementação do trabalho	3**](#_2osy7nktuam9)

[**3. Funcionamento do trabalho	5**](#_68s3hd3llr1s)

[**4. Conclusão	8**](#_uvstfvrocbgj)

[**Bibliografia	8**](#_fted68ksgqt0)


1. ## <a name="_5ytd58hv9tul"></a>Descrição do Trabalho
O professor da disciplina de Sistemas Distribuídos pediu que eu desenvolvesse um SmartContract em Solidity para permitir a venda de carros. Para efetuar uma venda, o comprador precisará enviar uma transação contendo informações sobre o carro, incluindo a marca, o modelo, o valor em Ether e o ID da compra. Em seguida, o valor do carro será transferido do comprador para o vendedor através da venda, e o pagamento em Ether será retirado da conta do comprador e enviado para a conta do vendedor.

2. ## <a name="_2osy7nktuam9"></a>Implementação do trabalho
Para começar, o smart contract foi desenvolvido em solidity e a versão utilizada foi a 0.8.2. O nome do contrato é Car Sales e declarei as primeiras variáveis. A variável minter do tipo address public que permite guardar o endereço do criador do contrato. A outra variável permite que após a conclusão da transação, o valor recebido pelo autor do contrato seja mantido. 

<img src="images/Remix contract car_sales.png">

Em seguida, foi desenvolvido um evento que possibilita a transferência de uma quantia específica de um endereço específico para outro endereço. Para além disso também foram declaradas as variáveis PriceCar, IdPurchase, BrandCar e ModelCar que permitem guardar o preço do carro, o id de venda, a marca e o modelo do carro, respetivamente. 

Depois é desenvolvido o construtor, que permite a inicialização do contrato. As variáveis que foram declaradas no passo anterior são atribuídas e configuradas dentro deste construtor.

<img src="images/Remix event Sent.png">

Após a criação do código anterior que permite inicializar o contrato, é implementada a função Purchase com o objetivo de permitir que um usuário faça uma compra. A função Purchase é definida como pública e pagável. Para executá-la, é necessário que o valor introduzido pelo comprador seja igual ou maior que o preço definido no contrato. Se a função for executada com sucesso, o valor introduzido pelo comprador será adicionado ao balanceReceived. Dentro dessa função, é utilizado o evento criado anteriormente, que possibilita o envio do valor pago pelo comprador (sender) para o criador do contrato (minter).

<img src="images/Function purchase.png">

Em seguida, é desenvolvida a função getBalance, que tem como objetivo retornar o valor armazenado no contrato a ser transacionado. Em outras palavras, essa função permite obter o saldo atualmente disponível no contrato.

<img src="images/Function getBalance.png">



Finalmente, a função withdrawMoney é implementada para que o criador do contrato possa retirar o valor armazenado nele.

<img src="images/Function withdrawMoney.png">

3. ## <a name="_68s3hd3llr1s"></a>Funcionamento do trabalho	
Depois de o código estar pronto, utilizarei o Ganache como plataforma de suporte para testar o funcionamento do contrato. O Ganache é uma ferramenta fornecida pelo Truffle Suite. O objetivo principal do Ganache é permitir o desenvolvimento e teste de contratos inteligentes em um ambiente local.

Para criar o contrato, é necessário escolher uma conta pertencente ao criador do contrato e preencher os campos de marca, modelo, valor e ID. Depois de preencher esses campos, o contrato pode ser criado e implantado. Para realizar uma compra e criar contrato, é preciso selecionar uma conta do comprador com saldo suficiente para a transação.

<img src="images/Deploy Contract.png">

<img src="images/Ganache account.png">

<img src="images/Contract Remix.png">

<img src="images/Ganache contract creation.png">

Depois de escolher a conta, é necessário inserir o valor correspondente ao campo "valor" do contrato no campo "valor" da transação e clicar no botão de venda. Após a compra, o valor da transação será retirado da conta do comprador e armazenado no contrato, e isso pode ser verificado clicando no botão "getBalance".

<img src="images/Remix contact getbalance.png">

<img src="images/Remix contract value.png">

<img src="images/ganache contract value.png">

Para o criador do contrato retirar o valor da transação, ele precisa selecionar sua própria conta, que está armazenada no contrato e pode ser consultada clicando no botão "minter". Depois de escolher a conta do criador do contrato, o botão "withdrawMoney" deve ser clicado para enviar o valor armazenado no contrato de volta para a conta do criador. Após esse procedimento, a transação estará totalmente concluída. Após a conclusão da transação, não haverá mais valor a ser transacionado, então o botão "getBalance" exibirá o valor 0. Através do botão "balanceReceived", é possível verificar o valor total recebido pelo criador neste contrato

<img src="images/Remix contract withdraw.png">

<img src="images/Ganache contract withdraw.png">

4. ## <a name="_uvstfvrocbgj"></a>Conclusão
Em conclusão, neste trabalho, explorei mais acerca dos SmartContrats e o funcionamento destes na Blockchain. Analisamos em detalhes os principais aspectos e abordagens relacionados aos contratos e a blockchain, tentando assim oferecer uma visão abrangente e mais fundamentada do assunto.

Ao longo do trabalho ressalto que o trabalho poderia estar melhor, podendo fazer melhorias na verificação de dados , transferências noutro tipo de valor sem ser ether e complementar também a complexidade do contrato. No entanto, o contrato funciona, onde o objetivo principal foi cumprido.

Em suma, este trabalho proporcionou uma compreensão mais aprofundada de SmartContrats/Blockchain e suas implicações, contribuindo para a ampliação do conhecimento nessa área.
## <a name="_fted68ksgqt0"></a>Bibliografia
Apontamentos fornecidos acerca de Solidity e Blockchain pelo docente da disciplina.

*Solidity tutorial*. (n.d.). Retrieved May 16, 2023, from https://www.tutorialspoint.com/solidity/index.htm 

*Introduction to Smart Contracts — Solidity 0.8.13 documentation*. (n.d.). Retrieved May 16, 2023, from https://docs.soliditylang.org/en/v0.8.13/introduction-to-smart-contracts.html#index- 

*Ganache*. (n.d.). Truffle Suite. Retrieved May 16, 2023, from https://trufflesuite.com/ganache/ 

