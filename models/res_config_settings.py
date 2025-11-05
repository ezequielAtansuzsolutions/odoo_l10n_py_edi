#import re

from odoo import _, fields, models
from odoo.exceptions import UserError, RedirectWarning

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #l10n_ar_afip_ws_environment = fields.Selection(related='company_id.l10n_ar_afip_ws_environment', readonly=False)



    def l10n_py_test(self):
        self.ensure_one()

        """
        errors = []
        if not self.l10n_ar_afip_ws_crt_id:
            errors.append(_("Please set a certificate in order to make the test"))
        if not self.l10n_ar_afip_ws_key_id:
            errors.append(_("Please set a private key in order to make the test"))
        if errors:
            raise UserError("\n* ".join(errors))

        results = []
        for webservice in [item[0] for item in self.env["l10n_ar.afipws.connection"]._get_l10n_ar_afip_ws()]:
            try:
                self.company_id._l10n_ar_get_connection(webservice)
                results.append(_("* %(webservice)s: Connection is available", webservice=webservice))
            except UserError as error:
                hint_msg = re.search('.*(HINT|CONSEJO): (.*)', str(error))
                if hint_msg:
                    msg = hint_msg.groups()[-1] if hint_msg and len(hint_msg.groups()) > 1 \
                        else '\n'.join(re.search('.*' + webservice + ': (.*)\n\n', str(error)).groups())
                else:
                    msg = str(error)
                results.append(
                    _("* %(webservice)s: Connection failed. %(message)s", webservice=webservice, message=msg.strip())
                )
            except Exception as error:
                results.append(
                    _(
                        "* %(webservice)s: Connection failed. This is what we get: %(error)s",
                        webservice=webservice,
                        error=repr(error),
                    ),
                )
                
        action = self.env.ref('account.action_account_config')
        
        raise RedirectWarning(
            "\n".join(results),
            action=action.id,
            button_text=_("Continue Configurations")
        )
        """
