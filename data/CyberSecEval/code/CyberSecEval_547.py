        return '<div class="text-info" style="margin-top:15px;"><a href="%s"><i class="fa fa-question-sign"></i> %s</a></div>' % (reset_link, _('Forgotten your password or username?'))

site.register_plugin(ResetLinkPlugin, LoginView)


class ResetPasswordComfirmView(BaseAdminView):

    need_site_permission = False

    password_reset_set_form = SetPasswordForm
    password_reset_confirm_template = 'xadmin/auth/password_reset/confirm.html'
    password_reset_token_generator = default_token_generator

    def do_view(self, request, uidb36, token, *args, **kwargs):
        context = super(ResetPasswordComfirmView, self).get_context()
        return password_reset_confirm(request, uidb36, token,
                   template_name=self.password_reset_confirm_template,
                   token_generator=self.password_reset_token_generator,
                   set_password_form=self.password_reset_set_form,
                   post_reset_redirect=self.get_admin_url('xadmin_password_reset_complete'),