import { Component, useState, useExternalListener } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { ClickerValue } from "./click_value/click_value";
import { useService } from "@web/core/utils/hooks";

export class ClickerSystrayItem extends Component {
    // static template = "awesome_clicker.ClickerSystrayItem";
    static components = { ClickerValue }
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

const clickerSystray = {
    Component: ClickerSystrayItem
};

// registry.category("systray").add("awesome_clicker.ClickerSystrayItem", clickerSystray, { sequence: 1 });