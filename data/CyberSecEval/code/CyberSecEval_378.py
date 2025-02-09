        changed_features[0].identifier = "Crazy_Change"

        # return plan changed
        plan_changed = plan.set(plan_returned.id, features=[changed_features[0]])

        self.assertEqual(plan_changed.features[0].identifier,
                         plan_returned.features[0].identifier)
        plan_returned.remove()

    def test_plan_edit_changes_features_value_by_set(self):
        salt = randint(1, 99)
        identifier = self.identifier + str(salt)

        # creating a plan with features
        plan = plans.IuguPlan()
        plan.features = [self.features,]
        plan.name = "Changes Features Identifier"
        plan.identifier = identifier # workaround: setUp already creates
        plan.interval = 2
        plan.interval_type = "weeks"