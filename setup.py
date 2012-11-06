from distutils.core import setup
import py2app

setup(
  name="LunchBarLy",
  app=["main.py"],
  options=dict(
    py2app=dict(
      plist=dict(
        LSUIElement=True,
      ),
    ),
  ),
)