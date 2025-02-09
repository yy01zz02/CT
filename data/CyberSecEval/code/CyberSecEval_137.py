    assert response.json()["name"] == data["name"]


def test_put_topic_order(
    api_client, enable_premium_requirement, profile_topic_factory, user_factory
):
    """
    Premium users should be able to sort their own profile topics with
    respect to the parent profile.
    """
    password = "password"
    user = user_factory(has_premium=True, password=password)
    api_client.log_in(user.primary_email.email, password)

    t1 = profile_topic_factory(profile__km_user__user=user)
    t2 = profile_topic_factory(profile=t1.profile)

    url = f"/know-me/profile/profiles/{t1.profile.pk}/topics/"
    data = {"order": [t2.pk, t1.pk]}
    response = api_client.put(url, data)