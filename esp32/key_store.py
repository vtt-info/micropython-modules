# This file creates, dumps, and removes the key_store.db file

import btree

file = 'key_store.db'

def update():
    try:
        f = open(file, 'r+b')
    except OSError:
        f = open(file, 'w+b')
    db = btree.open(f)

    db[b'ssid_name'] = input('Enter WiFi SSID: ')
    db[b'ssid_pass'] = input('Enter WiFi password: ')
    db[b'mqtt_broker'] = input('Enter the MQTT Server IP: ')

    db.flush()
    print("%s, %s, and %s added to %s file" % (db[b'ssid_name'].decode('utf-8'), db[b'ssid_pass'].decode('utf-8'), db[b'mqtt_broker'].decode('utf-8'), file))
    db.close()


def dump():

    f = open(file, 'r+b')
    db = btree.open(f)

    for key in db:
        print(key.decode('utf-8'), db[key].decode('utf-8'))

    db.close()


def remove():
    import uos
    uos.remove(file)
    print('%s removed' % file)