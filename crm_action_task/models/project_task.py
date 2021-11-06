# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    @api.depends(
        "project_id",
    )
    def _compute_allowed_lead_ids(self):
        for record in self:
            result = []
            if record.project_id:
                criteria = [
                    (
                        "analytic_account_id",
                        "=",
                        record.project_id.analytic_account_id.id,
                    )
                ]
                result = self.env["crm.lead"].search(criteria).ids
            record.allowed_lead_ids = result

    lead_id = fields.Many2one(
        string="Opportunity/Lead",
        comodel_name="crm.lead",
    )
    allowed_lead_ids = fields.Many2many(
        string="Allowed Opportunity/Leads",
        comodel_name="crm.lead",
        compute="_compute_allowed_lead_ids",
        store=False,
    )

    @api.onchange(
        "project_id",
    )
    def onchange_lead_id(self):
        self.lead_id = False
