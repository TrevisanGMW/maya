"""
 Attributes to  Python
 @Guilherme Trevisan - github.com/TrevisanGMW/gt-tools - 2021-12-01

 0.0.2 - 2022-03-31
 Re-created script after losing it to hard drive corruption


"""
import maya.cmds as cmds


DIMENSIONS = ['x', 'y', 'z']
DEFAULT_CHANNELS = ['t', 'r', 's']


def attr_to_list(obj_list, printing=True, decimal_place=2, separate_channels=False):
    """
    Returns transforms as list
    Args:
        obj_list (list, none): List objects to extract the transform from (if empty, it will try to use selection)
        printing (optional, bool): If active, the function will print the values to the script editor
        decimal_place (optional, int): How precise you want the extracted values to be (formats the float it gets)
        separate_channels (optional, bool): If separating channels, it will return T, R and S as different lists

    Returns:
        A list with transform values. [TX, TY, TZ, RX, RY, RZ, SX, SY, SZ]
        For example: attr_list = [0, 0, 0, 15, 15, 15, 1, 1, 1] # TRS (XYZ)

    """
    if not obj_list:
        obj_list = cmds.ls(selection=True)
    if not obj_list:
        return

    output = ''
    if printing:
        output += ('#' * 80)

    for obj in obj_list:
        output += '\n# Transform Data for "' + obj + '":\n'
        data = []
        for channel in DEFAULT_CHANNELS:  # TRS
            for dimension in DIMENSIONS:  # XYZ
                value = cmds.getAttr(obj + '.' + channel + dimension)
                data.append(float(format(value, "." + str(decimal_place) + "f")))
        if not separate_channels:
            output += 'object = "' + str(obj) + '"\n'
            output += 'trs_attr_list = ' + str(data) + '\n'
        else:
            output += 'object = "' + str(obj) + '"\n'
            output += 't_attr_list = [' + str(data[0]) + ', ' + str(data[1]) + ', ' + str(data[2]) + ']\n'
            output += 'r_attr_list = [' + str(data[3]) + ', ' + str(data[4]) + ', ' + str(data[5]) + ']\n'
            output += 's_attr_list = [' + str(data[6]) + ', ' + str(data[7]) + ', ' + str(data[8]) + ']\n'

    # Return / Print
    if printing:
        output += ('#' * 80)
        if output.replace('#', ''):
            print(output)
            return output
        else:
            print('No data found. Make sure your selection at least one object with unlocked transforms.')
            return None
    else:
        return output


def default_attr_to_python(obj_list, printing=True, use_loop=False, decimal_place=2):
    """
    Returns a string
    Args:
        obj_list (list, none): List objects to extract the transform from (if empty, it will try to use selection)
        printing (optional, bool): If active, the function will print the values to the script editor
        use_loop (optional, bool): If active, it will use a for loop in the output code (instead of simple lines)
        decimal_place (optional, int): How precise you want the extracted values to be (formats the float it gets)

    Returns:
        Python code with extracted transform values

    """
    if not obj_list:
        obj_list = cmds.ls(selection=True)
    if not obj_list:
        return

    output = ''
    if printing:
        output += ('#' * 80)

    for obj in obj_list:
        output += '\n# Transform Data for "' + obj + '":\n'
        data = {}
        for channel in DEFAULT_CHANNELS:  # TRS
            for dimension in DIMENSIONS:  # XYZ
                value = cmds.getAttr(obj + '.' + channel + dimension)
                data[channel + dimension] = value
                if not cmds.getAttr(obj + '.' + channel + dimension, lock=True) and not use_loop:
                    output += 'cmds.setAttr("' + obj + '.' + channel + dimension + '", '
                    output += str(float(format(value, "." + str(decimal_place) + "f"))) + ')\n'

        # Loop Version
        if use_loop:
            output += 'for key, value in ' + str(data) + '.items():\n'
            output += '\tif not cmds.getAttr(' + obj + '. + key, lock=True):\n'
            output += '\t\tcmds.setAttr("' + obj + '." + key, value)\n'

    # Return / Print
    if printing:
        output += ('#' * 80)
        if output.replace('#', ''):
            print(output)
            return output
        else:
            print('No data found. Make sure your selection at least one object with unlocked transforms.')
            return None
    else:
        return output


if __name__ == '__main__':
    # default_attr_to_python(None, use_loop=True)
    attr_to_list(None, separate_channels=False)