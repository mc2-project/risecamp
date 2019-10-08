import pandas as pd
import subprocess

def network_analysis(master, worker_1, worker_2, worker_3):
    tshark_cmd = 'tshark -r capture.pcap -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ip.dst -e frame.len -E header=y -E separator=, > capture.csv'
    tshark_process = subprocess.Popen(tshark_cmd, stdout=subprocess.PIPE, shell=True)
    while tshark_process.poll() is None:
        continue

    capture = pd.read_csv('capture.csv', names=['Frame Number', 'Ethernet Source', 'Ethernet Destination', 
                                            'IP Source', 'IP Destination', 'Frame Length'], header=0)
    capture.dropna(subset=['IP Source', 'IP Destination'], inplace=True)

    labels = {master: 'Master', worker_1: 'worker_1', worker_2: 'worker_2', worker_3: 'worker_3'}
    capture.replace(labels, inplace=True)

    capture['Transmission'] = capture.apply(lambda row: row['IP Source'] + ' -> ' + row['IP Destination'], axis=1)
    count_bytes = capture.groupby('Transmission', as_index=False)['Transmission', 'Frame Length'].sum()
    count_bytes.rename(mapper={'Frame Length': 'Total Bytes Transmitted'}, inplace=True, axis=1)
    count_packets = capture['Transmission'].value_counts().rename_axis('Transmission').reset_index(name='Number of Packets')

    count_bytes.set_index('Transmission', inplace=True)
    count_packets.set_index('Transmission', inplace=True)
    counts = count_packets.join(count_bytes, on='Transmission')
    counts.sort_values(by='Total Bytes Transmitted', inplace=True, ascending=False)
    return counts