import os, subprocess
import time

class GoogleProxy(object):

    def __init__(self, credentials_dict):
        # Start proxy
        self.port = credentials_dict.get('port', 3306)
        self.proxy_path = os.path.join('..','credentials','cloud_sql_proxy.exe')
        self.instances_string = '-instances=memoriadaesgrimabrasileira:us-central1:memoriadaesgrimabrasileira=tcp:' + \
                            str(self.port)
        self.proxy_credentials_string = '-credential_file=' + os.path.join('..','credentials','proxy_credentials.json')

    def open(self):
        self.proxy_subprocess = subprocess.Popen([self.proxy_path, self.instances_string, self.proxy_credentials_string])

        # TODO replace this with a proper check for whether the proxy has been opened correctly
        time.sleep(5)

        if self.proxy_subprocess and not self.proxy_subprocess.poll():
            print('\nProxy do Google aberto na porta', self.port)
            print('Subprocess ID: ', self.proxy_subprocess.pid, '\n')


    def close(self):
        # close proxy
        while not self.proxy_subprocess.poll():
            self.proxy_subprocess.terminate()
        print('\nProxy do Google terminado.')
