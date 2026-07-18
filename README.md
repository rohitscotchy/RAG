

Data Parsing 
Docling :- https://docling-project.github.io/docling/usage/advanced_options/

Docling GPU :- https://docling-project.github.io/docling/getting_started/rtx/#3-install-cudnn

Chunking:- https://github.com/ALucek/chunking-strategies/blob/main/chunking.ipynb
            https://docling-project.github.io/docling/concepts/chunking/#introduction

Embedding:-

sentence-transformers/all-mpnet-base-v2 = 768 dimensional
sentence-transformers/all-MiniLM-L6-v2 =  384 dimensional
BAAI/bge-m3                            =  1024 Strong multilingual retrieval, long documents, modern RAG
BAAI/bge-large-en-v1.5                 =  1024 Excellent English technical retrieval ⭐ Excellent if English only


Data Vectorization: 
    https://docs.langchain.com/oss/python/integrations/vectorstores/pgvector

PGVector settings:- 
    docker exec -it 77e3b1129adf2f36a64ebaa37b627fff28f4daeacf258559b6ae9100c6398d47 psql -U postgres
    postgres=# ALTER USER admin WITH SUPERUSER;
    postgres=# \c RAG_POC
    RAG_POC=# CREATE EXTENSION IF NOT EXISTS vector;
            CREATE EXTENSION
            RAG_POC=# \dx
                                        List of installed extensions
            Name   | Version |   Schema   |                     Description
            ---------+---------+------------+------------------------------------------------------
            plpgsql | 1.0     | pg_catalog | PL/pgSQL procedural language
            vector  | 0.8.0   | public     | vector data type and ivfflat and hnsw access methods
            (2 rows)




Retrieval :-
    https://docs.langchain.com/oss/python/langchain/retrieval?utm_source=chatgpt.com