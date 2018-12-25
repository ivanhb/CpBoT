
my_commands = {
    "/howToContactYou" : {"module": "ivanhbbot", "method": "how_to_contact_you", "notes":""},
}

ivanhb = {}

def get_my_commands():
    return my_commands


def update_date():
    urls = {
        'content_config.js':'https://ivanhb.github.io/content_config.js'
    }

    for url_entry in urls:
        url = urls[url_entry]
        r = requests.get(url, allow_redirects=True)
        open('data/'+url_entry, 'wb').write(r.content)
    return "Ivanhb status updated!"


def how_to_contact_you():
    str_contacts = ""
    with open('data/ivanhbbot/contacts.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            str_contacts = row['name']+": "+row['value']

    return str_contacts
