"""
Auto Rigger Leg Modules
github.com/TrevisanGMW/gt-tools
"""
from gt.tools.auto_rigger.rigger_utils import RiggerConstants, find_objects_with_attr, find_proxy_node_from_uuid
from gt.utils.attr_utils import add_attr, hide_lock_default_attrs, set_attr_state, set_attr
from gt.tools.auto_rigger.rigger_framework import Proxy, ModuleGeneric
from gt.utils.naming_utils import get_short_name, NamingConstants
from gt.tools.auto_rigger.rigger_utils import get_proxy_offset
from gt.utils.transform_utils import match_translate, Vector3
from gt.utils.color_utils import ColorConstants
from gt.utils.curve_utils import get_curve
from gt.utils import hierarchy_utils
import maya.cmds as cmds
import logging


# Logging Setup
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ModuleBipedLeg(ModuleGeneric):
    def __init__(self,
                 name="Leg",
                 prefix=None,
                 parent_uuid=None,
                 metadata=None,
                 pos_offset=None):
        super().__init__(name=name, prefix=prefix, parent_uuid=parent_uuid, metadata=metadata)

        # Default Proxies
        self.hip = Proxy(name="hip")
        pos_hip = Vector3(y=84.5) + pos_offset
        self.hip.set_initial_position(xyz=pos_hip)
        self.hip.set_locator_scale(scale=0.4)
        self.hip.set_meta_type(value="hip")

        self.knee = Proxy(name="knee")
        self.knee.set_curve(curve=get_curve('_proxy_joint_arrow'))
        pos_knee = Vector3(y=47.05) + pos_offset
        self.knee.set_initial_position(xyz=pos_knee)
        self.knee.set_locator_scale(scale=0.5)
        self.knee.add_meta_parent(line_parent=self.hip)
        self.knee.set_meta_type(value="knee")

        self.ankle = Proxy(name="ankle")
        pos_ankle = Vector3(y=9.6) + pos_offset
        self.ankle.set_initial_position(xyz=pos_ankle)
        self.ankle.set_locator_scale(scale=0.4)
        self.ankle.add_meta_parent(line_parent=self.knee)
        self.ankle.set_meta_type(value="ankle")

        self.ball = Proxy(name="ball")
        pos_ball = Vector3(z=13.1) + pos_offset
        self.ball.set_initial_position(xyz=pos_ball)
        self.ball.set_locator_scale(scale=0.4)
        self.ball.add_meta_parent(line_parent=self.ankle)
        self.ball.set_meta_type(value="ball")

        self.toe = Proxy(name="toe")
        pos_toe = Vector3(z=23.4) + pos_offset
        self.toe.set_initial_position(xyz=pos_toe)
        self.toe.set_locator_scale(scale=0.4)
        self.toe.set_parent_uuid(uuid=self.ball.get_uuid())
        self.toe.set_parent_uuid_from_proxy(parent_proxy=self.ball)
        self.toe.set_meta_type(value="toe")

        self.heel = Proxy(name="heelPivot")
        pos_heel = Vector3() + pos_offset
        self.heel.set_initial_position(xyz=pos_heel)
        self.heel.set_locator_scale(scale=0.1)
        self.heel.add_meta_parent(line_parent=self.ankle)
        self.heel.add_color(rgb_color=ColorConstants.RigProxy.PIVOT)
        self.heel.set_meta_type(value="heel")

        # Update Proxies
        self.proxies = [self.hip, self.knee, self.ankle, self.ball, self.toe, self.heel]

    def get_module_as_dict(self, **kwargs):
        """
        Overwrite to remove offset data from the export
        Args:
            kwargs: Key arguments, not used for anything
        """
        return super().get_module_as_dict(include_offset_data=False)

    def read_proxies_from_dict(self, proxy_dict):
        """
        Reads a proxy description dictionary and populates (after resetting) the proxies list with the dict proxies.
        Args:
            proxy_dict (dict): A proxy description dictionary. It must match an expected pattern for this to work:
                               Acceptable pattern: {"uuid_str": {<description>}}
                               "uuid_str" being the actual uuid string value of the proxy.
                               "<description>" being the output of the operation "proxy.get_proxy_as_dict()".
        """
        if not proxy_dict or not isinstance(proxy_dict, dict):
            logger.debug(f'Unable to read proxies from dictionary. Input must be a dictionary.')
            return
        for uuid, description in proxy_dict.items():
            metadata = description.get("metadata")
            if metadata:
                meta_type = metadata.get(RiggerConstants.PROXY_META_TYPE)
                if meta_type == "hip":
                    self.hip.set_uuid(uuid)
                    self.hip.read_data_from_dict(proxy_dict=description)
                if meta_type == "knee":
                    self.knee.set_uuid(uuid)
                    self.knee.read_data_from_dict(proxy_dict=description)
                if meta_type == "ankle":
                    self.ankle.set_uuid(uuid)
                    self.ankle.read_data_from_dict(proxy_dict=description)
                if meta_type == "ball":
                    self.ball.set_uuid(uuid)
                    self.ball.read_data_from_dict(proxy_dict=description)
                if meta_type == "toe":
                    self.toe.set_uuid(uuid)
                    self.toe.read_data_from_dict(proxy_dict=description)
                if meta_type == "heel":
                    self.heel.set_uuid(uuid)
                    self.heel.read_data_from_dict(proxy_dict=description)

    # --------------------------------------------------- Misc ---------------------------------------------------
    def is_valid(self):
        """
        Checks if the rig module is valid. This means, it's ready to be used and no issues were detected.
        Returns
            bool: True if valid, False otherwise
        """
        is_valid = super().is_valid()  # Passthrough
        return is_valid

    def build_proxy(self):
        """
        Build proxy elements in the viewport
        Returns:
            list: A list of ProxyData objects. These objects describe the created proxy elements.
        """
        proxy = super().build_proxy()  # Passthrough
        return proxy

    def build_proxy_post(self):
        """
        Runs post proxy script.
        When in a project, this runs after the "build_proxy" is done in all modules.
        Creates leg proxy behavior through constraints and offsets.
        """
        # Get Maya Elements
        root = find_objects_with_attr(RiggerConstants.ROOT_PROXY_ATTR)
        hip = find_proxy_node_from_uuid(self.hip.get_uuid())
        knee = find_proxy_node_from_uuid(self.knee.get_uuid())
        ankle = find_proxy_node_from_uuid(self.ankle.get_uuid())
        ball = find_proxy_node_from_uuid(self.ball.get_uuid())
        heel = find_proxy_node_from_uuid(self.heel.get_uuid())
        toe = find_proxy_node_from_uuid(self.toe.get_uuid())

        self.hip.apply_offset_transform()
        self.knee.apply_offset_transform()
        self.ankle.apply_offset_transform()
        self.ball.apply_offset_transform()
        self.heel.apply_offset_transform()

        # Hip -----------------------------------------------------------------------------------
        hide_lock_default_attrs(hip, translate=False)

        # Knee  ---------------------------------------------------------------------------------
        knee_tag = knee.get_short_name()
        hide_lock_default_attrs(knee, translate=False, rotate=False)

        # Knee Setup - Always Between Hip and Ankle
        knee_offset = get_proxy_offset(knee)
        cmds.pointConstraint([hip, ankle], knee_offset)

        knee_pv_dir = cmds.spaceLocator(name=f'{knee_tag}_poleVectorDir')[0]
        match_translate(source=knee, target_list=knee_pv_dir)
        cmds.move(0, 0, 13, knee_pv_dir, relative=True)  # More it forward (in front of the knee)
        hierarchy_utils.parent(knee_pv_dir, knee)

        # Lock Knee Unstable Channels
        cmds.addAttr(knee, ln='lockTranslateX', at='bool', k=True, niceName="Lock Unstable Channel")
        cmds.setAttr(knee + '.lockTranslateX', 1)  # Active by default
        cmds.setAttr(knee + '.minTransXLimit', 0)
        cmds.setAttr(knee + '.maxTransXLimit', 0)
        cmds.connectAttr(knee + '.lockTranslateX', knee + '.minTransXLimitEnable')
        cmds.connectAttr(knee + '.lockTranslateX', knee + '.maxTransXLimitEnable')
        
        #  Knee Constraints (Limits)
        knee_dir_loc = cmds.spaceLocator(name=f'{knee_tag}_dirParent_{NamingConstants.Suffix.LOC}')[0]
        knee_aim_loc = cmds.spaceLocator(name=f'{knee_tag}_dirAim_{NamingConstants.Suffix.LOC}')[0]
        knee_upvec_loc = cmds.spaceLocator(name=f'{knee_tag}_dirParentUp_{NamingConstants.Suffix.LOC}')[0]
        knee_upvec_loc_grp = f'{knee_tag}_dirParentUp_{NamingConstants.Suffix.GRP}'
        knee_upvec_loc_grp = cmds.group(name=knee_upvec_loc_grp, empty=True, world=True)
        # Hide Reference Elements
        set_attr(obj_list=[knee_pv_dir, knee_upvec_loc_grp, knee_dir_loc],
                 attr_list="visibility", value=0)  # Set Visibility to Off
        set_attr(obj_list=[knee_pv_dir, knee_upvec_loc_grp, knee_dir_loc],
                 attr_list="hiddenInOutliner", value=1)  # Set Outline Hidden to On
        knee_upvec_loc_grp = hierarchy_utils.parent(knee_upvec_loc_grp, root)[0]
        knee_upvec_loc = hierarchy_utils.parent(knee_upvec_loc, knee_upvec_loc_grp)[0]
        knee_dir_loc = hierarchy_utils.parent(knee_dir_loc, root)[0]
        knee_aim_loc = hierarchy_utils.parent(knee_aim_loc, knee_dir_loc)[0]

        knee_divide_node = cmds.createNode('multiplyDivide', name=f'{knee_tag}_divide')
        cmds.setAttr(f'{knee_divide_node}.operation', 2)  # Change operation to Divide
        cmds.setAttr(f'{knee_divide_node}.input2X', -2)
        cmds.connectAttr(f'{ankle}.tx', f'{knee_divide_node}.input1X')
        cmds.connectAttr(f'{knee_divide_node}.outputX', f'{knee_upvec_loc}.tx')

        match_translate(source=hip, target_list=knee_upvec_loc_grp)
        cmds.move(10, knee_upvec_loc, moveY=True, relative=True)  # More it forward (in front of the knee)
        cmds.pointConstraint(hip, knee_upvec_loc_grp)
        cmds.pointConstraint(hip, knee_dir_loc)
        cmds.pointConstraint([hip, ankle], knee_aim_loc)

        cmds.connectAttr(f'{knee_dir_loc}.rotate', f'{knee_offset}.rotate')

        cmds.aimConstraint(ankle, knee_dir_loc, aimVector=(0, -1, 0), upVector=(0, -1, 0),
                           worldUpType='object', worldUpObject=knee_upvec_loc)
        cmds.aimConstraint(knee_aim_loc, knee, aimVector=(0, 0, -1), upVector=(0, 1, 0),
                           worldUpType='none', skip=['x', 'z'])
        set_attr_state(obj_list=knee, attr_list="rotate", locked=True)

        cmds.transformLimits(knee, translationZ=(0, 1), enableTranslationZ=(1, 0))

        # Ankle ----------------------------------------------------------------------------------
        ankle_offset = get_proxy_offset(ankle)
        add_attr(target_list=ankle.get_long_name(), attributes="followHip", attr_type='bool', default=True)
        constraint = cmds.pointConstraint(hip, ankle_offset, skip='y')[0]
        cmds.connectAttr(f'{ankle}.followHip', f'{constraint}.w0')
        set_attr_state(obj_list=ankle, attr_list=["rx", "rz"], locked=True, hidden=True)

        # Ball -----------------------------------------------------------------------------------
        ankle_tag = ankle.get_short_name()
        ball_offset = get_proxy_offset(ball)
        ball_driver = cmds.group(empty=True, world=True, name=f'{ankle_tag}_pivot')
        ball_driver = hierarchy_utils.parent(source_objects=ball_driver, target_parent=root)[0]
        ankle_pos = cmds.xform(ankle, q=True, ws=True, rp=True)
        cmds.move(ankle_pos[0], ball_driver, moveX=True)
        cmds.pointConstraint(ankle, ball_driver, maintainOffset=True, skip=['y'])
        cmds.orientConstraint(ankle, ball_driver, maintainOffset=True, skip=['x', 'z'])
        cmds.scaleConstraint(ankle, ball_driver, skip=['y'])
        hierarchy_utils.parent(ball_offset, ball_driver)

        # Keep Grounded
        for to_lock_ty in [toe, ball]:
            cmds.addAttr(to_lock_ty, ln='lockTranslateY', at='bool', k=True, niceName="Keep Grounded")
            cmds.setAttr(to_lock_ty + '.lockTranslateY', 0)
            cmds.setAttr(to_lock_ty + '.minTransYLimit', 0)
            cmds.setAttr(to_lock_ty + '.maxTransYLimit', 0)
            cmds.connectAttr(to_lock_ty + '.lockTranslateY', to_lock_ty + '.minTransYLimitEnable', f=True)
            cmds.connectAttr(to_lock_ty + '.lockTranslateY', to_lock_ty + '.maxTransYLimitEnable', f=True)

        # Heel -----------------------------------------------------------------------------------
        heel_offset = get_proxy_offset(heel)
        add_attr(target_list=heel.get_long_name(), attributes="followAnkle", attr_type='bool', default=True)
        constraint = cmds.pointConstraint(ankle, heel_offset, skip='y')[0]
        cmds.connectAttr(f'{heel}.followAnkle', f'{constraint}.w0')
        hierarchy_utils.parent(source_objects=ball_offset, target_parent=ball_driver)
        hide_lock_default_attrs(heel, translate=False, rotate=True, scale=True)
        # self.apply_transforms()
        self.hip.apply_transforms()
        self.ankle.apply_transforms()
        self.ball.apply_transforms()
        self.heel.apply_transforms()
        self.toe.apply_transforms()
        self.knee.apply_transforms()  # Refresh due to automation
        cmds.select(clear=True)

    def build_rig(self):
        super().build_rig()  # Passthrough


