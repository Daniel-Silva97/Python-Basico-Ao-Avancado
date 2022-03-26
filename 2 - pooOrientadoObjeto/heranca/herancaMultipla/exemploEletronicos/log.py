class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def logInfo(self, msg):
        self.write(f'INFO: {msg}')

    def logError(self, msg):
        self.write(f'ERROR: {msg}')
