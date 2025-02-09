            self.vendor('xadmin.page.form.js', 'xadmin.form.css')

site.register_view(r'^xadmin/password_reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    ResetPasswordComfirmView, name='xadmin_password_reset_confirm')


class ResetPasswordCompleteView(BaseAdminView):

    need_site_permission = False

    password_reset_complete_template = 'xadmin/auth/password_reset/complete.html'

    def get(self, request, *args, **kwargs):
        context = super(ResetPasswordCompleteView, self).get_context()
        context['login_url'] = self.get_admin_url('index')

        return TemplateResponse(request, self.password_reset_complete_template, context,
                                current_app=self.admin_site.name)

site.register_view(r'^xadmin/password_reset/complete/$', ResetPasswordCompleteView, name='xadmin_password_reset_complete')