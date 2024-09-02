"""
Auto Rigger Constants

Code Namespace:
    tools_rig_const # import gt.tools.auto_rigger.rig_constants as tools_rig_const
"""


class RiggerConstants:
    def __init__(self):
        """
        Constant values used by the auto rigging system.
        e.g. Attribute names, dictionary keys or initial values.
        """

    # General Keys and Attributes
    PROJECT_EXTENSION = "json"
    FILE_FILTER = f"Rig Project (*.{PROJECT_EXTENSION});;"
    # Basic System Attributes
    ATTR_JOINT_BASE_NAME = "baseName"
    ATTR_JOINT_UUID = "jointUUID"
    ATTR_MODULE_UUID = "moduleUUID"
    ATTR_PROXY_UUID = "proxyUUID"
    ATTR_JOINT_DRIVEN_UUID = "jointDrivenUUID"  # Duplicated joints used in automation
    # Driver System Attributes
    ATTR_DRIVER_UUID = "driverUUID"  # Driver (often controls) used to animate joints
    ATTR_DRIVER_CHILD = "driverChild"  # Auxiliary control attr that receives data from "ATTR_DRIVER_UUID"
    ATTR_JOINT_PURPOSE = "jointPurpose"  # Proxy purpose is stored in this attribute when a joint is created
    ATTR_JOINT_DRIVERS = "jointDrivers"  # List of drivers is stored in this attribute when a joint is created
    # Misc Attributes
    ATTR_PROXY_SCALE = "locatorScale"
    ATTR_ROT_ORDER = "rotationOrder"  # Determines initial rotation order. Cannot be "rotateOrder", taken by Maya
    ATTR_ROT_ORDER_IK = "rotationOrderIK"  # Used to determine the rotation order of a control (only some modules)
    ATTR_LINE_CHILD_UUID = "lineProxySourceUUID"  # Used by the proxy lines to store source
    ATTR_LINE_PARENT_UUID = "lineProxyTargetUUID"  # Used by the proxy lines to store target
    ATTR_SHAPE_VIS = "shapeVisibility"  # Used to expose the visibility of the shapes of a control
    # Metadata Keys
    META_SETUP_NAME = "setupName"  # Metadata key for the system name. (Determines naming pattern)
    META_PROXY_LINE_PARENT = "lineParentUUID"  # Metadata key, line parent. Actual parent is ignored when present
    META_PROXY_PURPOSE = "proxyPurpose"  # Metadata key, used to recognize proxy purpose within modules
    META_PROXY_DRIVERS = "proxyDrivers"  # Metadata key, used to find drivers (aka controls) driving the created joint
    META_PROXY_CLR = "color"  # Metadata key, describes color to be used instead of side setup
    # Group Names
    GRP_RIG_NAME = f"rig"
    GRP_PROXY_NAME = f"rig_proxy"
    GRP_GEOMETRY_NAME = f"geometry"
    GRP_SKELETON_NAME = f"skeleton"
    GRP_CONTROL_NAME = f"controls"
    GRP_SETUP_NAME = f"setup"
    GRP_LINE_NAME = f"visualization_lines"
    # Reference Attributes
    REF_ATTR_ROOT_RIG = "rootRigLookupAttr"
    REF_ATTR_ROOT_PROXY = "rootProxyLookupAttr"
    REF_ATTR_CTRL_GLOBAL_PROXY = "globalProxyCtrlLookupAttr"
    REF_ATTR_CTRL_GLOBAL = "globalCtrlLookupAttr"
    REF_ATTR_CTRL_GLOBAL_OFFSET = "globalOffsetCtrlLookupAttr"
    REF_ATTR_GEOMETRY = "geometryGroupLookupAttr"
    REF_ATTR_SKELETON = "skeletonGroupLookupAttr"
    REF_ATTR_CONTROL = "controlsGroupLookupAttr"
    REF_ATTR_SETUP = "setupGroupLookupAttr"
    REF_ATTR_LINES = "linesGroupLookupAttr"
    # Multipliers
    LOC_RADIUS_MULTIPLIER_DRIVEN = 0.8
    LOC_RADIUS_MULTIPLIER_FK = 0.3
    LOC_RADIUS_MULTIPLIER_IK = 0.6
    LOC_RADIUS_MULTIPLIER_DATA_QUERY = 0.1
    # Framework Vars
    CLASS_ATTR_SKIP_AUTO_SERIALIZATION = [
        "name",
        "uuid",
        "prefix",
        "suffix",
        "active",
        "code",
        "proxies",
        "orientation",
        "parent_uuid",
        "module_children_drivers",
    ]


class RiggerDriverTypes:
    def __init__(self):
        """
        Driver Type Constant values used by the drivers and controls.
        """

    BLOCK = "block"  # Does not accept children and blocks the automatic creation of generic drivers.
    GENERIC = "generic"  # Any transform/control. When not found, a following group is created.
    FK = "fk"  # Forward kinematics
    IK = "ik"  # Inverse kinematics

    # WIP - Experimental:
    PIVOT = "pivot"
    SWITCH = "switch"  # Secondary driver that allows switching between systems. e.g. FK/IK
    OFFSET = "offset"  # Driver is the data of an offset control
    COG = "cog"  # Center of Gravity
    AIM = "aim"  # e.g. eyes
    ROLL = "roll"  # e.g. toe_roll
    UP_DOWN = "upDown"  # e.g. toe_upDown
    CURL = "curl"  # e.g. thumb_curl
    TWIST = "twist"  # Twist Joints
    LINE = "line"  # connection lines for the controls
