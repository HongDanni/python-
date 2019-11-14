# -*-coding:utf8-*-


def log_message(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('{0}\n'.format(msg))


###########################################################
def critical(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('[CRITICAL] {0}\n'.format(msg))


def error(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('[ERROR] {0}\n'.format(msg))


def warn(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('[WARN] {0}\n'.format(msg))


def info(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('[INFO] {0}\n'.format(msg))


def debug(msg):
    with open('logfile/log1.log', 'a') as log_file:
        log_file.write('[DEBUG] {0}\n'.format(msg))


###########################################################
# def write_log(level, msg):
#     with open('/logfile/log1.log', 'a') as log_file:
#         log_file.write('[{0}] {1}\n'.format(level, msg))


def write_log(filename, level, msg):
    with open(filename, 'a') as log_file:
        log_file.write('[{0}] {1}\n'.format(level, msg))


def critical(msg):
    write_log('CRITICAL', msg)


def error(msg):
    write_log('ERROR', msg)


def warn(msg):
    write_log('WARN', msg)


def info(msg):
    write_log('INFO', msg)


def debug(msg):
    write_log('DEBUG', msg)







