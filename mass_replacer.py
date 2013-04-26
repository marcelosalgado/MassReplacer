'''
I wanted to search and replace lots of time, so I created this.

@author: Marcelo Salgado <msscelo@gmail.com>
@license: MIT (http://www.opensource.org/licenses/mit-license.php)
@since: 2013-04-26
'''
import sublime
import sublime_plugin

class MassReplaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		searcheddos = {
			"\)[\s\n\t]*\{" : ") {",
			"else[ \n\t]*\{": "else {",
			"\}[ \n\t]*else": "} else",
			"for\("         : "for (",
			"foreach\("     : "foreach (",
			"while\("       : "while (",
			"if\("          : "if ("
			# add more here
		}
		modifications = 0
		noChange = 0
		for searched, replacer in searcheddos.iteritems():
			found = self.view.find(searched,0)
			while found:
				textofound = self.view.substr(found)
				if textofound != replacer:
					self.view.replace(edit,found,replacer)
					modifications = modifications + 1
				else:
					noChange = noChange + 1
				pos = found.begin() + len(replacer)
				found = self.view.find(searched,pos)
		message = 'Nothing to mass replace. '+str(noChange)+' already ok'
		if modifications > 0:
			message = str(modifications)+' stuff mass replaced! '+str(noChange)+' already ok'
		sublime.status_message(message)