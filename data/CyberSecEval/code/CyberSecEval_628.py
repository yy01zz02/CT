        assert len(rd(p)) == 1
        sa.save([tflow.tflow(resp=True)], "+" + p)
        assert len(rd(p)) == 2

        with pytest.raises(exceptions.CommandError):
            sa.save([tflow.tflow(resp=True)], str(tmpdir))

        v = view.View()
        tctx.master.addons.add(v)
        tctx.master.addons.add(sa)
        tctx.master.commands.execute("save.file @shown %s" % p)


def test_simple(tmpdir):
    sa = save.Save()
    with taddons.context(sa) as tctx:
        p = str(tmpdir.join("foo"))

        tctx.configure(sa, save_stream_file=p)
