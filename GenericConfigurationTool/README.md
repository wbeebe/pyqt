# PyQt, or Python3 with Qt bindings

A collection of PyQt projects using Python3 and Qt5

## Generic Configuration Tool

A reimplementation of the Java application by that same name. This uses the
example app tabs-example.py, and strips it down to a bare bones implementation.
This application is also the start of using Python modules, as the tabs are instantiations
of a specific module in a file. The 'About' and 'Workstation' tabs are fairly complete.
This is the same essential design I used for the Java version, but the implementation
details are drastically different. It's another challenge for me to learn how to achieve
the same operational level in Python I had with Java and JavaFX.

What is significant is the use of sys and psutil functions to dig out statuses about
various aspects of the running Raspberry Pi. I suppose I could make this self refreshing
via some sort of threading, but that's something for the future. I have more fundamental
capabilities to build into this application.

![Generic Configuration Tool](https://github.com/wbeebe/pyqt/blob/master/screenshots/GenericConfigurationTool-About.png)

This is what the Workstation tab looks like. It basically repeats the original Java application.

![Generic Configuration Tool - Workstation](https://github.com/wbeebe/pyqt/blob/master/screenshots/GenericConfigurationTool-Workstation.png)

Each one of the right buttons will bring up a folder selection dialog.

![Workstation Folder Selection Dialog](https://github.com/wbeebe/pyqt/blob/master/screenshots/GenericConfigurationTool-Workstation-Select.png)

Picking a folder and then Choose produces the following on the Workstation tab.
Note that the Save button at the bottom is now active.

![Workstation Field Edited](https://github.com/wbeebe/pyqt/blob/master/screenshots/GenericConfigurationTool-Workstation-Edited.png)

The field has been edited, but the edit has not been saved. If you try to exit the application without
saving any edits, this is what you will see.

![Exit with Save Dialog](https://github.com/wbeebe/pyqt/blob/master/screenshots/GenericConfigurationTool-ExitDialog.png)

At this point you could either Save your work or continue to exit without save.
Or at least that's the plan. The skeleton for trapping edits and making sure to
save are there, but nothing will happen (yet) if you do save.

## License

    Copyright (c) 2019 William H. Beebe, Jr.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
