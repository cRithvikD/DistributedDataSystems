# Dataset
The dataset selected was Crimes - 2001 to Present provided by the City of Chicago through Data.gov. It is a csv that describes reported crimes that are extracted from the Chicago Police Department’s reporting system. There are currently about 8 million rows in this dataset and each record represents a crime, with the columns providing details related to where a crime occurred and what type of crime was reported. We chose this dataset because we were all interested in exploring crime data and applying our skills on a dataset of this size to understand crime trends in a large city like Chicago.

# Goal Summary
Our goal for this dataset was to give overviews of total crime over time and the different types of crimes that occur in Chicago. We wanted to identify how the number of reported crimes has fluctuated in Chicago over time, as well as identify the most frequent types of crimes. In order to accomplish this, we loaded the data into Google Cloud storage, used Airflow to load data into MongoDB, created MongoDB aggregation pipelines to distill relevant fields, stored these subsets of the data in new MongoDB collections, and ran SparkSQL queries to further analyze the curated subsets stored on a MongoDB Atlas cluster. 

# Workflow Diagram:



# Google cloud bucket containing our data:

Composer Environment where we specify the connection and code to Airflow:


# Airflow UI:


# MongoDB Atlas UI showing the data have been loaded successfully:


# Query Summaries
We took advantage of MongoDB aggregations for both of our goals. We grouped the data by primary type, took counts, projected year information, and then stored these documents as a separate collection. Another aggregation pipeline counted the total crimes by year and stored this information in a new collection as well. We were then able to load these into Spark SQL dataframes and run select queries to see the data in each collection in tabular format. 

# Results
Trend in total crime, 2001-2023
Based on the 23 years that these data have been collected and reported, the total reported crime in Chicago has decreased from a maximum of 468,815 reported crimes in 2002 to 261,021 through 2023. The year with the lowest crime was 2021, with 209,069 crimes reported. This represents a decrease of about 44% in reported crimes from 2001 to 2021. 

Crime types, 2001-2023

Over the span of these data, there are 36 distinct categories of reported crime. The most reported crime is theft, with 1,690,886 incidents since 2001. The least reported is domestic violence, with just one reported incident since 2001. 
# Takeaways
Using distributed data tools was crucial to our exploration of crime data in Chicago. Without them, it would have been very difficult and tedious to load and analyze 8 million records. The project wasn’t without its setbacks though. We experienced some limitations due to exhausting our Google Cloud credits and some difficulty with the size of data and Airflow. Given more time and resources, we would have liked to explore more nuanced details of crime in Chicago such as how certain types of crime have fluctuated over time and how geographic area relates to the types and counts of reported incidents as well. 

# References
1. dd
2. Thanks to Jay Chung, Maricela Abarca and Solomon for being brilliant teammates!
