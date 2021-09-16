import ckan.plugins.toolkit as tk
import ckanext.latex.logic.schema as schema


@tk.side_effect_free
def latex_get_sum(context, data_dict):
    tk.check_access(
        "latex_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.latex_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'latex_get_sum': latex_get_sum,
    }
