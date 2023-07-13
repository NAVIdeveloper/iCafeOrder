from flet import *
import flet
from webapi import *
import conf

data = api_categorys_get()

def Add_New(e):
    name = new_add.value
    api_categorys_add(name)
    new_add.value = ""
    new_add.update()
    Cancel()

def Edit(e):
    def SaveEdit(e):
        name = field.value
        api_categorys_edit(e.control.data,name)
        Cancel()

        
    id = e.control.data
    category = None
    for i in data:
        if i['id'] == id:
            category = i
            break
    DATA_ROWS = []
    for i in data[::-1]:
        if i['id'] == id:
            field = TextField(value=i['name'])
            DATA_ROWS.append(
                DataRow(
                    cells=[
                        DataCell(Text(i['id'])),
                        DataCell(field),
                        DataCell(IconButton(icon=icons.CHECK_CIRCLE,icon_color="green",on_click=SaveEdit,data=i['id'])),
                        DataCell(IconButton(icon=icons.CANCEL,icon_color="blue",on_click=lambda e: Cancel())),
                    ]
                )
            )
        else:
            DATA_ROWS.append(
                DataRow(
                    cells=[
                        DataCell(Text(i['id'])),
                        DataCell(Text(i['name'])),
                        DataCell(IconButton(icon=icons.EDIT,icon_color=conf.button_color,on_click=Edit,data=i['id'])),
                        DataCell(IconButton(icon=icons.DELETE,icon_color="gray",on_click=Delete,data=i['id'])),
                    ]
                )
            )
    table.rows = DATA_ROWS
    table.update()
    
    

def Delete(e):
    def FuncDelete(e):
        api_categorys_delete(e.control.data)
        Cancel()

    id = e.control.data
    category = None
    for i in data:
        if i['id'] == id:
            category = i
            break
    DATA_ROWS = []
    for i in data[::-1]:
        if i['id'] == id:
            DATA_ROWS.append(
                DataRow(
                    cells=[
                        DataCell(Text(i['id'])),
                        DataCell(Text(i['name'])),
                        DataCell(IconButton(icon=icons.DELETE,icon_color="red",on_click=FuncDelete,data=i['id'])),
                        DataCell(IconButton(icon=icons.CANCEL,icon_color="blue",on_click=lambda e: Cancel())),
                    ]
                )
            )
        else:
            DATA_ROWS.append(
                DataRow(
                    cells=[
                        DataCell(Text(i['id'])),
                        DataCell(Text(i['name'])),
                        DataCell(IconButton(icon=icons.EDIT,icon_color=conf.button_color,on_click=Edit,data=i['id'])),
                        DataCell(IconButton(icon=icons.DELETE,icon_color="gray",on_click=Delete,data=i['id'])),
                    ]
                )
            )
    table.rows = DATA_ROWS
    table.update()

DATA_ROWS = []

table = DataTable(
    columns=[
        DataColumn(Text("ID")),
        DataColumn(Text("Nomi")),
        DataColumn(Text("")),
        DataColumn(Text("")),
    ],
    rows=DATA_ROWS,
    width=conf.width,
)

def Cancel():
    global DATA_ROWS,data
    try:
        DATA_ROWS = []
        data = api_categorys_get()
        
        for i in data[::-1]:
            DATA_ROWS.append(
                DataRow(
                    cells=[
                        DataCell(Text(i['id'])),
                        DataCell(Text(i['name'])),
                        DataCell(IconButton(icon=icons.EDIT,icon_color=conf.button_color,on_click=Edit,data=i['id'])),
                        DataCell(IconButton(icon=icons.DELETE,icon_color="gray",on_click=Delete,data=i['id'])),
                    ]
                )
            )
        table.rows = DATA_ROWS
        try:
            table.update()
        except:
            pass
    except:
        pass
Cancel()

new_add = TextField(hint_text="Yangi Kategoryiya",height=40,border='underline',border_color='green')

categorys = Container(
    Column([
        Container(
            Row([
                new_add,
                IconButton(icons.ADD,icon_color=conf.button_color,on_click=Add_New),
            ]),
            alignment=alignment.center
        ),
        table
    ],scroll='always'),
    padding=padding.only(50,50,50,50)
)