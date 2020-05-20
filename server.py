from flask import Flask, render_template, request
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_csv_database(data):
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as csv_database:
        text = f"\n{name}, {email}, {subject}, {message}"
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv_database(data)
        return render_template('/thankyou.html', name=data['name'])
    else:
        return 'something went wrong'
