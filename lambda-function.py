import json
import boto3
import psycopg2
import os
import time

def lambda_handler(event, context):
    # rds保存処理
    try:
        conn = psycopg2.connect(host=os.environ['RDS_ENDPOINT'], database=os.environ['RDS_DBNAME'], user=os.environ['RDS_USR'],password=os.environ['RDS_PASS'], connect_timeout=3)
        cur = conn.cursor()
        cur.execute(INSERT INTO News VALUES (2, 'b', '2021/06/08 12:00:01', 'c'))
        results = conn.commit()
        print(results)
    except psycopg2.OperationalError as e:
        print(str(e))
    return {
        'statusCode': 200,
        'body': json.dumps('ok!')
    }
