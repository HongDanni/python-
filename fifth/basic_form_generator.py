# -*-coding:utf8-*-

def generate_webform(field_list):
    generated_fields = "\n".join(
        map(lambda x: '{0}<br><input type="text" name="{0}"><br>'.format(x), field_list)
    )
    return "<form>{fields}</form>".format(fields=generated_fields)


if __name__ == '__main__':
    fields = ['name', 'age', 'email', 'telephone']
    content = generate_webform(fields)
    print(content)
    with open('basic_form_generator.html', 'w') as f:
        f.write(content)



