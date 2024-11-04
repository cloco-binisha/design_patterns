class CustomLogger:
    _instance = None

    @staticmethod
    def get_instance():
        if CustomLogger._instance is None:
            CustomLogger._instance = CustomLogger()
            print("logger instance created")
        return CustomLogger._instance


if __name__ == "__main__":

    logger1 = CustomLogger.get_instance()
    print(logger1,"logger1")

    logger2 = CustomLogger.get_instance()
    print(logger2,"logger2")