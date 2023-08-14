"""
Control Utilities (a.k.a. Complex Curves)
github.com/TrevisanGMW/gt-tools

Dependencies: "gt.utils.curve_utils" and "gt.utils.data.controls"
"""
from gt.utils.attribute_utils import add_attr_double_three
from gt.utils.data.controls import cluster_driven
from gt.utils.curve_utils import Curve
import maya.cmds as cmds
import logging

# Logging Setup

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Constants
CTRL_ATTR_COLOR = "autoColor"


def add_side_color_setup(obj, left_clr=(0, 0.5, 1), right_clr=(1, 0.5, 0.5)):
    """
    TODO: Add center color to args, inherit colors and functions from color_utils
    This function sets up a side color setup for the specified object in the Maya scene.
    It creates connections and attributes to control the color of the object based on its position in the scene.

    Parameters:
        obj (str): The name of the object to set up the color for.
        left_clr (tuple, optional): The RGB color values for the left side of the object. Default is (0, 0.5, 1).
        right_clr (tuple, optional): The RGB color values for the right side of the object. Default is (1, 0.5, 0.5).

    Example:
        # Example usage in Maya Python script editor:
        add_side_color_setup("pCube1", left_clr=(0, 1, 0), right_clr=(1, 0, 0))
    """
    if not obj or not cmds.objExists(obj):
        return

    # Setup Base Connections
    default_clr = (1, 1, 0.65)
    cmds.setAttr(obj + ".overrideEnabled", 1)
    cmds.setAttr(obj + ".overrideRGBColors", 1)
    clr_side_condition = cmds.createNode("condition", name=obj + "_clr_side_condition")
    clr_center_condition = cmds.createNode("condition", name=obj + "_clr_center_condition")
    decompose_matrix = cmds.createNode("decomposeMatrix", name=obj + "_decompose_matrix")
    cmds.connectAttr(obj + ".worldMatrix[0]", decompose_matrix + ".inputMatrix")
    cmds.connectAttr(decompose_matrix + ".outputTranslateX", clr_side_condition + ".firstTerm")
    cmds.connectAttr(decompose_matrix + ".outputTranslateX", clr_center_condition + ".firstTerm")
    cmds.connectAttr(clr_side_condition + ".outColor", clr_center_condition + ".colorIfFalse")
    cmds.setAttr(clr_side_condition + ".operation", 2)

    # Create Auto Color Attribute
    cmds.addAttr(obj, ln=CTRL_ATTR_COLOR, at='bool', k=True)
    cmds.setAttr(obj + "." + CTRL_ATTR_COLOR, 1)
    clr_auto_blend = cmds.createNode("blendColors", name=obj + "_clr_auto_blend")
    cmds.connectAttr(clr_auto_blend + ".output", obj + ".overrideColorRGB")
    cmds.connectAttr(clr_center_condition + ".outColor", clr_auto_blend + ".color1")
    cmds.connectAttr(obj + "." + CTRL_ATTR_COLOR, clr_auto_blend + ".blender")

    # Setup Color Attributes
    clr_attr = "colorDefault"
    add_attr_double_three(obj, clr_attr, keyable=False)
    cmds.setAttr(obj + "." + clr_attr + "R", default_clr[0])
    cmds.setAttr(obj + "." + clr_attr + "G", default_clr[1])
    cmds.setAttr(obj + "." + clr_attr + "B", default_clr[2])
    cmds.connectAttr(obj + "." + clr_attr + "R", clr_center_condition + ".colorIfTrueR")
    cmds.connectAttr(obj + "." + clr_attr + "G", clr_center_condition + ".colorIfTrueG")
    cmds.connectAttr(obj + "." + clr_attr + "B", clr_center_condition + ".colorIfTrueB")
    cmds.connectAttr(obj + "." + clr_attr, clr_auto_blend + ".color2")  # Blend node input
    r_clr_attr = "colorRight"
    add_attr_double_three(obj, r_clr_attr, keyable=False)
    cmds.setAttr(obj + "." + r_clr_attr + "R", left_clr[0])
    cmds.setAttr(obj + "." + r_clr_attr + "G", left_clr[1])
    cmds.setAttr(obj + "." + r_clr_attr + "B", left_clr[2])
    cmds.connectAttr(obj + "." + r_clr_attr + "R", clr_side_condition + ".colorIfTrueR")
    cmds.connectAttr(obj + "." + r_clr_attr + "G", clr_side_condition + ".colorIfTrueG")
    cmds.connectAttr(obj + "." + r_clr_attr + "B", clr_side_condition + ".colorIfTrueB")
    l_clr_attr = "colorLeft"
    add_attr_double_three(obj, l_clr_attr, keyable=False)
    cmds.setAttr(obj + "." + l_clr_attr + "R", right_clr[0])
    cmds.setAttr(obj + "." + l_clr_attr + "G", right_clr[1])
    cmds.setAttr(obj + "." + l_clr_attr + "B", right_clr[2])
    cmds.connectAttr(obj + "." + l_clr_attr + "R", clr_side_condition + ".colorIfFalseR")
    cmds.connectAttr(obj + "." + l_clr_attr + "G", clr_side_condition + ".colorIfFalseG")
    cmds.connectAttr(obj + "." + l_clr_attr + "B", clr_side_condition + ".colorIfFalseB")


