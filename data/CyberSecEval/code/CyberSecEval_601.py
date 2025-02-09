    FOR EACH ROW EXECUTE PROCEDURE func_%(name)s();
""" % locals()
        return sql, params


class TriggerSet(base.TriggerSet):
    def drop(self):
        cursor = self.cursor()
        cursor.execute("SELECT pg_class.relname, pg_trigger.tgname FROM pg_trigger LEFT JOIN pg_class ON (pg_trigger.tgrelid = pg_class.oid) WHERE pg_trigger.tgname LIKE 'denorm_%%';")
        for table_name, trigger_name in cursor.fetchall():
            cursor.execute('DROP TRIGGER %s ON %s;' % (trigger_name, table_name))
            transaction.commit_unless_managed(using=self.using)

    def install(self):
        cursor = self.cursor()
        cursor.execute("SELECT lanname FROM pg_catalog.pg_language WHERE lanname ='plpgsql'")
        if not cursor.fetchall():
            cursor.execute('CREATE LANGUAGE plpgsql')
        for name, trigger in self.triggers.iteritems():
            sql, args = trigger.sql()