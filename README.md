Finder
======
Sublime text 3 plugin, to make handy shortcut for "Where" field in search panel.


*Usage:*

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

*Example:*

![FinderScreenShot](https://downloader.disk.yandex.ru/preview/0cda702c60e5ed311aab9562ee53fbd0/mpfs/tEJtcDLp438_5vmkcKfDRSyJ6Z0TYuZYfPvjwqjvU7BN0gWBrZ6oMSV_oy8QXX_AaPI4lyZZHNxCDVNN-m6tOg%3D%3D?uid=0&filename=Finderpng&disposition=inline&hash=&limit=0&content_type=image%2Fpng&size=XXL&crop=0)
