def raise_exception():
    try:
        raise TypeError("Type exception raised")
    except TypeError as e:
        raise e
