import sublime
import sublime_plugin


class FinderCommand(sublime_plugin.WindowCommand):
    paths = []

    def run(self, finder_folders=None):
        window = sublime.active_window()
        view = window.active_view()
        selection = view.substr(view.sel()[0])
        sublime.set_clipboard(selection)
        self.names = []
        self.paths = []
        if not finder_folders:
            finder_folders = window.project_data().get('finder_folders', [])

        for path in finder_folders:
            self.names.append([path['name'], path['path']])
            self.paths.append(path['path'])
        if self.names:
            sublime.active_window().show_quick_panel(self.names, on_select=self.on_select)
        else:
            args = {"panel": "find_in_files", "where": '<project>', "reverse": "false"}
            sublime.active_window().run_command("show_panel", args)

    def on_select(self, i):
        if i != -1:
            args = {"panel": "find_in_files", "where": self.paths[i], "replace": "", "reverse": "false"}
            sublime.active_window().run_command("show_panel", args)
