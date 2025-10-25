# Medallion Project: End-to-End Data Pipeline

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

---

This repository showcases a robust **End-to-End Data Pipeline (ETL)** built upon the modern **Medallion Architecture** pattern. The primary goal of this project is to **practice and demonstrate the full data lifecycle**, transforming raw, heterogeneous source data into clean, curated assets ready for analytical consumption.

We use fictitious data (CSV and a public API) to simulate the transformation and storage process, focusing on data quality and preparation for analytics.

---

The architecture is divided into three layers, ensuring data quality, traceability, and historical integrity:

| Layer | Folder / Quality Level | Key Processing Focus |
| :--- | :--- | :--- |
| **BRONZE** | `01-bronze-raw` (Raw) | **Ingestion:** Immutable storage of raw, historical data from external sources (CSV, API). |
| **SILVER** | `02-silver-validated` (Validated) | **Cleaning & Enrichment:** Data deduplication, standardization, and integration with external data (e.g., ViaCEP). |
| **GOLD** | `03-gold-enriched` (Curated) | **Modeling:** Final, aggregated, and highly structured data optimized for fast BI queries and Machine Learning consumption. |

---

## Technology and Tools Stack

Python 3.14, Pandas, Psycopg2, Matplotlib.pyplot, Seaborn, SQL, DBeaver, Docker,
---
