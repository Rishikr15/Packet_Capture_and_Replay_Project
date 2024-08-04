import requests
import pyshark

url = 'http://localhost:8000/'  
save_url = 'http://localhost:8000/save'  # Endpoint to save packets to a file

file_path = '/home/rishi/Desktop/TELAVERGE/captured.pcap' 

# Read and send packets
cap = pyshark.FileCapture(file_path, use_json=True, include_raw=True)

for packet in cap:
    # Ensure you are sending raw packet bytes correctly
    raw_packet = packet.get_raw_packet()
    response = requests.post(url, data=raw_packet)
    print(response.text)

cap.close()

save_response = requests.get(save_url)
print(save_response.text) 