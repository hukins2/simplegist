class SimpleGistError(Exception):
    """
    Base error class for errors from simplegist
    """
    pass


class GistStatusCodeError(SimpleGistError):
    """
    An HTTP status code was not HTTP_OK (200)
    """
    pass


class UserNotFoundError(SimpleGistError):
    """

    """
    pass


class GistNotFoundError(SimpleGistError):
    """
    A Gist requested by ID or name was not found
    """
    pass


class GistDeletionError(SimpleGistError):
    """
    An error occur while attempting to delete a Gist
    """
    pass
