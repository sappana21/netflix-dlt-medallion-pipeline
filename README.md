#  netflix-dlt-medallion-pipeline

**End-to-end ETL pipeline on the Netflix Titles dataset using Databricks Delta Live Tables (DLT), built on the Medallion Architecture (Bronze → Silver → Gold).**


##  Architecture

```
┌─────────────┐      ┌─────────────┐      ┌──────────────────────────────┐
│   Bronze     │ ───▶ │   Silver     │ ───▶ │             Gold               │
│ (Raw Ingest) │      │ (Cleaned)    │      │   (Business Aggregates)        │
└─────────────┘      └─────────────┘      └──────────────────────────────┘
    bronzeN              silverN            gold_SUMMARY_BY_COUNTRY
  (CSV → Delta,       (dedup, dropna,       gold_summary_by_type
   Autoloader)         null-filtered)       gold_summary_by_year
```

| Layer | Table(s) | Purpose |
|---|---|---|
| **Bronze** | `bronzeN` | Raw ingestion from CSV via Autoloader, with ingest timestamp |
| **Silver** | `silverN` | Deduplicated, null-cleaned, processed timestamp added |
| **Gold** | `gold_SUMMARY_BY_COUNTRY`, `gold_summary_by_type`, `gold_summary_by_year` | Business-level aggregations |

---

##  Bronze Layer — Raw Ingestion

Ingests raw Netflix CSV data via Databricks Autoloader, tagging each record with an ingestion timestamp.

---

##  Silver Layer — Cleaning

Removes duplicates, drops rows with nulls, ensures `show_id` is present, and tags each record with a processing timestamp.

---

##  Gold Layer — Business Aggregations

##  How to Run

1. Upload pipeline notebooks/files to a Databricks Repo.
2. Upload `netflix_titles.csv` to the Volume path referenced in `bronzeN` (`/Volumes/netflix_catalog/netflix_schema/netflix_volume/raw/`).
3. Create a **Delta Live Tables Pipeline** in Databricks pointing to these notebooks.
4. Run the pipeline (Triggered/Continuous).
5. Query Gold tables via Databricks SQL or connect to a BI tool.

---

##  Tech Stack
- Databricks Delta Live Tables (DLT)
- PySpark / `pyspark.sql.functions`
- Delta Lake
- Medallion Architecture (Bronze / Silver / Gold)

---

##  Dataset Source
Netflix Titles dataset — ~8,800 movies and TV shows with metadata.
