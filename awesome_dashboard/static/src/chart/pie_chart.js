import { Component, useEffect, onWillStart, useRef, onWillUnmount } from "@odoo/owl";
import { loadJS } from "@web/core/assets";

export class PieChart extends Component {
    static template = "awesome_dashboard.PieChart";

    setup() {
        this.chart = null;
        this.canvasRef = useRef("canvas");
        onWillStart(() =>
            loadJS(["/web/static/lib/Chart/Chart.js"])
        );
        useEffect(() => this.renderChart());
        onWillUnmount(this.onWillUnmount);
    }

    onWillUnmount() {
        if (this.chart) {
            this.chart.destroy();
        }
    }

    renderChart() {
        let data = {
            datasets: [{
                data: [10, 20, 30]
            }],

            labels: [
                'Red',
                'Yellow',
                'Blue'
            ]
        };

        this.chart = new Chart(this.canvasRef.el, {
            type: 'pie',
            data: data,
        });
    }
}