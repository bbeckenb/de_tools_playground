from classes.S3Manager import S3Manager
from classes.YahooFiManager import YahooFiManager
'''
I think a mini-project here would be a great way to go about learning these tools. A potential project you could do:

1. Set up airflow instance to run locally
    - Directed Acyclic Graphs (DAGs) of tasks
2. Create personal AWS account (the rest of this should be within the free tier of usage)
3. Create airflow job to:
    - Pull structured data from an online data source (stock data is pretty easy to get, could also do sports or travel information)
    - Write the data to an S3 bucket
4. Create a Glue database and crawler and crawl the data you just wrote to S3 so that it creates a table in your Athena database
5. Create a second airflow job to:
    - Query the Athena database to pull interesting information from the data (whatever you find interesting)
    - Send the data to yourself in an email with the details in an excel attachment to the file
'''

S3Client = S3Manager()
YahooClient = YahooFiManager()