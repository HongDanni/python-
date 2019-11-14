# -*-coding:utf8-*-


def generato_webform(field_list):
    generated_fields = '\n'.join(
        map(lambda x: '{0}<br><input type="text" name={0}><br>'.format(x), field_list)
    )
    return '<form>{fields}</form>'.format(fields=generated_fields)


def build_html_form(fields):
    with open('form_file.html', 'w') as f:
        f.write(
            "<html><head></head><body>{}</body></html>".format(generato_webform(fields))
        )

if __name__ == '__main__':
    fields = ['name', 'age', 'email', 'telephone']
    build_html_form(fields)





