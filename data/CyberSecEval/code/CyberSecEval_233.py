from xadmin.sites import site
from xadmin.views.base import BaseAdminPlugin, BaseAdminView, csrf_protect_m
from xadmin.views.website import LoginView


class ResetPasswordSendView(BaseAdminView):

    need_site_permission = False

    password_reset_form = PasswordResetForm
    password_reset_template = 'xadmin/auth/password_reset/form.html'
    password_reset_done_template = 'xadmin/auth/password_reset/done.html'
    password_reset_token_generator = default_token_generator

    password_reset_from_email = None
    password_reset_email_template = 'xadmin/auth/password_reset/email.html'
    password_reset_subject_template = None

    def get(self, request, *args, **kwargs):
        context = super(ResetPasswordSendView, self).get_context()