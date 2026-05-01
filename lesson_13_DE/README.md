# Lesson 13: Data Engineering Hometask

## Prerequisites

Before you begin, ensure you have the following installed:
- **Docker** and **Docker Compose** (to run the PostgreSQL database)
- **Python 3.9+**
- **Jupyter Notebook** (to execute the `.ipynb` file)

## How to Run

### Step 1: Start the PostgreSQL Database
1. Open a terminal and navigate to the `lesson_13_DE` directory.
2. Run the following command to start the database in the background:
   ```bash
   docker-compose up -d
   ```
   *(This will spin up a PostgreSQL instance on `localhost:5432` with user `postgres`, password `password123`, and create the `ecommerce_db` database).*

### Step 2: Set up the Python Environment
1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Execute the ETL Pipeline
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open the `lesson_13_DE_hometask.ipynb` notebook.
3. Select "Run All Cells" to execute the pipeline.

### Step 4: Verify the Results
- The notebook will automatically clean the data and load it into the PostgreSQL database.
- It will create two additional analytical tables: `customer_summary` and `product_performance`.
- The final cells in the notebook will display a preview of these analytical tables using pandas.
