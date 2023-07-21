# Author Aleksandar Urosevic <urke.kg@gmail.com>
# Written for Sublime Text 3
# Convert HEX to ASCII

import sublime, sublime_plugin

class HexToAsciiCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# get self view
		view = self.view

		# define region to replace (whole file)
		region = sublime.Region(0, view.size())
		content = view.substr(region)

		# special characters
		content = content.replace(u"\\x20", u" ")
		content = content.replace(u"\\x21", u"!")
		content = content.replace(u"\\x22", u"\"")
		content = content.replace(u"\\x23", u"#")
		content = content.replace(u"\\x24", u"$")
		content = content.replace(u"\\x25", u"%")
		content = content.replace(u"\\x26", u"&")
		content = content.replace(u"\\x27", u"'")
		content = content.replace(u"\\x28", u"(")
		content = content.replace(u"\\x29", u")")
		content = content.replace(u"\\x2a", u"*")
		content = content.replace(u"\\x2b", u"+")
		content = content.replace(u"\\x2c", u",")
		content = content.replace(u"\\x2d", u"-")
		content = content.replace(u"\\x2e", u".")
		content = content.replace(u"\\x2f", u"/")

		#digits
		content = content.replace(u"\\x30", u"0")
		content = content.replace(u"\\x31", u"1")
		content = content.replace(u"\\x32", u"2")
		content = content.replace(u"\\x33", u"3")
		content = content.replace(u"\\x34", u"4")
		content = content.replace(u"\\x35", u"5")
		content = content.replace(u"\\x36", u"6")
		content = content.replace(u"\\x37", u"7")
		content = content.replace(u"\\x38", u"8")
		content = content.replace(u"\\x39", u"9")

		# other special characters
		content = content.replace(u"\\x3a", u":")
		content = content.replace(u"\\x3b", u";")
		content = content.replace(u"\\x3c", u"<")
		content = content.replace(u"\\x3d", u"=")
		content = content.replace(u"\\x3e", u">")
		content = content.replace(u"\\x3f", u"?")
		content = content.replace(u"\\x40", u"@")

		# uppercase characters
		content = content.replace(u"\\x41", u"A")
		content = content.replace(u"\\x42", u"B")
		content = content.replace(u"\\x43", u"C")
		content = content.replace(u"\\x44", u"D")
		content = content.replace(u"\\x45", u"E")
		content = content.replace(u"\\x46", u"F")
		content = content.replace(u"\\x47", u"G")
		content = content.replace(u"\\x48", u"H")
		content = content.replace(u"\\x49", u"I")
		content = content.replace(u"\\x4a", u"J")
		content = content.replace(u"\\x4b", u"K")
		content = content.replace(u"\\x4c", u"L")
		content = content.replace(u"\\x4d", u"M")
		content = content.replace(u"\\x4e", u"N")
		content = content.replace(u"\\x4f", u"O")
		content = content.replace(u"\\x50", u"P")
		content = content.replace(u"\\x51", u"Q")
		content = content.replace(u"\\x52", u"R")
		content = content.replace(u"\\x53", u"S")
		content = content.replace(u"\\x54", u"T")
		content = content.replace(u"\\x55", u"U")
		content = content.replace(u"\\x56", u"V")
		content = content.replace(u"\\x57", u"W")
		content = content.replace(u"\\x58", u"X")
		content = content.replace(u"\\x59", u"Y")
		content = content.replace(u"\\x5a", u"Z")

		# more special characters
		content = content.replace(u"\\x5b", u"[")
		content = content.replace(u"\\x5c", u"\\")
		content = content.replace(u"\\x5d", u"]")
		content = content.replace(u"\\x5e", u"^")
		content = content.replace(u"\\x5f", u"_")
		content = content.replace(u"\\x60", u"`")

		# lowercase characters
		content = content.replace(u"\\x61", u"a")
		content = content.replace(u"\\x62", u"b")
		content = content.replace(u"\\x63", u"c")
		content = content.replace(u"\\x64", u"d")
		content = content.replace(u"\\x65", u"e")
		content = content.replace(u"\\x66", u"f")
		content = content.replace(u"\\x67", u"g")
		content = content.replace(u"\\x68", u"h")
		content = content.replace(u"\\x69", u"i")
		content = content.replace(u"\\x6a", u"j")
		content = content.replace(u"\\x6b", u"k")
		content = content.replace(u"\\x6c", u"l")
		content = content.replace(u"\\x6d", u"m")
		content = content.replace(u"\\x6e", u"n")
		content = content.replace(u"\\x6f", u"o")
		content = content.replace(u"\\x70", u"p")
		content = content.replace(u"\\x71", u"q")
		content = content.replace(u"\\x72", u"r")
		content = content.replace(u"\\x73", u"s")
		content = content.replace(u"\\x74", u"t")
		content = content.replace(u"\\x75", u"u")
		content = content.replace(u"\\x76", u"v")
		content = content.replace(u"\\x77", u"w")
		content = content.replace(u"\\x78", u"x")
		content = content.replace(u"\\x79", u"y")
		content = content.replace(u"\\x7a", u"z")

		content = content.replace(u"\\x7b", u"{")
		content = content.replace(u"\\x7c", u"|")
		content = content.replace(u"\\x7d", u"}")
		content = content.replace(u"\\x7e", u"~")

		# single
		content = content.replace(u"\101", u"A")
		content = content.replace(u"\141", u"a")
		content = content.replace(u"\142", u"b")
		content = content.replace(u"\143", u"c")
		content = content.replace(u"\144", u"d")
		content = content.replace(u"\145", u"e")
		content = content.replace(u"\146", u"f")
		content = content.replace(u"\147", u"g")
		content = content.replace(u"\154", u"l")
		content = content.replace(u"\160", u"p")
		content = content.replace(u"\161", u"q")
		content = content.replace(u"\162", u"r")
		content = content.replace(u"\163", u"s")
		content = content.replace(u"\164", u"t")
		
		# update content in view
		view.replace(edit, region, content)

		# close edit buffer
		view.end_edit(edit)

