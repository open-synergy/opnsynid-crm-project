# -*- coding: utf-8 -*-
# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class CrmLead(models.Model):
    _name = "crm.lead"
    _inherit = "crm.lead"

    @api.depends(
        "analytic_account_id",
        "task_ids",
        "task_ids.project_id",
        "task_ids.lead_id",
        "task_ids.stage_id",
        "task_ids.stage_id.state",
    )
    def _compute_task_count(self):
        for record in self:
            record.task_count_open = len(
                record.task_ids.filtered(lambda r: r.stage_id.state == "open")
            )

    task_ids = fields.One2many(
        string="Tasks",
        comodel_name="project.task",
        inverse_name="lead_id",
    )
    task_count_open = fields.Integer(
        string="Num. of Open Tasks",
        compute="_compute_task_count",
        store=True,
    )

    @api.multi
    def action_open_tasks(self):
        self.ensure_one()
        waction = self.env.ref("project.action_view_task").read()[0]
        criteria = [
            ("analytic_account_id", "=", self.analytic_account_id.id),
        ]
        projects = self.env["project.project"].search(criteria)
        if len(projects) == 0:
            error_msg = _("No project associated to analytic account")
            raise UserError(error_msg)
        project = projects[0]
        waction["domain"] = [
            ("lead_id", "=", self.id),
        ]
        waction["context"] = {
            "default_project_id": project.id,
            "default_lead_id": self.id,
        }
        return waction
