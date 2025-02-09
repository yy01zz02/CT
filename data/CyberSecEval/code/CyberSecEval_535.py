            PyGdbUtil.log(2, '删除表失败!')


    # 获取测试样例
    def get_test_case_by_tid(self, tid):
        self.execute("SELECT testStr FROM " + self.table_prefix + "TestCase WHERE tid='%s'" % tid)
        return self.cursor.fetchone()[0]

    # 获取测试样例总数
    def get_test_case_cnt(self):
        self.execute('SELECT max(tid) FROM ' + self.table_prefix + 'TestCase')
        return int(self.cursor.fetchone()[0])

    # 获取指定程序的断点列表
    def get_breakpoint_list(self, pid):
        self.execute('SELECT lineNumber FROM ' + self.table_prefix + 'BreakPoint WHERE pid="%s"' % pid)
        all = self.cursor.fetchall()
        return [x[0] for x in all]

    # 执行 sql 语句