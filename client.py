# Member 2:
# Client-side networking

import socket
import json

from config import HOST, PORT


def send_request(request):

    """
    Send request to Python server
    and receive response.
    """

    try:

        # Create TCP socket
        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # Set connection timeout
        client.settimeout(5)

        # Connect to server
        client.connect(
            (HOST, PORT)
        )

        # Convert Python dictionary
        # into JSON
        data = json.dumps(request)

        # Send request
        client.sendall(
            data.encode("utf-8")
        )

        # Receive response
        response = client.recv(
            16384
        ).decode("utf-8")

        # Close connection
        client.close()

        # Convert JSON back to dictionary
        return json.loads(response)


    except Exception as error:

        return {

            "success": False,

            "message":
                f"Server connection failed: {error}"
        }