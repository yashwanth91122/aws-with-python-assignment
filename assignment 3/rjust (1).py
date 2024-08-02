def custom_rjust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    else:
        return fillchar * (width - len(s)) + s