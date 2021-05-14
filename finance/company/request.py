import csv
import urllib
import psycopg2
import json
import os

from finance.settings import MEDIA_ROOT


def chek_if_table(table_name):
    """The function checks for the presence of a table"""

    conn = psycopg2.connect("host=localhost dbname=finance user=beksultan password=beksultan")
    cursor = conn.cursor()
    cursor.execute("select * from information_schema.tables where table_name=%s", (table_name,))
    bool_cond = bool(cursor.rowcount)
    return bool_cond


def create_tables(name_table, csv_column_name=None):
    """" Function for create table """

    create_table_query = '''CREATE TABLE {}
            (
              date date ,
              open  varchar(255),
              high varchar(255) ,
              low varchar(255),
              close varchar(255),
              adjclose varchar(255),
              volume varchar(255)
               );'''.format(name_table)
    conn = psycopg2.connect("host=localhost dbname=finance user=beksultan password=beksultan")
    cursor = conn.cursor()
    with conn:
        cursor.execute(create_table_query)
        conn.commit()


def commit_psql(csv_name, csv_path, name_table):
    """For commit from csv data to Postgresql"""

    conn = psycopg2.connect("host=localhost dbname=finance user=beksultan password=beksultan")
    cur = conn.cursor()
    os.chdir(csv_path)
    with open(csv_name, 'r') as f:
        next(f)
        cur.copy_from(f, name_table, sep=',')
    conn.commit()
    f.close()


def get_csv(url, file_path=None):
    """Test function for modifikation"""

    sec_url = url[url.find("d/") + 2:]
    third_url = '-'.join(sec_url.split('?')[:-1])
    csv_path = f"{MEDIA_ROOT}/csv/"
    os.chdir(csv_path)
    name_csv = f"{third_url}.csv"
    csv = urllib.request.urlretrieve(url, name_csv)
    if not chek_if_table(third_url):
        create_tables(third_url)
    commit_psql(name_csv, csv_path, third_url)


def read_CSV(file, json_file):
    """Test function modifikation"""

    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]: row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)
    csvfile.close()


def convert_write_json(data, json_file):
    """Test function modifikation"""

    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))  # for pretty
        f.write(json.dumps(data))
    f.close()
