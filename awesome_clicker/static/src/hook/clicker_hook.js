import { reactive, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export function useClicker() {
    const state = useState({ clicks: 0 });

    return {
        state,
        increment(inc) {
            state.clicks += inc
        }
    };
}

// const clickerService = {
//     start() {
//         const state = reactive({ clicks: 0 });
//         return {
//             state,
//             increment(inc) {
//                 state.clicks += inc
//             }
//         };
//     }
// }

// registry.category("services").add("awesome_clicker.clicker_service", clickerService);