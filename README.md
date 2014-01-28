Finder
======
Sublime text 3 plugin, to make handy shortcut for "Where" field in search panel.


*Usage*

You could set this key binding:

```
{
    "keys": ["super+shift+f"], "command": "finder", "args": {"finder_folders": [
        {
            "name": "Python sources",
            "path": "/path/to/your/python/source/folder/",
        },
        {
            "name": "Js sources",
            "path": "/another/path/",
        }
    ]}
},
```

or add this settings in project settings *Project->Edit Project*

```
    ...
    "finder_folders": [
        {
            "name": "Python sources",
            "path": "/path/to/your/python/source/folder/",
        },
        {
            "name": "Js sources",
            "path": "/another/path/",
        }
    ]
    ...
```

and set key bindig without *args*
