import sys
import maya.utils
from module_example import echo_test


def show():
    cmds.setParent('MayaWindow')
    cmds.menu(label=u'ModuleExample', tearOff=True)
    cmds.menuItem(subMenu=True, label='Example', tearOff=True)
    cmds.menuItem(l='echo_test',
                  c='echo_test.echo()')
    cmds.setParent('..', menu=True)

maya.utils.executeDeferred(show)
