# Copyright 2017 David BEAL @ Akretion
# Copyright 2019 Camptocamp SA

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from premailer import Premailer

from odoo import models


class MailTemplate(models.Model):
    _inherit = "mail.template"

    def _render_template_postprocess(self, model, rendered):
        rendered = super()._render_template_postprocess(model, rendered)
        for res_id, html in rendered.items():
            rendered[res_id] = self._premailer_apply_transform(html)
        return rendered

    def _premailer_apply_transform(self, html):
        if not html.strip():
            return html
        premailer = Premailer(html=html, **self._get_premailer_options())
        return premailer.transform()

    def _get_premailer_options(self):
        return {}
