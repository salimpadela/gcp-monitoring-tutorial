import os
import random
from time import sleep

from flask import Flask, Response, make_response

app = Flask(__name__)

latency_lower_bound=0.1
latency_upper_bound=0.9

response_codes = [200,401,500]


@app.route('/')
def hello():

    random_latency = random.uniform(latency_lower_bound, latency_upper_bound)
    sleep(random_latency)

    
    resp = make_response(f"<h1>Thank you for visiting the website!!!.</br> Your request's HTTPStatus code was 200.</h1>" , 200)
    
    return resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
