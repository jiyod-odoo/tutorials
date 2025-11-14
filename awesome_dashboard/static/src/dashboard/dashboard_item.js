import { Component } from "@odoo/owl";

export class DashBoardItem extends Component {
    static template = "awesome_dashboard.DashBoardItem";

    static props = {
        size: { type: Number, default: 1, optional: true },
        title: { type: String, optional: true },
        slots: {
            type: Object,
            shape: {
                default: Object
            },
            optional: true
        }
    }

}