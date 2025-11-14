import { Component, useState, useRef } from "@odoo/owl";
import { ToDoItem } from "./todoitem";
import { useAutofocus } from "../utils";

export class ToDoList extends Component {
    static template = "awesome_owl.todolist";

    static props = {
    };
    setup() {
        this.description = useRef('input_description');
        useAutofocus('description');
        this.todos = useState([]);
        this.counter = useState({ value: 0 });
    }

    addToDo(ev) {
        // Check If enter press
        if (ev.keyCode === 13) {
            ev.preventDefault();
            // Create ToDo
            this.todos.push({
                id: this.counter.value,
                description: (this.description.el.value != null) ? this.description.el.value : "",
                isCompleted: false,
            })
            this.description.el.value = "";
            this.toggleState = this.toggleState.bind(this);
            this.removeItem = this.removeItem.bind(this);
            this.increment();
        }
    }

    increment() {
        this.counter.value++;
    }

    toggleState(id) {
        const todo = this.todos.find(t => t.id === id);
        todo.isCompleted = !todo.isCompleted;
    }

    removeItem(id) {
        const index = this.todos.findIndex(t => t.id === id);
        if (index >= 0) {
            this.todos.splice(index,1)
        }
    }

    static components = { ToDoItem };

}
