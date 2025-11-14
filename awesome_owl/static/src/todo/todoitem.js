import { Component, useState } from "@odoo/owl";

export class ToDoItem extends Component {
    static template = "awesome_owl.todoitem";

    static props = {
        todo: { type: Object, shape: { id: Number, description: String, isCompleted: Boolean } },
        toggleState: { type: Function, optional: true },
        removeItem: { type: Function, optional: true },
    };

    setup() {
    }

    onToggleState(id) {
        this.props.toggleState(id);
    }

    onRemoveItem(id) {
        this.props.removeItem(id);

    }
}