def add_snapping_shape(target_object):
    """
    Parents a locator shape to the target object so objects can be snapped to it.
    The parented locator shape has a scale of 0, so it doesn't change the look of the target object.
    Args:
        target_object (str): Name of the object to add the locator shape.
    Returns:
        str: Name of the added invisible locator shape
    """
    if not target_object or not cmds.objExists(target_object):
        return
    locator = cmds.spaceLocator(name=target_object + "Point")[0]
    locator_shape = cmds.listRelatives(locator, s=True, f=True) or []
    cmds.setAttr(locator_shape[0] + ".localScaleX", 0)
    cmds.setAttr(locator_shape[0] + ".localScaleY", 0)
    cmds.setAttr(locator_shape[0] + ".localScaleZ", 0)
    cmds.select(locator_shape)
    cmds.select(target_object, add=True)
    cmds.parent(relative=True, shape=True)
    cmds.delete(locator)
    return locator_shape[0]


class Control(Curve):
    def __init__(self, name=None, build_function=None):
        """
        Initializes a Control (Curve) object. Essentially a complex Curve with extra logic and elements.
        Args:
            name (str, optional): Control transform name (shapes names are determined by the Callable function)
        """
        super().__init__(name=name)  # Call the parent class constructor
        self.build_function = None
        self.set_build_function(build_function=build_function)
        self.last_callable_output = None

    def set_build_function(self, build_function):
        """
        Sets the build function for this complex curve
        Args:
            build_function (callable): A function used to build the curve
        """
        if callable(build_function):
            self.build_function = build_function

    def build(self, *args, **kwargs):
        """
        Use the provided callable function to generate/create a Maya curve.
        Also renames the generated curve using the string stored in "self.name"
        If a list is returned from the "self.build_function" the parent transform is assumed to be the first object.
        e.g. ["parent_transform", "curve_shape", "something_else"] = Returns "parent_transform"
        Args:
            args (any): Arguments to give the complex curve callable object.
            kwargs (any): Keyword arguments to give the complex curve callable object.
        Returns:
            str or Any: Name of the transform of the newly generated curve. (Result of the callable function)
                        "None" if curve is invalid (does not have a callable function)
                        Any if "return_callable_output" is active.
        """
        if not self.is_curve_valid():
            logger.warning("Control object is missing a callable function.")
            return
        try:
            callable_result = self.build_function(*args, **kwargs)
            self.last_callable_output = callable_result
            return callable_result
        except Exception as e:
            logger.warning(f'Unable to build control. Build function raised an error: {e}')

    def is_curve_valid(self):
        """
        Checks if the Curve object has enough data to create/generate a curve.
        Returns:
            bool: True if it's valid (can create a curve), False if invalid.
                  In this case it's valid if it has a callable function.
        """
        if self.build_function is not None:
            return True
        return False

    def get_last_callable_output(self):
        """
        Returns the last output received from the build call
        Returns:
            any: Anything received as the last output from the callable function. If it was never called, it is None.
        """
        return self.last_callable_output


class Controls:
    def __init__(self):
        """
        A library of controls (complex curves) objects. These are created using a callable function.
        Use "build()" to create them in Maya.
        """
    scalable_arrow = Control(build_function=cluster_driven.create_scalable_arrow)


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    out = Controls.scalable_arrow
    out.build()
