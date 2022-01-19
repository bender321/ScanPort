import nmap
import sys
import time
import json

HOST = '127.0.0.1'
WAIT_POINT = 5

class PortMonitor:

    def __init__(self):
        self._nmScan = nmap.PortScanner()
        self._args = sys.argv

        self._number_of_scans = 1
        self._res = []

        self._save_result = False
        self._read_result = False
        self._visual = False

        self._host = HOST
        self._wait_point = WAIT_POINT

    def setup_run(self):

        self._args.pop(0)
        counter = 0

        for arg in self._args:
            if arg == '-s':
                self.save_result = True
                counter += 1

            elif arg == '-r':
                self.read_result = True
                counter += 1

            elif arg == '-v':
                self._visual = True
                counter += 1

            elif '-t=' in arg:
                self._number_of_scans = int(arg[3:])
                counter += 1
            else:
                break
        self.args = self._args[counter:]
        self._run()

    def _run(self):
        i = 0
        while i < self._number_of_scans:
            ports = {}
            for arg in self.args:
                try:
                    print('scannig...')
                    scan_res = self._nmScan.scan(self._host, arg)
                    state = scan_res['scan'][self._host]['tcp'][int(arg)]['state']
                    ports[str(arg)] = state.upper()
                except Exception as e:
                    print('Wrong parameters were given...')
                    exit(-1)

            record = {
                "timestamp": str(int(time.time())),
                "ports": ports
            }
            self._res.append(record)

            time.sleep(self._wait_point)
            i += 1
            if self._visual:
                print(self._res)

        if self._save_result:
            self._write()

        if self._read_result:
            self._read()

        print('Done')
        exit(1)

    def _write(self):
        try:
            with open('scan_results.json', 'w', encoding='utf-8') as f:
                json.dump(self._res, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)

    def _read(self):
        try:
            with open('scan_results.json') as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        else:
            for i in data:
                print(i)


if __name__ == "__main__":
    monitor = PortMonitor()
    monitor.setup_run()
