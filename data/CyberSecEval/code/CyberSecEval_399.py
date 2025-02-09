
        sleep(2)
        all_plans_limit = plans.IuguPlan.getitems(limit=3)
        all_plans_skip = plans.IuguPlan.getitems(skip=2, limit=3)
        self.assertEqual(all_plans_limit[2].id, all_plans_skip[0].id)
        plan_a.remove()
        plan_b.remove()
        plan_c.remove()

    def test_plan_getitems_filter_query(self):
        salt = str(randint(1, 199)) + self.identifier
        name_repeated = salt
        plan = plans.IuguPlan()
        plan_a = plan.create(name=name_repeated,
                                    identifier=salt, interval=2,
                                    interval_type="weeks", currency="BRL",
                                    value_cents=1000)
        salt = str(randint(1, 199)) + self.identifier
        plan_b = plan.create(name=name_repeated,
                                    identifier=salt, interval=2,