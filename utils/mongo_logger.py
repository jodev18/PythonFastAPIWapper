
from datetime import datetime

class MongoLogger:

    def __init__(self):
        self.log_file_name = 'sample_log_file.log' # To replace this
        self.log_file = open(self.log_file_name,'a+')\

    def get_timestamp_str(self):
        """
            Gets current time and date in a specific format
            and returns it as a string. This is used for
            writing log events with specific time.
        :return:
        """
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return timestamp_str

    def write_log(self, module_name: str='', log_msg: str=''):
        """
            Simply formats a message string and writes it as
            a log information.
        :param module_name:
        :param log_msg:
        :return:
        """
        if len(module_name) > 0:
            log_message = f"[{module_name}][{self.get_timestamp_str()}]: {log_msg}"
            print(log_message)
            self.log_file.write(log_message)
        else:
            log_message = f"[{module_name}][{self.get_timestamp_str()}]: {log_msg}"
            print(log_message)
            self.log_file.write(log_message)

    def close_file(self):

        if self.log_file is not None:
            if not self.log_file.closed:
                self.log_file.flush()
                self.log_file.close()
            else:
                pass
        else:
            pass



## TEST CODE
if __name__ == "__main__":

    log = MongoLogger()
    log.write_log(module_name="Test Module", log_msg="Error message recorded!")
    log.close_file()