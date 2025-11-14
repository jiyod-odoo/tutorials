import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { useClicker } from "./hook/clicker_hook";


export class ClientAction extends Component {
    static template = "awesome_clicker.client_action";

    setup() {
        this.action = useService("action");
    }

    onOpenClicker() {
        this.action.doAction({
            type: "ir.actions.client",
            tag: "awesome_clicker.client_action_open",
            target: "new",
            name: "Clicker"
        })
    }
}

const clientAction = {
    Component: ClientAction
};

export class ClientActionOpen extends Component {
    static template = "awesome_clicker.client_action_open";

    setup() {
        this.clicker = useClicker();
        this.action = useService("action");
        this.clickerService = useState(useService("awesome_clicker.clicker_service"));
    }

    onOpenClicker() {
        this.action.doAction({
            type: "ir.actions.client",
            tag: "awesome_clicker.client_action",
            target: "new",
            name: "Clicker"
        })
    }
}

registry.category("actions").add("awesome_clicker.client_action_open", ClientActionOpen);
registry.category("systray").add("awesome_clicker.client_action", clientAction, { sequence: 2 });