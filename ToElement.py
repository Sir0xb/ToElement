import sublime, sublime_plugin

class ToElementCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selection in self.view.sel():
			if(selection == None):
				continue

			word = self.view.substr(selection)
			wordStar = selection.begin()
			wordEnd = selection.end()

			self.view.replace(edit, selection, "<" + word + "></" + word + ">")
