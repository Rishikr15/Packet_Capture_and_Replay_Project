from flask import Flask, request, jsonify
from scapy.all import wrpcap, Ether

app = Flask(__name__)
packets = []

@app.route('/', methods=['POST'])
def receive_packet():
    packet_data = request.data  
    try:
        packet = Ether(packet_data)
        packets.append(packet)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Packet received successfully.'}), 200

@app.route('/save', methods=['GET'])
def save_packets():
    if packets:
        wrpcap('received_packets2.pcap', packets)
        packets.clear()
        return jsonify({'message': 'All packets saved.'}), 200
    else:
        return jsonify({'message': 'No packets to save.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
