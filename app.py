from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    """Show Header asking for Pokemon to use"""
    return render_template("index.html")


@app.route("/error")
def error():
    """Give User an Error Message and Direct them to Some Popular Pokemon"""
    return render_template("buy.html")


@app.route("/paste", methods=["GET", "POST"])
def paste():
    """Display team in format to copy and paste into Pokemon Showdown"""
    return render_template("paste.html")
