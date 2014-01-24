'''
Created on Dec 22, 2013

@author: Chris
'''

import wx 
import sys
from app.dialogs.model import Model

YES = 5103
NO 	= 5104

class Controller(object):
	'''
	Main controller for the gui. 
	
	All controlls are delegated to this central control point. 
	It's kind of a bi-directional observer sort of thing, thus 
	weirdly initialized with references to the BaseWindows panels, 
	and then 'registered' with the panels . 
	
	
	
	Args: 
		base			 = Reference to the Basewindow
		head_panel = reference to the BaseWindow's Head Panel 	  
		body_panel = reference to the BaseWindow's Body Panel 	  
		footer_panel = reference to the BaseWindow's Footer Panel 	  
	'''
	
	def __init__(self, base, head_panel, body_panel, footer_panel):
		self._base = base
		self._head = head_panel
		self._body = body_panel 
		self._foot = footer_panel
		
		self._model = Model.GetInstance()
	
	def OnConfigCancel(self, event):
		msg = "Are you sure you want to exit?"
		dlg = wx.MessageDialog(None, msg, "Close Program?", wx.YES_NO)
		result = dlg.ShowModal()
		print result
		if result == YES:
			dlg.Destroy()
			self._base.Destroy()
			sys.exit()
			
	def OnConfigNext(self, event):
		cmd_line_args = self._body.GetOptions()
		if not self._model.IsValidArgString(cmd_line_args):
			error_msg = self._model.GetErrorMsg(cmd_line_args)
			self.ShowArgumentErrorDlg(error_msg) 
			return 
		self._model.AddToArgv(cmd_line_args)
		self._base.NextPage()
		self.RunClientCode()
	
	def RunClientCode(self):
		pass 
	
	def AddPayload(self, payload):
		pass
		
			
			
		
	def OnMainCancel(self, event):
		print 'OnMaingCancel pressed!'
	def OnMainNext(self, event):
		print 'OnCongigNext pressed!'
		
	def ShowArgumentErrorDlg(self, error):
		a = wx.MessageDialog(None, error, 'Argument Error')	
		a.ShowModal()
		a.Destroy()
		