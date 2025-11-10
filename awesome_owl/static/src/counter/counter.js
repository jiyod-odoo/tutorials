import { Component, useState } from "@odoo/owl";

export class Counter extends Component {
    static template = "awesome_owl.counter";

    // useState  Init
    setup() {
        this.state = useState({ value: 0 })
    }

    // function
    increment() {
        this.state.value++;
    }

}
