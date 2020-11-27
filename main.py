import sys
import requests
import json
import csv
import time

def main():
    args = sys.argv
    app_id = args[1]
    token = args[2]
    sample_type = args[3]
    query_params = args[4]
    file_name = args[5]
    base_url = "https://appsignal.com/api/% s/samples/"% app_id
    samples_url = base_url + "% s.json?token=% s% s"%(sample_type, token, query_params)
    print(base_url)
    print(samples_url)

    response = requests.get(samples_url).json()

    # print(response)
    current_time = time.time()
    with open('% s-% s.csv'%(file_name, current_time), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        if sample_type == "performance":
            csv_writer.writerow(['Time', 'Duration', 'API path', 'Is Exception?'])
            for entry in response['log_entries']:
                csv_writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry['time'])), entry['duration'], entry['path'], entry['is_exception']])
        else:
            csv_writer.writerow(['Error Id on Appsignal', 'Action', 'Exception Name', 'Exception Message', 'Headers', 'Params'])
            for entry in response['log_entries']:
                sample_url = base_url + "% s.json?token=% s"%(entry['id'], token)
                print(sample_url)
                sample_log = requests.get(sample_url).json()
                csv_writer.writerow([sample_log['id'], sample_log['action'], sample_log['exception']['name'], sample_log['exception']['message'], sample_log['environment'], sample_log['params']])

if __name__=="__main__": 
    main()