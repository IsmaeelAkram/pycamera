import cv2


class UserQuit(Exception):
    pass


def waitForKey(delay=15, key=27):
    """Returns if key (Escape, by default) is pressed"""
    if cv2.waitKey(delay) == key:
        raise UserQuit("User has quit, this is perfectly normal.")