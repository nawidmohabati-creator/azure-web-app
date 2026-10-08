from flask import Flask, abort, render_template
from datetime import datetime

from dotenv import find_dotenv, load_dotenv

from azure_web_app import auth, db
from azure_web_app._constants import SECRET_ENV_FILE


FAVORITES = [
    {"id": 1, "title": "Network Security", "why": "I like learning how networks can be protected."},
    {"id": 2, "title": "Ethical Hacking", "why": "I like learning how to find and fix security weaknesses."},
    {"id": 3, "title": "Digital Forensics", "why": "I like learning how digital evidence can be investigated."},
    {"id": 4, "title": "Cyber Defense", "why": "I like learning how to protect systems from cyber attacks."},
]

CYBER_TOOLS = [
    {
        "name": "Wireshark",
        "purpose": "Analyze network traffic",
        "category": "Network Security",
        "beginner_friendly": True,
    },
    {
        "name": "Nmap",
        "purpose": "Scan and discover devices on a network",
        "category": "Network Security",
        "beginner_friendly": True,
    },
    {
        "name": "Burp Suite",
        "purpose": "Test web application security",
        "category": "Web Security",
        "beginner_friendly": True,
    },
    {
        "name": "Metasploit",
        "purpose": "Practice security testing in authorized environments",
        "category": "Security Testing",
        "beginner_friendly": False,
    },
    {
        "name": "Autopsy",
        "purpose": "Investigate digital evidence",
        "category": "Digital Forensics",
        "beginner_friendly": True,
    },
]

def create_app():
    load_dotenv(find_dotenv(SECRET_ENV_FILE))
    app = Flask(__name__)
    db.setup_for_app(app)
    auth.setup_auth(app)
    setup_routes(app)
    return app


def index():
    return render_template(
        "index.html",
        name="Nawid",
        hobby="Cybersecurity",
        hours_per_week=5,
        fun_fact="I enjoy learning about technology.",
        hour=datetime.now().hour,
        show_counter=False,
        favorites=FAVORITES
        
    )

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)


def cyber_tools():
    return render_template(
        "cyber_tools.html",
        tools=CYBER_TOOLS
    )

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/cyber-tools")(cyber_tools)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
