from flask import Flask, render_template, jsonify
from utils import *
from logger import *
app = Flask(__name__, template_folder='templates')
log = get_logger(__name__)


@app.route("/")
def main_page():
    posts = load_all()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:todayid>")
def today_page(todayid):
    post = get_info_today(todayid)
    return render_template("post.html", post=post)


@app.route("/api/posts")
def api_main_page():
    posts = load_all()
    log.info("load info")
    return jsonify(posts)


@app.route("/api/posts/<int:todayid>")
def api_post_page(todayid):
    post = today_page(todayid)
    log.info("load info{todayid}")
    return jsonify(post)

@app.errorhandler(404)
def page_error_404(e):
    return '<h1>Error</h1><p>not found(((</p>', 404


@app.errorhandler(500)
def page_error_500(e):
    return '<h1>Error</h1><p>not found(((</p>', 500

app.run()
