import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

conn_url = 'postgresql://postgres:123@localhost/uni_large'

# Create an engine that connects to PostgreSQL
engine = create_engine(conn_url)

# Establish a connection
connection = engine.connect()

# Pass SQL statement
stmt = """
    SELECT * FROM instructor;
"""

# Execute the statement and get the results
results = connection.execute(stmt).fetchall()

print(results)
print(type(results[0]))

# Extract column names
column_names = results[0].keys()
print(column_names, results)

# Store results in a DataFrame
df = pd.DataFrame(results, columns= column_names)
df.salary = df.salary.astype(float)

df.salary.hist(bins=8)
plt.savefig('zimg.png')