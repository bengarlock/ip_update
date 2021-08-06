import requests
from passwords import return_username, return_password
from datetime import datetime
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f'{dir_path}ip_log.txt')

my_ip = requests.get('https://myip.dnsomatic.com/')
my_ip = str(my_ip.text)

url = f'https://{return_username(1)}:{return_password(1)}@domains.google.com/nic/update?hostname=bengarlock.com&myip={my_ip}'
update_ip_response1 = requests.post(url)

url = f'https://{return_username(2)}:{return_password(2)}@domains.google.com/nic/update?hostname=www.bengarlock.com&myip={my_ip}'
update_ip_response2 = requests.post(url)

with open(f'{dir_path}ip_log.txt', 'a', encoding='utf-8') as file:
    file.write(f'{datetime.now()}       bengarlock.com          {update_ip_response1.text} \n')
    file.write(f'{datetime.now()}       www.bengarlock.com      {update_ip_response2.text} \n')

