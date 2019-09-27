
def er_tlf_nr(nr):
    """Tar inn en streng og sier om den er et telefonnummer"""
    if len(nr) == 8 and nr.isdigit():
        return True
    elif len(nr) == 11 and nr.startswith("+") and nr[1:].isdigit():
        return True
    else:
        return False

assert er_tlf_nr("45623960")

assert not er_tlf_nr("abc")

assert not er_tlf_nr("abcdefgh")

assert er_tlf_nr("+4745623960")

assert not er_tlf_nr("+474+623960")

assert not er_tlf_nr("++745623960")

print("*** ALLE TESTER BESTÅTT ***")
