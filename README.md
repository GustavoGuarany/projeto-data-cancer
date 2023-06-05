

<h1 align="center">Engenharia de Dados na Análise de um Dataset sobre Casos de Câncer no Brasil</h1>

### Este projeto aplica técnicas de engenharia de dados para analisar e interpretar um vasto conjunto de dados disponível no site kaggle sobre o câncer no Brasil. 

## Overview da solução 
![overview](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/e38434da-aa19-413e-88d1-d3985557dc1f)

## Tecnologias utilizadas
| Tecnologia | Descrição |
| :------------- |:-------------|
| Python  | Linguagem de programação de alto nível (Pandas, Seaborn) |
| Pandas  | Ferramenta de análise e manipulação de dados de código aberto |
| Seaborn  | Biblioteca de visualização de dados Python baseada em matplotlib|
| Matplotlib  | Biblioteca abrangente para criar visualizações estáticas, animadas e interativas em Python|
| Jupyter Notebook  | Biblioteca de visualização de dados Python baseada em matplotlib|
| SQL  | Linguagem padrão para manipulação de registros em bancos de dados |  
| AWS | Plataforma de serviços de computação em nuvem da Amazon.com |
| AWS Glue | Serviço de integração de dados com tecnologia sem servidor |
| AWS S3 | Serviço de armazenamento de objetos |
| AWS Athena | Análise interativa e sem servidor criado em frameworks de código aberto |
| Terraform | Automação de infraestrutura para provisionar e gerenciar recursos em qualquer nuvem |
| Apache Spark | Mecanismo de análise unificada para código aberto em computação distribuída |
<br>

![tecnologias](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/126abbeb-0cee-48bb-919e-cee85c142437)




## Potenciais impactos
 - Identificação de áreas de alta incidência
 - Identificação de fatores de risco
 - Contribuir para políticas de saúde mais eficazes
 - Melhor alocação de recursos
 - Melhorar práticas de tratamento
 - Influenciar positivamente a prevenção, diagnóstico e tratamento
 - Previsão de tendências futuras
 - Melhorar o prognóstico do paciente

<br>

## Diagrama modelagem dos dados
![diagrama](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/c1f1ad7e-5c92-4501-b371-715d70971bd7)

<br>
Foi construída uma solução robusta para gerir, armazenar, limpar, modelar e processar dados, com o auxílio de tecnologias da AWS. Essas tecnologias incluíram:<br>
<br>

![AWS](	https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

| AWS S3  | AWS Glue | AWS Athena|
| ------------- | ------------- | ------------- |
| Armazenamento dos dados brutos csv | ETL  | Análise dos dados  |
| Armazenamento dos dados Convertidos para parquet | Limpeza  | Consultas SQL  |
| Armazenamento dos dados Processados e modelados | Modelagem  | Sem servidor  |
|  | Processamento  |  |


![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)<br>

Para automatizar e gerenciar nossa infraestrutura de maneira eficiente, foi utilizado o **Terraform**, uma ferramenta de Infraestrutura como Código (IaC). 
 - Gestão de Infraestrutura como Código (IaC)
 - Gerenciamento de dependências de recursos
 - Segurança e Conformidade
 - Automação
 - Orquestração de serviços
 - Gerenciamento do estado
<br>
<br>
## Na etapa de Análise Exploratória foram descobertos os vários insights importantes abaixo:<br>
<br>

## A incidência de casos por gênero:<br>

| Mulheres  | Homens |
| ------------- | ------------- |
| 971.471  | 806.534  |
  
Podemos assumir que no Brasil, as mulheres apresentam uma maior incidência de câncer em comparação aos homens.
<br>

### Relação faixa etária e diagnóstico de câncer.
![0 a 24](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/9734d253-d1ca-4b41-bbe6-bf67941140bb)
![25 a 54](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/cf684047-8bd7-4cc7-ad25-9ecf5d5fbbe7)
![55 a 84](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/414ce18b-4608-4209-9649-f8921b2661d4)


### Quando analisamos a relação morte por câncer e tipo do câncer, percebemos altas taxas de mortalidades em tipos de canceres relativamente comuns, como é o caso do câncer nos brônquios ou pulmões, no estomago, no esôfago. 
![01](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/2e120953-37a8-4547-a366-dd38f58a66a8)
<br>

### Os 20 principais cânceres que mais levam a óbito na faixa etária de 25-34 anos.
![02](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/cb93d774-859e-46b3-b040-fd4fecc53953)
<br>

### Mortes por faixa etária, altos índices entre 65 a 74 anos, 55 a 64 anos e 75 a 84 anos.
![03](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/142d4565-5a70-47eb-a8ab-2fc8428e5a31)
<br>

### Os 20 principais cânceres que mais levam a óbito na faixa etária de 35-44 anos. 
![04](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/f0d38576-0b91-447b-b950-be2a210d2118)
<br>

### Os 20 principais cânceres que mais levam a óbito na faixa etária de 45-54 anos.
![05](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/51454913-92d7-496c-a0ff-ce7f5c01bb18)
<br>

### Os 20 principais cânceres que mais levam a óbito na faixa etária de 55-64 anos.
![07](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/34b35c65-8916-4057-b51d-7356c76c542e)
<br>

### Mortes por câncer por estado, os principais estados para se ter atenção são, Minas Gerais, Paraná, Mato Grosso.
![06](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/07923922-0d89-486e-ad69-d63318566319)
<br>

### Diagnósticos e óbitos por câncer por cidades, preocupação principalmente para as cidades de Belo Horizonte pelos altos índices de diagnósticos e as cidades de Curitiba, Belém e Manaus por apresentarem uma alta taxa de mortalidade e relação a quantidade de diagnósticos.
![08](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/c5ad5b4d-d12c-4675-b122-b72a7586e7e5)
<br>

Este projeto proporcionou uma oportunidade para aplicar e aprofundar conhecimentos em Ciência e Engenharia de Dados, ao abordar uma questão de importância global: a incidência de câncer. Foi proposto uma solução para um problema persistente e universal, usando recursos para analisar e entender as complexas relações entre os dados relacionados a essa doença.
A melhor compreensão dessas relações tem potencial para contribuir em muitas áreas da sociedade, oferecendo insights sobre o impacto do câncer na vida das pessoas e identificando estratégias eficazes para minimizar a incidência e prevenir as mortes associadas à doença. Os dados, quando corretamente interpretados, podem fornecer as ferramentas necessárias para enfrentar esta questão com uma resposta informada e baseada em evidências.
Em termos de desenvolvimento futuro deste projeto, vemos oportunidades para expandir nossa análise, estabelecendo mais conexões entre os dados disponíveis. Além disso, a automação de processos em cada etapa do projeto permitirá uma eficiência maior e garantirá a relevância contínua de nossas descobertas à medida que novos dados forem disponibilizados. 

## Referências

O governo brasileiro, por meio do Instituto Nacional do Câncer (INCA), é responsável pela geração de estimativas relacionadas ao câncer no país. Para isso, o INCA estabelece centros de coleta de dados sistemáticos, conhecidos como Registros de Câncer com Base Populacional (RCBP). Esses registros seguem as leis regionais vigentes e estão disponíveis para solicitação por qualquer indivíduo interessado.<br>
