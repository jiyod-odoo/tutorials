import { reactive } from "@odoo/owl";
import { registry } from "@web/core/registry";


const clickerService = {
    start() {
        const state = reactive({ clicks: 0 });
        return {
            state,
            increment(inc) {
                state.clicks += inc
            }
        };
    }
}

registry.category("services").add("awesome_clicker.clicker_service", clickerService);