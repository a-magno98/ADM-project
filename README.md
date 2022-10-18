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
