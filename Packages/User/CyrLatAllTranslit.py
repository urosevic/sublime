# Author Aleksandar Urosevic <urke.kg@gmail.com>
# Written for Sublime Text 3
# Convert Serbian Cyrillic to Latin script

import sublime, sublime_plugin

class CyrLatAllTranslitCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# get self view
		view = self.view

		# define region to replace (whole file)
		region = sublime.Region(0, view.size())
		content = view.substr(region)

		# lowercase characters
		content = content.replace(u"а", "a")
		content = content.replace(u"б", "b")
		content = content.replace(u"в", "v")
		content = content.replace(u"г", "g")
		content = content.replace(u"д", "d")
		content = content.replace(u"ђ", "đ")
		content = content.replace(u"е", "e")
		content = content.replace(u"ж", "ž")
		content = content.replace(u"з", "z")
		content = content.replace(u"и", "i")
		content = content.replace(u"ј", "j")
		content = content.replace(u"к", "k")
		content = content.replace(u"л", "l")
		content = content.replace(u"љ", "lj")
		content = content.replace(u"м", "m")
		content = content.replace(u"н", "n")
		content = content.replace(u"њ", "nj")
		content = content.replace(u"о", "o")
		content = content.replace(u"п", "p")
		content = content.replace(u"р", "r")
		content = content.replace(u"с", "s")
		content = content.replace(u"т", "t")
		content = content.replace(u"ћ", "ć")
		content = content.replace(u"у", "u")
		content = content.replace(u"ф", "f")
		content = content.replace(u"х", "h")
		content = content.replace(u"ц", "c")
		content = content.replace(u"ч", "č")
		content = content.replace(u"џ", "dž")
		content = content.replace(u"ш", "š")

		# uppercase characters
		content = content.replace(u"А", "A")
		content = content.replace(u"Б", "B")
		content = content.replace(u"В", "V")
		content = content.replace(u"Г", "G")
		content = content.replace(u"Д", "D")
		content = content.replace(u"Ђ", "Đ")
		content = content.replace(u"Е", "E")
		content = content.replace(u"Ж", "Ž")
		content = content.replace(u"З", "Z")
		content = content.replace(u"И", "I")
		content = content.replace(u"Ј", "J")
		content = content.replace(u"К", "K")
		content = content.replace(u"Л", "L")
		content = content.replace(u"Љ", "Lj")
		content = content.replace(u"М", "M")
		content = content.replace(u"Н", "N")
		content = content.replace(u"Њ", "Nj")
		content = content.replace(u"О", "O")
		content = content.replace(u"П", "P")
		content = content.replace(u"Р", "R")
		content = content.replace(u"С", "S")
		content = content.replace(u"Т", "T")
		content = content.replace(u"Ћ", "Ć")
		content = content.replace(u"У", "U")
		content = content.replace(u"Ф", "F")
		content = content.replace(u"Х", "H")
		content = content.replace(u"Ц", "C")
		content = content.replace(u"Ч", "Č")
		content = content.replace(u"Џ", "Dž")
		content = content.replace(u"Ш", "Š")

		# uppercase two-letter chars
		content = content.replace(u"NjA", "NJA")
		content = content.replace(u"NjE", "NJE")
		content = content.replace(u"NjI", "NJI")
		content = content.replace(u"NjO", "NJO")
		content = content.replace(u"NjU", "NJU")
		content = content.replace(u"ANj", "ANJ")
		content = content.replace(u"ENj", "ENJ")
		content = content.replace(u"INj", "INJ")
		content = content.replace(u"ONj", "ONJ")
		content = content.replace(u"UNj", "UNJ")

		content = content.replace(u"LjA", "LJA")
		content = content.replace(u"LjE", "LJE")
		content = content.replace(u"LjI", "LJI")
		content = content.replace(u"LjO", "LJO")
		content = content.replace(u"LjU", "LJU")
		content = content.replace(u"ALj", "ALJ")
		content = content.replace(u"ELj", "ELJ")
		content = content.replace(u"ILj", "ILJ")
		content = content.replace(u"OLj", "OLJ")
		content = content.replace(u"ULj", "ULJ")

		content = content.replace(u"DžA", "DŽA")
		content = content.replace(u"DžE", "DŽE")
		content = content.replace(u"DžI", "DŽI")
		content = content.replace(u"DžO", "DŽO")
		content = content.replace(u"DžU", "DŽU")
		content = content.replace(u"ADž", "ADŽ")
		content = content.replace(u"EDž", "EDŽ")
		content = content.replace(u"IDž", "IDŽ")
		content = content.replace(u"ODž", "ODŽ")
		content = content.replace(u"UDž", "UDŽ")

		# update content in view
		view.replace(edit, region, content)

		# close edit buffer
		view.end_edit(edit)

