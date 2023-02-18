from the_python_code import inc_dec   # The code to test

def test_increment():
    """
    Function should increment the value of x by 1.
    """
    assert inc_dec.increment(3) == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    """
    Function should decrement the value of x by 1.
    """
    assert inc_dec.decrement(3) == 4
