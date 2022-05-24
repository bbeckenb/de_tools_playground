Brandon
Python
Pandas is especially important here
Wouldn’t worry as much about SQL Alchemy, less important for the type of work you’ll be doing
AWS Athena (Presto)/Glue Crawlers/Glue Data Catalog/S3
https://aws.amazon.com/athena/
https://aws.amazon.com/s3/
Slightly different form of SQL, with a different query engine running it.
We use Athena heavily in our work. Presto is the query engine used by AWS Athena with some slight modifications
Apache Airflow
https://airflow.apache.org/
You won’t be responsible for the deployment at PGx, but it’s not too challenging to set up a test environment to play around with
Focus more on the creation of DAGs, that’s where we spend most of our time.
SQL
https://www.microsoft.com/en-us/sql-server/sql-server-downloads
We use a Microsoft SQL Server database – you should be able to get a free developer version online
This will be important to know, but the basics of SQL you’ll pick up learning about Athena and the database management work is not something you’ll be responsible for.
Spark/Glue
We’re looking to move away from this technology, but it is still in use. Would not emphasize as much
 

I think a mini-project here would be a great way to go about learning these tools. A potential project you could do:

Set up airflow instance to run locally
Create personal AWS account (the rest of this should be within the free tier of usage)
Create airflow job to:
Pull structured data from an online data source (stock data is pretty easy to get, could also do sports or travel information)
Write the data to an S3 bucket
Create a Glue database and crawler and crawl the data you just wrote to S3 so that it creates a table in your Athena database
Create a second airflow job to:
Query the Athena database to pull interesting information from the data (whatever you find interesting)
Send the data to yourself in an email with the details in an excel attachment to the file


Alex
tldr:

Good idea Brandon, do what he says. Additionally

If you get stuck, move on to the next thing
Try both crawlers in Glue and SQL statements in Athena to create tables in Athena from S3 files
Get some experience with CTAS
You can interact with AWS using the boto3 library. Try it
 

My suggestion was going to be to create an AWS account and try to learn S3 and Athena in the dashboard as well as use boto3 to interact with both Athena and S3, so this lines up really well with what I was thinking.

 

The only things I would add:

General: If you end up getting stuck on any tool like you can’t seem to get airflow started for some reason, skip it, and come back to it after becoming familiar with another tool. This is all bonus learning work, so there isn’t really a need to bash your head against any particular tool for too long. It’s better to become familiar with the tools that are working for you.
Athena/S3: Try a Glue Crawler as well as a CREATE EXTERNAL TABLE statement to create objects in S3. I would start with a simple csv format file uploaded to S3, and then see if you can use Athena to create a new table with data written in parquet format.
To use CREATE EXTERNAL TABLE, this StackOverflow question and answer has my favorite examples of how to use the statement along with info about nuances related to reading dates. Both the SQL question and the answer should work for you as long as you don’t try to include dates in your first attempt. I would recommend starting with all strings.
In the CREATE EXTERNAL TABLE, notice how the path given in the LOCATION parameter is a path to the folder containing the file and not the file itself.
                                                    i.     e.g.: when you have the file stored at 's3://my_bucket/som_bucket/dat/date.csv', a LOCATION of 's3://my_bucket/som_bucket/dat/' works, but 's3://my_bucket/som_bucket/dat/date.csv' will not work.

Athena/S3: Try to create a new table in Athena from an existing table using a CTAS statement and store the data in a parquet format with SNAPPY compression.
Using Python to interact with AWS: We use boto3 primarily to interact with AWS and sometimes we’ll use s3fs to upload files to s3 just because it’s a little easier.
In order to use boto3 and s3fs, you will need to authenticate with your credentials. This StackOverflow question has multiple solutions for that. The answer that uses the .aws/credentials file is similar to what we use on our team, although I’m not sure exactly how that works on a windows machine if that’s what you are using
