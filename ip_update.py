import requests
from passwords import return_username, return_password

my_ip = requests.get('https://myip.dnsomatic.com/')
my_ip = str(my_ip.text)


url = f'https://{return_username(1)}:{return_password(1)}@domains.google.com/nic/update?hostname=bengarlock.com&myip={my_ip}'
update_ip_response1 = requests.post(url)

url = f'https://{return_username(2)}:{return_password(2)}@domains.google.com/nic/update?hostname=www.bengarlock.com&myip={my_ip}'
update_ip_response2 = requests.post(url)

print(update_ip_response1.text)
print(update_ip_response2.text)
