import { Component } from "@odoo/owl";
import { useClicker } from "../hook/clicker_hook";
import { humanNumber } from "@web/core/utils/numbers";


export class ClickerValue extends Component {
    static template = "awesome_clicker.click_value";
    static props = {}
    setup() {
        this.useClicker = useClicker();
    }

    get humanizedNumber() {
        return humanNumber(this.useClicker.clicks, { decimals: 1 });
    }

}

