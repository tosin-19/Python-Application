from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Flask on AWS EC2 via GitHub Actions!"

if __name__ == "__main__":
    # Runs on port 5000 by default
    app.run(host="0.0.0.0", port=5000)
