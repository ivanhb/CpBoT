
import csv
import urllib.request

my_commands = {
    "/howToContactYou" : {"notes":"How to contact me !"},
    "/lastActivity" : {"notes":" My last activity."},
    "/listPublications" : {"notes":" The list of my publications."},
    "/listProjects" : {"notes":" The list of projects I have worked/working on."}
}

def get_my_commands():
    return my_commands

def exec_my_commands(command,param):
    if command == "/howToContactYou":
        return how_to_contact_you(param)
    elif command == "/lastActivity":
        return last_activity(param)
    elif command == "/listPublications":
        return list_publications(param)
    elif command == "/listProjects":
        return list_projects(param)


def how_to_contact_you(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/contacts.csv"
    csv_matrix = get_csv_file(api_call)

    for i in range(1,len(csv_matrix)):
        str_to_return = str_to_return + "\n"+csv_matrix[i][0]+": "+csv_matrix[i][1]
    return str_to_return

def list_publications(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/publication.csv"
    csv_matrix = get_csv_file(api_call)

    str_to_send = ""
    if csv_matrix != [] and csv_matrix != -1:
        for i in range(1,len(csv_matrix)):
            str_to_send = str_to_send + "\n"+csv_matrix[i][0]
            if csv_matrix[i][2] != "":
                str_to_send = str_to_send + "\n" + handle_extra_elem(csv_matrix[i][2])
            str_to_send = str_to_send + " \n\n"

    return str_to_send

def list_projects(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/project.csv"
    csv_matrix = get_csv_file(api_call)

    str_to_send = ""
    if csv_matrix != [] and csv_matrix != -1:
        for i in range(1,len(csv_matrix)):
            str_to_send = str_to_send + "\n"+csv_matrix[i][0]+"\n"+csv_matrix[i][1]
            if csv_matrix[i][2] != "":
                str_to_send = str_to_send + "\n" + handle_extra_elem(csv_matrix[i][2])
            str_to_send = str_to_send + " \n\n"

    return str_to_send

def last_activity(a_text):
    str_to_return = ""
    api_call = "https://ivanhb.github.io/data/activity.csv"
    csv_matrix = get_csv_file(api_call)

    if csv_matrix != [] and csv_matrix != -1:
        str_to_send = ""
        str_to_send += "Event: "+csv_matrix[1][0] + "\n"
        str_to_send += "At : "+csv_matrix[1][1] + "\n"
        str_to_send += "On : "+csv_matrix[1][2] + "\n"
        str_to_send += "My contribution: "+csv_matrix[1][3] + "\n"
        str_to_send += "About: "+csv_matrix[1][4] + "\n"
        str_to_send = str_to_send + handle_extra_elem(csv_matrix[1][5])

    return str_to_send


def get_csv_file(api_call):
    try:
        contents = urllib.request.urlopen(api_call).read().decode('utf-8')
        arr_rows = str(contents).split('\n')
        return list(csv.reader(arr_rows))
    except Exception as e:
        return -1

def handle_extra_elem(ext_elem):
    arr_ext = ext_elem.split(']],[[')
    str_all_ext = ""
    for ex_i in arr_ext:
        ex_i = ex_i.replace('[[','')
        ex_i = ex_i.replace(']]','')
        ex_parts_i = ex_i.split(',')

        if ex_parts_i[0][:4] == 'link':
            str_all_ext = str_all_ext + ex_parts_i[1]+ ": " + ex_parts_i[2] + '\n'
    return str_all_ext
