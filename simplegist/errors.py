class GistError(Exception):
    """
    Base error class for errors from simplegist
    """
    pass


class GistStatusCodeError(GistError):
    """
    An HTTP status code was not HTTP_OK (200)
    """
    pass


class UserNotFoundError(GistError):
    """

    """
    pass


class GistNotFoundError(GistError):
    """
    A Gist requested by ID or name was not found
    """
    pass


class GistDeletionError(GistError):
    """
    An error occur while attempting to delete a Gist
    """
    pass
