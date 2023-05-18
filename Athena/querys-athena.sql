
-- Anos com maior numero de registros de obitos por cancer 
SELECT ano_morte, COUNT(*) AS num_mortes_por_cancer
FROM df_table
WHERE cancer_dead = 1
GROUP BY ano_morte
ORDER BY num_mortes_por_cancer DESC;


-- Tipos de cancer que mais evoluem para obito
SELECT tipo_cancer, COUNT(*) AS num_mortes_por_cancer
FROM df_table
WHERE cancer_dead = 1
GROUP BY tipo_cancer
ORDER BY num_mortes_por_cancer DESC;


-- Cidades com mais registros de obitos por cançer
SELECT cidade, COUNT(*) AS num_mortes_por_cancer
FROM df_table
WHERE cancer_dead = 1
GROUP BY cidade
ORDER BY num_mortes_por_cancer DESC;

-- tipos de cancer com maior numero de diagnosticos e sua taxa de mortalidade
WITH 
diagnosticos_cancer AS (
  SELECT 
    tipo_cancer,
    COUNT(cod_paci) AS num_diagnosticos,
    FLOOR(AVG(taxa_morte_tipo_cancer) * 100) AS taxa_mortalidade_porcent
  FROM df_table
  GROUP BY tipo_cancer
)

SELECT 
  tipo_cancer,
  num_diagnosticos,
  taxa_mortalidade_porcent
FROM diagnosticos_cancer
ORDER BY num_diagnosticos DESC;

-- cidade com mais mortes por cancer e quais tipos mais causam mortes
WITH
cidade_mais_mortes AS (
  SELECT 
    cidade,
    COUNT(*) AS num_mortes
  FROM df_table
  WHERE cancer_dead = 1
  GROUP BY cidade
  ORDER BY num_mortes DESC
  LIMIT 1
),

tipos_cancer_mais_mortais AS (
  SELECT 
    (SELECT cidade FROM cidade_mais_mortes) AS cidade,
    tipo_cancer,
    COUNT(*) AS num_mortes
  FROM df_table
  WHERE cancer_dead = 1 AND cidade = (SELECT cidade FROM cidade_mais_mortes)
  GROUP BY tipo_cancer
  ORDER BY num_mortes DESC
)

SELECT * FROM tipos_cancer_mais_mortais;