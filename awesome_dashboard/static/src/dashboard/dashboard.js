import { Component, useState, onWillStart } from "@odoo/owl";
import { Layout } from "@web/search/layout";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { DashBoardItem } from "./dashboard_item";
import { memoize } from "@web/core/utils/functions";

class AwesomeDashboard extends Component {
    static template = "awesome_dashboard.AwesomeDashboard";
    static components = { Layout, DashBoardItem }

    setup() {
        this.action = useService("action");
        this.statistics_service = useState(useService("awesome_dashboard.statistics"));
        this.items = registry.category("awesome_dashboard").getAll();
    }

    openCustomers() {
        this.action.doAction("base.action_partner_form");
    }

    openLeads(activity) {
        this.action.doAction({
            type: 'ir.actions.act_window',
            name: 'Open Lead',
            target: 'current',
            res_id: activity.res_id,
            res_model: 'crm.lead',
            views: [[false, 'list'],
            [false, 'form']]
        });
    }
}

class DialogConfiguration extends Component {
    static template = "awesome_dashboard.Dialog_Configuration";
    static components = {};
}

registry.category("lazy_components").add("AwesomeDashboard", AwesomeDashboard);
