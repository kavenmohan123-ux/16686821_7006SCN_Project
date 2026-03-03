# Tableau Dashboards – Reddit Finance Analytics

## Dataset
**File:** `00_combined.csv`  
**Description:** Cleaned and reduced Reddit finance dataset covering S&P 500 companies.  
**Key Columns:**  
- id  
- title  
- text  
- created_utc  
- created_datetime  
- score  
- num_comments  
- upvote_ratio  
- subreddit  
- company  
- year  
- month  

This dataset is optimized for visualization and analytics, with no calculated fields or bins required in Tableau.

---

## Dashboard 1: Data Quality & Pipeline Monitoring
This dashboard focuses on validating the stability and reliability of the data pipeline. It visualizes record counts over time, distribution of records across companies and subreddits, and trends in upvote ratios. These views help identify ingestion gaps, data skew, and anomalies, ensuring that preprocessing and collection steps are functioning correctly.

**Visualizations:**
- Records Over Time  
- Records per Company  
- Subreddit Distribution  
- Upvote Ratio Quality Check  

---

## Dashboard 2: Model Performance & Feature Importance
This dashboard demonstrates why Reddit engagement metrics are meaningful features for modeling. It highlights relationships between post scores and comments, compares average scores across companies, tracks engagement trends over time, and contrasts upvote ratios across subreddits to indicate signal quality.

**Visualizations:**
- Score vs Comments  
- Average Score by Company  
- Engagement Over Time  
- Upvote Ratio by Subreddit  

---

## Dashboard 3: Business Insights & Recommendations
This dashboard translates social media activity into actionable business insights. It identifies the most discussed companies, tracks sentiment proxies over time, highlights comment intensity by company, and shows which subreddits contribute the most influence, supporting market monitoring and decision-making.

**Visualizations:**
- Most Discussed Companies  
- Sentiment Proxy Over Time  
- Comment Intensity by Company  
- Subreddit Influence Map  

---

## Dashboard 4: Scalability & Cost Analysis
This dashboard supports system design and architectural decisions. It visualizes data growth trends, monthly ingestion volumes, company-level data load, and engagement density, helping justify the use of scalable data processing frameworks and efficient resource allocation.

**Visualizations:**
- Data Volume Over Time  
- Records per Month  
- Company Data Load  
- Engagement Density  

---

## Notes
- All dashboards use only raw fields (no calculated fields, bins, or LOD expressions).
- Visualizations are designed to be simple, reproducible, and academically defensible.
- Suitable for coursework, project submissions, and applied data engineering or analytics demonstrations.
