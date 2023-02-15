import pytest


@pytest.mark.parametrize("email, expected", [
 ("aZ0.-_a@Aa0-9.cZ", True),
 ("*.ownsite@our-earth.org", False),
 ("ankitra@&326.com", False),
 ("ankitra@326.c", False),
 ("ankit.ra@326.com", True),
 ("ankit-ra@326.com", True),
 ("ankit_ra@326.com", True),
 ("ankit..ra@326.com", False),
 ("ankit--ra@326.com", False),
 ("ankit__ra@326.com", False),
 ("ankit-_ra@326.com", True),
 ("ankit._ra@326.com", True),
 ("ankit-ra-@326.com", False),
 ("ankit_ra_@326.com", False),
 (".ankit-ra@326.com", False),
 ("ankit-ra@-326.com", False),
 ("ankit-ra@326-.com", False),
 ("ankit-ra@3--26.com", False),
 ("ankit-ra@32-6.com", True)
 ])
def test_is_email(email, expected):
    from email_checker import is_email
    answer = is_email(email)
    assert answer == expected
