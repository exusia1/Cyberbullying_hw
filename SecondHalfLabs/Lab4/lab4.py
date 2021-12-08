import re

f = open('small_log.crash', 'r')

messages = f.read().split('\n')

ip_set = set()
host_set = set()
tag_set = set()
print(messages[0])

for msg in messages:
    ips = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', msg)
    for ip in ips:
        ip_set.add(ip)

    hostname = re.search('([0-9]{1,2}[:]){2}[0-9]{1,2}[\s][^\s]*', msg)
    if hostname is None:
        continue
    host_set.add(hostname.group(0).split()[1])

    tag = re.search('master [^\s]*', msg)
    if not(tag is None):
        tag_set.add(tag.group(0).split()[1])

    tag = re.search('backup [^\s]*', msg)
    if not(tag is None):
        tag_set.add(tag.group(0).split()[1])

    tag = re.search('([0-9]{1,2}[:]){2}[0-9]{1,2}([\s][^\s]*){3}', msg)  # сразу после хостнейма
    if not(tag is None) and tag.group(0).split()[2] not in ['master', 'last', 'backup']:  # убираю слова которые могут идти перед тэгом
        tag_set.add(tag.group(0).split()[2])
        print(tag.group(0).split()[2])
        print(msg)

f.close()

f = open('ips.txt', 'w+')

for ip in ip_set:
    f.write(ip + '\n')
f.close()

f = open('hostnames.txt', 'w+')
for hostname in host_set:
    f.write(hostname + '\n')

f.close()

f = open('tags.txt', 'w+')
for tag in tag_set:
    f.write(tag + '\n')

f.close()
