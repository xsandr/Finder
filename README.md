Finder
======
Sublime text 3 plugin, that can make handy shortcuts for "Where" field in search panel.


*Usage:*

You can declare shortcut like:

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

or add this settings to *Project->Edit Project*

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

and declare shortcuts without arguments.

*Example:*

![FinderScreenShot](https://downloader.disk.yandex.ru/preview/0cda702c60e5ed311aab9562ee53fbd0/mpfs/tEJtcDLp438_5vmkcKfDRSyJ6Z0TYuZYfPvjwqjvU7BN0gWBrZ6oMSV_oy8QXX_AaPI4lyZZHNxCDVNN-m6tOg%3D%3D?uid=0&filename=Finderpng&disposition=inline&hash=&limit=0&content_type=image%2Fpng&size=XXL&crop=0)
