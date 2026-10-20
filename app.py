
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>YMB Banking Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                text-align: center;
                margin: 0;
            }
            header {
                background: #17365d;
                color: white;
                padding: 30px;
            }
            main {
                background: white;
                max-width: 700px;
                margin: 40px auto;
                padding: 30px;
                border-radius: 10px;
            }
            h2 {
                color: #17365d;
            }
            footer {
                margin-top: 30px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Yarrow-Mullein Bank</h1>
            <p>Banking Application</p>
        </header>

        <main>
            <h2>Welcome to YMB Online Banking</h2>
            <p>This application is running dynamically using Python Flask.</p>
            <p><strong>Server Time:</strong> {{ current_time }}</p>
            <p>Docker Deployment Project - COMP-4001</p>
        </main>

        <footer>
            <p>Yarrow-Mullein Bank | Educational Demo</p>
        </footer>
    </body>
    </html>
    """, current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5090)
