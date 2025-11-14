import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";
import { memoize } from "@web/core/utils/functions";
import { reactive } from "@odoo/owl";



// export async function getStatistics(statistics) {
//     const result = await rpc("/awesome_dashboard/statistics");
//     const newResult = {
//         data: [
//             { id: 0, value: { title: "avg t-shirt", content: result.average_quantity } },
//             { id: 1, value: { title: "avg time order", content: result.average_time } },
//             { id: 2, value: { title: "avg new order", content: result.nb_new_orders } },
//             { id: 3, value: { title: "no of cancel order", content: result.nb_new_orders } },
//             { id: 4, value: { title: "total order", content: result.total_amount } },
//         ]
//     }
//     Object.assign(statistics, newResult, { isReady: true });
//     return statistics;
// }

export async function getStatisticsNew(statistics) {
    const result = await rpc("/awesome_dashboard/statistics");
    Object.assign(statistics, result, { isReady: true });
    return statistics;
}


export const statistics_service = {
    start() {
        const statistics = reactive({ isReady: false });
        setInterval(() => getStatisticsNew(statistics), 10 * 60000);
        getStatisticsNew(statistics);
        return statistics;
    }
}

registry.category("services").add("awesome_dashboard.statistics", statistics_service);
