from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('Bootstrap_ex1.html') #render_template('index.html') render_template('Bootstrap_ex1.html')


@app.route('/about')
def about():
    return render_template('about.html')




app.run()



role = 'admin'

{% if {{role}} == "admin" %}
    print('yra')

# {% if "role" = admin %}
# {% if (role) == "admin" %}
# {{ if {{role}} == "admin" }}