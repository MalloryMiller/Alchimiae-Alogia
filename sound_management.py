import winsound


def bad_request():
    winsound.PlaySound('bad_request.wav',
                       winsound.SND_ASYNC)
