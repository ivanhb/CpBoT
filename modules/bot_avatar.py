
import csv
import urllib.request

my_commands = {
    "/howToContactYou" : {"notes":""},
    "/lastActivity" : {"notes":""}
}

ivanhbbot = {}

def get_my_commands():
    #in case you want disable this module
    #return {}
    return my_commands

def exec_my_commands(command,param):
    if command == "/howToContactYou":
        return how_to_contact_you(param)
    elif command == "/lastActivity":
        return last_activity(param)

def update_date():
    urls = {
        'content_config.js':'https://ivanhb.github.io/content_config.js'
    }

    #for url_entry in urls:
    #    url = urls[url_entry]
    #    r = requests.get(url, allow_redirects=True)
    #    open('data/'+url_entry, 'wb').write(r.content)
    return "Ivanhb status updated!"


def how_to_contact_you(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/contacts.csv"
    csv_matrix = get_csv_file(api_call)
    for c in csv_matrix:
        str_to_return = str_to_return + "\n"+c[0]+": "+c[1]
    return str_to_return


def last_activity(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/activity.csv"
    csv_matrix = get_csv_file(api_call)

    str_to_send = ""
    str_to_send += "Event: "+csv_matrix[1][0] + "\n"
    str_to_send += "At : "+csv_matrix[1][1] + "\n"
    str_to_send += "On : "+csv_matrix[1][2] + "\n"
    str_to_send += "My contribution: "+csv_matrix[1][3] + "\n"
    str_to_send += "About: "+csv_matrix[1][4] + "\n"

    arr_ext = csv_matrix[1][5].split(']],[[')
    str_all_ext = ""
    for ex_i in arr_ext:
        ex_i = ex_i.replace('[[','')
        ex_i = ex_i.replace(']]','')
        ex_parts_i = ex_i.split(',')

        if ex_parts_i[0][:4] == 'link':
            str_all_ext = str_all_ext + ex_parts_i[1]+ ": " + ex_parts_i[2] + '\n'

    str_to_send = str_to_send + str_all_ext

    return str_to_send


def get_csv_file(api_call):
    contents = urllib.request.urlopen(api_call).read().decode('utf-8')
    arr_rows = str(contents).split('\n')
    return list(csv.reader(arr_rows))
