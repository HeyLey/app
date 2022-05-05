from flask import Flask, render_template, request, session, redirect, url_for
import logging

from google.cloud import bigquery

app = Flask(__name__)
log_level = logging.INFO

@app.route('/')
def nginx_auth():
   # if 'X-Juddling' in request.headers:
    return render_template("info.html"), 200
#    else:
 #       return "Error", 401

def get_bq_table(date):
    project_id = 'datos-collector'
    client = bigquery.Client.from_service_account_json('ley.json')
    sql = "SELECT * FROM `prod_dataset.product_astian` DATE(fileDate)='{}'".format(date)
    df = client.query(sql, project=project_id).to_dataframe()
    df.to_csv("static/data.csv")

def get_access_log():
    pass

def get_error_log():
    pass

def update(interval):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)