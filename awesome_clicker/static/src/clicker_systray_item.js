import { Component, useState, useExternalListener } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class ClickerSystrayItem extends Component {
    static template = "awesome_clicker.ClickerSystrayItem";

    setup() {
        this.state = useState({ value: 0 });
        useExternalListener(window, "click", (ev) => this.increment());
    }

    increment() {
        this.state.value += 10;
    }

}

const clickerSystray = {
    Component: ClickerSystrayItem
};

registry.category("systray").add("awesome_clicker.ClickerSystrayItem", clickerSystray, { sequence: 1 });