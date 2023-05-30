
<h1 align="center">Engenharia de Dados na Análise de um Dataset sobre Casos de Câncer no Brasil</h1>

# Overview da solução
![overview](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/e38434da-aa19-413e-88d1-d3985557dc1f)

# Tecnologias utilizadas
![tecnologias](https://github.com/GustavoGuarany/projeto-data-cancer/assets/126171692/126abbeb-0cee-48bb-919e-cee85c142437)


Este projeto aplica técnicas de engenharia de dados para analisar e interpretar um vasto conjunto de dados disponível no site kaggle sobre o câncer no Brasil. Com a finalidade de explorar a incidência de casos, relação faixa etária/óbitos por câncer e outros. A análise de dados pode ajudar a responder questões cruciais na área médica, contribuindo para políticas de saúde mais eficazes e melhores práticas de tratamento. Com um enfoque específico na doença do câncer, este projeto tem o potencial de influenciar positivamente a prevenção, diagnóstico e tratamento.<br>
O governo brasileiro, por meio do Instituto Nacional do Câncer (INCA), é responsável pela geração de estimativas relacionadas ao câncer no país. Para isso, o INCA estabelece centros de coleta de dados sistemáticos, conhecidos como Registros de Câncer com Base Populacional (RCBP). Esses registros seguem as leis regionais vigentes e estão disponíveis para solicitação por qualquer indivíduo interessado.<br>
Foi construída uma solução robusta para gerir, armazenar, limpar, modelar e processar dados, com o auxílio de tecnologias da AWS. Essas tecnologias incluíram:<br>
<br>
**AWS S3**: Ferramenta que permitiu armazenar dados brutos e processados com segurança e flexibilidade.<br>
<br>
**AWS Glue**: Utilizamos o Glue para realizar o ETL (Extração, Transformação e Carregamento) dos dados. Extração, processamento, limpeza e modelagem dados com glue job.<br>
<br>
**AWS Athena**: Analise dos dados diretamente do S3. Execução de consultas SQL sem a necessidade de configurar servidores ou clusters.<br>
<br>
Para automatizar e gerenciar nossa infraestrutura de maneira eficiente, foi utilizado o **Terraform**, uma ferramenta de Infraestrutura como Código (IaC). Criação e provisionamento da infraestrutura de forma declarativa, aumentando a produtividade e a eficiência de nas operações.<br>
<br>
Na etapa de Análise Exploratória foram descobertos os vários insights importantes abaixo:<br>
<br>
Mais mulheres sofrem com câncer no Brasil<br>
A incidência de casos por gênero:<br>
<br>
**Feminino: 971.471**<br>
**Masculino: 806.534**<br>   
Podemos assumir que no Brasil, as mulheres apresentam uma maior incidência de câncer em comparação aos homens.


