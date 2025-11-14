import { Component } from "@odoo/owl";
import { NumberCard } from "../number_card/number_card";
import { PieChartCard } from "../chart/pie_chart_card";
import { registry } from "@web/core/registry";

const items = [
    {
        id: 0,
        Component: NumberCard,
        size: 2,
        props: (data) => ({
            title: "avg t-shirt", content: data.average_quantity
        })
    }, {
        id: 1,
        Component: NumberCard,
        size: 2,
        props: (data) => ({
            title: "avg time order", content: data.average_time
        })
    },
    {
        id: 2,
        Component: NumberCard,
        size: 2,
        props: (data) => ({
            title: "avg new order", content: data.nb_new_orders
        })
    },
    {
        id: 3,
        Component: NumberCard,
        size: 2,
        props: (data) => ({
            title: "no of cancel order", content: data.nb_new_orders
        })
    },
    {
        id: 4,
        Component: NumberCard,
        size: 2,
        props: (data) => ({
            title: "total order", content: data.total_amount
        })
    },
    {
        id: 5,
        Component: PieChartCard,
        size: 2,
        props: (data) => ({
            title: "shirt order by size"
        })
    }
]

items.forEach(item => {
    registry.category("awesome_dashboard").add(item.id, item);
});