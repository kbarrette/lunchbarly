"""
Menu bar item for lunch!

Borrows heavily from http://the.taoofmac.com/space/blog/2007/04/22/1745

Thanks to Tom Murphy for the initial spark of this idea
"""

from datetime import datetime

from AppKit import *
from PyObjCTools import AppHelper

TIME_FORMAT = "%%(dayname)s %b %d %l:%M %p"
TIMER_INTERVAL = 20
DAY_NAMES = [
  "Ruebisday",
  "Autumnsday",
  "Bradfordsday",
  "Gourmetsday",
  "TBDay",
  "Noworksday",
  "Funday",
] 

class LunchBar(NSObject):
  statusbar = None

  def applicationDidFinishLaunching_(self, notification):

    # Get status bar and create item
    statusbar = NSStatusBar.systemStatusBar()
    self.statusitem = statusbar.statusItemWithLength_(NSVariableStatusItemLength)
    self.setDateTime()
    
    # Add some niceties - highlighting, tool tip
    self.statusitem.setHighlightMode_(True)
    self.statusitem.setToolTip_("LunchBarLy")

    # Build
    menu = NSMenu.alloc().init()
    menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "terminate:", "")
    menu.addItem_(menuitem)
    self.statusitem.setMenu_(menu)

    # Start timer to call tick every 5 seconds
    timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(TIMER_INTERVAL, self, "tick:", None, True)

  def tick_(self, notification):
    """
    Timer callback - called when timer set above fires
    """

    self.setDateTime()

  def setDateTime(self):
    """
    Set the date and time in the status bar
    """

    now = datetime.now()
    dayname = DAY_NAMES[now.weekday()]
    self.statusitem.setTitle_(now.strftime(TIME_FORMAT) % locals())

if __name__ == "__main__":
  app = NSApplication.sharedApplication()
  delegate = LunchBar.alloc().init()
  app.setDelegate_(delegate)
  AppHelper.runEventLoop()