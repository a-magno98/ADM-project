# ADM-project
## AIM OF THE PROJECT
The goal of the project is two folds:

- **PART I + PART II, for all the students**: the design and the development of the large-scale data management/data processing layer for a specific application at your choice. To this aim, you can rely on any NoSQL system presented in the context of the  Advanced Data Management course (Riak, Redis, Cassandra, MongoDB, Neo4j).
- **PART III, only for Computer Science students**: modeling, in RDF, RDFS and OWL, some requirements and query them through SPARQL.

**The aim of Project PART I is to present requirements related to the design and development of a large scale application through the usage of NoSQL technology.**

More precisely, in Project PART I you should:

- Propose a domain and a related application you plan to consider (e.g.,e-commerce domain, shopping cart and session data management application), explaining what are the main entities, relationships and present a typical workload.
- Provide details about the nature of the proposed application (e.g., the application is read/write intensive, requires batch processing, ...), according to what discussed in the course.
- Provide system requirements for the considered application: partitioning and replication requirements, consistency and availability requirements (e.g., partitioning and replication needed, eventual consistency, high availability).
- Provide details about the dataset you plan to consider. You can choose either an already available dataset or a synthetic one but we encourage the first option (it might be difficult to synthetically generate a relevant dataset for your reference application). We suggest you to have a look at https://www.kaggle.com for some datasets you might consider for your project. The dataset should have a reasonable size (few Mb).
- Based on the features of your domain and application, identify the NoSQL system, covered by the course, that you plan to use for storing and processing your data, with a short motivation (e.g., Cassandra, since it supports partitioning, replication eventual consistency and high availability).
In case you select Cassandra and MongoDB, you should rely  on the system available on the cluster.

**The aim of Project PART II is to design and develop a NoSQL data store, according to the requirements collected in Project PART I.**
More precisely, in Project PART II you should:

1. Design a conceptual schema for the domain identified in Project PART I. The schema should include at least three associations.
2. Identify a workload, i.e., a set of relevant and frequent operations, related to the application you have described in Project PART I. The workload should contain at least 10, structurally different operations.
3. Based on (1) and (2), design a set of aggregates or a graph schema using the approaches/methodologies proposed in the course.
4. Design a logical schema for the tool selected in Project PART I, starting from (1) and (3).
5. For each operation in the workload, specify the corresponding operation in the language supported by the system you have selected in Project PART I.
6. Provide details about the system configuration needed in the chosen systems for storing/processing your data according to the application requirements selected in Project PART I.
7. Create an instance of your dataset in the system selected for storage in Project PART I (5), according to the logical schema proposed in step (3).
Notice that selected datasets might need to be transformed in order to be used by your application. For dataset transformation, you can rely on either data transformation tools, such as Tableaux Prep (www.tableau.com), Apache Superset (superset.apache.org) Trifacta ( www.trifacta.com ), or other ETL tools such as Talend ( www.talend.com ), or scripts in your favorite language.
For importing datasets in the chosen system, you should refer to the available documentation for the system you have selected (e.g. https://www.datastax.com/dev/blog/simple-data-importing-and-exporting-with-cassandra for Cassandra and https://neo4j.com/developer/guide-importing-data-and-etl/perneo4J for Neo4J).
8. Implement the workload in the selected system.
