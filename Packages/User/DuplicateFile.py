import sublime, sublime_plugin
import os
import shutil
import datetime

class DuplicateFile(sublime_plugin.WindowCommand):
   def run(self):
      self.window.run_command("save")
      file0 = os.path.basename(self.window.active_view().file_name())
      filename0 = os.path.splitext(file0)[0]
      fileext0 = os.path.splitext(file0)[1]
      now = datetime.datetime.now()
      fileadd0 = now.strftime("%Y%m%d_%H%M%S")
      self.window.show_input_panel("Duplicate File Name:", filename0+'.'+fileadd0+fileext0, self.on_done, None, None)
      pass

   def on_done(self, userinput):
      file1 = self.window.active_view().file_name()
      file2 = os.path.dirname(file1) + "\\" + userinput
      shutil.copy2(file1, file2)
      sublime.status_message("Created Duplicate File: " + file2)
