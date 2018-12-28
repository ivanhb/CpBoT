
# coding: utf-8

# In[44]:

my_commands = {
    "#addItem" : {"module": "shoppingList", "method": "add_entry", "notes":"insert item name and some notes if needed."},
    "#removeItem" : {"module": "shoppingList", "method": "remove_entry", "notes":"insert item name"},
    "#removeAll" : {"module": "shoppingList", "method": "remove_all", "notes":""},
    "#getList" : {"module": "shoppingList", "method": "get_list", "notes":""},
}

shopping_list = {}

def get_my_commands():
    return my_commands

def add_entry(a_text):
    name = ""
    notes = ""
    if len(a_text) > 0:
        name = a_text[0]
    if len(a_text) > 1:
        notes = " ".join(a_text[1:])
    if name != "":
        shopping_list[name] = {"notes": notes}
        return "Item '"+name+"' added"
    else:
        return "I will not insert an empty Item!"

def remove_entry(a_text):
    name = ""
    if len(a_text) > 0:
        name = a_text[0]

    if name in shopping_list:
        shopping_list.pop(name, None)
        return "Item '"+name+"' removed"
    return "No Item in the list with name '"+name+"'"

def remove_all(a_text):
    #list_copy = shopping_list
    #for key in list_copy:
    #    shopping_list.pop(key, None)
    for key in shopping_list.keys():
        shopping_list.pop(key, None)

    return "All Items removed"

def get_list(a_text):
    all_items = ""
    for key in shopping_list:
        all_items = "- "+str(key)+" : " + str(shopping_list[key]["notes"]) +"\n" +all_items

    if(all_items != ""):
        return str(all_items)
    else:
        return "No items in list!"



# In[ ]:




# In[ ]:
