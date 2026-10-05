import speedtest
import time
import tweepy
import os

API_KEY = os.getenv("CONSUMER_KEY")
API_SECRET = os.getenv("CONSUMER_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def send_complaint_tweet(speed: float, target_speed: float, isp_handle: str = "@Airtel_Presence"):
    """Posts a complaint tweet when internet speed is below threshold."""
    message = (
        f"Hey {isp_handle}, I am paying for {target_speed:.0f} Mbps, "
        f"but my speed is currently averaging {speed:.2f} Mbps. "
        f"Please fix this connection issue."
    )
    
    try:
        response = client.create_tweet(text=message)
        print(f"Complaint posted successfully! Tweet ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"Failed to send tweet: {e}")

st = speedtest.Speedtest()
st.get_best_server()
download_speeds = []
upload_speeds = []
num_tests = 3
for _ in range(num_tests):
    download_speed = st.download() / 1_000_000. # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  
    download_speeds.append(float(f"{download_speed:.2f}"))
    upload_speeds.append(float(f"{upload_speed:.2f}"))
    time.sleep(2)
    
average_download_speed = sum(download_speeds) / num_tests
average_upload_speed = sum(upload_speeds) / num_tests
print(f"Average Download Speed: {average_download_speed:.2f} Mbps")
print(f"Average Upload Speed: {average_upload_speed:.2f} Mbps")

promised_download_speed = 10.0 # Example promised download speed in Mbps
promised_upload_speed = 5.0 # Example promised upload speed in Mbps

if average_download_speed < promised_download_speed or average_upload_speed < promised_upload_speed:
    send_complaint_tweet(average_download_speed, promised_download_speed)
else:
    print ("Internet speed is within the promised range. No complaint needed.")        