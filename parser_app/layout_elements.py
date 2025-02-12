import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import FolderBrowse, ThisRow

def make_window():
    """Make window with set elements, returns window object"""
    sg.theme('DarkBlack1')
    file_list_column = [
        [
            sg.Text("Select File"),
            sg.In(size=(35, 1), key="-FILE-"),
            sg.FileBrowse(button_text = 'File',file_types=(('Text Files', '*.txt'),)),
            sg.FolderBrowse(button_text ='Folder', target = (ThisRow,-2),key = '-FOB PARSE-'),
            sg.Button(button_text = 'Add', enable_events=True, key = '-ADD FILE-')
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(64, 5), key="-FILE LIST-"
            )

        ],
        [
            sg.Button(
                button_text='Remove', key="-REMOVE FILE-"
            ),
            sg.Button(
                button_text='Clear', key="-CLEAR FILES-",button_color='red'
            )
        ],
    ]

    keyword_list_column = [
        [
            sg.Text('Enter keyword to filter'),
            sg.In(size=(40, 1), enable_events=True, key="-KEY-"),
            sg.Button(button_text='Add', key="-ADD KEY-"),

        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(58, 5), key="-KEY LIST-"
            ),
            sg.Button(
                button_text='Parse', key='-PARSE-', size=(5, 3), button_color='green'
            ),
        ],
        [
            sg.Button(
                button_text='Remove', key="-REMOVE KEY-"
            ),
            sg.Button(
                button_text='Clear', key="-CLEAR KEYS-",button_color='red'
            ),
            sg.Checkbox('Exact', key ='-EXACT CB-', default = False),
        ],
    ]

    selection_full_display = [
        [
            sg.Text('Select file'),
        ],
        [
            sg.Combo(values=[],
            auto_size_text = True,
            enable_events=True, 
            disabled = True,
            key='-PARSED FILE SELECT-'
            ),
        ],
        [
            sg.Button(button_text='All with keyword',key = '-ALL KW-', enable_events = True),
            sg.Button(button_text='All without keyword',key = '-ALL NO KW-',enable_events = True),
            sg.Button(button_text = 'Clear',key = '-CLEAR FULL OUTPUT-',button_color='red')
        ],
        [
            sg.Multiline(
               size=(20, 5), 
               key='-KEYS DISPLAY-',
               disabled=True
            ),
            
            sg.Button(button_text = 'Extract keys', enable_events= True, key ='-EXTRACT KEYS-')
        ],
        [
            sg.Button(button_text = 'Export Selected', enable_events = True, key = '-FULL EXPORT-'),
            sg.Button(button_text = 'Export Displayed', enable_events = True, key = '-FULL EXPORT DISPLAYED-'),
            sg.Button(button_text = 'Export All', enable_events = True, key = '-FULL EXPORT ALL-'),
            
        ]
    ] 

    selection_expandable_display = [
        [
            sg.Text('Select file'),
        ],
        [
            sg.Combo(values=[],
            auto_size_text = True,
            enable_events=True, 
            disabled = True,
            key='-PARSED FILE SELECT EXPANDABLE-'
            ),
        ],
        [
            sg.Button(button_text = 'Clear',key = '-CLEAR EXPANDABLE OUTPUT-',button_color='red'),
            sg.Button(button_text = 'Collapse', key = '-COLLAPSE EXPANDABLE OUTPUT-')
        ],
    ]

    selection_searchable_display = [
        [
            sg.Text('Select file'),
        ],
        [
            sg.Combo(values=[],
            auto_size_text = True,
            enable_events=True, 
            disabled = True,
            key='-PARSED FILE SELECT SEARCHABLE-'
            ),
        ],
        [
            sg.Text('Select LAC'),
        ],
        [
            sg.Combo(values=[],
            auto_size_text = True,
            enable_events=True, 
            disabled = True,
            key='-PARSED LAC SELECT SEARCHABLE-'
            ),
        ],
        [
            sg.Text('Select conveyor'),
            sg.Checkbox('All', default= False, k = '-ALL CONV CB-', enable_events = True),
        ],
        [
            sg.Combo(values=[],
            auto_size_text = True,
            enable_events=True, 
            disabled = True,
            key='-PARSED CONVEYOR SELECT SEARCHABLE-'
            ),
        ],
        [
            sg.Button(button_text = 'Search',key = '-SEARCH SEARCHABLE OUTPUT-'),
            sg.Checkbox('Keep previous searches', default=False, k='-MULTI SEARCH CB-'),
        ],
        [   
            sg.Button(button_text = 'Export', enable_events = True, key = '-SEARCHABLE EXPORT-'),
            sg.Button(button_text = 'Clear',key = '-CLEAR SEARCHABLE OUTPUT-',button_color='red')
        ],
    ]

    full_display = [
        [
            sg.Multiline(
               size=(90, 20), 
               key='-FULL OUTPUT-',
               disabled=True
            ),
            sg.Column(selection_full_display,vertical_alignment = 'top'),
        ],
    ]

    expandable_display = [
        [
            sg.Listbox(
               size=(90, 19), 
               key='-EXPANDABLE OUTPUT-',
               values=[],
               enable_events= True
            ),
            sg.Column(selection_expandable_display,vertical_alignment = 'top'),
        ],

    ]

    searchable_display = [
        [
            sg.Multiline(
               size=(90, 20), 
               key='-SEARCHABLE OUTPUT-',
               disabled = True
            ),
            sg.Column(selection_searchable_display,vertical_alignment = 'top'),
        ],
    ]

    parsing_input = [[
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(keyword_list_column),
    ]]

    parsed_input = [
            [
            sg.Text("Select File"),
            sg.In(size=(110, 1), key="-JSON FILE-"),
            sg.FileBrowse(button_text ='File',file_types=(('Json Files', '*.json'),),key = '-FB PARSED-'),
            sg.FolderBrowse(button_text ='Folder', target = (ThisRow,-2),key = '-FOB PARSED-'),
            sg.Button(button_text = 'Add', enable_events=True, key = '-ADD PARSED-')
            ],
            [
            sg.Listbox(
                values=[], 
                enable_events=True, 
                size=(100, 5), 
                key="-FILE LIST LOAD-",
                pad = ((80,5),(0,5))
            ), 
            sg.Button(
                button_text='Load', key='-LOAD-', size=(5, 3), button_color='green'
            ),

            ],
            [
                sg.Button(
                    button_text='Remove', key="-REMOVE FILE LOAD-",pad = ((80,0),(0,0))
                ),
                sg.Button(
                    button_text='Clear', key="-CLEAR FILES LOAD-",button_color='red'
                )
            ],
    ]
    tree_data = sg.TreeData()
    tree_test = [
        [sg.Tree(data = tree_data,)],
        
    ]


    layout = [
        [sg.TabGroup([[
                        sg.Tab('Parse New',parsing_input,key = '-PARSE NEW TAB-'),
                        sg.Tab('Load', parsed_input,key = '-PARSED TAB-'),
        ]])
        ],
        [sg.TabGroup([[
                        sg.Tab('Full', full_display,key = '-FULL TAB-'),
                        sg.Tab('Expandable', expandable_display,key = '-EXPANDABLE TAB-'),
                        sg.Tab('Searchable', searchable_display,key = '-SEARCHABLE TAB-'),
                        sg.Tab('Tree test',tree_test),
                    ]],enable_events=True,key = '-DISPLAY TAB-', size = (1000,335)),
                    
        ],
        [
            sg.Text('Created by Gianluca Traversa (RME Intern), Joe Rush and Jessica Lucas © 2021.',
            tooltip='Source Code',
            enable_events = True,
            font = ('Helvetica',7),
            text_color='Gray',
            key = '-COPYRIGHT-'),
        ]

    ]
    return sg.Window("S7 Parser", layout,finalize=True,icon = r'C:\Users\gttraver\Desktop\Inbound ESM\parser_app\Logo\logo.ico')
