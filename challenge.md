<img src="logo.png" alt="drawing" width="500"/>

## Python Software Engineering Challenge

Our system ingests search term data from Google Ads API into a PostgreSQL database, via an AWS S3 Data Lake.

Once ingested we score each search term with its Return On Ad Spend (ROAS).

```text
ROAS = conversion value / cost
```

### Task

1. Some CSVs have been given (campaigns.csv, adgroups.csv and search_terms.csv). Ingest these 3 CSVs into a database.


2. Create some end points to return the Top 10 Search Terms by ROAS for a campaign `structure_value` or adgroup `alias`.


3. Write a simple Makefile to run:
   ```text
    - Python Formatter [I hear Black is nice ;-)]
    - Python Linter
    ```

Extra Kudos for tests, a nice git history, demonstration of valuable best practises, virtual envs etc - all the things that make it pleasant for other developers to work on your code!

### Submission

Please fork this repo to complete the challenge.

Good luck we are rooting for you, show us what you can do!
