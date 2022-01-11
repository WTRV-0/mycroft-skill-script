"""
skill RunCommand
Created by: WTRV-0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from mycroft.util.parse import extract_number
import os

class RunScript(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.stop_requested = False

    @intent_file_handler('runscript.intent')
    def handle_count(self, message):
        self.stop_requested = False
        try:
            response = {'script': message.data.get("script")}
            self.speak_dialog("script_start", data=response)
          
            localpath = '/opt/mycroft/skills/mycroft-skill-script.wtrv-0/scripts'
            extractvalue = message.data.get("script").replace("underscore", "_").replace(" ","")

            os.system('cd ' + localpath + '; bash ' + extractvalue + '.sh')
        
            """
            Loop functionality

            for blah:
                if self.stop_requested:
                    break
                self.speak(str(i) + " .")
                wait_while_speaking()
            """
            
            if not self.stop_requested:
                self.speak_dialog("script_stop")
        except:
            self.speak_dialog("script_error")

    def stop(self):
        self.stop_requested = True

def create_skill():
    return RunScript()
