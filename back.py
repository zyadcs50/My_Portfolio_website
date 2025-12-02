from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zezozoz131@gmail.com'
app.config['MAIL_PASSWORD'] = 'pwlq puxy gjuz lfja'

mail = Mail(app)

# Route الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html")

# Route إرسال البريد
@app.post("/send-email")
def send_email():
    data = request.json
    full_name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not full_name or not email or not message:
        return jsonify({"status": "error", "message": "All fields are required."})
    msg = Message(
        subject="New message from website",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']]
    )

    msg.body = f"""
New message from your website:

Name: {full_name}
Email: {email}
Message:
{message}
"""

    try:
        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
