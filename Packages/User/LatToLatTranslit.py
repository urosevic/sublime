# Author Aleksandar Urosevic <urke.kg@gmail.com>
# Written for Sublime Text 3
# Convert Latin to Latin cp1250 script

import sublime, sublime_plugin

class LatToLatAllTranslitCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# get self view
		view = self.view

		# define region to replace (whole file)
		region = sublime.Region(0, view.size())
		content = view.substr(region)

		# lowercase characters
		content = content.replace(u"ð", "đ")
		#content = content.replace(u"ž", "ž")
		content = content.replace(u"æ", "ć")
		content = content.replace(u"è", "č")
		#content = content.replace(u"š", "š")

		# uppercase characters
		#content = content.replace(u"Ð", "Đ")
		#content = content.replace(u"Ž", "Ž")
		content = content.replace(u"Æ", "Ć")
		content = content.replace(u"È", "Č")
		#content = content.replace(u"Š", "Š")

		# update content in view
		view.replace(edit, region, content)

		# close edit buffer
		view.end_edit(edit)

