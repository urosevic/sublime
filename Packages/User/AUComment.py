# Author Aleksandar Urosevic <urke.kg@gmail.com>
# Written for Sublime Text 3
# Insert PHP/JS comment signature with current date

import sublime, sublime_plugin, datetime

class AlUrCommentCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# get self view
		view = self.view

		# define region to replace (whole file)
		position = view.sel()[0].begin()

		# get current date and time
		now = datetime.datetime.now()
		d = now.strftime("%Y%m%d")

		# compose content
		content = "/* AU: %s  */" % d

		# update content in view
		view.insert(edit, position, content)

		# set new position for cursor
		position = view.sel()[0].begin() - 3

		# clear selection
		view.sel().clear()

		# move cursor 3 characters backward (prepare for comment)
		view.sel().add(sublime.Region(position))

		# close edit buffer
		view.end_edit(edit)

