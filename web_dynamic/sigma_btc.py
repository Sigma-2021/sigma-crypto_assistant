#!/usr/bin/python3
"""File containing methods for rendering templates"""

from flask.wrappers import Request
from objects import btc, doge, eth
import persistence
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Rendering index template"""
    return render_template('index.html')

@app.route('/landing-page', strict_slashes=False)
def landing_page():
    """Rendering landing page template"""
    return render_template('landing_page.html')


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """Rendering bitcoin template"""
    btc.refresh_coin(btc.name)
    eth.refresh_coin(eth.name)
    doge.refresh_coin(doge.name)
    return render_template('bitcoin.html', btc=btc, eth=eth, doge=doge)

@app.route('/ethereum', strict_slashes=False)
def ethereum():
    """Rendering ethereum template"""
    btc.refresh_coin(btc.name)
    eth.refresh_coin(eth.name)
    doge.refresh_coin(doge.name)
    return render_template('ethereum.html', btc=btc, eth=eth, doge=doge)

@app.route('/dogecoin', strict_slashes=False)
def dogecoin():
    """Rendering dogecoin template"""
    btc.refresh_coin(btc.name)
    eth.refresh_coin(eth.name)
    doge.refresh_coin(doge.name)
    return render_template('dogecoin.html', btc=btc, eth=eth, doge=doge)

@app.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    """Rendering suscribe template."""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        persistence.insert_new_user(str(name), str(email))
        return redirect("/")
    return render_template('subscribe.html')

if  __name__ == "__main__":
    """Main Function"""
    app.run(host='0.0.0.0', port='5000')
