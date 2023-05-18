from os.path import abspath
import datetime
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# setup da aplicação Spark
spark = SparkSession \
    .builder \
    .appName("job-glue-spark") \
    .getOrCreate()

# definindo o método de logging da aplicação use INFO somente para DEV [INFO,ERROR]
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.format("csv")\
    .option("header", "True")\
    .option("inferSchema","True")\
    .option("encoding", "ISO-8859-1")\
    .csv("s3a://data-cancer-landing-prod/*.csv")

# imprime os dados lidos da raw
print ("\nImprime os dados lidos da landing:")
print (df.show())

# imprime o schema do dataframe
print ("\nImprime o schema do dataframe lido da raw:")
print (df.printSchema())

# converte para formato parquet
print ("\nEscrevendo os dados lidos da raw para parquet na processing zone...")
df.write.format("parquet")\
        .mode("overwrite")\
        .save("s3a://data-cancer-processing-prod/df-parquet-file.parquet")

# lendo arquivos parquet
df_parquet = spark.read.format("parquet")\
 .load("s3a://data-cancer-processing-prod/df-parquet-file.parquet")

# imprime os dados lidos em parquet
print ("\nImprime os dados lidos em parquet da processing zone")
print (df_parquet.show())

df_soft = df_parquet.drop("RCBP_Name","Code_of_Disease.Adult_Young.","Topography_Code","Morphology_Description","Code_of_Morphology",\
                   "Code_of_Disease_Adult_Young","Youth_Adult_Illness_Description","Naturality","State_Civil","Code_Profession",\
                   "Name_Occupation","Description_of_Topography","Indicator_of_Rare_Case","year","Distant_metastasis","Date_of_Diagnostic",\
                   "Date_of_Last_Contact","Date_of_Last_Contact","TNM","Statement","Laterality","Extension","Diagnostic_means",\
                   "Code_of_Disease_Adult_Young","Youth_Adult_Illness_Descriptio","Child_Illness_Code", "Child_Illness_Description",\
                   "Date_of_Birth","Raca_Color","Degree_of_Education","Naturality_State","Nationality","status_vital","Illness_Code")

df_soft = df_soft\
.withColumnRenamed('Patient_Code','cod_paci')\
.withColumnRenamed('Status_Address','estado')\
.withColumnRenamed('City_Address','cidade')\
.withColumnRenamed('Type_of_Death','tipo_morte')\
.withColumnRenamed('Date_of_Death','data_morte')\
.withColumnRenamed('Description_of_Disease','tipo_cancer')

df_soft = df_soft.withColumn("cod_paci", df_soft["cod_paci"].cast(IntegerType()))\
                   .withColumn("Age", df_soft["Age"].cast(IntegerType()))

df_soft = df_soft.withColumn("cancer_dead", when(df_soft["tipo_morte"] == "CÂNCER", 1).otherwise(0))\
.withColumn("ano_morte", year(df_soft["data_morte"]))

# Registra o DataFrame como uma tabela temporária
df_soft.createOrReplaceTempView("df_table")

# Use a cláusula CASE WHEN THEN ELSE em SQL
query_age = """
SELECT *,
CASE 
    WHEN Age BETWEEN 0 AND 4 THEN '0-4'
    WHEN Age BETWEEN 5 AND 14 THEN '5-14'
    WHEN Age BETWEEN 15 AND 24 THEN '15-24'
    WHEN Age BETWEEN 25 AND 34 THEN '25-34'
    WHEN Age BETWEEN 35 AND 44 THEN '35-44'
    WHEN Age BETWEEN 45 AND 54 THEN '45-54'
    WHEN Age BETWEEN 55 AND 64 THEN '55-64'
    WHEN Age BETWEEN 65 AND 74 THEN '65-74'
    WHEN Age BETWEEN 75 AND 84 THEN '75-84'
    ELSE '85+'
END AS Faixa_etaria
FROM df_table
"""

df_soft = spark.sql(query_age)

# imprime os dados lidos em parquet
print ("\nImprime os dados com a coluna faixa etaria")
print (df_soft.show())

df_soft.createOrReplaceTempView("df_table")

query_taxa = """
WITH cancer_stats AS (
    SELECT 
        tipo_cancer, 
        SUM(cancer_dead) as num_mortes, 
        COUNT(cod_paci) as num_casos,
        SUM(cancer_dead) / COUNT(cod_paci) as taxa_morte_tipo_cancer
    FROM df_table
    GROUP BY tipo_cancer
)
SELECT df_table.*, cancer_stats.taxa_morte_tipo_cancer
FROM df_table
LEFT JOIN cancer_stats
ON df_table.tipo_cancer = cancer_stats.tipo_cancer
"""

df_soft = spark.sql(query_taxa)


df_soft.repartition(1)\
          .write\
          .format("parquet")\
          .mode("overwrite")\
          .save("s3a://data-cancer-curated-prod/df-parquet-result.parquet")

# imprime os dados lidos em parquet
print ("\nImprime os dados que foram processados para curated")
print (df_soft.show())

# para a aplicação
spark.stop()