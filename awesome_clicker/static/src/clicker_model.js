import { EventBus } from "@odoo/owl";
import { Reactive } from "@web/core/utils/reactive";

export class ClickerModel extends Reactive {

    constructor() {
        super();
        this.clicks = 990;
        this.level = 0;
        this.bot = {
            clickBots: {
                value: 0
            },
            bigBots: {
                value: 0
            },
        }
        this.bus = new EventBus();
    }

    setup() {
    }

    increment(_inc) {
        this.clicks += _inc;
        if (this.clicks >= 1000 && this.level === 0) {
            this.bus.trigger("MILESTONE");
            this.levelInc();
        }
    }

    buyBot(_data) {
        this.bot.clickBots.value += 1;
        this.increment(-1000);
    }

    buyBigBot() {
        this.bot.bigBots.value += 1;
        this.increment(-5000);
    }

    tick() {
        this.increment(this.bot.clickBots.value * 10);
        this.increment(this.bot.bigBots.value * 100);
    }

    levelInc() {
        this.level += 1;
    }

}
