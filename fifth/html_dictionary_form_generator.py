# -*-coding:utf8-*-


def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        if field_dict['type'] == 'text_field':
            generated_field_list.append(
                '{0}:<br><input type="text" name="{1}"><br>'.format(field_dict['label'], field_dict['name'])
            )
        # elif