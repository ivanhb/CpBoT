
import csv
import datetime
import re

my_commands = {
    "/turniPulizie" : {"module": "triplev", "method": "turni_pulizie", "notes":" Visualizza i turni di pulizia"},
    "/aggiungiSpesa" : {"module": "triplev", "method": "add_entry", "notes":" Aggiungi una spesa comune (esempio: 'pane,2,ivan')"},
    "/eliminaSpesa" : {"module": "triplev", "method": "remove_entry", "notes":" Elimina una spesa comune (esempio: 'pane')"},
    "/svuotaListaSpesa" : {"module": "triplev", "method": "remove_all", "notes":" Svuota la lista della spesa comune"},
    "/listaSpesa" : {"module": "triplev", "method": "get_list", "notes":" Visualizza la lista della spesa comune"},
}


def get_my_commands():
    return my_commands


def update_data():
    urls = {
        'content_config.js':'https://ivanhb.github.io/content_config.js'
    }

    #for url_entry in urls:
    #    url = urls[url_entry]
    #    r = requests.get(url, allow_redirects=True)
    #    open('data/'+url_entry, 'wb').write(r.content)
    return "TripleV data updated !"

def turni_pulizie(a_text):
    time_now = datetime.datetime.now();
    str_contacts = ""
    with open('data/triplev/calendar.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            c_data = datetime.datetime.strptime(row['Data'], '%d/%m/%Y')
            if c_data > time_now:
                return "\n"+ "Data: "+row['Data'] + "\n"+ "Cucina -> "+row['Cucina'] + "\n"+ "Bagno -> "+row['Bagno'] + "\n"+ "Corridoio -> "+row['Corridoio'] + "\n"
                break

    return str_contacts


def add_entry(a_text):
    name = ""
    value = ""
    person = ""
    try:
        parts = re.match( r'(.*),(.*),(.*)', a_text[0], re.M|re.I)
    except Exception as e:
        return "Formato del messaggio non corretto! (esempio: 'pane,2,ivan')."

    if parts:
        name = parts.group(1)
        value = parts.group(2)
        person = parts.group(3)
        file = open('data/triplev/spese.csv','a')
        file.write('\n'+name+','+value+','+person)
        file.close()
        return "Elemento '"+name+"' inserito!"
    else:
        return "Formato del messaggio non corretto! (esempio: 'pane,2,ivan')."




def remove_entry(a_text):
    new_entries = []
    with open('data/triplev/spese.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if a_text[0] in row['name']:
                continue
            else:
                new_entries.append(row)

    remove_all("")
    file = open('data/triplev/spese.csv','a')
    for e in new_entries:
        file.write('\n'+e['name']+','+e['value']+','+e['person'])

    file.close()
    return "L'elemento '"+a_text[0]+"' è stato cancellato dalla lista."


def remove_all(a_text):
    file = open('data/triplev/spese.csv','w')
    file.write('name,value,person')
    file.close()
    return "Lista svuotata"


def get_list(a_text):
    all_str = ""
    with open('data/triplev/spese.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        all_str = all_str + "\n"+"Elemento"+"| Prezzo(Euro) |"+" Comprato da"
        for row in csv_reader:
            all_str = all_str + "\n"+row['name']+","+row['value']+" -> "+row['person']
    return all_str
