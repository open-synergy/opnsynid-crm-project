# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Action From Task",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "version": "8.0.1.1.0",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "crm_timesheet",
        "project_stage_state",
    ],
    "data": [
        "views/project_task_views.xml",
        "views/crm_lead_views.xml",
    ],
}
