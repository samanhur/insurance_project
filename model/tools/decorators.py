from model.tools.logger import Logger


# This decorator is designed for handling exceptions in oop and return a formated log message
def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            output = function(*args, **kwargs)
            if "find" not in function.__name__:
                Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output}")

            else:
                Logger.info(f"{function.__qualname__}{args[1:]}")

            return output

        except Exception as e:
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : {e}")
            return False, str(e)

    return inner
