import { EventBus } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { ClickerModel } from "./clicker_model";

const clickerService = {
    dependencies: ["action", "effect"],
    start(env, services) {
        // const state = reactive({ clicks: 0, level: 0, clickBots: 0 });
        const model = new ClickerModel();
        const bus = model.bus;
        bus.addEventListener("MILESTONE", (ev) => {
            services.effect.add({
                type: "rainbow_man", // can be omitted, default type is already "rainbow_man"
                message: "Boom! Team record for the past 30 days.",
            });
        });
        setInterval(() => { model.tick() }, 10000);
        return model;
    }
}

registry.category("services").add("awesome_clicker.clicker_service", clickerService);