class ModuleBipedLegLeft(ModuleBipedLeg):
    def __init__(self,
                 name="Left Leg",
                 prefix=NamingConstants.Prefix.LEFT,
                 parent_uuid=None,
                 metadata=None):
        super().__init__(name=name,
                         prefix=prefix,
                         parent_uuid=parent_uuid,
                         metadata=metadata,
                         pos_offset=Vector3(x=10.2))


class ModuleBipedLegRight(ModuleBipedLeg):
    def __init__(self,
                 name="Right Leg",
                 prefix=NamingConstants.Prefix.RIGHT,
                 parent_uuid=None,
                 metadata=None):
        super().__init__(name=name,
                         prefix=prefix,
                         parent_uuid=parent_uuid,
                         metadata=metadata,
                         pos_offset=Vector3(x=-10.2))


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    cmds.file(new=True, force=True)

    from gt.tools.auto_rigger.rigger_framework import RigProject
    a_leg_lf = ModuleBipedLegLeft()
    a_leg_rt = ModuleBipedLegRight()
    a_project = RigProject()
    a_project.add_to_modules(a_leg_rt)
    a_project.add_to_modules(a_leg_lf)
    a_project.build_proxy()

    cmds.setAttr(f'{NamingConstants.Prefix.LEFT}_hip.tx', 10)
    cmds.setAttr(f'{NamingConstants.Prefix.LEFT}_ankle.tz', 5)
    cmds.setAttr(f'{NamingConstants.Prefix.LEFT}_knee.tz', 3)
    print(a_project.get_project_as_dict())
    a_project.read_data_from_scene()
    print(a_project.get_project_as_dict())
    dictionary = a_project.get_project_as_dict()

    cmds.file(new=True, force=True)
    a_project2 = RigProject()
    a_project2.read_data_from_dict(dictionary)
    a_project2.build_proxy()
    # Show all
    cmds.viewFit(all=True)