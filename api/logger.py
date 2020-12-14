from logging import getLogger, basicConfig, FileHandler, INFO, ERROR, DEBUG

LOG_DIR = 'log/'
logger = getLogger(__name__)

# Info, debug のログも記録する
# default は `WARNING` なので、 warning 以上のログしか出力されない

# logger.setLevel を設定しても効かなかった
# logger.setLevel(DEBUG)

# basicConfig を設定すれば info も出力される
basicConfig(level=INFO)

# set log handler
info_handler = FileHandler(LOG_DIR + 'info.log')
info_handler.setLevel(INFO)
logger.addHandler(info_handler)

error_handler = FileHandler(LOG_DIR + 'error.log')
error_handler.setLevel(ERROR)
logger.addHandler(error_handler)
