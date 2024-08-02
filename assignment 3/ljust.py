def custom_ljust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    else:
        return s + fillchar * (width - len(s))