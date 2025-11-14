import { Component, useState, markup } from "@odoo/owl";
import { Counter } from "./counter/counter";
import { Card } from "./card";
import { ToDoList } from "./todo/todolist";
export class Playground extends Component {
    static template = "awesome_owl.playground";

    setup() {
        this.title = "<div><strong>some content</strong></div>";
        this.titleMarkup = markup("<div><strong>some content</strong></div>");
        this.total = useState({ value: 0 });
        this.incrementSum = this.incrementSum.bind(this);
    }

    incrementSum() {
        this.total.value++;
    }

    static components = { Card, Counter, ToDoList };
}
