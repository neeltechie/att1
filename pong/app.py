#!/usr/bin/env python
import connexion
import socket

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def bookget():
    return {"hostname": socket.gethostname()}, 200


if __name__ == "__main__":
    app = connexion.FlaskApp(__name__)
    app.add_api("swagger.yaml")
    app.run(host="0.0.0.0", port=6000)
