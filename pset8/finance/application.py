import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Look up user
    users = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])
    quotes = {}

    for stock in stocks:
        quotes[stock["symbol"]] = lookup(stock["symbol"])

    cash_remaining = users[0]["cash"]
    total = cash_remaining

    return render_template("portfolio.html", quotes=quotes, stocks=stocks, total=total, cash_remaining=cash_remaining)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # Query Symbol and Get shares
        symbol = lookup(request.form.get("symbol"))
        shares = request.form.get("shares")
        shares_int = int(shares)

        # Check user input
        if symbol == None:
            return apology("Invalid Symbol")

        # Check shares are positive
        if shares_int <= 0:
            return apology ("You must buy a positive number of shares", 400)

        # Query database for username
        user = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])

        # Get User Funds & Share Price
        user_funds = user[0]["cash"]
        price_per_share = symbol["price"]

        # Total Share Price
        total_price = price_per_share * shares_int

        # Check User Funds
        if total_price > user_funds:
            return apology("Insufficient Funds")

        # Buys Shares
        db.execute("UPDATE users SET cash = cash - :price WHERE id = :user_id", price=total_price, user_id=session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price_per_share) VALUES(:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"],
                   symbol=request.form.get("symbol"),
                   shares=shares,
                   price=price_per_share)

        # Redirect User to Homepage
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    # Check Username is Available for New User
    username = request.args.get("username")

    # Check for user in DB
    username_available = len(db.execute(f"SELECT username FROM users WHERE username = '{username}'")) == 0

    # BOOL is User Available
    is_available = False if len(username) < 2 or not username_available else True

    # Return boolean status of if username is valid and available
    return jsonify(is_available)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute("SELECT symbol, shares, price_per_share, created_at FROM transactions WHERE user_id = :user_id ORDER BY created_at ASC",
                        user_id = session["user_id"])

    return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Check username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Check password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Check username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))

        # Check for user input
        if quote == None:
            return apology("Please Provide a Symbol")

        # Return Quote
        return render_template("quoted.html", quote=quote)

    # Return Quote Page
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register User"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not request.form.get("username"):
            session.clear()
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            session.clear()
            return apology("must provide password", 400)

        # Ensure Passwords Match
        elif password != confirmation:
            session.clear()
            return apology("Passwords Do Not Match")

        # Ensure Username is not taken
        username_taken = len(db.execute(f"SELECT username FROM users WHERE username = '{username}'")) > 0
        if (username_taken):
            return apology("username taken")

        # ALL OK insert user into DB
        else:
            password_hash = generate_password_hash(password)
            user = db.execute("INSERT INTO users (username, hash) VALUES (:username, :password_hash)",
            username = username,
            password_hash = password_hash,
        )

        # If User Exists Return
        if not user:
            session.clear()
            return apology("Username Taken")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        # Query Symbol and Get shares
        symbol = lookup(request.form.get("symbol"))
        shares = request.form.get("shares")
        shares_float = float(shares)

        # Check user input
        if symbol == None:
            return apology("Invalid Symbol", 400)

        # Check shares are positive
        if shares_float < 0:
            return apology ("You must sell a positive number of shares", 400)

        # Get Users shares
        stock = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id AND symbol = :symbol GROUP BY symbol",
                           user_id=session["user_id"], symbol=request.form.get("symbol"))

        # Ensure User has shares to sell
        if len(stock) != 1 or stock[0]["total_shares"] <= 0 or stock[0]["total_shares"] < shares:
            return apology("you can't sell less than 0 or more th                                  an you own", 400)

        # Query database for username
        user = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])

        # Get users Cash
        cash_remaining = user[0]["cash"]
        price_per_share = symbol["price"]

        # Calculate Total Share Value
        total_price = price_per_share * shares

        # Sell Shares and update DB
        db.execute("UPDATE users SET cash = cash + :price WHERE id = :user_id", price=total_price, user_id=session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price_per_share) VALUES(:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"],
                   symbol=request.form.get("symbol"),
                   shares=-shares,
                   price=price_per_share)

        return redirect("/")

    else:
        stocks = db.execute(
            "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])

    return render_template("sell.html")

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change Users Password"""

    # IF request method Post
    if request.method == "POST":

        # Get current users session id
        user_id = session["user_id"]

        # Get user data from db
        user_data = db.execute(f"SELECT * FROM users WHERE id = {user_id}")

        # Get user input
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        # Check for Input
        if not check_password_hash(user_data["hash"], new_password):
            return apology("Invalid Password Try Again", 400)

        # Check for input
        if not check_password_hash(user_data["hash"], new_password):
            return apology("New password cannot be the same as old password", 400)

        # Generate new hash and input to db
        new_password_hash = generate_password_hash(new_password)
        db.execute(f"UPDATE users SET hash = '{new_password_hash}' WHERE id = {user_data}")
        return redirect("/")

    # Return HTML change pass page
    else:
        return render_template("change_password.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
