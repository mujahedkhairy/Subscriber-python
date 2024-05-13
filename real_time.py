import os
from realtime.connection import Socket
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.env')
load_dotenv(dotenv_path)

url: str = os.environ.get("SUPABASE_URL")
API_KEY: str = os.environ.get("SUPABASE_KEY")
SUPABASE_ID: str = os.environ.get("SUPABASE_ID")
# API_KEY: str ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcW5ndGxjcWxtamFkZnpqY3dvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTUxODIxNjEsImV4cCI6MjAzMDc1ODE2MX0.rchZx-t4mh9vZc8P8T-PfMusZVlpRD6IJixPz6wyczY"
# SUPABASE_ID: str ="bfqngtlcqlmjadfzjcwo"


def callback1(payload):
    print("Callback 1: ", payload)


if __name__ == "__main__":
    URL = f"wss://{SUPABASE_ID}.supabase.co/realtime/v1/websocket?apikey={API_KEY}&vsn=1.0.0"
    s = Socket(URL)
    s.connect()

    channel_1 = s.set_channel("realtime:*")
    channel_1.join().on("UPDATE", callback1)
    channel_1.join().on("INSERT", callback1)
    channel_1.join().on("DELETE", callback1)

    s.listen()
