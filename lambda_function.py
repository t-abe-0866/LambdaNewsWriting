import json
import psycopg2
import os
import feedparser

def lambda_handler(event, context):
    # rds保存処理
    try:
        conn = psycopg2.connect(host=os.environ['RDS_ENDPOINT'], database=os.environ['RDS_DBNAME'], user=os.environ['RDS_USR'],password=os.environ['RDS_PASS'], connect_timeout=3)
        cur = conn.cursor()
        
        #スクレイピング
        d = feedparser.parse('https://www.lifehacker.jp/feed')
        for entry in d.entries:
            cur.execute('INSERT INTO news (title,date,link) VALUES (%s,%s,%s)',(entry.title,entry.lastBuildDate,entry.link))
        results = conn.commit()
        print(results)
    except psycopg2.OperationalError as e:
        print(str(e))
    return {
        'statusCode': 200,
        'body': json.dumps('ok!')
    }