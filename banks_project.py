import csv

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./project_log.txt", "a") as f:
        f.write(timestamp + " - " + message + "\n")


def extract(url, table_attribs):
    print("Initializing extraction process... ")
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.findAll('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict = {"Bank_Name": col[1].contents[2].text,
                         "MC_USD_Billions": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[1])
            df = pd.concat([df, df1], ignore_index=True)
    print("Extraction process complete! \n")
    return df


def transform(df, csv_file):
    print("Initializing transform process... ")
    exchange_rate = {}
    mc_usd = df["MC_USD_Billions"].tolist()
    mc_usd = [float("".join(x.split(","))) for x in mc_usd]
    df["MC_USD_Billions"] = mc_usd

    with open(csv_file, 'r') as exchange:
        for line in csv.DictReader(exchange, fieldnames=("Currency", "Rate")):
            if line["Currency"] != "Currency":
                exchange_rate[line["Currency"]] = float(line["Rate"])

    df['MC_EUR_Billion'] = [np.round(x * exchange_rate["EUR"], 2) for x in df['MC_USD_Billions']]
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate["GBP"], 2) for x in df['MC_USD_Billions']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate["INR"], 2) for x in df['MC_USD_Billions']]
    print("Transformation process complete! \n")
    return df


def load_to_csv(df, output_path):
    print("Initializing loading to CSV process... ")
    df.to_csv(output_path)
    print("Data saved to CSV file. \n")


def load_to_db(df, sql_connection, table):
    print("SQL Connection initiated")
    df.to_sql(table, sql_connection, if_exists='replace', index=False)
    print("Data loaded to database as table. \n")


def run_query(query_statement, sql_connection):
    print(F"Running the query: '{query_statement}'")
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output + "\n")


url_page = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes = ["Bank_Name", "MC_USD_Billions"]
db_name = "Banks.db"
table_name = "Largest_banks"
exchange_rate_file = "./exchange_rate.csv"
csv_path = "./Largest_Banks.csv"


log_progress("Starting ETL Pipeline!")
dataframe = extract(url_page, table_attributes)

log_progress("Data Extraction complete. Initializing transform process...")
dataframe = transform(dataframe, exchange_rate_file)

log_progress("Data Transformation complete. Initializing loading process...")
load_to_csv(dataframe, csv_path)

# sql_connection = sqlite3.connect(db_name)
# log_progress("SQL Connection initiated")
# load_to_db(df, sql_connection, table_name)

# log_progress("Data loaded to database as table. Running the query...")
# query_statement_1 = f"SELECT * from {table_name}"
# query_statement_2 = f"SELECT AVG(MC_GBP_Billion) from {table_name}"
# query_statement_3 = f"SELECT Name from {table_name} LIMIT 5"
# run_query(query_statement, sql_connection)