from flask import Flask, render_template

from datetime import datetime

import pytz



app = Flask(__name__)



def get_time_in_timezone(timezone):

    tz = pytz.timezone(timezone)

    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')



@app.route('/')

def home():

    times = {

        "Polska": get_time_in_timezone("Europe/Warsaw"),

        "USA (Nowy Jork)": get_time_in_timezone("America/New_York"),

        "Chiny (Pekin)": get_time_in_timezone("Asia/Shanghai"),

        "Turcja": get_time_in_timezone("Europe/Istanbul")


    }

    return render_template('index.html', times=times)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

