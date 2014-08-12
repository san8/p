def test_foo():
    from hello_world import foo
    from StringIO import StringIO

    out = StringIO()
    foo(out=out)
    output = out.getvalue().strip()
    assert output == 'welcome to pearl'


