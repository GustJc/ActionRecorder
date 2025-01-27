# region Imports
# external modules
from typing import Optional

# blender modules
import bpy
from bpy.app.handlers import persistent

# relative imports
from . import globals, shared
from .. import shared_data
from .shared import get_preferences
# endregion


# region functions


def get_category_id(ActRec_pref: bpy.types.AddonPreferences, id: str, index: int) -> str:
    """
    get category id based on id (check for existence) or index
    fallback to selected category if no match occurred

    Args:
        ActRec_pref (bpy.types.AddonPreferences): preferences of this addon
        id (str): id to check
        index (int): index of the category

    Returns:
        str: id of the category, fallback to selected category if not found
    """
    # REFACTOR indentation
    if ActRec_pref.categories.find(id) == -1:
        if index >= 0 and len(ActRec_pref.categories) > index:
            return ActRec_pref.categories[index].id
        else:
            return ActRec_pref.selected_category
    else:
        return id


def read_category_visibility(ActRec_pref: bpy.types.AddonPreferences, id: str) -> Optional[list]:
    """
    get all areas and modes where the category with the given id is visible

    Args:
        ActRec_pref (bpy.types.AddonPreferences): preferences of this addon
        id (str): id of the category

    Returns:
        Optional[list]: dict on success, None on fail
    """
    # REFACTOR indentation
    visibility = []
    category = ActRec_pref.categories.get(id, None)
    if category:
        for area in category.areas:
            for mode in area.modes:
                visibility.append((area.type, mode.type))
            if len(area.modes) == 0:
                visibility.append((area.type, 'all'))
        return visibility
# endregion
