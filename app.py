import os
from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Navigation link routes
@app.route("/")
def index():
    return render_template("index.html");

@app.route("/index")
def home():
    return render_template("index.html");

# Different Beam
@app.route("/simple")
def simple():
   return render_template("simple.html");

# Simple Beam Option Routes
@app.route("/simple1")
def simple1():
    return render_template("simple1.html");

@app.route("/simple2")
def simple2():
    return render_template("simple2.html");

@app.route("/simple3")
def simple3():
    return render_template("simple3.html");

@app.route("/simple4")
def simple7():
    return render_template("simple4.html");

@app.route("/simple5")
def simple8():
    return render_template("simple5.html");

@app.route("/simple6")
def simple9():
    return render_template("simple6.html");

@app.route("/cantilever")
def cantilever():
    return render_template("cantilever.html");

# Cantilever Beam Option Routes
@app.route("/cantilever1")
def cantilever1():
    return render_template("cantilever1.html");

@app.route("/cantilever2")
def cantilever2():
    return render_template("cantilever2.html");

@app.route("/cantilever3")
def cantilever3():
    return render_template("cantilever3.html");

@app.route("/fix-support")
def fix_support():
    return render_template("fix-support.html");

# Fix-Support Beam Option Routes
@app.route("/fix-support1")
def fix_support1():
    return render_template("fix-support1.html");

@app.route("/fix-support2")
def fix_support2():
    return render_template("fix-support2.html");

@app.route("/fix-support3")
def fix_support3():
    return render_template("fix-support3.html");

@app.route("/fixed")
def fixed():
    return render_template("fixed.html");

# Fixed Beam Option Routes
@app.route("/fixed1")
def fixed1():
    return render_template("fixed1.html");

@app.route("/fixed2")
def fixed2():
    return render_template("fixed2.html");

@app.route("/fixed3")
def fixed3():
    return render_template("fixed3.html");