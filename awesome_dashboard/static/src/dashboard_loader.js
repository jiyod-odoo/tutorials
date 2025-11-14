import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { LazyComponent } from "@web/core/assets";


export class DashBoardLoader extends Component {
    static components = { LazyComponent };
    static template = "awesome_dashboard.AwesomeDashboardAction";
}

registry.category("actions").add("awesome_dashboard.dashboard", DashBoardLoader);