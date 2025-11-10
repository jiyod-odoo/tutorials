import { Component, useState } from "@odoo/owl";
import { Card } from "./card";

export class Playground extends Component {
    static template = "awesome_owl.playground";

    static components = { Card };
}
