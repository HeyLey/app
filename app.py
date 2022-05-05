from flask import Flask, render_template, request, session, redirect, url_for
import logging

from google.cloud import bigquery

app = Flask(__name__)
log_level = logging.INFO


@app.route('/')
def index():
    return render_template("info.html"), 200


@app.route('/table')
def get_table():
    df = get_bq_table("2022-05-01")

    return df.to_html()


def get_bq_table(date):
    project_id = 'datos-collector'
    client = bigquery.Client.from_service_account_json('ley.json')
    sql = "SELECT * FROM `prod_dataset.product_astian` DATE(fileDate)='{}'".format(date)
    df = client.query(sql, project=project_id).to_dataframe()
    return df


def get_access_log():
    pass


def get_error_log():
    pass


def update(interval):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
