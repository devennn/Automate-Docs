import json

TEMPLATE_FILENAME = "../template.json"


def make_template(crop_values, template_name):
    TEMPLATE_CONFIG = {
        template_name: {
            "Crop_Value": crop_values
        }
    }
    write_template(TEMPLATE_CONFIG)


def is_template_name_valid(template_name):
    try:
        content = read_template()
    except json.decoder.JSONDecodeError:
        return False

    # Return false if name is empty string
    if template_name == "":
        return False

    # Return false if name exists
    if template_name in content:
        return False

    return True


def read_template():
    while True:
        try:
            with open(TEMPLATE_FILENAME, "r") as f:
                content_json = json.loads(f.read())
            break
        except FileNotFoundError:
            empty_dict = {}
            with open(TEMPLATE_FILENAME, "x") as f:
                json.dump(empty_dict, f)

    return content_json


def write_template(content_raw):
    content_prev = read_template()
    content_prev.update(content_raw)
    with open(TEMPLATE_FILENAME, "w+") as f:
        json.dump(content_prev, f, indent=4)


def get_template_name_list():
    try:
        return [template_name for template_name in read_template()]
    except FileNotFoundError:
        return []


def get_template_crop_values(template_name):
    content = read_template()
    return content[template_name]["Crop_Value"]
