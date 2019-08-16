#!/usr/bin/python
# Example file with custom commands, located at /Users/sunyanguo/lldbhelper/openhome.py
import lldb
import shlex
import fblldbbase as fb

def lldbcommands():
  return [ OpenHome() ]

class OpenHome(fb.FBCommand):
  def name(self):
    return 'openhome'

  def description(self):
    return 'open home of the app.'

  def lex(self, commandLine):
    return shlex.split(commandLine)

  def run(self, arguments, options):
    homePath = fb.describeObject('(NSString *)NSHomeDirectory()')
    toexe = 'platform shell open %s' % homePath
    lldb.debugger.HandleCommand(toexe)
      
 